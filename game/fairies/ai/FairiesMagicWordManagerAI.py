from direct.distributed.DistributedObjectAI import DistributedObjectAI

class FairiesMagicWordManagerAI(DistributedObjectAI):
    notify = directNotify.newCategory("FairiesMagicWordManagerAI")

    def __init__(self, air) -> None:
        super().__init__(air)

        self.identifier: int = 0

    def setMagicWord(self, magicWord: str, avId: int, zoneId: int, signature: str):
        av = self.air.doId2do.get(avId)

        if not av:
            self.notify.warning(f"setMagicWord from unknown avatar {avId}")
            return

        mw_parts = magicWord.split(" ")
        command = mw_parts[0]
        args = mw_parts[1:]

        if command == "set-level":
            av.b_setLevel(int(args[0]))

        # TODO: Implement magic words located in `LiveMod`, etc.
        # For now, we will just send back a test response.
        self.sendUpdateToAvatarId(av.doId, "setMagicWordResponse", ["Test response from server!"])

    def setID(self, identifier: int) -> None:
        self.identifier = identifier

    def getID(self) -> int:
        return self.identifier
