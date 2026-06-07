"""
Ingredient spawn configuration — single source of truth for meadow ingredient spawning.

This file is DATA ONLY. Runtime spawning is handled by IngredientSpawnMgrAI.py, which
calls build_active_spawn_pools() at server startup and creates one SpawnPool per
active (zone_id, item_id) pair.

File layout (top to bottom)
---------------------------
1. Meadow Groups      — zone ID tuples grouped by season (Autumn, Spring, etc.)
2. Rarity             — spawn density and respawn timing per rarity tier
3. Zone Map Bounds    — full-map random spawn area per meadow
4. Exclusion Zones    — keep-out areas for signs/gateways (TODO, not yet populated)
5. Ingredient Defs    — which ingredients exist, their rarity, and eligible zones
6. Future Ingredients — disabled entries for zones not yet in the game
7. Build Helpers      — pool construction for the AI server

How spawning works
------------------
Items do NOT have fixed or per-item spawn spots. For each (ingredient, zone) pair
listed in INGREDIENT_SPAWNS, the engine picks random (x, y) within that zone's
ZONE_MAP_BOUNDS rectangle. Position is random every spawn and respawn.

To add an ingredient to a meadow: add the zone to that ingredient's zones tuple
in INGREDIENT_SPAWNS. No per-item coordinate tables needed.

To enable a new meadow: add an entry to ZONE_MAP_BOUNDS (and ZONE_EXCLUSIONS).

How to tune spawn density
-------------------------
Edit RARITY_SPAWN_SETTINGS — stack count and respawn seconds apply to every
ingredient of that rarity in every zone. No engine changes needed.

Related files
-------------
- IngredientSpawnMgrAI.py  — spawns/collects/respawns DistributedSpawnStackAI objects
- GatewayConstants.py      — gateway/sign positions (for future exclusion zones)
- web-main/meadows/zone###/config.xml — ground layer dimensions for ZONE_MAP_BOUNDS
- FairiesConstants.py      — ingredient item IDs (fc.ACORNS, etc.)
- ZoneConstants.py         — meadow zone IDs (zc.ACORN_SUMMIT, etc.)

TODO (future work)
------------------
- Populate ZONE_EXCLUSIONS with rectangular keep-out zones around gateways/signs
  (positions from GatewayConstants.GATEWAYS; use exclusion_rect() helper)
- Optionally auto-generate exclusions via _build_gateway_exclusions()
- Add BUBBLY_BOG, SILVER_TREES, NEVER_MINE to ZoneConstants and enable
  FUTURE_INGREDIENT_SPAWNS
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import NamedTuple

from direct.directnotify import DirectNotifyGlobal
from game.fairies.ai import FairiesConstants as fc
from game.fairies.ai import ZoneConstants as zc
from game.fairies.gateway import GatewayConstants as gc

notify = DirectNotifyGlobal.directNotify.newCategory("IngredientSpawnData")

# =============================================================================
# Meadow Groups
#
# Reusable zone ID tuples. Referenced by INGREDIENT_SPAWNS to declare which
# meadows an ingredient can appear in without listing every zone individually.
# =============================================================================

AUTUMN_MEADOWS = (
    zc.ACORN_SUMMIT,
    zc.MAPLE_TREE_HILL,
    zc.COTTONPUFF_FIELD,
    zc.PUMPKIN_PATCH,
)

SPRING_MEADOWS = (
    zc.SPRINGTIME_ORCHARD,
    zc.TREETOP_BEND,
    zc.NEVERBERRY_THICKET,
    zc.CHERRYBLOSSOM_HEIGHTS,
    zc.DEWDROP_VALE,
)

WINTER_MEADOWS = (
    zc.CHILLY_FALLS,
    zc.EVERGREEN_OVERLOOK,
    zc.SNOWCAP_GLADE,
)

SUMMER_MEADOWS = (
    zc.PALM_TREE_COVE,
    zc.NEVERFRUIT_GROVE,
    zc.SUNFLOWER_GULLY,
)

HAVENDISH_SQUARE = (zc.HAVENDISH_SQUARE,)


# =============================================================================
# Rarity
#
# Controls how many stacks exist per zone and how long before one respawns
# after collection. Applied automatically based on each ingredient's rarity.
#
#   Tier         | Stacks/zone | Respawn
#   Most Common  | 7           | 2 min
#   Common       | 5           | 2 min
#   Average      | 3           | 3 min
#   Rare         | 2           | 3 min
#   Very Rare    | 1           | 4 min
# =============================================================================

class Rarity(Enum):
    MOST_COMMON = auto()
    COMMON = auto()
    AVERAGE = auto()
    RARE = auto()
    VERY_RARE = auto()


@dataclass(frozen=True)
class RaritySpawnSettings:
    max_stacks: int
    respawn_min_sec: int
    respawn_max_sec: int


RARITY_SPAWN_SETTINGS: dict[Rarity, RaritySpawnSettings] = {
    Rarity.MOST_COMMON: RaritySpawnSettings(max_stacks=7, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.COMMON: RaritySpawnSettings(max_stacks=5, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.AVERAGE: RaritySpawnSettings(max_stacks=3, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.RARE: RaritySpawnSettings(max_stacks=2, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.VERY_RARE: RaritySpawnSettings(max_stacks=1, respawn_min_sec=240, respawn_max_sec=240),
}


# =============================================================================
# Zone Map Bounds
#
# Random spawn area per meadow — all eligible ingredients in a zone pick random
# (x, y) within this rectangle. Derived from config.xml ground layer dimensions
# minus SPAWN_EDGE_MARGIN. No per-item spot configuration.
# =============================================================================

class SpawnBounds(NamedTuple):
    x_min: int
    x_max: int
    y_min: int
    y_max: int


SPAWN_EDGE_MARGIN = 100


def _map_bounds(width: int, height: int, margin: int = SPAWN_EDGE_MARGIN) -> SpawnBounds:
    return SpawnBounds(margin, width - margin, margin, height - margin)


# Full-map spawn bounds per meadow (from web-main/meadows/zone###/config.xml ground layer)
ZONE_MAP_BOUNDS: dict[int, SpawnBounds] = {
    zc.CHERRYBLOSSOM_HEIGHTS: _map_bounds(1907, 1131),
    zc.SPRINGTIME_ORCHARD: _map_bounds(1922, 1130),
    zc.DEWDROP_VALE: _map_bounds(1402, 1589),
    zc.NEVERBERRY_THICKET: _map_bounds(2021, 1190),
    zc.TREETOP_BEND: _map_bounds(1711, 1489),
    zc.ACORN_SUMMIT: _map_bounds(1896, 1115),
    zc.COTTONPUFF_FIELD: _map_bounds(1895, 1307),
    zc.MAPLE_TREE_HILL: _map_bounds(1269, 1827),
    zc.PUMPKIN_PATCH: _map_bounds(1733, 1019),
    zc.EVERGREEN_OVERLOOK: _map_bounds(1271, 1827),
    zc.SNOWCAP_GLADE: _map_bounds(2548, 1011),
    zc.CHILLY_FALLS: _map_bounds(1255, 1781),
    zc.PALM_TREE_COVE: _map_bounds(1960, 1204),
    zc.SUNFLOWER_GULLY: _map_bounds(1115, 1603),
    zc.NEVERFRUIT_GROVE: _map_bounds(1464, 1000),
    zc.HAVENDISH_SQUARE: _map_bounds(2166, 1509),
}


def zone_map_bounds(zone_id: int) -> SpawnBounds:
    return ZONE_MAP_BOUNDS[zone_id]


# =============================================================================
# Exclusion Zones
#
# Rectangular keep-out areas where items must NOT spawn (signs, gateways, etc.).
# Uses the same SpawnBounds shape as map bounds. Shared by all ingredients in a
# zone. Enforced by IngredientSpawnMgrAI once entries are added here.
# =============================================================================

# Rectangular exclusion zone — same fields as SpawnBounds (x_min, x_max, y_min, y_max).
SpawnExclusionZone = SpawnBounds


def exclusion_rect(x_min: int, x_max: int, y_min: int, y_max: int) -> SpawnExclusionZone:
    return SpawnExclusionZone(x_min, x_max, y_min, y_max)

DEFAULT_SIGN_WIDTH = 160 # averages for normal signs
DEFAULT_SIGN_HEIGHT = 190

def exclusion_rect_around(
    origin_x: int,
    origin_y: int,
    padding: int = 120,
    sign_width: int = DEFAULT_SIGN_WIDTH,
    sign_height: int = DEFAULT_SIGN_HEIGHT,
) -> SpawnExclusionZone:
    """Build a keep-out rectangle from the upper-left corner of a sign/gateway."""
    half_w = sign_width // 2
    half_h = sign_height // 2
    center_x = origin_x + half_w
    center_y = origin_y + half_h
    return SpawnExclusionZone(
        center_x - half_w - padding,
        center_x + half_w + padding,
        center_y - half_h - padding,
        center_y + half_h + padding,
    )

def _build_gateway_exclusions(zone_id: int) -> tuple[SpawnExclusionZone, ...]:
    """Derive keep-out rectangles from GatewayConstants.GATEWAYS[zone_id] positions."""
    return tuple(
        exclusion_rect_around(*gw["position"], *gw.get("sign_size", (DEFAULT_SIGN_WIDTH, DEFAULT_SIGN_HEIGHT)))
        for gw in gc.GATEWAYS.get(zone_id, [])
        if gw["name"] not in _MANUAL_EXCLUSION_GATEWAY_NAMES
    )


# Gateway names with hand-tuned rects below (skip auto keep-out for those signs).
_MANUAL_EXCLUSION_GATEWAY_NAMES = frozenset({"9278"})

#       Gateway positions are in GatewayConstants.GATEWAYS[zone_id]["position"].
ZONE_EXCLUSIONS: dict[int, tuple[SpawnExclusionZone, ...]] = {
    zc.CHERRYBLOSSOM_HEIGHTS: _build_gateway_exclusions(zc.CHERRYBLOSSOM_HEIGHTS),
    zc.SPRINGTIME_ORCHARD: _build_gateway_exclusions(zc.SPRINGTIME_ORCHARD),
    zc.DEWDROP_VALE: _build_gateway_exclusions(zc.DEWDROP_VALE),
    zc.NEVERBERRY_THICKET: _build_gateway_exclusions(zc.NEVERBERRY_THICKET),
    zc.TREETOP_BEND: _build_gateway_exclusions(zc.TREETOP_BEND),
    zc.ACORN_SUMMIT: _build_gateway_exclusions(zc.ACORN_SUMMIT),
    zc.COTTONPUFF_FIELD: _build_gateway_exclusions(zc.COTTONPUFF_FIELD),
    zc.MAPLE_TREE_HILL: _build_gateway_exclusions(zc.MAPLE_TREE_HILL),
    zc.PUMPKIN_PATCH: _build_gateway_exclusions(zc.PUMPKIN_PATCH),
    zc.EVERGREEN_OVERLOOK: _build_gateway_exclusions(zc.EVERGREEN_OVERLOOK),
    zc.SNOWCAP_GLADE: _build_gateway_exclusions(zc.SNOWCAP_GLADE),
    zc.CHILLY_FALLS: _build_gateway_exclusions(zc.CHILLY_FALLS),
    zc.PALM_TREE_COVE: _build_gateway_exclusions(zc.PALM_TREE_COVE),
    zc.SUNFLOWER_GULLY: _build_gateway_exclusions(zc.SUNFLOWER_GULLY),
    zc.NEVERFRUIT_GROVE: (
        # Pixie Post Office (gateway 9278) — anchor (337,140) != clickable footprint
        exclusion_rect(20, 870, 5, 530),
    ) + _build_gateway_exclusions(zc.NEVERFRUIT_GROVE),
    zc.HAVENDISH_SQUARE: _build_gateway_exclusions(zc.HAVENDISH_SQUARE),
}

# =============================================================================
# Ingredient Definitions
#
# INGREDIENT_SPAWNS — master list of all collectible ingredients. Each entry
# declares item ID, display name, rarity, and which zones it can spawn in.
# Spawn position within a zone is random (see ZONE_MAP_BOUNDS).
#
# ActiveSpawnPool — runtime config built by build_active_spawn_pools(); consumed
# by IngredientSpawnMgrAI.SpawnPool (one pool per active zone+item pair).
# =============================================================================

@dataclass(frozen=True)
class IngredientSpawnDef:
    item_id: int
    display_name: str
    rarity: Rarity
    zones: tuple[int, ...]
    enabled: bool = True


@dataclass(frozen=True)
class ActiveSpawnPool:
    zone_id: int
    item_id: int
    display_name: str
    rarity: Rarity
    bounds: SpawnBounds
    max_stacks: int
    respawn_min_sec: int
    respawn_max_sec: int
    exclusions: tuple[SpawnExclusionZone, ...] = ()


INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    IngredientSpawnDef(fc.ACORNS, "Acorn", Rarity.RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.BLUEBERRIES, "Blueberries", Rarity.AVERAGE, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.BUTTERCUP_PETALS, "Buttercup Petals", Rarity.AVERAGE, SPRING_MEADOWS),
    IngredientSpawnDef(fc.DAISY_PETALS, "Daisy Petals", Rarity.COMMON, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.DANDELION_FLUFF, "Dandelion Fluff", Rarity.MOST_COMMON, AUTUMN_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.HONEYCOMBS, "Honeycombs", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.IVY, "Ivy Leaves", Rarity.VERY_RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.LILY_PETALS, "Lily Petals", Rarity.VERY_RARE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.MAPLE_LEAVES, "Maple Leaf", Rarity.COMMON, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.MEADOW_GRASS, "Meadow Grass", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.OAK_LEAVES, "Oak Leaves", Rarity.RARE, AUTUMN_MEADOWS + (zc.SNOWCAP_GLADE,)),
    IngredientSpawnDef(fc.PINE_NEEDLES, "Pine Needles", Rarity.AVERAGE, WINTER_MEADOWS + (zc.ACORN_SUMMIT,)),
    IngredientSpawnDef(fc.RASPBERRIES, "Raspberries", Rarity.COMMON, SPRING_MEADOWS + (zc.NEVERFRUIT_GROVE,)),
    IngredientSpawnDef(fc.ROSE_PETALS, "Rose Petals", Rarity.RARE, SPRING_MEADOWS),
    IngredientSpawnDef(fc.SNOWFLAKES, "Snowflakes", Rarity.MOST_COMMON, WINTER_MEADOWS),
    IngredientSpawnDef(fc.SPIDER_SILK, "Spider Silk", Rarity.MOST_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.SUNFLOWER_SEEDS, "Sunflower Seeds", Rarity.MOST_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.TWIGS, "Twigs", Rarity.MOST_COMMON, AUTUMN_MEADOWS + WINTER_MEADOWS),
)


# =============================================================================
# Future Ingredients
#
# Disabled entries for ingredients/locations not yet in the game. To enable:
#   1. Add zone IDs to ZoneConstants (e.g. BUBBLY_BOG)
#   2. Add ZONE_MAP_BOUNDS and ZONE_EXCLUSIONS entries for those zones
#   3. Set zones on the IngredientSpawnDef and enabled=True (or move to INGREDIENT_SPAWNS)
# =============================================================================

# TODO: add BUBBLY_BOG, SILVER_TREES, NEVER_MINE to ZoneConstants
FUTURE_INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    IngredientSpawnDef(fc.TRUFFLES, "Truffles", Rarity.MOST_COMMON, (), enabled=False),
    IngredientSpawnDef(fc.FEATHERS, "Feathers", Rarity.COMMON, (), enabled=False),
    IngredientSpawnDef(fc.YELLOW_GEMS, "Yellow Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BLUE_GEMS, "Blue Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BITS_OF_METAL, "Bits of Metal", Rarity.RARE, (), enabled=False),
)


def _validate_zone_map_bounds() -> None:
    """Raise if any enabled ingredient references a zone missing from ZONE_MAP_BOUNDS."""
    missing: set[int] = set()

    for ingredient in INGREDIENT_SPAWNS:
        if not ingredient.enabled:
            continue

        for zone_id in ingredient.zones:
            if zone_id not in ZONE_MAP_BOUNDS:
                missing.add(zone_id)

    if missing:
        raise ValueError(
            "Missing ZONE_MAP_BOUNDS for zone IDs: %s"
            % ", ".join(str(z) for z in sorted(missing))
        )


def build_active_spawn_pools() -> list[ActiveSpawnPool]:
    """Build runtime spawn configs for every enabled (zone, ingredient) pair."""
    _validate_zone_map_bounds()

    pools: list[ActiveSpawnPool] = []

    for ingredient in INGREDIENT_SPAWNS:
        if not ingredient.enabled:
            continue

        settings = RARITY_SPAWN_SETTINGS[ingredient.rarity]

        for zone_id in ingredient.zones:
            bounds = ZONE_MAP_BOUNDS.get(zone_id)
            if bounds is None:
                continue

            pools.append(
                ActiveSpawnPool(
                    zone_id=zone_id,
                    item_id=ingredient.item_id,
                    display_name=ingredient.display_name,
                    rarity=ingredient.rarity,
                    bounds=bounds,
                    max_stacks=settings.max_stacks,
                    respawn_min_sec=settings.respawn_min_sec,
                    respawn_max_sec=settings.respawn_max_sec,
                    exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
                )
            )

    return pools
