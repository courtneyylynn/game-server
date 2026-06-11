from direct.directnotify import DirectNotifyGlobal

from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.fairy.AuraMapping import AURA_MAPPING, SKIN_COLOR_MAPPING, WING_COLOR_MAPPING
from game.fairies.fairy.structs.MiscItem import MiscItem

from game.fairies.daily.DailyChanceData import (
    DEV_TEST_PRIZE,
    owned_spin_badge_exclude_mask,
    roll_rewards,
)
from game.fairies.daily.DailyChanceEligibility import (
    can_spin_today,
    current_spin_day,
    played_flag_for_client,
)
from game.fairies.daily.DailyChanceGrant import get_earned_spin_badge_ids, grant_prize

notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFairyPlayerAI")

DAILY_CHANCE_GRANTS_ENABLED = True
DAILY_CHANCE_ONCE_PER_DAY_ENABLED = True

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ""
        self.DISLid: int = 0
        self.gold: int = 0
        self.access: int = 0
        self.level: int = 0
        self.dailyChancePlayed: int = 0
        self.dailyChanceLastSpinDay: int = 0

        self._originalDNA = {}

    def announceGenerate(self):
        self.air.incrementPopulation()

        self.air.fillInFairyPlayer(self)
        if not DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._sync_daily_chance_not_played_for_client()

        self.air.inventoryManager.avatarOnline(self.doId)
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [1000])
        glblpurchase = MiscItem.unpackFromTuple((90003, 8006, 500, 200, 1))
        self.sendUpdateToAvatarId(self.doId, "setGlobalPurchaseData", [[glblpurchase]])

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

    def setDailyChancePlayed(self, played: int) -> None:
        self.dailyChancePlayed = played

    def getDailyChancePlayed(self) -> int:
        return self.dailyChancePlayed

    def d_setDailyChancePlayed(self, played: int) -> None:
        self.sendUpdate("setDailyChancePlayed", [played])

    def setDailyChanceLastSpinDay(self, spin_day: int) -> None:
        self.dailyChanceLastSpinDay = int(spin_day)
        if DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._sync_daily_chance_played_from_spin_day()

    def getDailyChanceLastSpinDay(self) -> int:
        return self.dailyChanceLastSpinDay

    def _sync_daily_chance_played_from_spin_day(self) -> None:
        played = played_flag_for_client(self.getDailyChanceLastSpinDay())
        self.setDailyChancePlayed(played)
        self.d_setDailyChancePlayed(played)

    def _record_daily_chance_spin(self) -> None:
        if not DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            return

        spin_day = current_spin_day()
        self.setDailyChanceLastSpinDay(spin_day)
        self.air.mongoInterface.updateField(
            "fairies", "dailyChanceLastSpinDay", self.doId, spin_day
        )

    def _sync_daily_chance_not_played_for_client(self) -> None:
        self.setDailyChancePlayed(0)
        self.d_setDailyChancePlayed(0)

    def requestDailyChance(self, excludeMask: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        if avId != self.doId:
            self.notify.warning(
                f"requestDailyChance from {avId} but sender DO is {self.doId}"
            )
            return

        if DAILY_CHANCE_ONCE_PER_DAY_ENABLED and not can_spin_today(
            self.getDailyChanceLastSpinDay()
        ):
            self._sync_daily_chance_played_from_spin_day()
            self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [[]])
            return

        if not DAILY_CHANCE_GRANTS_ENABLED:
            self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [[]])
            return

        avatar_gender = self.fairyDNA.gender
        earned_spin_badges = get_earned_spin_badge_ids(self.air, avId)
        effective_mask = excludeMask | owned_spin_badge_exclude_mask(earned_spin_badges)
        prizes = roll_rewards(effective_mask, self.isPaid(), avatar_gender)
        if not prizes:
            prizes = [DEV_TEST_PRIZE]

        granted: list[tuple[int, int, int, int]] = []
        for prize in prizes:
            if grant_prize(self.air, avId, self, prize):
                granted.append(prize.as_reward_ext())
            else:
                self.notify.warning(
                    f"requestDailyChance: failed to grant item {prize.item_id} to {avId}"
                )

        if not granted and prizes:
            self.notify.warning(
                f"requestDailyChance: no grants applied for {avId}, "
                f"prizes={[p.item_id for p in prizes]}"
            )

        self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [granted])
        if granted and DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._record_daily_chance_spin()
        elif not DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._sync_daily_chance_not_played_for_client()

    def requestDailyGoldTradeCapData(self) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [100])
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

    def tradeItemForGold(self, invItemToGive: int, amountToGive: int, amountToGet: int) -> None:
        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, invItemToGive, amountToGive):
            print("tradeItem - Couldn't Remove Ingredients??")
            return

        self.addGold(amountToGet)
        # Apparently setPouch has to be sent back to the client twice here because `onCheckForGiveGetUpdates`
        # only fires if pouchUpdateCalls is greater than 1
        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def tradeItem(self, invItemToGive: int, amountToGive: int, invItemToGet: int, amountToGet: int) -> None:
        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, invItemToGive, amountToGive):
            print("tradeItemForGold - Couldn't Remove Ingredients??")
            return

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

    def invisRemover(self, task):
        self.sendUpdateToAvatarId(self.doId, "setRenderEffects", [0])
        self.sendUpdateToAvatarId(self.doId, "setRedraw", [1])

    def _getSweetType(self, itemId):
        """Determine which kind of silly sweet this item is."""
        if itemId == 22525:
            return "invisible"
        if itemId in AURA_MAPPING:
            return "aura"
        if itemId in SKIN_COLOR_MAPPING:
            return "skin"
        if itemId in WING_COLOR_MAPPING:
            return "wing"
        return None

    def _handleAuraSweet(self, itemId, _):
        aura_id = AURA_MAPPING[itemId]
        self.sendUpdateToAvatarId(self.doId, "setAura", [aura_id])

        # Cancel any existing aura timer and start fresh
        taskMgr.remove("AuraRemover")
        taskMgr.doMethodLater(60, self.auraRemover, "AuraRemover")

    def _handleSkinSweet(self, itemId, avatar):
        color = SKIN_COLOR_MAPPING[itemId]
        self._applyDNAColor(avatar, color, slotIndex=12)

    def _handleWingSweet(self, itemId, avatar):
        color = WING_COLOR_MAPPING[itemId]
        self._applyDNAColor(avatar, color, slotIndex=13)

    def _handleInvisibleSweet(self, _, avatar):
        self.sendUpdateToAvatarId(self.doId, "setRenderEffects", [1])
        avatar.redrawFairy()

        taskMgr.remove("InvisRemover")
        taskMgr.doMethodLater(60, self.invisRemover, "InvisRemover")

    def _cancelColorSweet(self, slotIndex):
        taskMgr.remove(f"DNARestore-{slotIndex}")
        taskMgr.remove(f"ColorCycle-{slotIndex}")

    def _restoreDNATask(self, task):
        avatar = self.air.doId2do.get(self.doId)
        if avatar and task.slotIndex in self._originalDNA:
            self._restoreDNA(avatar, task.slotIndex)
        return task.done

    def _runColorCycleTask(self, task):
        avatar = self.air.doId2do.get(self.doId)
        if avatar:
            self._applyColorStep(avatar, task.colors[task.cycleIndex], task.slotIndex)
            task.cycleIndex = (task.cycleIndex + 1) % len(task.colors)
        return task.again

    def _applyDNAColor(self, avatar, color, slotIndex):
        if isinstance(color, list):
            self._scheduleCyclingColors(avatar, color, slotIndex)
            return

        restore_task_name = f"DNARestore-{slotIndex}"

        if not taskMgr.hasTaskNamed(restore_task_name):
            self._originalDNA[slotIndex] = avatar.getFairyDNA()[slotIndex]

        self._cancelColorSweet(slotIndex)

        dna = list(avatar.getFairyDNA())
        dna[slotIndex] = color
        avatar.b_setFairyDNA(tuple(dna))
        avatar.redrawFairy()

        restore_task = taskMgr.doMethodLater(60, self._restoreDNATask, restore_task_name)
        restore_task.slotIndex = slotIndex

    def _applyColorStep(self, avatar, color, slotIndex):
        """Single color application step, used by cycling tasks."""
        dna = list(avatar.getFairyDNA())
        dna[slotIndex] = color
        avatar.b_setFairyDNA(tuple(dna))
        avatar.redrawFairy()

    def _runColorCycle(self, avatar, colors, slotIndex, cycleIndex=0):
        self._applyColorStep(avatar, colors[cycleIndex], slotIndex)

        cycle_task = taskMgr.doMethodLater(5, self._runColorCycleTask, f"ColorCycle-{slotIndex}")
        cycle_task.colors = colors
        cycle_task.slotIndex = slotIndex
        cycle_task.cycleIndex = (cycleIndex + 1) % len(colors)

    def _scheduleCyclingColors(self, avatar, colors, slotIndex):
        restore_task_name = f"DNARestore-{slotIndex}"

        if not taskMgr.hasTaskNamed(restore_task_name):
            self._originalDNA[slotIndex] = avatar.getFairyDNA()[slotIndex]

        self._cancelColorSweet(slotIndex)

        self._runColorCycle(avatar, colors, slotIndex, cycleIndex=0)

        restore_task = taskMgr.doMethodLater(60, self._restoreDNATask, restore_task_name)
        restore_task.slotIndex = slotIndex

    def consumePouchItem(self, itemId, amount) -> None:
        avatar = self.air.doId2do.get(self.doId)

        baked = BAKED_ITEMS.get(itemId)
        if not baked:
            return

        if baked["bakedType"] == "sillysweet":
            sweet_type = self._getSweetType(itemId)

            if sweet_type is None:
                print(f"ITEM MISSING FROM ALL SWEET MAPPINGS: {itemId}")
                return

            # Calls _handleAuraSweet, _handleSkinSweet, or _handleWingSweet
            # depending on sweet_type. Add new types by adding a matching method.
            handler = getattr(self, f"_handle{sweet_type.capitalize()}Sweet")
            handler(itemId, avatar)

        self.sendUpdateToAvatarId(self.doId, "setItemEvent", [itemId, amount, 0, 0])
        self.air.inventoryManager.removeIngredientsFromPouch(self.doId, itemId, amount)

        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def redrawFairy(self) -> None:
        self.sendUpdate("setRedraw", [1])

    def setLevel(self, level: int) -> None:
        self.level = level

    def d_setLevel(self, level: int) -> None:
        self.sendUpdate("setLevel", [level])

    def b_setLevel(self, level: int) -> None:
        self.setLevel(level)
        self.d_setLevel(level)

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

    def removeFromInventory(self, invId, itemId):
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": self.doId},
                {
                    "$pull": {
                        "avatar.items": {
                            "inv_id": invId
                        }
                    }
                }
        )

        self.air.inventoryManager.sendUpdateToAvatarId(self.doId, "wardrobeRemove", [0, invId])

    def requestGlobalPurchase(self, item):
        glblpId, qty = item[0]

        if not self.takeGold(qty):
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [1])

    def requestSendUpdateFairyName(self, name):
        self.b_setName(name)
        self.sendUpdateToAvatarId(self.doId, "setRedraw", [1])
