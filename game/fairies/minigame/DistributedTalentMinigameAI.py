from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.MinigameConstants import MINIGAME_DAILY_CHANCE
from game.fairies.minigame.MinigameRewards import calc_rewards

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gameID: int = 0
        self.totalScore: int = 0
        self._pendingRewards: dict[int, list] = {}  # avId -> rewards list

    def setGameID(self, gameID: int) -> None:
        self.gameID = gameID

    def getGameID(self) -> int:
        return self.gameID

    def reportScore(self, score: int) -> None:
        if self.gameID == MINIGAME_DAILY_CHANCE:
            return
        self.totalScore += score
        print("reportScore", score, self.totalScore)

    def endGame(self, unknown: int) -> None:
        if self.gameID == MINIGAME_DAILY_CHANCE:
            # Daily Spin uses DistributedFairyPlayer.requestDailyChance, not minigame rewards.
            return

        print("endGame", unknown)

        avatarId = self.air.getAvatarIdFromSender()

        rewards = calc_rewards(self.gameID, self.totalScore)
        self._pendingRewards[avatarId] = rewards
        self.sendUpdateToAvatarId(avatarId, "setRewards", [rewards])
        self.totalScore = 0

    def chooseReward(self, rewardId: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"chooseReward: no avatar on AI for avId={avId}")
            return

        rewards = self._pendingRewards.get(avId)

        if not rewards:
            self.notify.warning(f"chooseReward: no pending rewards for avId={avId}")
            return

        if not isinstance(rewardId, int) or not (0 <= rewardId < len(rewards)):
            self.notify.warning(
                f"chooseReward: invalid rewardId={rewardId} "
                f"(rewards length={len(rewards)}, avId={avId})"
            )
            return

        chosenReward = rewards[rewardId]
        # Clear immediately so the client can't call chooseReward twice
        del self._pendingRewards[avId]

        itemID, itemCount = chosenReward.asTuple()
        itemSlot = -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemID, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))