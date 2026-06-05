from collections.abc import Sequence

from game.fairies.fairy.structs.ShopTriedOnItems import ShopTriedOnItems

from .DistributedFairyNPCAI import DistributedFairyNPCAI

from game.fairies.fairy.structs.ShopCollection import ShopCollection

from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.OutfitItem import OutfitItem

from game.fairies.shop.ShopData import getShopByZone, getShopOutfitByOutfitId, getShopItemByIndex
from game.fairies.ai import FairiesConstants as fc

PURCHASE_FAIL = 0
PURCHASE_SUCCESS = 1

class DistributedFairyShopkeeperNPCAI(DistributedFairyNPCAI):
    def __init__(self, air) -> None:
        DistributedFairyNPCAI.__init__(self, air)

        self.shopId: int = 0

        self.shopItems: list[ShopCollection] = []

        self.dyeCostItemId: int = 0
        self.dye1Price: int = 0
        self.dye2Price: int = 0
        self.dye1Gold: int = 0
        self.dye2Gold: int = 0

    def setShopId(self, shopId: int) -> None:
        self.shopId = shopId

    def getShopId(self) -> int:
        return self.shopId

    def setShopItems(self, shopItems: Sequence) -> None:
        self.shopItems = [
            ShopCollection.unpackFromTuple(collectionData)
            for collectionData in shopItems
        ]

    def getShopItems(self) -> list[tuple]:
        return [
            collection.asTuple()
            for collection in self.shopItems
        ]

    def setDyePrice(self, costItemId: int, dye1Price: int, dye2Price: int, dye1Gold: int, dye2Gold: int) -> None:
        self.dyeCostItemId = costItemId
        self.dye1Price = dye1Price
        self.dye2Price = dye2Price
        self.dye1Gold = dye1Gold
        self.dye2Gold = dye2Gold
        print("setprice")

    def getDyePrice(self) -> tuple[int, int, int, int, int]:
        return (
            self.dyeCostItemId,
            self.dye1Price,
            self.dye2Price,
            self.dye1Gold,
            self.dye2Gold
        )

    def setTryOn(self, items) -> None:
        avId = self.air.getAvatarIdFromSender()
        itemsTriedOn = ShopTriedOnItems.unpackFromTuple((avId, items))
        self.sendUpdateToAvatarId(avId, "setTriedOnItems", [[itemsTriedOn]])
    
    def setRequestDyeItem(self, invId, color1, color2, type, unk2):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        price: int = 0

        fields = {}
        dyes = []

        if color1 != -1:
            fields["avatar.items.$.color1"] = color1
            price += self.dye1Price
            dyes.append(color1)
        if color2 != -1:
            fields["avatar.items.$.color2"] = color2
            price += self.dye2Price
            dyes.append(color2)

        if not fields:
            return False  # Nothing to update
        
        ing_type = self.dyeCostItemId
        success = self.air.inventoryManager.removeIngredientsFromPouch(avId, ing_type, price)
        avatar.d_syncPouchAfterChanges()

        if success:
            for d in dyes:
                dye_id = d + 14000
                self.air.inventoryManager.removeIngredientsFromPouch(avId, dye_id, 1)
                avatar.d_syncPouchAfterChanges()

            result = self.air.mongoInterface.mongodb.fairies.update_one(
                {"_id": avId, "avatar.items.inv_id": invId},
                {"$set": fields}
            )

            self.d_setPurchaseResponse(avId, result)
        else:
            # Send failure purchase response back to the client.
            self.d_setPurchaseResponse(avId, success)


    def setRequestPurchase(self, items, usingGold) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setRequestPurchase: {avId}")
            return

        shop = getShopByZone(self.zoneId)

        purchaseRequests: list = []

        priceTotal: int = 0

        for itemData in items:
            itemIndex, amount, collectionId = itemData

            if itemIndex == -1:
                # Outfits have the amount set as the outfitId for some reason...
                requestItems = list(getShopOutfitByOutfitId(shop, collectionId, amount).items)

                requestPrice = sum(
                    outfitItem.goldPrice if usingGold else outfitItem.price
                    for outfitItem in requestItems
                )
            else:
                item = getShopItemByIndex(shop, collectionId, itemIndex)

                requestItems = [item]

                requestPrice = item.goldPrice if usingGold else item.price

            purchaseRequests.append((requestItems, amount, collectionId))

            priceTotal += requestPrice

        if usingGold:
            success = avatar.takeGold(priceTotal) 
        else:
            ing_type = shop.collectionsById.get(collectionId).currencyId
            success = self.air.inventoryManager.removeIngredientsFromPouch(avId, ing_type, priceTotal)
            avatar.d_syncPouchAfterChanges()
            print(ing_type)
            print(success)

        if not success:
            # Send failure purchase response back to the client.
            self.d_setPurchaseResponse(avId, success)
            return

        for requestItems, amount, collectionId in purchaseRequests:
            for item in requestItems:
                if not self.handleSpecialPurchase(avId, avatar, item, amount, collectionId):
                    self.handleItemPurchase(avId, item)

        self.d_setPurchaseResponse(avId, True)

    def handleSpecialPurchase(self, avId: int, avatar, item: ShopItem | OutfitItem, amount: int, collectionId: int) -> bool:
        if self.zoneId == 110010: # harmony's
            self.purchasePouchItemsHelper(avId, item.itemId, amount)

            return True

        if self.zoneId == 112000: # Daisy's Dyes
            self.purchasePouchItemsHelper(avId, item.itemId, amount)

            return True

        elif self.zoneId == 117000: # SPA
            if collectionId == 4019: # skin colors
                color = item.itemId - 14000

                self.updateDNAHelper(avId, avatar, color, slotnum=12)

            elif collectionId == 4020: # eye colors
                color = item.itemId - 14000

                self.updateDNAHelper(avId, avatar, color, slotnum=11)

            elif collectionId == 4017: # wings
                self.updateDNAHelper(avId, avatar, item.itemId, slotnum=8)

            else: # expressions
                eyeid = item.itemId - 500

                self.updateDNAHelper(avId, avatar, item.itemId, slotnum=6)

                self.updateDNAHelper(avId, avatar, eyeid, slotnum=7)

            return True

        elif self.zoneId == 114000: # hairsalon
            if 5000 <= item.itemId < 5500:
                self.updateDNAHelper(avId, avatar, item.itemId, slotnum=5)

                return True

            elif 5500 <= item.itemId < 6000:
                self.updateDNAHelper(avId, avatar, item.itemId, slotnum=4)

                return True

            if collectionId == 4014: # Hair color
                colorId = item.itemId - 14000
                self.updateDNAHelper(avId, avatar, colorId, slotnum=9)

                return True

            elif collectionId == 4015: # Highlights
                colorId = item.itemId - 14000
                self.updateDNAHelper(avId, avatar, colorId, slotnum=10)

                return True

        return False

    def handleItemPurchase(self, avId: int, item: ShopItem | OutfitItem) -> None:
        invId = self.air.mongoInterface.getNextDoId()
        itemId = item.itemId
        slot = -1
        createdById = 0 # TODO
        createdByName = "" # TODO
        giftedById = 0 # TODO
        giftedByName = "" # TODO
        quality = 0 # TODO
        color1 = item.color1
        color2 = item.color2
        howAcquired = 11 # howAcquired > 10 takes up a wardrobe spot

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": invId,
                        "type": item.itemType,
                        "item_id": itemId,
                        "slot": slot,
                        "createdById": createdById,
                        "createdByName": createdByName,
                        "giftedById": giftedById,
                        "giftedByName": giftedByName,
                        "quality": quality,
                        "color1": color1,
                        "color2": color2,
                        "howAcquired": howAcquired,
                        "location": "Wardrobe"
                    }
                }
            }
        )

        self.air.inventoryManager.sendUpdateToAvatarId(avId, "wardrobeItem", [
            itemId,
            [invId, itemId, slot, createdById, createdByName, giftedById, giftedByName, quality, color1, color2, howAcquired
        ]])

    def d_setPurchaseResponse(self, avId: int, success: bool) -> None:
        self.sendUpdateToAvatarId(avId, "setPurchase", [PURCHASE_SUCCESS if success else PURCHASE_FAIL])

    def purchasePouchItemsHelper(self, avId, itemId, amount):
        avatar = self.air.doId2do.get(avId)

        itemCount = amount
        itemSlot = -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def updateDNAHelper(self, avId, avatar, itemId, slotnum: int):
        # struct FairyDNA {
            #int16 talent; 0
            #int8 head; 1
            #int8 height; 2
            #int8 body; 3
            #int16 hair_back; 4
            #int16 hair_front; 5
            #int16 face; 6
            #int16 eye; 7
            #int16 wing; 8
            #int16 hair_color; 9
            #int16 hair_color2; 10
            #int16 eye_color; 11
            #int16 skin_color; 12
            #int16 wing_color; 13
            #int8 gender; 14
        # }
        dna = avatar.getFairyDNA()

        dnal = list(dna)
        dnal[slotnum] = itemId
        dna = tuple(dnal)

        avatar.b_setFairyDNA(dna)

        avatar.redrawFairy()
