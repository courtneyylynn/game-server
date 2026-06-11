"""Daily Spin prize pool and roll logic."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import random
from typing import Callable

from game.fairies.meadow import IngredientSpawnData as isd


class Rarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    SUPER_RARE = "super_rare"


DEFAULT_WEIGHT_BY_RARITY: dict[Rarity, int] = {
    Rarity.COMMON: 100,
    Rarity.UNCOMMON: 40,
    Rarity.RARE: 10,
    Rarity.SUPER_RARE: 1,
}

USE_RARITY_WEIGHTS = True

# Per-index overrides take priority over DEFAULT_WEIGHT_BY_RARITY when set.
POOL_WEIGHT_BY_INDEX: dict[int, int] = {}
POOL_RARITY_BY_INDEX: dict[int, Rarity] = {}

DEFAULT_SPIN_INGREDIENT_AMOUNT = 1
# Pouch stack size on win; keyed off meadow spawn rarity in INGREDIENT_SPAWNS.
_MEADOW_RARITY_TO_SPIN_AMOUNT: dict[isd.Rarity, int] = {
    isd.Rarity.MOST_COMMON: 15,
    isd.Rarity.COMMON: 10,
    isd.Rarity.AVERAGE: 8,
    isd.Rarity.RARE: 5,
    isd.Rarity.VERY_RARE: 5,
}
SPIN_INGREDIENT_AMOUNT_BY_ID: dict[int, int] = {}

SPIN_INGREDIENT_IDS = frozenset(s.item_id for s in isd.INGREDIENT_SPAWNS)

RIVER_ROCK_ITEM_ID = 7665
_SPIN_DYE_IDS = frozenset({14183, 14052, 14043, 14129})

BADGE_ITEM_ID_MIN = 10000
BADGE_ITEM_ID_MAX = 12000

SPIN_BADGE_SOUR_PLUM = 10903
SPIN_BADGE_LUCKY_PURPLE_FEATHERS = 10902
SPIN_BADGE_SNEAKY_MR_TWITCHES = 11130
SPIN_BADGE_IDS = frozenset({
    SPIN_BADGE_SOUR_PLUM,
    SPIN_BADGE_LUCKY_PURPLE_FEATHERS,
    SPIN_BADGE_SNEAKY_MR_TWITCHES,
})

SPIN_BADGE_DEFAULT_RARITY: dict[int, Rarity] = {
    SPIN_BADGE_SOUR_PLUM: Rarity.UNCOMMON,
    SPIN_BADGE_LUCKY_PURPLE_FEATHERS: Rarity.RARE,
    SPIN_BADGE_SNEAKY_MR_TWITCHES: Rarity.SUPER_RARE,
}

SPIN_BADGE_MEMBER_ONLY_IDS = frozenset({SPIN_BADGE_SOUR_PLUM})

GENDER_BOTH = 3
GENDER_FAIRY = 1
GENDER_SPARROW = 2

CATEGORY_WARDROBE = "wardrobe"
CATEGORY_HOME = "home"
CATEGORY_POUCH = "pouch"
CATEGORY_INGREDIENT = "ingredient"
CATEGORY_BADGE = "badge"

FREE_ACORNS = 1
MEMBER_ACORNS = 3


@dataclass(frozen=True)
class DailyChancePrize:
    item_id: int
    amount: int
    color1: int
    color2: int
    gender: int
    category: str
    item_type: str
    pool_index: int
    rarity: Rarity | None = None
    weight: int | None = None

    def as_reward_ext(self) -> tuple[int, int, int, int]:
        return (self.item_id, self.amount, self.color1, self.color2)


def is_badge_item(item_id: int) -> bool:
    return BADGE_ITEM_ID_MIN <= item_id < BADGE_ITEM_ID_MAX


def is_spin_winnable_badge(item_id: int) -> bool:
    return item_id in SPIN_BADGE_IDS


def is_ingredient_item(item_id: int) -> bool:
    return item_id in SPIN_INGREDIENT_IDS


def _meadow_ingredient_spin_amount(spawn: isd.IngredientSpawnDef) -> int:
    return _MEADOW_RARITY_TO_SPIN_AMOUNT[spawn.rarity]


def spin_ingredient_amount(item_id: int) -> int:
    if item_id in SPIN_INGREDIENT_AMOUNT_BY_ID:
        return SPIN_INGREDIENT_AMOUNT_BY_ID[item_id]
    return _INGREDIENT_DEFAULT_AMOUNT.get(item_id, DEFAULT_SPIN_INGREDIENT_AMOUNT)


def home_item_type(item_id: int) -> str:
    if 7001 <= item_id <= 7099:
        return "Lamp"
    if 7501 <= item_id <= 7999:
        return "Decoration"
    return "Furniture"


def _ingredient_entries() -> list[tuple[int, int, int, int, str, str]]:
    return [
        (spawn.item_id, 0, 0, GENDER_BOTH, CATEGORY_INGREDIENT, "MiscItem")
        for spawn in isd.INGREDIENT_SPAWNS
    ]


_INGREDIENT_DEFAULT_AMOUNT: dict[int, int] = {
    spawn.item_id: _meadow_ingredient_spin_amount(spawn) for spawn in isd.INGREDIENT_SPAWNS
}


def _resolve_spin_rarity(
    pool_index: int,
    item_id: int,
    color1: int,
    color2: int,
    category: str,
    item_type: str,
) -> Rarity:
    if pool_index in POOL_RARITY_BY_INDEX:
        return POOL_RARITY_BY_INDEX[pool_index]
    if item_id in SPIN_BADGE_DEFAULT_RARITY:
        return SPIN_BADGE_DEFAULT_RARITY[item_id]
    if category == CATEGORY_INGREDIENT:
        return Rarity.COMMON
    if item_id == RIVER_ROCK_ITEM_ID:
        return Rarity.COMMON
    if item_id in _SPIN_DYE_IDS:
        return Rarity.UNCOMMON
    if category in (CATEGORY_WARDROBE, CATEGORY_HOME):
        return Rarity.RARE

    return Rarity.COMMON


def _entries() -> list[tuple[int, int, int, int, str, str]]:
    rows: list[tuple[int, int, int, int, str, str]] = []

    def w(item_id, c1, c2, gender, item_type):
        rows.append((item_id, c1, c2, gender, CATEGORY_WARDROBE, item_type))

    def h(item_id, c1, c2=0):
        rows.append((item_id, c1, c2 or c1, GENDER_BOTH, CATEGORY_HOME, home_item_type(item_id)))

    def d(item_id):
        rows.append((item_id, 0, 0, GENDER_BOTH, CATEGORY_POUCH, "MiscItem"))

    def badge(item_id):
        rows.append((item_id, 0, 0, GENDER_BOTH, CATEGORY_BADGE, "Talent"))

    # shared wardrobe
    w(2136, 141, 183, GENDER_BOTH, "HeadItem")

    # fairy wardrobe
    w(181, 183, 183, GENDER_FAIRY, "Shirt")
    w(576, 60, 60, GENDER_FAIRY, "Belt")
    w(1163, 183, 183, GENDER_FAIRY, "Skirt")
    w(3614, 183, 183, GENDER_FAIRY, "Shoes")
    w(2166, 191, 183, GENDER_FAIRY, "HeadItem")
    w(210, 191, 183, GENDER_FAIRY, "Shirt")
    w(1178, 191, 183, GENDER_FAIRY, "Skirt")
    w(2166, 191, 46, GENDER_FAIRY, "HeadItem")
    w(210, 191, 46, GENDER_FAIRY, "Shirt")
    w(1178, 191, 46, GENDER_FAIRY, "Skirt")
    w(2216, 55, 141, GENDER_FAIRY, "HeadItem")
    w(2209, 141, 141, GENDER_FAIRY, "HeadItem")
    w(2216, 55, 259, GENDER_FAIRY, "HeadItem")  # verify: Kiwi Green trim
    w(2209, 55, 121, GENDER_FAIRY, "HeadItem")
    w(2209, 55, 54, GENDER_FAIRY, "HeadItem")  # verify: Peony Pink trim
    w(2209, 141, 110, GENDER_FAIRY, "HeadItem")
    w(1657, 162, 162, GENDER_FAIRY, "WristItem")
    w(1656, 162, 162, GENDER_FAIRY, "WristItem")

    # sparrow wardrobe
    w(174, 183, 183, GENDER_SPARROW, "Shirt")
    w(573, 60, 60, GENDER_SPARROW, "Belt")
    w(1158, 183, 183, GENDER_SPARROW, "Skirt")
    w(3611, 183, 183, GENDER_SPARROW, "Shoes")
    w(2167, 191, 183, GENDER_SPARROW, "HeadItem")
    w(211, 191, 183, GENDER_SPARROW, "Shirt")
    w(1179, 191, 183, GENDER_SPARROW, "Skirt")
    w(2167, 191, 46, GENDER_SPARROW, "HeadItem")
    w(211, 191, 46, GENDER_SPARROW, "Shirt")
    w(1179, 191, 46, GENDER_SPARROW, "Skirt")
    w(2228, 55, 55, GENDER_SPARROW, "HeadItem")
    w(2215, 141, 141, GENDER_SPARROW, "HeadItem")
    w(2228, 55, 259, GENDER_SPARROW, "HeadItem")  # verify: Kiwi Green trim
    w(2215, 55, 55, GENDER_SPARROW, "HeadItem")
    w(2304, 55, 54, GENDER_SPARROW, "HeadItem")  # verify: Peony Pink trim
    w(2215, 141, 110, GENDER_SPARROW, "HeadItem")
    w(1654, 162, 162, GENDER_SPARROW, "WristItem")
    w(1655, 162, 162, GENDER_SPARROW, "WristItem")

    # home
    h(6655, 33)
    h(6654, 183)
    h(6734, 46)
    h(6735, 116)
    h(6734, 116)
    h(7028, 46)
    h(7640, 46)
    h(7616, 129)
    h(7639, 17)
    h(7641, 60)
    h(7598, 183)
    h(7668, 183)
    h(7667, 183)
    h(7728, 30)
    h(7738, 13)
    h(7734, 191)
    h(7785, 186)
    for rock_color in (37, 150, 116, 61, 110, 109):
        h(7665, rock_color)

    rows.extend(_ingredient_entries())

    d(14183)
    d(14052)
    d(14043)
    d(14129)

    badge(SPIN_BADGE_SOUR_PLUM)
    badge(SPIN_BADGE_LUCKY_PURPLE_FEATHERS)
    badge(SPIN_BADGE_SNEAKY_MR_TWITCHES)

    return rows


def _prize_amount(item_id: int, category: str) -> int:
    if category == CATEGORY_INGREDIENT:
        return spin_ingredient_amount(item_id)
    return 1


def _build_pool() -> tuple[DailyChancePrize, ...]:
    pool: list[DailyChancePrize] = []
    for index, (item_id, c1, c2, gender, category, item_type) in enumerate(_entries()):
        rarity = _resolve_spin_rarity(index, item_id, c1, c2, category, item_type)
        pool.append(
            DailyChancePrize(
                item_id=item_id,
                amount=_prize_amount(item_id, category),
                color1=c1,
                color2=c2,
                gender=gender,
                category=category,
                item_type=item_type,
                pool_index=index,
                rarity=rarity,
            )
        )
    for prize in pool:
        if is_badge_item(prize.item_id) and prize.item_id not in SPIN_BADGE_IDS:
            raise ValueError(f"unexpected badge in daily spin pool: {prize.item_id}")
        if prize.category == CATEGORY_INGREDIENT and prize.item_id not in SPIN_INGREDIENT_IDS:
            raise ValueError(f"unexpected ingredient in daily spin pool: {prize.item_id}")
    return tuple(pool)


POOL: tuple[DailyChancePrize, ...] = _build_pool()

SPIN_BADGE_POOL_BIT: dict[int, int] = {
    prize.item_id: (1 << prize.pool_index)
    for prize in POOL
    if prize.item_id in SPIN_BADGE_IDS
}

DEV_TEST_PRIZE = next(p for p in POOL if p.category == CATEGORY_INGREDIENT)


def owned_spin_badge_exclude_mask(earned_badge_ids: set[int]) -> int:
    # Bits for spin badges already earned; merged into excludeMask before roll_rewards.
    mask = 0
    for badge_id in earned_badge_ids:
        mask |= SPIN_BADGE_POOL_BIT.get(badge_id, 0)
    return mask


def acorn_count(is_member: bool) -> int:
    return MEMBER_ACORNS if is_member else FREE_ACORNS


def is_gender_eligible(prize: DailyChancePrize, avatar_gender: int) -> bool:
    if prize.category != CATEGORY_WARDROBE:
        return True
    if prize.gender == GENDER_BOTH:
        return True
    return prize.gender == avatar_gender


def filter_pool(
    exclude_mask: int, avatar_gender: int, is_member: bool = False
) -> list[DailyChancePrize]:
    return [
        prize
        for prize in POOL
        if not (exclude_mask & (1 << prize.pool_index))
        and is_gender_eligible(prize, avatar_gender)
        and not (
            prize.item_id in SPIN_BADGE_MEMBER_ONLY_IDS and not is_member
        )
    ]


def prize_rarity(prize: DailyChancePrize) -> Rarity:
    if prize.rarity is not None:
        return prize.rarity
    return Rarity.COMMON


def prize_roll_weight(prize: DailyChancePrize) -> int:
    if not USE_RARITY_WEIGHTS:
        return 1
    if prize.weight is not None:
        return prize.weight
    if prize.pool_index in POOL_WEIGHT_BY_INDEX:
        return POOL_WEIGHT_BY_INDEX[prize.pool_index]
    return DEFAULT_WEIGHT_BY_RARITY[prize_rarity(prize)]


def weighted_sample_without_replacement(
    candidates: list[DailyChancePrize],
    count: int,
    weight_fn: Callable[[DailyChancePrize], int] | None = None,
) -> list[DailyChancePrize]:
    if count <= 0 or not candidates:
        return []

    weight_fn = weight_fn or prize_roll_weight
    remaining = list(candidates)
    chosen: list[DailyChancePrize] = []

    for _ in range(min(count, len(remaining))):
        weights = [max(0, weight_fn(prize)) for prize in remaining]
        total = sum(weights)
        if total <= 0:
            break

        pick = random.choices(remaining, weights=weights, k=1)[0]
        chosen.append(pick)
        remaining.remove(pick)

    return chosen


def roll_rewards(
    exclude_mask: int, is_member: bool, avatar_gender: int
) -> list[DailyChancePrize]:
    eligible = filter_pool(exclude_mask, avatar_gender, is_member)
    count = min(acorn_count(is_member), len(eligible))

    if count <= 0:
        return []

    return weighted_sample_without_replacement(eligible, count)
