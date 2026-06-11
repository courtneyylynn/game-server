from collections.abc import Sequence

from direct.distributed.DistributedObjectAI import DistributedObjectAI

from game.fairies.fairy.structs.FairyDNA import FairyDNA
from game.fairies.fairy.structs.FairyPose import FairyPose

from game.fairies.fairy.structs.LiteInvItemExt import LiteInvItemExt

class DistributedFairyBaseAI(DistributedObjectAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.name: str = ""

        self.position: tuple[int, int] = (0, 0)
        self.rotation: int = 0

        self.fairyDNA: FairyDNA = FairyDNA()

        self.fairyPose: FairyPose = FairyPose()

        self.headItem: LiteInvItemExt = LiteInvItemExt()
        self.necklace: LiteInvItemExt = LiteInvItemExt()
        self.chestItem: LiteInvItemExt = LiteInvItemExt()
        self.belt: LiteInvItemExt = LiteInvItemExt()
        self.skirt: LiteInvItemExt = LiteInvItemExt()
        self.wrist: LiteInvItemExt = LiteInvItemExt()
        self.ankle: LiteInvItemExt = LiteInvItemExt()
        self.shoes: LiteInvItemExt = LiteInvItemExt()

        self.roomID: int = 0

    def setName(self, name: str) -> None:
        self.name = name

    def d_setName(self, name: str) -> None:
        self.sendUpdate("setName", [name])

    def b_setName(self, name: str) -> None:
        self.setName(name)
        self.d_setName(name)

    def getName(self) -> str:
        return self.name

    def setPosition(self, x: int, y: int) -> None:
        self.position = (x, y)

    def getPosition(self) -> tuple[int, int]:
        return self.position

    def setRotation(self, rotation: int) -> None:
        self.rotation = rotation

    def getRotation(self) -> int:
        return self.rotation

    def setFairyDNA(self, fairyDNA: Sequence[int]) -> None:
        self.fairyDNA = FairyDNA.unpackFromTuple(fairyDNA)

    def d_setFairyDNA(self, fairyDNA: Sequence[int]):
        self.sendUpdate("setFairyDNA", [fairyDNA])

    def b_setFairyDNA(self, fairyDNA: Sequence[int]):
        self.setFairyDNA(fairyDNA)
        self.d_setFairyDNA(fairyDNA)

    def getFairyDNA(self) -> tuple[int, ...]:
        return self.fairyDNA.asTuple()

    def setFairyPose(self, fairyPose: Sequence[int]) -> None:
        self.fairyPose = FairyPose.unpackFromTuple(fairyPose)

    def getFairyPose(self) -> tuple[int, ...]:
        return self.fairyPose.asTuple()

    def setHeadItem(self, item: Sequence[int]) -> None:
        self.headItem = LiteInvItemExt.unpackFromTuple(item)

    def getHeadItem(self) -> tuple[int, ...]:
        return self.headItem.asTuple()

    def setNecklace(self, item: Sequence[int]) -> None:
        self.necklace = LiteInvItemExt.unpackFromTuple(item)

    def getNecklace(self) -> tuple[int, ...]:
        return self.necklace.asTuple()

    def setChestItem(self, item: Sequence[int]) -> None:
        self.chestItem = LiteInvItemExt.unpackFromTuple(item)

    def getChestItem(self) -> tuple[int, ...]:
        return self.chestItem.asTuple()

    def setBelt(self, item: Sequence[int]) -> None:
        self.belt = LiteInvItemExt.unpackFromTuple(item)

    def getBelt(self) -> tuple[int, ...]:
        return self.belt.asTuple()

    def setSkirt(self, item: Sequence[int]) -> None:
        self.skirt = LiteInvItemExt.unpackFromTuple(item)

    def getSkirt(self) -> tuple[int, ...]:
        return self.skirt.asTuple()

    def setWrist(self, item: Sequence[int]) -> None:
        self.wrist = LiteInvItemExt.unpackFromTuple(item)

    def getWrist(self) -> tuple[int, ...]:
        return self.wrist.asTuple()

    def setAnkle(self, item: Sequence[int]) -> None:
        self.ankle = LiteInvItemExt.unpackFromTuple(item)

    def getAnkle(self) -> tuple[int, ...]:
        return self.ankle.asTuple()

    def setShoes(self, item: Sequence[int]) -> None:
        self.shoes = LiteInvItemExt.unpackFromTuple(item)

    def getShoes(self) -> tuple[int, ...]:
        return self.shoes.asTuple()

    def setRoomID(self, roomID: int) -> None:
        self.roomID = roomID

    def getRoomID(self) -> int:
        return self.roomID
