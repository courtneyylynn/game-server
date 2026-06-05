from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.fairy.AuraMapping import AURA_MAPPING

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ""
        self.DISLid: int = 0
        self.gold: int = 0
        self.access: int = 0
        self.level: int = 0

    def announceGenerate(self):
        self.air.incrementPopulation()

        # Fill in the missing information from the database (i.e. gold)
        self.air.fillInFairyPlayer(self)

        self.air.inventoryManager.avatarOnline(self.doId)

    def delete(self):
        # TODO: Set a post-remove message in case of an AI crash.
        self.air.sendFriendManagerAccountOffline(self.DISLid)

        self.air.decrementPopulation()

        DistributedFairyBaseAI.delete(self)

    def setDISLname(self, DISLname: str) -> None:
        self.DISLname = DISLname

    def getDISLname(self) -> str:
        return self.DISLname

    def setDISLid(self, DISLid: int) -> None:
        self.air.sendFriendManagerAccountOnline(DISLid)

        self.DISLid = DISLid

    def getDISLid(self) -> int:
        return self.DISLid

    def setAccess(self, access: int) -> None:
        self.access = access

        if self.isPaid():
            self.sendUpdateToAvatarId(self.doId, "setAccess", [access])

    def getAccess(self) -> int:
        return self.access

    def isPaid(self) -> bool:
        return self.getAccess() == OTPGlobals.AccessFull

    def requestDailyGoldTradeCapData(self) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [1000])
        self.sendUpdateToAvatarId(self.doId, "setAmountGoldTradedForToday", [0])

    def requestGetSavedOutfits(self) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [1])
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])

    def requestAddSavedOutfit(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])

    def setOutfitDB(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        SLOT_METHODS = {
            1: "setHeadItem",
            2: "setNecklace",
            3: "setChestItem",
            4: "setBelt",
            5: "setSkirt",
            6: "setWrist",
            7: "setAnkle",
            8: "setShoes"
        }

        EMPTY_LITE_INV = [0, 0, 0, 0]

        desiredOutfit = {
            1: headId, 2: necklaceId, 3: shirtId, 4: beltId,
            5: skirtId, 6: wristId, 7: ankleId, 8: shoesId
        }
        equippedIds = {invId: slot for slot, invId in desiredOutfit.items() if invId != 0}
        filledSlots = set(equippedIds.values())

        table = self.air.mongoInterface.mongodb.fairies
        fairy = table.find_one({"_id": self.doId})

        if not fairy:
            return

        dirty = False
        for item in fairy["avatar"]["items"]:
            invId = item["inv_id"]

            if invId in equippedIds:
                slot = equippedIds[invId]
                changed = item["location"] != "Equipped" or item["slot"] != slot
                item["location"] = "Equipped"
                item["slot"] = slot

                if changed:
                    dirty = True
                    payload = [invId, item["item_id"], item["color1"], item["color2"]]
                    self.sendUpdate(SLOT_METHODS[slot], [payload])

            elif item["location"] == "Equipped":
                oldSlot = item["slot"]
                item["location"] = "Wardrobe"
                item["slot"] = 0
                dirty = True

                if oldSlot in SLOT_METHODS and oldSlot not in filledSlots:
                    self.sendUpdate(SLOT_METHODS[oldSlot], [EMPTY_LITE_INV])

        if dirty:
            table.update_one(
                {"_id": self.doId},
                {"$set": {"avatar.items": fairy["avatar"]["items"]}}
            )

            self.redrawFairy()

    def setHotspotTriggered(self, hotspotId, hotspotFrame) -> None:
        if not (meadow := self.air.zoneToMeadow.get(self.zoneId)):
            return

        if self.zoneId == 100 and hotspotId in (0, 10): # CBH TTT Reset - HACK - FIX THIS
            for id in range(hotspotId + 1, hotspotId + 10):
                meadow.sendUpdate("setHotspotFrame", [id, 3])
            hotspotFrame = 1

        meadow.sendUpdate("setHotspotFrame", [hotspotId, hotspotFrame])

    def setGold(self, gold: int) -> None:
        self.gold = gold

    def getGold(self) -> int:
        return self.gold

    def d_setGold(self, gold: int) -> None:
        self.sendUpdate("setGold", [gold])

    def d_setPouch(self, pouch: list) -> None:
        self.sendUpdateToAvatarId(self.doId, "setPouch", [pouch])

    def d_syncPouchAfterChanges(self) -> None:
        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def b_setGold(self, gold: int) -> None:
        self.setGold(gold)
        self.d_setGold(gold)

    def addGold(self, deltaGold: int) -> None:
        self.b_setGold(deltaGold + self.getGold())

    def takeGold(self, deltaGold: int) -> bool:
        totalGold = self.gold

        if deltaGold > totalGold:
            return False

        self.b_setGold(self.gold - deltaGold)

        return True

    def tradeGoldForItem(self, amountToGive: int, invItemToGet: int, amountToGet: int) -> None:
        if self.takeGold(amountToGive):
            if not self.air.inventoryManager.addIngredientsToPouch(self.doId, invItemToGet, amountToGet, -1):
                self.notify.warning("Failed to add ingredient %d to pouch!" % (invItemToGet))
                return

            # Apparently setPouch has to be sent back to the client twice here because `onCheckForGiveGetUpdates`
            # only fires if pouchUpdateCalls is greater than 1
            pouch = self.air.inventoryManager.getPouch(self.doId)
            self.d_setPouch(pouch)
            self.d_setPouch(pouch)

    def auraRemover(self, task):
        self.sendUpdateToAvatarId(self.doId, "setAura", [0])

    def consumePouchItem(self, itemId, amount) -> None:
        baked = BAKED_ITEMS.get(itemId)
        if baked:
            if baked["bakedType"] == "sillysweet":
                aura_id = AURA_MAPPING.get(itemId)

                if not aura_id:
                    print("ITEM A SILLY SWEET BUT NOT IN AURA MAPPING!")
                    return

                self.sendUpdateToAvatarId(self.doId, "setAura", [aura_id])
                # Aura Task
                taskMgr.doMethodLater(60, self.auraRemover, 'Aura Remover')
        else:
            pass

    def redrawFairy(self) -> None:
        self.sendUpdate("setRedraw", [1])

    def setLevel(self, level: int) -> None:
        self.level = level

    def getLevel(self) -> int:
        return self.level

    def requestFairyInfo(self, fairyId: int, unk: int) -> None:
        from game.fairies.ai.DatabaseObject import DatabaseObject

        from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI

        def gotFairyLocation(doId: int, parentId: int, zoneId: int) -> None:
            if fairyId != doId:
                self.notify.warning(f"Got unexpected location for doId {doId}, was expecting {fairyId}!")
                return

            DISLid = fairy.getDISLid()
            fairyName = fairy.getName()
            DISLname = fairy.getDISLname()
            fairyDNA = fairy.fairyDNA.asTuple()
            fairyAccess = fairy.getAccess()
            fairyLevel = fairy.getLevel()

            # TODO: Implement this
            place: int = 0

            self.sendUpdateToAvatarId(self.doId, "responseFairyInfo", [[
                fairyId,
                DISLid,
                parentId,
                zoneId,
                fairyName,
                DISLname,
                fairyDNA[0], # talent
                fairyAccess,
                fairyLevel,
                place
            ]])

        fairy = self.air.getDo(fairyId)

        if fairy:
            # This fairy is present on this shard, no need to query location from OTP server.
            gotFairyLocation(fairyId, fairy.parentId, fairy.zoneId)
            return

        def fieldsCallback(db: DatabaseObject, retCode: int) -> None:
            nonlocal fairy

            if retCode != 0:
                return

            fairy = DistributedFairyPlayerAI(self.air)

            db.fillin(fairy, db.dclass)

            # Dispatch a request to the OTP server to find out where this fairy is.
            self.air.getObjectLocation(fairyId, gotFairyLocation)

        # Query the fairy for data since they are not present on this shard:
        gotFairyEvent = self.air.uniqueName(f"gotFairy-{fairyId}")
        self.acceptOnce(gotFairyEvent, fieldsCallback)

        db = DatabaseObject(self.air, fairyId)
        db.doneEvent = gotFairyEvent
        db.dclass = self.air.dclassesByName[self.__class__.__name__]
        db.getFields(["setDISLid", "setName", "setDISLname", "setFairyDNA", "setAccess", "setLevel"])

    def teleportRequestTo(self, fairyId: int) -> None:
        def gotFairyLocation(doId: int, parentId: int, zoneId: int) -> None:
            if fairyId != doId:
                self.notify.warning(f"Got unexpected location for doId {doId}, was expecting {fairyId}!")
                return

            # TODO: Implement these
            available: bool = True
            roomId: int = 0

            self.sendUpdateToAvatarId(self.doId, "teleportResponse", [
                fairyId,
                available,
                parentId,
                zoneId,
                roomId
            ])

        fairy = self.air.getDo(fairyId)

        if fairy:
            # This fairy is present on this shard, no need to query location from OTP server.
            gotFairyLocation(fairyId, fairy.parentId, fairy.zoneId)
            return

        # Dispatch a request to the OTP server to find out where this fairy is.
        self.air.getObjectLocation(fairyId, gotFairyLocation)

    def setWhisperSCEmoteTo(self, toId: int, emoteId: int) -> None:
        channelId = self.GetPuppetConnectionChannel(toId)

        fromId = self.doId

        self.air.sendUpdateToChannelFrom(self, channelId, "setWhisperSCEmoteFrom", fromId, [fromId, emoteId])
