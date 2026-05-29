from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

class FairyInventoryMgrAI(DistributedObjectGlobalAI):
    def __init__(self, air) -> None:
        super().__init__(air)

    def getPouch(self, avId: int) -> list:
        pouchData = self.air.mongoInterface.retrieveDocs("fairies", avId, "_id")[0]["pouch"]
        pouch = []

        for item in pouchData:
            pouch.append([item["item_id"], item["slot"], item["amount"]])

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
