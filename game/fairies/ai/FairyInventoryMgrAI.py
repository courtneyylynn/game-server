from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

class FairyInventoryMgrAI(DistributedObjectGlobalAI):
    def __init__(self, air) -> None:
        super().__init__(air)

    def getPouch(self, avId: int) -> list:
        pouchData = self.air.mongoInterface.retrieveDocs("fairies", avId, "_id")[0]["pouch"]
        pouch = []

        for index, item in enumerate(pouchData):
            slot = item["slot"]
            if slot < 0:
                slot = index

            pouch.append([item["item_id"], slot, item["amount"]])

        return pouch

    def avatarOnline(self, avId: int) -> None:
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for avatarOnline: {avId}")
            return

        avatar.d_setPouch(self.getPouch(avId))

    def wardrobeConversion(self, inv_id):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"wardrobeConversion: no avatar on AI for avId={avId}")
            return

        CONV_COSTS = {
            "Shirt": 6,
            "Skirt": 7,
            "Shoes": 5,
            "Belt": 4,
            "HeadItem": 5,
            "Necklace": 3,
            "WristItem": 3,
            "AnkleItem": 3,
        }

        result = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": avId, "avatar.items.inv_id": inv_id},
            {"avatar.items.$": 1}
        )
        if result:
            item_type = result["avatar"]["items"][0]["type"]
        else:
            print("WARDROBECONVERSION PANIC")
            return

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$set": {
                    "avatar.items.$[item].howAcquired": 0
                }
            },
            array_filters=[{"item.inv_id": inv_id}]
        )

        avatar.takeGold(CONV_COSTS[item_type])

    def addIngredientsToPouch(self, avId: int, itemID: int, itemCount: int, slot: int) -> bool:
        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId, "pouch.item_id": itemID},
            {"$inc": {"pouch.$.amount": itemCount}}
        )

        if result.modified_count > 0:
            return True

        if slot < 0:
            slot = self._nextPouchSlot(avId)

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "pouch": {
                        "item_id": itemID,
                        "slot": slot,
                        "amount": itemCount
                    }
                }
            }
        )

        return result.modified_count > 0

    def removeIngredientsFromPouch(self, avId: int, itemID: int, itemCount: int) -> bool:
        # First, read the current pouch entry
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": avId, "pouch.item_id": itemID},
            {"pouch.$": 1}  # Only return the matching pouch element
        )

        if not fairy or not fairy.get("pouch"):
            return False  # Item doesn't exist in pouch

        currentAmount = fairy["pouch"][0]["amount"]

        if currentAmount < itemCount:
            return False  # Not enough

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId, "pouch.item_id": itemID},
            {"$inc": {"pouch.$.amount": -itemCount}}
        )

        if result.modified_count == 0:
            return False

        # Clean up if amount hit 0
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {"$pull": {"pouch": {"item_id": itemID, "amount": {"$lte": 0}}}}
        )

        return True

    def _nextPouchSlot(self, avId: int) -> int:
        usedSlots = {slot for _itemId, slot, _amount in self.getPouch(avId) if slot >= 0}
        slot = 0

        while slot in usedSlots:
            slot += 1

        return slot

    def _getPouchSlotForItem(self, avId: int, itemID: int) -> int:
        for itemId, slot, _amount in self.getPouch(avId):
            if itemId == itemID:
                return max(0, slot)

        return 0

    def addIngredientsToPouchWithPickupFeedback(self, avId: int, itemID: int, itemCount: int, slot: int = -1) -> bool:
        if not self.addIngredientsToPouch(avId, itemID, itemCount, slot):
            return False

        avatar = self.air.doId2do.get(avId)

        if not avatar:
            return True

        pouchSlot = self._getPouchSlotForItem(avId, itemID)
        avatar.sendUpdate("setItemEvent", [itemID, itemCount, 0, 0])
        avatar.d_syncPouchAfterChanges()
        return True
