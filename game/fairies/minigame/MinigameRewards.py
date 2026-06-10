from dataclasses import dataclass
import math
import game.fairies.ai.FairiesConstants as fc
from game.fairies.fairy.structs.Reward import Reward


# ════════════════════════════════════════════════════════════════════════════════════ #
#                               Game and Tier Definitions                              #
# ════════════════════════════════════════════════════════════════════════════════════ #
@dataclass(frozen=True)
class GameDef:
    id: int
    name: str
    badge_threshold: int
    ingredient_ids: tuple[int, int, int]  # (rare, uncommon, common)


GAMES = {
    g.id: g for g in [
        GameDef(2,  "Bubble Bounce",     15000,  (fc.LILY_PETALS, fc.DAISY_PETALS, fc.SPIDER_SILK)),
        GameDef(45, "Butterfly Painter", 50000,  (fc.LILY_PETALS, fc.BLUEBERRIES, fc.SUNFLOWER_SEEDS)),
        GameDef(10, "Fairy Fireworks",   50000,  (fc.OAK_LEAVES, fc.MAPLE_LEAVES, fc.DANDELION_FLUFF)),
        GameDef(1,  "Firefly Light-Up",  40000,  (fc.IVY, fc.MEADOW_GRASS, fc.SUNFLOWER_SEEDS)),
        GameDef(44, "First Flight",      85000,  (fc.OAK_LEAVES, fc.HONEYCOMBS, fc.SUNFLOWER_SEEDS)),
        GameDef(49, "Gem Juggle",        155000, (fc.IVY, fc.PINE_NEEDLES, fc.TWIGS)),
        GameDef(8,  "Harvest Hustle",    55000,  (fc.ACORNS, fc.BLUEBERRIES, fc.RASPBERRIES)),
        GameDef(9,  "Petal Pick-Up",     40000,  (fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.DAISY_PETALS)),
        GameDef(47, "Pinecone Pop",      100000, (fc.ACORNS, fc.PINE_NEEDLES, fc.SNOWFLAKES)),
        GameDef(43, "Seed Sorter",       130000, (fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.RASPBERRIES)),
        GameDef(11, "Snowflake Sweep",   50000,  (fc.IVY, fc.PINE_NEEDLES, fc.SNOWFLAKES)),
        GameDef(15, "Snowy Lullaby",     20000,  (fc.ACORNS, fc.MAPLE_LEAVES, fc.DANDELION_FLUFF)),
        GameDef(48, "Sunbeam Bend",      50000,  (fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.RASPBERRIES)),
        GameDef(14, "Tinker Toss",       70000,  (fc.OAK_LEAVES, fc.HONEYCOMBS, fc.TWIGS)),
        GameDef(7,  "Water Web",         110000, (fc.LILY_PETALS, fc.MEADOW_GRASS, fc.SPIDER_SILK)),
    ]
}

@dataclass(frozen=True)
class TierDef:
    max_qty: int
    power: float
    floor: int


TIERS = {
    "rare":     TierDef(max_qty=55, power=1.6, floor=0),
    "uncommon": TierDef(max_qty=110, power=1.2, floor=0),
    "common":   TierDef(max_qty=220, power=0.7, floor=1),
}

# K is solved so that norm=1.0 (badge score) yields 75% of max_qty.
# K = -ln(1 - 0.75)
K = -math.log(1 - 0.75)  # ≈ 1.3863


# ════════════════════════════════════════════════════════════════════════════════════ #
#                                    Core Algorithm                                    #
# ════════════════════════════════════════════════════════════════════════════════════ #
def calc_tier_reward(norm: float, tier: TierDef) -> int:
    """
    Return the ingredient quantity for one tier given a normalised score.

    norm        -- playerScore / badgeThreshold (can exceed 1.0)
    tier        -- TierDef with max_qty, power, and floor
    """
    if norm <= 0:
        return tier.floor
    raw = tier.max_qty * (1 - math.exp(-K * (norm ** tier.power)))
    return max(tier.floor, round(raw))


def calc_rewards(game_id: int, player_score: int) -> list[Reward]:
    """
    Return a list of Reward objects. (itemId, itemCount)

    game_id      -- must exist in GAMES
    player_score -- the player's final score for this run
    """
    game = GAMES[game_id]
    norm = player_score / game.badge_threshold
    results = []
    for ingredient_id, tier_def in zip(game.ingredient_ids, TIERS.values()):
        quantity = calc_tier_reward(norm, tier_def)
        if quantity > 0:
            results.append(Reward.unpackFromTuple((ingredient_id, quantity)))
    return results
