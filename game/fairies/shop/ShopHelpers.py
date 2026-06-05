from dataclasses import dataclass, field
from game.fairies.fairy.structs.FairyDNA import FairyDNA
from game.fairies.fairy.structs.ShopCollection import ShopCollection

@dataclass
class Shopkeeper:
    name: str
    position: tuple
    famousFairyId: int
    fairyDNA: FairyDNA = field(default_factory=FairyDNA)
    gender: int = 1

    def __post_init__(self):
        self.fairyDNA.gender = self.gender

    def to_tuple(self) -> tuple:
        return (self.name, self.fairyDNA.asTuple(), self.position, self.famousFairyID)

@dataclass
class NPCShop():
    zone: int
    shopId: int
    shopkeeper: Shopkeeper
    collections: list[ShopCollection] = field(default_factory=list)

    def generate_shop(self, DFS_NPCAI):
        shop = DFS_NPCAI
        shop.setShopId(self.shopId)
        shop.setName(self.shopkeeper.name)
        shop.setFairyDNA(self.shopkeeper.fairyDNA.asTuple())
        shop.setPosition(self.shopkeeper.position[0], self.shopkeeper.position[1])
        shop.setFamousFairyId(self.shopkeeper.famousFairyId)
        shop.setRoomID(1)
        shop.setShopItems(tuple(c.asTuple() for c in self.collections))
        if self.shopId == 2000: # Daisy's Dyes
             shop.setDyePrice(8014, 4, 4, 0, 0)
        shop.generateWithRequired(self.zone)
