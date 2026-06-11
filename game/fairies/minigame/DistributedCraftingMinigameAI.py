import os
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.recipe import recipe_parser
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.ai.FairiesConstants import get_item_type

DEFAULT_XML = os.path.join(os.path.dirname(__file__), "recipe/recipes.xml")

class DistributedCraftingMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.professionId: int = 1
        self.recipeId = 0
        self.craftingStyle: int = 0

    def setProfessionID(self, professionId: int):
        # CRAFT_TYPE_TAILORING = 0
        # CRAFT_TYPE_BAKING = 1
        # CRAFT_TYPE_TINKERING = 2
        self.professionId = professionId

    def getProfessionID(self) -> int:
        return self.professionId

    def setCommunityDyeIDList(self):
        # Array of dye IDs
        pass

    def getCommunityDyeIDList(self) -> list:
        return [45, 50, 53, 54, 38]

    def setRecipeChoice(self, recId, style):
        # Current Recipe ID, 1 or 2
        # CRAFT_STYLE_COMMUNITY = 2
        # CRAFT_STYLE_PERSONAL = 1
        self.recipeId = recId
        self.craftingStyle = style

    def setResults(self, recipeId, quality, color1, color2, length):
        if self.craftingStyle == 2:
            print("PRACTICE BAIL")
            return # don't take stuff if practice baking
        
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        recipes = recipe_parser.parse_recipes(DEFAULT_XML, recipeId)
        if not recipes:
            print("something broke - fix it or else you dummy dumbo dimwit")
            return
        recipe = recipes[0]

        self._removeRecipeIngredients(avId, avatar, recipe)
        self._removeDyes(avId, avatar, color1, color2)

        if recipeId in BAKED_ITEMS:
            self._giveBakedItem(avId, avatar, recipeId, quality)
        else:
            self._giveCraftedItem(avId, avatar, recipeId, quality, color1, color2)

    def _removeRecipeIngredients(self, avId, avatar, recipe):
        for ingredient in recipe.ingredients:
            self.air.inventoryManager.removeIngredientsFromPouch(avId, ingredient.item_id, ingredient.amount)
        avatar.d_syncPouchAfterChanges()

    def _removeDyes(self, avId, avatar, color1, color2):
        for color in (color1, color2):
            if color:
                dye_id = color + 14000
                self.air.inventoryManager.removeIngredientsFromPouch(avId, dye_id, 1)
        if color1 or color2:
            avatar.d_syncPouchAfterChanges()

    def _giveBakedItem(self, avId, avatar, itemId, quality):
        if 96 <= quality <= 100:
            amount = 6
        elif 81 <= quality <= 95:
            amount = 3
        else:
            amount = 2

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, amount, -1):
            print("adding:", itemId, amount)
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def _giveCraftedItem(self, avId, avatar, recipeId, quality, color1, color2):
        
        if get_item_type(recipeId) in ("Furniture", "Lamp", "Decoration"):
            self._grant_home(avId, avatar, recipeId, quality, color1, color2)
        else:
            self._grant_wardrobe(avId, avatar, recipeId, quality, color1, color2)


    def _grant_wardrobe(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
        inv_id = self.air.mongoInterface.getNextDoId()
        itemType = get_item_type(recipeId)
        how_acquired = 11

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": inv_id,
                        "type": itemType,
                        "item_id": recipeId,
                        "slot": -1,
                        "createdById": avId,
                        "createdByName": avatar.getName(),
                        "giftedById": 0,
                        "giftedByName": "",
                        "quality": quality,
                        "color1": color1,
                        "color2": color2,
                        "howAcquired": how_acquired,
                        "location": "Wardrobe",
                    }
                }
            },
        )

        if result.modified_count == 0:
            return False

        self.air.inventoryManager.sendUpdateToAvatarId(
            avId,
            "wardrobeItem",
            [
                recipeId,
                [
                    inv_id,
                    recipeId,
                    -1,
                    avId,
                    avatar.getName(),
                    0,
                    "",
                    quality,
                    color1,
                    color2,
                    how_acquired,
                ],
            ],
        )
        return True


    def _grant_home(self, avId, avatar, recipeId, quality, color1, color2) -> bool:
        inv_id = self.air.mongoInterface.getNextDoId()
        itemType = get_item_type(recipeId)
        how_acquired = 11

        inv_item_ext = [
            inv_id,
            recipeId,
            -1,
            avId,
            avatar.getName(),
            0,
            "",
            quality,
            color1,
            color2,
            how_acquired,
        ]

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": inv_id,
                        "type": itemType,
                        "item_id": recipeId,
                        "slot": -1,
                        "createdById": avId,
                        "createdByName": avatar.getName(),
                        "giftedById": 0,
                        "giftedByName": "",
                        "quality": quality,
                        "color1": color1,
                        "color2": color2,
                        "howAcquired": how_acquired,
                        "location": "Storage",
                    }
                }
            },
        )

        if result.modified_count == 0:
            return False

        self.air.inventoryManager.sendUpdateToAvatarId(
            avId, "storageItem", [recipeId, inv_item_ext]
        )
        return True

    def setEmbellishResults(self):
        # Seems to be empty function in Client
        pass

    def craftingResponse(self):
        # If param1 !=1 throws an App Panic with invalidCraftError
        pass
