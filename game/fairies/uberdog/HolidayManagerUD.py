from direct.distributed.DistributedObjectUD import DistributedObjectUD

class HolidayManagerUD(DistributedObjectUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def getTimeSpan(self) -> list[str]:
        return [
            "Meadow_Summer",
            "Tearoom_Summer",
            "Meadow_Theater_Camp",
            "Meadow_Camp2013",
            "Meadow_Decorations_SummmerSplash",
            "Meadow_SummerSplash",
            "Meadow_CampPixie2012",
            "Emote_Camp"
        ]

    def getTimeSpanMessage(self) -> str:
        return "Welcome to the test server. Missing features and bugs are to be expected. Enjoy!"

    def getShopsOpen(self) -> int:
        return 1
