DBSERVER_CREATE_STORED_OBJECT      = 1003
DBSERVER_CREATE_STORED_OBJECT_RESP = 1004

DBSERVER_GET_STORED_VALUES         = 1012
DBSERVER_GET_STORED_VALUES_RESP    = 1013

DBSERVER_SET_STORED_VALUES         = 1014

DATABASE_ID = 4003

-- This is act as a database server to bridge with the
-- API server, which hosts its own database.

-- Load the configuration varables (see config.example.lua)
dofile("config.lua")

local API_BASE

local http = require("http")
local json = require("json")
local inspect = require("inspect")

if PRODUCTION_ENABLED then
    API_BASE = "https://fairies.sunrise.games/fairies/api/internal/"
else
    API_BASE = "http://127.0.0.1/fairies/api/internal/"
end

function retrieveObject(participant, doId)
    local connAttempts = 0

    while (connAttempts < 3) do
        local response, error_message = http.get(API_BASE .. string.format("retrieveObject/%d", doId), {
            headers={
                ["User-Agent"]=USER_AGENT,
                ["Authorization"]=API_TOKEN
            }
        })

        if error_message then
            participant:error(string.format("retrieveObject returned an error! \"%s\"", error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            participant:error(string.format("retrieveObject returned %d!, \"%s\"", response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            -- If we're here, then we can return the response body.
            return true, response.body
        end

        -- retry goto to iterate again if we failed to retrieve our car data.
        ::retry::
    end

    -- If we're here, then we failed to get valid car data. Send an error response
    return false, ""
end

function updateObject(participant, doId, data)
    local connAttempts = 0

    while (connAttempts < 3) do
        local response, error_message = http.post(API_BASE .. string.format("updateObject/%d", doId), {
            body=json.encode(data),
            headers={
                ["User-Agent"]=USER_AGENT,
                ["Authorization"]=API_TOKEN,
                ["Content-Type"]="application/json"
            }
        })

        if error_message then
            participant:error(string.format("updateObject returned an error! \"%s\"", error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            participant:error(string.format("updateObject returned %d!, \"%s\"", response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            -- If we're here, then we can return the response body.
            return true, response.body
        end

        -- retry goto to iterate again if we failed to retrieve our car data.
        ::retry::
    end

    -- If we're here, then we failed to get valid car data. Send an error response
    return false, ""
end

-- NOTE: setFairyDNA and other DNA fields are handled separately
Api2Field = {
    -- TODO: Figure out the rest
    -- Account
    lastLogin = "LAST_LOGIN",

    -- DistributedFairyPlayer
    accountId = "setDISLid",
    name = "setName",
    moreOptions = "setMoreOptions",
    tutorialBitmask = "setHelpFlags",
    optionsBitmask = "setOptionsMask",
    bio = "setBio",
    gold = "setGold",
    level = "setLevel"
}

Field2Api = {}
for key, value in pairs(Api2Field) do
    Field2Api[value] = key
end

function init(participant)
    participant:subscribeChannel(DATABASE_ID)
end

function handleDatagram(participant, msgType, dgi)
    if msgType == DBSERVER_CREATE_STORED_OBJECT then
        participant:warn("CreateStoredObject not supported.")
    elseif msgType == DBSERVER_GET_STORED_VALUES then
        handleGetStoredValues(participant, dgi)
    elseif msgType == DBSERVER_SET_STORED_VALUES then
        handleSetStoredValues(participant, dgi)
    end
end

function handleGetStoredValues(participant, dgi)
    local sender = participant:getSender()
    local context = dgi:readUint32()
    local doId = dgi:readUint32()

    local requestedFields = {}
    local count = dgi:readUint16()
    for _ = 1, count, 1 do
        table.insert(requestedFields, dgi:readString())
    end

    local success, body = retrieveObject(participant, doId)
    if not success then
        -- Reply with an error
        local dg = datagram:new()
        dg:addServerHeader(sender, DATABASE_ID, DBSERVER_GET_STORED_VALUES_RESP)
        dg:addUint32(context)
        dg:addUint32(doId)
        dg:addUint16(#requestedFields)
        for _, field in ipairs(requestedFields) do
            dg:addString(field)
        end
        dg:addUint8(1) -- error code
        participant:routeDatagram(dg)
        return
    end

    local data = json.decode(body)
    local packedFieldData = {}
    local dcClass = dcFile:getClassByName(data.objectName)
    local packer = dcpacker:new()

    if data.objectName == "Account" then
        -- FairyClient only use ACCOUNT_AV_SET, so let's set that up
        local avSet = {data.playerId}
        local packedDg = datagram:new()
        if packer:packField(dcClass:getFieldByName("ACCOUNT_AV_SET"), packedDg, avSet) then
            local packedDgi = datagramiterator.new(packedDg)
            packedFieldData["ACCOUNT_AV_SET"] = packedDgi:readRemainder()
        else
            participant:error("ACCOUNT_AV_SET has failed to pack!")
            -- Reply with an error
            local dg = datagram:new()
            dg:addServerHeader(sender, DATABASE_ID, DBSERVER_GET_STORED_VALUES_RESP)
            dg:addUint32(context)
            dg:addUint32(doId)
            dg:addUint16(#requestedFields)
            for _, field in ipairs(requestedFields) do
                dg:addString(field)
            end
            dg:addUint8(1) -- error code
            participant:routeDatagram(dg)
            return
        end
        goto finish
    end

    for _, field in ipairs(requestedFields) do
        local dcField = dcClass:getFieldByName(field)
        local fieldData

        local function getItemByType(items, itemType)
            for _, item in ipairs(items) do
                if item.type == itemType and item.location == "Equipped" then
                    return item
                end
            end
            return nil
        end

        local function makeItemPayload(slotType)
            local item = getItemByType(data.avatar.items, slotType)
            if item ~= nil then
                return {
                    {
                        item.inv_id,
                        item.item_id,
                        item.color1,
                        item.color2
                    }
                }
            else
                return {{0, 0, 0, 0}}
            end
        end

        local fieldHandlers = {
            setFairyDNA = function()
                return {
                    {
                        data.talent,
                        data.avatar.proportions.head,
                        data.avatar.proportions.height,
                        data.avatar.proportions.body,
                        data.avatar.hair_back,
                        data.avatar.hair_front,
                        data.avatar.face,
                        data.avatar.eye,
                        data.avatar.wing,
                        data.avatar.hair_color,
                        data.avatar.hair_color2,
                        data.avatar.eye_color,
                        data.avatar.skin_color,
                        data.avatar.wing_color,
                        data.gender
                    }
                }
            end,
            setFairyPose = function()
                return {
                    {
                        data.avatar.rotations.head_rot,
                        data.avatar.rotations.ul_arm_rot,
                        data.avatar.rotations.ur_arm_rot,
                        data.avatar.rotations.ll_arm_rot,
                        data.avatar.rotations.lr_arm_rot,
                        data.avatar.rotations.ul_leg_rot,
                        data.avatar.rotations.ur_leg_rot,
                        data.avatar.rotations.ll_leg_rot,
                        data.avatar.rotations.lr_leg_rot
                    }
                }
            end,
            setHeadItem = function()
                return makeItemPayload("HeadItem")
            end,
            setNecklace = function()
                return makeItemPayload("Necklace")
            end,
            setChestItem = function()
                return makeItemPayload("Shirt")
            end,
            setBelt = function()
                return makeItemPayload("Belt")
            end,
            setSkirt = function()
                return makeItemPayload("Skirt")
            end,
            setWrist = function()
                return makeItemPayload("WristItem")
            end,
            setAnkle = function()
                return makeItemPayload("AnkleItem")
            end,
            setShoes = function()
                return makeItemPayload("Shoes")
            end
        }

        local handler = fieldHandlers[field]
        if handler then
            fieldData = handler()
        else
            if Field2Api[field] ~= nil then
                fieldData = {data[Field2Api[field]]}
                if fieldData == {nil} then
                    participant:warn(string.format("\"%s\" is missing in API response, returning default value", field))
                    packedFieldData[field] = dcField:getDefaultValue()
                    goto continue
                end
            else
                participant:warn(string.format("\"%s\" is not in Field2Api, returning default value", field))
                packedFieldData[field] = dcField:getDefaultValue()
                goto continue
            end
        end
        local packedDg = datagram:new()
        if packer:packField(dcField, packedDg, fieldData) then
            local packedDgi = datagramiterator.new(packedDg)
            packedFieldData[field] = packedDgi:readRemainder()
        else
            participant:warn(string.format("\"%s\" has failed to pack!", field))
        end
    ::continue::
    end

    ::finish::
    packer:delete()

    -- Send a response:
    local dg = datagram:new()
    dg:addServerHeader(sender, DATABASE_ID, DBSERVER_GET_STORED_VALUES_RESP)
    dg:addUint32(context)
    dg:addUint32(doId)
    dg:addUint16(#requestedFields)
    for _, field in ipairs(requestedFields) do
        dg:addString(field)
    end
    dg:addUint8(0) -- error code

    for _, field in ipairs(requestedFields) do
        if packedFieldData[field] ~= nil then
            dg:addString(packedFieldData[field])
            dg:addBool(true) -- found
        else
            dg:addString("")
            dg:addBool(false) -- found
        end
    end
    participant:routeDatagram(dg)
end

function handleSetStoredValues(participant, dgi)
    local doId = dgi:readUint32()

    local count = dgi:readUint16()
    local packedFields = {}
    for _ = 1, count, 1 do
        packedFields[dgi:readString()] = dgi:readString()
    end

    -- Get the object just so we'll know what we're dealing with.
    local success, body = retrieveObject(participant, doId)
    if not success then
        participant:error(string.format("SetStoredValues: Can't get object for ID: %d", doId))
        return
    end

    local data = json.decode(body)
    local dcClass = dcFile:getClassByName(data.objectName)

    local unpacker = dcpacker:new()
    local Api2Value = {}
    for field, packedValue in pairs(packedFields) do
        local dcField = dcClass:getFieldByName(field)
        local value = unpacker:unpackField(dcField, packedValue)
        if dcField:isAtomic() then
            value = value[1]
        end
        if field == "setFairyDNA" then
            Api2Value["talent"] = value[1]
            Api2Value["head"] = value[2]
            Api2Value["height"] = value[3]
            Api2Value["body"] = value[4]
            Api2Value["hair_back"] = value[5]
            Api2Value["hair_front"] = value[6]
            Api2Value["face"] = value[7]
            Api2Value["eye"] = value[8]
            Api2Value["wing"] = value[9]
            Api2Value["hair_color"] = value[10]
            Api2Value["hair_color2"] = value[11]
            Api2Value["eye_color"] = value[12]
            Api2Value["skin_color"] = value[13]
            Api2Value["wing_color"] = value[14]
            Api2Value["gender"] = value[15]
        else
            if Field2Api[field] ~= nil then
                Api2Value[Field2Api[field]] = value
            else
                participant:warn(string.format("SetStoredValues: %s is not in Field2Api, ignoring.", field))
            end
        end
    end

    ::finish::
    unpacker:delete()
    if Api2Value ~= {} then
        participant:debug(string.format("Sending update to %s(%d): %s", data.objectName, doId, inspect(Api2Value)))
        updateObject(participant, doId, Api2Value)
    end
end
