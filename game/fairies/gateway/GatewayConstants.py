from game.fairies.ai import ZoneConstants
from game.fairies.ai import FairiesConstants as fc

# targetLocationName is the Location name of where you want the fairy to appear
# on the other side (so in the other meadow). These can be found in each meadow's
# config.xml in /meadows/zone###
#
# Games and Quest zones won't have one, can leave blank. Any that are left blank,
# go to the coords of the location named "default" in the xml. I write default here
# just purely for completion sake. It's functionally the same as leaving it as "".
#
# - Jessi

GATEWAYS: dict[int, list[dict]] = {
    # ════════════════════════════════════════════════════════════════════════════════════ #
    #                                  Havendish Gateways                                  #
    # ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.HAVENDISH_SQUARE: [
        {
            # Fairy Coliseum
            "name": "9274",
            "position": (65, 90),
            "targetLocationName": "fromZone500",
            "targetZoneID": ZoneConstants.FAIRY_COLISEUM,
        },
        {
            # Cottonpuff Field
            "name": "9083",
            "position": (2, 314),
            "targetLocationName": "fromHavendishSquare",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
        {
            # Queen's Boutique
            "name": "9282",
            "position": (40, 23),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.QUEENS_BOUTIQUE,
        },
        {
            # Cassie's Costume Shop
            "name": "9214",
            "position": (270, 100),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.CASSIES_COSTUME_SHOP,
        },
        {
            # Pixie Dust Mill
            "name": "9267",
            "position": (290, 1160),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PIXIE_DUST_MILL,
        },
        {
            # Fairy Tale Theater
            "name": "9179",
            "position": (851, 439),
            "targetLocationName": "fromZone500",
            "targetZoneID": ZoneConstants.FAIRY_TALE_THEATER,
        },
        {
            # Neverfruit Grove
            "name": "9161",
            "position": (990, 1145),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.NEVERFRUIT_GROVE,
        },
        {
            # Ballroom
            "name": "9188",
            "position": (1272, 388),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.THE_BALLROOM,
        },
        {
            # Pixie Postings
            "name": "9206", # 9206 (Spring), 9225 (Summer), 9181 (Autumn), 9183 (Winter)
            "position": (1635, 949),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PIXIE_POSTINGS,
        },
        {
            # Tearoom
            "name": "9180",
            "position": (2001, 457),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.THE_TEAROOM,
        },
        {
            # Springtime Orchard
            "name": "9028",
            "position": (1995, 760),
            "targetLocationName": "fromBeck'sAnimalNursery",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
    ],
    ZoneConstants.QUEENS_BOUTIQUE: [
        {
            # Havendish Square
            "name": "9283",
            "position": (209, 336),
            "targetLocationName": "fromZone110004",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.FAIRY_TALE_THEATER: [
        {
            # Havendish Square
            "name": "9174",
            "position": (0, 310),
            "targetLocationName": "fromFairyTaleTheater",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Cassie's Costume Shop
            "name": "9169",
            "position": (1173, 176),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.CASSIES_COSTUME_SHOP,
        },
    ],
    ZoneConstants.CASSIES_COSTUME_SHOP: [
        {
            # Fairy Tale Theater
            "name": "9198",
            "position": (252, 248),
            "targetLocationName": "fromZone110004",
            "targetZoneID": ZoneConstants.FAIRY_TALE_THEATER,
        },
    ],
    ZoneConstants.THE_BALLROOM: [
        {
            # Havendish Square
            "name": "9186",
            "position": (750, 305),
            "targetLocationName": "fromBallRoom",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.THE_TEAROOM: [
        {
            # Havendish Square
            "name": "9185",
            "position": (61, 57),
            "targetLocationName": "fromTeaRoom",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.LIZZYS_HOUSE: [
        {
            # Havendish Square
            "name": "9237",
            "position": (46, 140),
            "targetLocationName": "fromZone504",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.FAIRY_COLISEUM: [
        {
            # Havendish Square
            "name": "9174",
            "position": (35, 253),
            "targetLocationName": "famousFairyHome",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Marina's Place
            "name": "9273",
            "position": (360, 482),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MARINAS_PLACE,
        },
        {
            # Zephyr's Zoom Room
            "name": "9276",
            "position": (762, 219),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.ZEPHYRS_ZOOM_ROOM,
        },
    ],
    ZoneConstants.ZEPHYRS_ZOOM_ROOM: [
        {
            # Fairy Coliseum
            "name": "9277",
            "position": (175, 303),
            "targetLocationName": "fromZone110007",
            "targetZoneID": ZoneConstants.FAIRY_COLISEUM,
        },
    ],
    
    # ════════════════════════════════════════════════════════════════════════════════════ #
    #                                    Winter Gateways                                   #
    # ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.EVERGREEN_OVERLOOK: [
        {
            # Chilly Falls
            "name": "9120",
            "position": (840, 398),
            "targetLocationName": "fromEvergreenOverlook",
            "targetZoneID": ZoneConstants.CHILLY_FALLS,
        },
        {
            # Kits
            "name": "9280",
            "position": (908, 1082),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.KITS_PLACE,
        },
        {
            # Snowflake Sweep
            "name": "9125",
            "position": (645, 1500),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWFLAKE_SWEEP_GAME,
            "rewardList": [fc.IVY, fc.PINE_NEEDLES, fc.SNOWFLAKES],
        },
        {
            # Snowcap Glade
            "name": "9114",
            "position": (35, 1618),
            "targetLocationName": "fromEvergreenOverlook",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
        {
            # Havendish Square
            "name": "9177",
            "position": (875, 1600),
            "targetLocationName": "fromEvergreenOverlook",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.CHILLY_FALLS: [
        {
            # Evergreen Overlook
            "name": "9103",
            "position": (180, 820),
            "targetLocationName": "fromChillyFalls",
            "targetZoneID": ZoneConstants.EVERGREEN_OVERLOOK,
        },
        {
            # Treetop Bend
            "name": "9060",
            "position": (833, 1568),
            "targetLocationName": "fromChillyFalls",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
        {
            # Ember's Essentials
            "name": "9124",
            "position": (960, 831),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.EMBERS_ESSENTIALS,
        },
        {
            # Gem Juggle
            "name": "9269",
            "position": (1001, 1071),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.GEM_JUGGLE_GAME,
            "rewardList": [fc.IVY, fc.PINE_NEEDLES, fc.TWIGS],
        },
    ],
    ZoneConstants.GALES_OUTFITTERS: [
        {
            # Snowcap Glade
            "name": "9108",
            "position": (810, 380),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
    ],
    ZoneConstants.SNOWCAP_GLADE: [
        {
            # Evergreen Overlook
            "name": "9101",
            "position": (1985, 100),
            "targetLocationName": "fromSnowdriftPass",
            "targetZoneID": ZoneConstants.EVERGREEN_OVERLOOK,
        },
        {
            # Acorn Summit
            "name": "9075",
            "position": (201, 632),
            "targetLocationName": "fromSnowdriftPass",
            "targetZoneID": ZoneConstants.ACORN_SUMMIT,
        },
        {
            # Pinecone Pop
            "name": "9246",
            "position": (214, 124),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PINECONE_POP_GAME,
            "rewardList": [fc.ACORNS, fc.PINE_NEEDLES, fc.SNOWFLAKES],
        },
        {
            # Snowy Lullaby
            "name": "9144",
            "position": (1830, 550),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWY_LULLABY_GAME,
            "rewardList": [fc.ACORNS, fc.MAPLE_LEAVES, fc.DANDELION_FLUFF],
        },
        {
            # Gale's Outfitters
            "name": "9126",
            "position": (1509, 215),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.GALES_OUTFITTERS,
        }
    ],
    ZoneConstants.EMBERS_ESSENTIALS: [
        {
            # Chilly Falls
            "name": "9116",
            "position": (780, 390),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.CHILLY_FALLS,
        },
    ],
    ZoneConstants.FROSTED_FOREST: [
        {
            # Spike's Sweet Shop
            "name": "9290",
            "position": (1127, 352),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.SPIKES_SWEETS,
        },
        {
            # Evergreen Overlook (northwest)
            "name": "9103",
            "position": (470, 1040),
            "targetLocationName": "fromZone304",
            "targetZoneID": ZoneConstants.EVERGREEN_OVERLOOK,
        },
    ],
    ZoneConstants.ICE_PALACE: [
        {
            # Chilly Falls (west)
            "name": "9239",
            "position": (175, 610),
            "targetLocationName": "fromZone303",
            "targetZoneID": ZoneConstants.CHILLY_FALLS,
        },
    ],
    ZoneConstants.SPIKES_SWEETS: [
        {
            # Frosted Forest (west)
            "name": "9288",
            "position": (185, 157),
            "targetLocationName": "fromZone110011",
            "targetZoneID": ZoneConstants.FROSTED_FOREST,
        },
    ],

    # ════════════════════════════════════════════════════════════════════════════════════ #
    #                                    Summer Gateways                                   #
    # ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.PALM_TREE_COVE: [
        {
            # Neverfruit Grove
            "name": "9159",
            "position": (180, 215),
            "targetLocationName": "fromZone400",
            "targetZoneID": ZoneConstants.NEVERFRUIT_GROVE,
        },
        {
            # Prism's Pixie Spa
            "name": "9299",
            "position": (406, 571),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.PRISMS_PIXIE_SPA,
        },
        {
            # Shelly's Shears
            "name": "9148",
            "position": (406, 571),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.SCHELLYS_HAIR_SALON,
        },
        {
            # Butterfly Painter
            "name": "9216",
            "position": (1707, 602),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.BUTTERFLY_PAINTER_GAME,
            "rewardList": [fc.LILY_PETALS, fc.BLUEBERRIES, fc.SUNFLOWER_SEEDS],
        },
        {
            # Dewdrop Vale
            "name": "9045",
            "position": (1605, 233),
            "targetLocationName": "fromZone400",
            "targetZoneID": ZoneConstants.DEWDROP_VALE,

        },
    ],
    ZoneConstants.PRISMS_PIXIE_SPA: [
        {
            # Palm Tree Cove
            "name": "9300",
            "position": (775, 283),
            "targetLocationName": "fromZone114000",
            "targetZoneID": ZoneConstants.PALM_TREE_COVE,
        },
    ],
    ZoneConstants.SCHELLYS_HAIR_SALON: [
        {
            # Palm Tree Cove
            "name": "9193",
            "position": (880, 415),
            "targetLocationName": "fromZone114000",
            "targetZoneID": ZoneConstants.PALM_TREE_COVE,
        },
    ],
    ZoneConstants.MERMAID_GROTTO: [
        {
            # Palm Tree Cove
            "name": "9265",
            "position": (110, 288),
            "targetLocationName": "fromZone403",
            "targetZoneID": ZoneConstants.PALM_TREE_COVE,
        },
    ],
    ZoneConstants.NEVERFRUIT_GROVE: [
        {
            # Sunflower Gully
            "name": "9142",
            "position": (52, 250),
            "targetLocationName": "fromZone402",
            "targetZoneID": ZoneConstants.SUNFLOWER_GULLY,
        },
        {
            # Havendish Square
            "name": "9173",
            "position": (280, 30),
            "targetLocationName": "fromZone402",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Pixie Post Office
            "name": "9278",
            "position": (337, 140),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.PIXIE_POST_OFFICE,
        },
        {
            # First Flight
            "name": "9209",
            "position": (1232, 412),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FIRST_FLIGHT_GAME,
            "rewardList": [fc.OAK_LEAVES, fc.HONEYCOMBS, fc.SUNFLOWER_SEEDS],
        },
        {
            # Palm Tree Cove
            "name": "9132",
            "position": (815, 805),
            "targetLocationName": "fromZone402",
            "targetZoneID": ZoneConstants.PALM_TREE_COVE,
        },
    ],
    ZoneConstants.PIXIE_POST_OFFICE: [
        {
            # Neverfruit Grove
            "name": "9279",
            "position": (74, 220),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.NEVERFRUIT_GROVE,
        },
    ],
    ZoneConstants.SUNFLOWER_GULLY: [
        {
            # Neverfruit Grove
            "name": "9157",
            "position": (905, 440),
            "targetLocationName": "fromZone401",
            "targetZoneID": ZoneConstants.NEVERFRUIT_GROVE,
        },
        {   # Troop Glowworm Hideout
            "name": "9305",
            "position": (905,640),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TROOP_GLOWWORM_HIDEOUT,
        },
        {
            # Pheobe's
            "name": "9147",
            "position": (508, 406),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PHOEBES_PARTY_FAVORS,
        },
        {
            # Sunbeam Bend
            "name": "9272",
            "position": (900, 650),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.LIGHT_PIPE_GAME,
            "rewardList": [fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.RASPBERRIES],
        },
        {
            # Iridessa's Glade
            "name": "9146",
            "position": (435, 1080),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.IRIDESSAS_GLADE,
        },
        {
            # Cottonpuff Field
            "name": "9079",
            "position": (220, 1437),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        }
    ],

    ZoneConstants.PHOEBES_PARTY_FAVORS: [
        {
            # Sunflower Gully
            "name": "9136",
            "position": (610, 710),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SUNFLOWER_GULLY,
        },
    ],
    # ════════════════════════════════════════════════════════════════════════════════════ #
    #                                    Autumn Gateways                                   #
    # ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.ACORN_SUMMIT: [
        {
            # Fairy Fireworks
            "name": "9024",
            "position": (460, 52),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_FIREWORKS_GAME,
            "rewardList": [fc.OAK_LEAVES, fc.MAPLE_LEAVES, fc.DANDELION_FLUFF],
        },
        {
            # Vidia's Daily Spin
            "name": "9228",
            "position": (967, 185),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.VIDIAS_DAILY_SPIN,
        },
        {
            # Summit Style
            "name": "9023",
            "position": (964, 402),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.SUMMIT_STYLE,
        },
        {
            # Pumpkin Patch
            "name": "9201",
            "position": (70, 870),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.PUMPKIN_PATCH,
        },
        {
            # Maple Tree Hill
            "name": "9072",
            "position": (900, 920),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
        {
            # Cottonpuff Field
            "name": "9080",
            "position": (1460, 800),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
        {
            # Snowcap Glade
            "name": "9108",
            "position": (1650, 300),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
    ],
    ZoneConstants.SUMMIT_STYLE: [
        {
            # Acorn Summit
            "name": "9068",
            "position": (780, 400),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.ACORN_SUMMIT,
        },
    ],
    ZoneConstants.COTTONPUFF_FIELD: [
        {
            # Acorn Summit
            "name": "9071",
            "position": (195, 150),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.ACORN_SUMMIT,
        },
        {
            # Sunflower Gully
            "name": "9140",
            "position": (390, 815),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SUNFLOWER_GULLY,
        },
        {   # Troop Turtle Hideout
            "name": "9304",
            "position": (330,815),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TROOP_TURTLE_HIDEOUT,
        },
        {
            # Tinker Toss
            "name": "9145",
            "position": (632, 745),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TINKER_TOSS_GAME,
            "rewardList": [fc.OAK_LEAVES, fc.HONEYCOMBS, fc.TWIGS],
        },
        {
            # Maple Tree Hill
            "name": "9091",
            "position": (85, 915),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
        {
            # Tinkers Nook
            "name": "9026",
            "position": (1765, 765),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TINKERS_NOOK,
        },
        {
            # Havendish Square
            "name": "9175",
            "position": (1650, 410),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Coal's Clothiers
            "name": "9210",
            "position": (496, 208),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COALS_CLOTHIERS,
        },
    ],
    ZoneConstants.COALS_CLOTHIERS: [
        {
            # Cottonpuff Field (west)
            "name": "9213",
            "position": (223, 260),
            "targetLocationName": "fromCoal'sClothiersShop",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
    ],
    ZoneConstants.MAPLE_TREE_HILL: [
        {
            # Cottonpuff Field
            "name": "9076",
            "position": (1055, 1325),
            "targetLocationName": "fromMapleHill",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
        {
            # Mendy's Tailoring
            "name": "9012",
            "position": (738, 1318),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MENDYS_TAILORING,
        },
        {
            # Fawn's Hideout
            "name": "9027",
            "position": (342, 1740),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAWNS_HIDEOUT,
        },
        {
            # Copper's Tinkering
            "name": "9154",
            "position": (482, 940),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COPPERS_TINKERING,
        },
        {
            # Pumpkin Patch
            "name": "9098",
            "position": (0, 805),
            "targetLocationName": "fromMapleHill",
            "targetZoneID": ZoneConstants.PUMPKIN_PATCH,
        },
        {
            # Springtime Orchard
            "name": "9028",
            "position": (1075, 445),
            "targetLocationName": "fromMapleHill",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
        {
            # Acorn Summit
            "name": "9071",
            "position": (255, 225),
            "targetLocationName": "fromMapleHill",
            "targetZoneID": ZoneConstants.ACORN_SUMMIT,
        },
        {
            # Troop Rabbit Hideout
            "name": "9301",
            "position": (625, 280),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TROOP_RABBIT_HIDEOUT,
        },
    ],
    ZoneConstants.PUMPKIN_PATCH: [
        {
            # Acorn Summit (north)
            "name": "9070",
            "position": (630, 60),
            "targetLocationName": "fromPumpkinPatch",
            "targetZoneID": ZoneConstants.ACORN_SUMMIT,
        },
        {
            # Maple Tree Hill (northeast)
            "name": "9085",
            "position": (1560, 420),
            "targetLocationName": "fromPumpkinPatch",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
        {
            # Harvest Hustle
            "name": "9015",
            "position": (980, 670),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HARVEST_HUSTLE_GAME,
            "rewardList": [fc.ACORNS, fc.BLUEBERRIES, fc.RASPBERRIES],
        },
    ],

    # ════════════════════════════════════════════════════════════════════════════════════ #
    #                                    Spring Gateways                                   #
    # ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.SPRINGTIME_ORCHARD:[
        {
            # Bobbin's Tailoring Nook
            "name": "9011",
            "position": (365, 765),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.BOBBINS_TAILORING,
        },
        {
            # Firefly Light Up
            "name": "9009",
            "position": (1460, 853),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FIREFLY_LIGHT_UP_GAME,
            "rewardList": [fc.IVY, fc.MEADOW_GRASS, fc.SUNFLOWER_SEEDS]
        },
        {
            # Dewdrop Vale
            "name": "9048",
            "position": (1730, 750),
            "targetLocationName": "fromSpringtimeOrchard",
            "targetZoneID": ZoneConstants.DEWDROP_VALE,
        },
        {
            # Havendish
            "name": "9170",
            "position": (0, 450),
            "targetLocationName": "fromSpringtimeOrchard",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Beck's
            "name": "9203",
            "position": (402, 338),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.BECKS_ANIMAL_NURSERY,
        },
        {
            # CherryBlossom Heights
            "name": "9037",
            "position": (1255, 255),
            "targetLocationName": "fromSpringtimeOrchard",
            "targetZoneID": ZoneConstants.CHERRYBLOSSOM_HEIGHTS,
        },
    ],
    ZoneConstants.NEVERBERRY_THICKET: [
        {
            # Dewdrop Vale
            "name": "9050",
            "position": (250, 850),
            "targetLocationName": "fromNeverberryThicket",
            "targetZoneID": ZoneConstants.DEWDROP_VALE,
        },
        {
            # Dulcie's Baking
            "name": "9155",
            "position": (850, 710),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.DULCIES_BAKING,
        },
        {
            # Elixa's
            "name": "9205",
            "position": (1646, 595),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.ELIXAS_HOSPITAL,
        },
        {
            # Water Web
            "name": "9013",
            "position": (1750, 705),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.WATER_WEB_GAME,
            "rewardList": [fc.LILY_PETALS, fc.MEADOW_GRASS, fc.SPIDER_SILK]
        },
        {
            # Treetop Bend
            "name": "9062",
            "position": (1620, 90),
            "targetLocationName": "fromNeverberryThicket",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
        {
            # Harmony's Sweet Shop
            "name": "9286",
            "position": (1183, 274),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.HARMONYS_SWEET_SHOP,
        },
        {
            # Cherryblossom Heights
            "name": "9039",
            "position": (410, 208),
            "targetLocationName": "fromNeverberryThicket",
            "targetZoneID": ZoneConstants.CHERRYBLOSSOM_HEIGHTS,
        },
    ],
    ZoneConstants.HARMONYS_SWEET_SHOP: [
        {
            # Neverberry Thicket
            "name": "9287",
            "position": (150, 675),
            "targetLocationName": "fromZone111000",
            "targetZoneID": ZoneConstants.NEVERBERRY_THICKET,
        },
    ],
    ZoneConstants.CHERRYBLOSSOM_HEIGHTS: [
        {
            # Springtime Orchard (southwest)
            "name": "9034",
            "position": (990, 940),
            "targetLocationName": "fromCherryblossomHeights",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
        {   # Troop Butterfly Hideout
            "name": "9302",
            "position": (880,815),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TROOP_BUTTERFLY_HIDEOUT,
        },
        {
            # Neverberry Thicket (southeast)
            "name": "9056",
            "position": (1700, 950),
            "targetLocationName": "fromCherryblossomHeights",
            "targetZoneID": ZoneConstants.NEVERBERRY_THICKET,
        },
        {
            # Rosetta's Garden (Rosetta face gateway)
            "name": "9149",
            "position": (90, 555),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.ROSETTAS_GARDEN,
        },
        {
            # Petal Pick-Up
            "name": "9014",
            "position": (385, 100),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PETAL_PICKUP_GAME,
            "rewardList": [fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.DAISY_PETALS],
        },
        {
            # Treetop Bend (northeast)
            "name": "9061",
            "position": (1565, 420),
            "targetLocationName": "fromCherryblossomHeights",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
        {
            # Daisy's Dyes
            "name": "9017",
            "position": (1345, 645),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.DAISYS_DYES,
        },
    ],
    ZoneConstants.DAISYS_DYES: [
        {
            # Cherryblossom Heights (west)
            "name": "9043",
            "position": (143, 395),
            "targetLocationName": "fromZone112000",
            "targetZoneID": ZoneConstants.CHERRYBLOSSOM_HEIGHTS,
        },
    ],
    ZoneConstants.BECKS_ANIMAL_NURSERY: [
        {
            # Springtime Orchard (southwest)
            "name": "9207",
            "position": (140, 120),
            "targetLocationName": "fromBeck'sAnimalNursery",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
    ],
    ZoneConstants.GARDEN_SUPPLY: [
        {
            # Dewdrop Vale (Brook's shop return sign)
            "name": "9285",
            "position": (180, 325),
            "targetLocationName": "fromZone110001",
            "targetZoneID": ZoneConstants.DEWDROP_VALE,
        },
    ],
    ZoneConstants.DEWDROP_VALE: [
        {
            # Springtime Orchard (northwest)
            "name": "9031",
            "position": (98, 410),
            "targetLocationName": "fromSpringtimeValley",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
        {   # Troop Otter Hideout
            "name": "9303",
            "position": (508,330),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TROOP_OTTER_HIDEOUT,
        },
        {
            # Bubble Bounce
            "name": "9010",
            "position": (100, 1190),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.BUBBLE_BOUNCE_GAME,
            "rewardList": [fc.LILY_PETALS, fc.DAISY_PETALS, fc.SPIDER_SILK],
        },
        {
            # Palm Tree Cove (southwest)
            "name": "9134",
            "position": (225, 1400),
            "targetLocationName": "fromZone102",
            "targetZoneID": ZoneConstants.PALM_TREE_COVE,
        },
        {
            # Silvermist's Grotto
            "name": "9025",
            "position": (995, 1260),
            "targetLocationName": "default",
            "targetZoneID": ZoneConstants.SILVERMISTS_GROTTO,
        },
        {
            # Garden Supply
            "name": "9021",
            "position": (270, 450),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.GARDEN_SUPPLY,
        },
        {
            # Neverberry Thicket (northeast)
            "name": "9053",
            "position": (1125, 910),
            "targetLocationName": "fromDewdropVale",
            "targetZoneID": ZoneConstants.NEVERBERRY_THICKET,
        },
    ],
    ZoneConstants.TREETOP_BEND: [
        {
            # Seed Sorting Game
            "name": "9187",
            "position": (1340, 960),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SEED_SORTING_GAME,
            "rewardList": [fc.ROSE_PETALS, fc.BUTTERCUP_PETALS, fc.RASPBERRIES],
        },
        {
            # Treetop Housewares
            "name": "9020",
            "position": (1019, 648),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.TREETOP_HOUSEWARES,
        },
        {
            # Bella's Baubles
            "name": "9019",
            "position": (216, 1042),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.BELLAS_BAUBLES,
        },
        {
            # Neverberry Thicket
            "name": "9057",
            "position": (720, 1305),
            "targetLocationName": "fromTreetopBend",
            "targetZoneID": ZoneConstants.NEVERBERRY_THICKET,
        },
        {
            # Cherryblossom Heights
            "name": "9042",
            "position": (90, 789),
            "targetLocationName": "fromTreetopBend",
            "targetZoneID": ZoneConstants.CHERRYBLOSSOM_HEIGHTS,
        },
        {
            # Chilly Falls
            "name": "9123",
            "position": (87, 250),
            "targetLocationName": "fromTreetopBend",
            "targetZoneID": ZoneConstants.CHILLY_FALLS,
        },
        {
            # Neville's New Homes
            "name": "9224",
            "position": (422, 238),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.NEVILLES_NEW_HOMES,
        },
    ],
    ZoneConstants.TREETOP_HOUSEWARES: [
        {
            # Treetop Bend
            "name": "9060",
            "position": (780, 380),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
    ],
    ZoneConstants.BELLAS_BAUBLES: [
        {
            # Treetop Bend
            "name": "9060",
            "position": (780, 395),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
    ],
    ZoneConstants.NEVILLES_NEW_HOMES: [
        {
            # Treetop Bend
            "name": "9066",
            "position": (195, 231),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.TREETOP_BEND,
        },
    ],
# ════════════════════════════════════════════════════════════════════════════════════ #
#                             Troop Hideout Gateways                                   #
# ════════════════════════════════════════════════════════════════════════════════════ #
    ZoneConstants.TROOP_BUTTERFLY_HIDEOUT: [
        {
            # Cherryblossom Heights
            "name": "9036",
            "position": (800, 450),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.CHERRYBLOSSOM_HEIGHTS,
        },
    ],
    ZoneConstants.TROOP_OTTER_HIDEOUT: [
        {
            # Dewdrop Vale
            "name": "9044",
            "position": (800, 390),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.DEWDROP_VALE,
        },
    ],
    ZoneConstants.TROOP_TURTLE_HIDEOUT: [
        {
            # Cottonpuff Field
            "name": "9076",
            "position": (800, 380),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
    ],
    ZoneConstants.TROOP_GLOWWORM_HIDEOUT: [
        {
            # Sunflower Gully
            "name": "9136",
            "position": (825, 400),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SUNFLOWER_GULLY,
        },
    ],
    ZoneConstants.TROOP_RABBIT_HIDEOUT: [
        {
            # Maple Tree Hill
            "name": "9084",
            "position": (820, 450),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
    ],
}