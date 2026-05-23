from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI
from game.fairies.ai.BakingAssets import BAKED_ITEMS

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ''
        self.DISLid: int = 0
        self.gold: int = 0
        self.access: int = 0

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

    def setDISLname(self, DISLname: str):
        self.DISLname = DISLname

    def getDISLname(self) -> str:
        return self.DISLname

    def setDISLid(self, DISLid: int) -> int:
        self.air.sendFriendManagerAccountOnline(DISLid)

        self.DISLid = DISLid

    def getDISLid(self) -> int:
        return self.DISLid

    def setAccess(self, access) -> None:
        self.access = access

        if self.isPaid():
            self.sendUpdateToAvatarId(self.doId, "setAccess", [access])

    def isPaid(self) -> bool:
        return self.access == OTPGlobals.AccessFull

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

            self.sendUpdate("setRedraw", [1])

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

    def consumePouchItem(self, itemId, amount):
        if itemId == 22543:
            self.sendUpdateToAvatarId(self.doId, "setAura", [13])

        #baked = BAKED_ITEMS.get(itemId)
       # if baked:
            #if baked["bakedType"] == "sillysweet":
             #   pass
       # else:
            #pass
