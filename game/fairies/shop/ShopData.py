from game.fairies.ai import ZoneConstants
from game.fairies.ai import FairiesConstants
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

TEST_SHOP_DATA = ShopCollection(collectionId=1, currencyId=1, items=[ShopItem(itemId=77515, price=100, goldPrice=100)])

# Note that shopId 1 is locked to the Garden Shop despite shopId 7000 *also* being the Garden Shop

SHOPS = [
    NPCShop(
        zone=ZoneConstants.BELLAS_BAUBLES,
        shopId=0,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BELLA_ROSE,
            position=(420, 420),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BELLA_ROSE
        ),
        collections=[
            ShopCollection(
                collectionId=6, # Hats and Hairpieces
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=2005, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Vine Headband
                    ShopItem(itemId=2009, price=30, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Rose Bloom Barrettes
                    ShopItem(itemId=2012, price=30, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Hickory Leaf Headdress
                    ShopItem(itemId=2013, price=30, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Feather Cap
                    ShopItem(itemId=2032, price=30, goldPrice=3, color1=258, color2=258, itemType="HeadItem"), # Spearmint Green Little Lily Pad Barrette
                    ShopItem(itemId=2097, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Coin Headband
                    ShopItem(itemId=2098, price=30, goldPrice=3, color1=227, color2=227, itemType="HeadItem"), # Moonlight Gray Timely Barrette
                    ShopItem(itemId=2237, price=30, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Spider Web Veil Hat
                    ShopItem(itemId=2400, price=30, goldPrice=3, color1=161, color2=78, itemType="HeadItem"), # Buried Treasure Brown Straw Fascinator with Fawn Brown Trim
                    ShopItem(itemId=2401, price=30, goldPrice=3, color1=141, color2=141, itemType="HeadItem"), # Thundercloud Gray Peacock Plume Fascinator
                    ShopItem(itemId=2402, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Butterfly Fascinator
                    ShopItem(itemId=2404, price=30, goldPrice=3, color1=168, color2=168, itemType="HeadItem"), # Never Gold Gemstone Accessory Set
                    ShopItem(itemId=2417, price=30, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Cherry Pie Hat
                    ShopItem(itemId=2419, price=30, goldPrice=3, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Cute Cupcake Headband
                    ShopItem(itemId=2420, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Cake Slice Headband
                    ShopItem(itemId=2168, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Friendship Headband
                    ShopItem(itemId=2291, price=30, goldPrice=3, color1=224, color2=267, itemType="HeadItem"), # Ivory White Cherry-On-Top Hat with Celestial Blue Trim
                    ShopItem(itemId=2437, price=30, goldPrice=3, color1=10, color2=10, itemType="HeadItem"), # Cantaloupe Orange Siren Style Headband
                    ShopItem(itemId=2095, price=30, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Clam Ribbon Headband
                    ShopItem(itemId=2094, price=30, goldPrice=3, color1=109, color2=139, itemType="HeadItem"), # Soft Orange Sand Dollar Headband with Seedling Green Trim
                    ShopItem(itemId=2270, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Feather Headpiece
                    ShopItem(itemId=2305, price=30, goldPrice=3, color1=140, color2=140, itemType="HeadItem"), # Bunnynose Pink Beautiful Bow Headband
                    ShopItem(itemId=2196, price=30, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Dewdrop Headpiece
                    ShopItem(itemId=2207, price=30, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Sun 'n' Sand Beach Hat
                    ShopItem(itemId=2468, price=30, goldPrice=3, color1=224, color2=18, itemType="HeadItem"), # Ivory White Enchantress Crown with Waterfall Blue Trim
                    ShopItem(itemId=2469, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Sorceress Barrette
                    ShopItem(itemId=2199, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Little Bow Cap
                    ShopItem(itemId=2202, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Cute Little Cap
                    ShopItem(itemId=2198, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Fly Backwards Cap
                    ShopItem(itemId=2210, price=30, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Tassled Knit Hat
                    ShopItem(itemId=2211, price=30, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Chunky Knit Hat
                    ShopItem(itemId=2212, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Pixie Puff Beanie
                    ShopItem(itemId=2197, price=30, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Teardrop Headpiece
                    ShopItem(itemId=2369, price=30, goldPrice=3, color1=207, color2=207, itemType="HeadItem"), # Diamond Blue Frozen Flower Tiara
                    ShopItem(itemId=2236, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Harvest Moon Tiara
                    ShopItem(itemId=2388, price=30, goldPrice=3, color1=188, color2=188, itemType="HeadItem"), # Dahlia Pink Butterfly Tiara
                    ShopItem(itemId=2389, price=30, goldPrice=3, color1=167, color2=167, itemType="HeadItem"), # Never Silver Crystal Tiara
                    ShopItem(itemId=2390, price=30, goldPrice=3, color1=207, color2=162, itemType="HeadItem"), # Diamond Blue Frosty Tiara with Sunglow Yellow Trim
                    ShopItem(itemId=2146, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Comb
                    ShopItem(itemId=2145, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Chain
                    ShopItem(itemId=2147, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Tiara
                    ShopItem(itemId=2044, price=30, goldPrice=3, color1=283, color2=283, itemType="HeadItem"), # Thistle Pink Flower Sunglasses
                    ShopItem(itemId=2324, price=30, goldPrice=3, color1=206, color2=162, itemType="HeadItem"), # Raven Black Casual Shades with Yellow Trim
                    ShopItem(itemId=2141, price=30, goldPrice=3, color1=215, color2=215, itemType="HeadItem"), # Pewter Gray Sharp Sun-Shades
                    ShopItem(itemId=2159, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Heart Glasses
                ],
            ),
            ShopCollection(
                collectionId=7, # Bracelets
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=1663, price=10, goldPrice=1, color1=168, color2=168, itemType="WristItem"), # Never Gold Gemstone Bangle
                    ShopItem(itemId=1519, price=10, goldPrice=1, color1=121, color2=230, itemType="WristItem"), # Daisy Pink Friendship Bracelet with Scarlet Red Trim
                    ShopItem(itemId=1560, price=10, goldPrice=1, color1=211, color2=211, itemType="WristItem"), # Gentian Purple Friendship Wrap
                    ShopItem(itemId=1628, price=10, goldPrice=1, color1=45, color2=45, itemType="WristItem"), # Strawberry Red Licorice Twist Bracelet
                    ShopItem(itemId=1549, price=10, goldPrice=1, color1=42, color2=42, itemType="WristItem"), # Blueberry Blue Rainbow Wrist Bands
                    ShopItem(itemId=1548, price=10, goldPrice=1, color1=126, color2=227, itemType="WristItem"), # Raindrop Blue Raindrop Bracelet with Moonlight Gray Trim
                    ShopItem(itemId=1681, price=10, goldPrice=1, color1=121, color2=224, itemType="WristItem"), # Daisy Pink Delicate Daisy Corsage with Ivory White Trim
                    ShopItem(itemId=1680, price=10, goldPrice=1, color1=63, color2=63, itemType="WristItem"), # Butterfly Blue Opulent Orchid Corsage
                    ShopItem(itemId=1679, price=10, goldPrice=1, color1=166, color2=166, itemType="WristItem"), # Snow White Ravishing Rose Corsage
                    ShopItem(itemId=1526, price=10, goldPrice=1, color1=180, color2=180, itemType="WristItem"), # Seashell Blue Clam Ribbon Bracelet
                    ShopItem(itemId=1527, price=10, goldPrice=1, color1=152, color2=152, itemType="WristItem"), # Pale Purple Shell Bracelet
                    ShopItem(itemId=1604, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Feathered Bracelet
                    ShopItem(itemId=1631, price=10, goldPrice=1, color1=200, color2=200, itemType="WristItem"), # Ruby Pink Ribbon Wrap
                    ShopItem(itemId=1561, price=10, goldPrice=1, color1=30, color2=30, itemType="WristItem"), # Pumpkin Orange Freesia Wrist Flounce
                    ShopItem(itemId=1523, price=10, goldPrice=1, color1=200, color2=200, itemType="WristItem"), # Ruby Pink Dear Droplets Bracelet
                    ShopItem(itemId=1546, price=10, goldPrice=1, color1=18, color2=18, itemType="WristItem"), # Waterfall Blue Triple Tie Bracelet
                    ShopItem(itemId=1629, price=10, goldPrice=1, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Twirly Jeweled Bracelet
                    ShopItem(itemId=1566, price=10, goldPrice=1, color1=138, color2=138, itemType="WristItem"), # Persimmon Orange Bottle Cap Bracelet
                    ShopItem(itemId=1649, price=10, goldPrice=1, color1=129, color2=129, itemType="WristItem"), # Fig Purple Jeweled Bracelet Ring
                    ShopItem(itemId=1650, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Pearl Pendant Ring
                    ShopItem(itemId=1652, price=10, goldPrice=1, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Chain Ring Bracelet
                    ShopItem(itemId=1598, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Clover Bracelet
                    ShopItem(itemId=1522, price=10, goldPrice=1, color1=126, color2=126, itemType="WristItem"), # Raindrop Blue Teardrop Bracelet
                    ShopItem(itemId=1516, price=10, goldPrice=1, color1=69, color2=69, itemType="WristItem"), # Powder Blue Double Bubble Bracelet
                    ShopItem(itemId=1509, price=10, goldPrice=1, color1=64, color2=64, itemType="WristItem"), # Emerald Green Grass Multi-Wrap Bracelet
                    ShopItem(itemId=1653, price=10, goldPrice=1, color1=45, color2=45, itemType="WristItem"), # Strawberry Red Spider Web Bracelet
                    ShopItem(itemId=1521, price=10, goldPrice=3, color1=265, color2=10, itemType="WristItem"), # Bright Sky Blue Tiger Lily Bracelet with Cantaloupe Orange Trim
                    ShopItem(itemId=1593, price=10, goldPrice=3, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Harvest Moon Bracelet
                    ShopItem(itemId=1543, price=10, goldPrice=3, color1=216, color2=216, itemType="WristItem"), # Slate Gray Pinned Cuff
                    ShopItem(itemId=1544, price=10, goldPrice=3, color1=277, color2=277, itemType="WristItem"), # Misty Purple Knotted Cuff	
                    ShopItem(itemId=1545, price=10, goldPrice=3, color1=258, color2=258, itemType="WristItem"), # Spearmint Green Two Ribbon Bracelet
                    ShopItem(itemId=1636, price=10, goldPrice=3, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Festive Ball Bracelet
                    ShopItem(itemId=1607, price=10, goldPrice=3, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Pixie Pals Bracelet
                    ShopItem(itemId=1606, price=10, goldPrice=3, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Fairy Friends Forever Bracelet
                    ShopItem(itemId=1584, price=10, goldPrice=3, color1=17, color2=17, itemType="WristItem"), # Tendershoot Green Trinity Leaf Bracelet
                    ShopItem(itemId=1575, price=10, goldPrice=3, color1=247, color2=247, itemType="WristItem"), # Jasmine Yellow Flower Pom-Pom
                    ShopItem(itemId=1542, price=10, goldPrice=3, color1=167, color2=167, itemType="WristItem"), # Never Silver Vine Wrap Cuff
                    ShopItem(itemId=1541, price=10, goldPrice=3, color1=208, color2=208, itemType="WristItem"), # Cerulean Blue Bandana Cuff
                    ShopItem(itemId=1528, price=10, goldPrice=3, color1=227, color2=227, itemType="WristItem"), # Moonlight Gray Tinkered Cuff
                    ShopItem(itemId=1510, price=10, goldPrice=3, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Buttercup Bracelet
                    ShopItem(itemId=1507, price=10, goldPrice=3, color1=69, color2=69, itemType="WristItem"), # Powder Blue Cherry Blossom Bracelet
                    ShopItem(itemId=1505, price=10, goldPrice=3, color1=139, color2=139, itemType="WristItem"), # Seedling Green Silk Leaf Sprouter
                    ShopItem(itemId=1504, price=10, goldPrice=3, color1=27, color2=27, itemType="WristItem"), # Corn Cob Yellow Hibiscus Wrap Bracelet
                    ShopItem(itemId=1503, price=10, goldPrice=3, color1=152, color2=152, itemType="WristItem"), # Pale Purple Double Blossom Bracelet
                    ShopItem(itemId=1502, price=10, goldPrice=3, color1=201, color2=201, itemType="WristItem"), # Velvet Red Rose Bud Bracelet
                ],
            ),
            ShopCollection(
                collectionId=8, # Purses and Props
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=1574, price=10, goldPrice=1, color1=154, color2=154, itemType="WristItem"), # Beetle Brown Frilly Flower Tote
                    ShopItem(itemId=1579, price=10, goldPrice=1, color1=136, color2=162, itemType="WristItem"), # Peacock Blue Peacock Clutch with Sunglow Yellow Trim
                    ShopItem(itemId=1580, price=10, goldPrice=1, color1=189, color2=189, itemType="WristItem"), # Ladybug Red Polka-Dot Clutch
                    ShopItem(itemId=1581, price=10, goldPrice=1, color1=265, color2=265, itemType="WristItem"), # Bright Sky Blue Flower Clutch
                    ShopItem(itemId=1678, price=10, goldPrice=1, color1=30, color2=30, itemType="WristItem"), # Pumpkin Orange Sweet Spring Citrus Purse
                    ShopItem(itemId=1668, price=10, goldPrice=1, color1=211, color2=211, itemType="WristItem"), # Gentian Purple Elegant Egg Purse
                    ShopItem(itemId=1576, price=10, goldPrice=1, color1=199, color2=199, itemType="WristItem"), # Cherryblossom Pink Posey Purse
                    ShopItem(itemId=2645, price=10, goldPrice=1, color1=105, color2=105, itemType="Necklace"), # Siltstone Tan Ruffled Rose Purse
                    ShopItem(itemId=2619, price=10, goldPrice=1, color1=267, color2=267, itemType="Necklace"), # Celestial Blue Feather Fringe Purse
                    ShopItem(itemId=2620, price=10, goldPrice=1, color1=10, color2=10, itemType="Necklace"), # Cantaloupe Orange Vine Chain Purse
                    ShopItem(itemId=2623, price=10, goldPrice=1, color1=221, color2=221, itemType="Necklace"), # Jade Green Peacock Plume Purse
                    ShopItem(itemId=1672, price=10, goldPrice=1, color1=168, color2=168, itemType="WristItem"), # Never Gold Radiant Rainbow Clutch
                    ShopItem(itemId=1677, price=10, goldPrice=1, color1=18, color2=18, itemType="WristItem"), # Waterfall Blue Siren's Scepter
                    ShopItem(itemId=1676, price=10, goldPrice=1, color1=18, color2=18, itemType="WristItem"), # Waterfall Blue Siren's Harp
                    ShopItem(itemId=1588, price=10, goldPrice=1, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Spring Bouquet
                    ShopItem(itemId=1589, price=10, goldPrice=1, color1=69, color2=69, itemType="WristItem"), # Powder Blue Summer Bouquet
                    ShopItem(itemId=1587, price=10, goldPrice=1, color1=45, color2=45, itemType="WristItem"), # Strawberry Red Autumn Bouquet
                    ShopItem(itemId=1590, price=10, goldPrice=1, color1=207, color2=207, itemType="WristItem"), # Diamond Blue Winter Bouquet
                    ShopItem(itemId=1632, price=10, goldPrice=1, color1=224, color2=111, itemType="WristItem"), # Ivory White Shopping Bags with Sparkling Yellow Trim
                    ShopItem(itemId=2640, price=10, goldPrice=1, color1=154, color2=154, itemType="Necklace"), # Beetle Brown Box Camera
                    ShopItem(itemId=1675, price=10, goldPrice=1, color1=109, color2=109, itemType="WristItem"), # Soft Orange Camping Backpack
                    ShopItem(itemId=1671, price=10, goldPrice=1, color1=63, color2=63, itemType="WristItem"), # Butterfly Blue Butterfly Umbrella
                    ShopItem(itemId=1657, price=10, goldPrice=1, color1=162, color2=106, itemType="WristItem"), # Sunglow Yellow Star Wand with Butternut Tan Trim
                    ShopItem(itemId=1656, price=10, goldPrice=1, color1=111, color2=111, itemType="WristItem"), # Sparkling Yellow Wooden Wand
                    ShopItem(itemId=1644, price=10, goldPrice=1, color1=199, color2=199, itemType="WristItem"), # Cherryblossom Pink Hand Fan

                ],
            ),
            ShopCollection(
                collectionId=13, # Necklaces
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=2630, price=10, goldPrice=1, color1=168, color2=168, itemType="Necklace"), # Never Gold Gemstone Necklace
                    ShopItem(itemId=2580, price=10, goldPrice=1, color1=152, color2=152, itemType="Necklace"), # Pale Purple Twisty Winter Warmer
                    ShopItem(itemId=2594, price=10, goldPrice=1, color1=10, color2=18, itemType="Necklace"), # Cantaloupe Orange Gummy Necklace with Waterfall Blue Trim
                    ShopItem(itemId=2633, price=10, goldPrice=1, color1=166, color2=166, itemType="Necklace"), # Snow White Rainbow Scarf
                    ShopItem(itemId=2550, price=10, goldPrice=1, color1=126, color2=227, itemType="Necklace"), # Raindrop Blue Raindrop Necklace with Moonlight Gray Trim
                    ShopItem(itemId=2638, price=10, goldPrice=1, color1=199, color2=199, itemType="Necklace"), # Cherryblossom Pink Siren Style Necklace
                    ShopItem(itemId=2597, price=10, goldPrice=1, color1=200, color2=200, itemType="Necklace"), # Ruby Pink Ravishing Ribbon Necklace
                    ShopItem(itemId=2521, price=10, goldPrice=1, color1=13, color2=13, itemType="Necklace"), # Coral Pink Leafy Necklace
                    ShopItem(itemId=2535, price=10, goldPrice=1, color1=200, color2=200, itemType="Necklace"), # Ruby Pink Dear Droplets Necklace
                    ShopItem(itemId=2530, price=10, goldPrice=1, color1=5, color2=69, itemType="Necklace"), # Wysteria Purple Flowery Lei with Powder Blue Trim
                    ShopItem(itemId=2595, price=10, goldPrice=1, color1=162, color2=162, itemType="Necklace"), # Sunglow Yellow Twirly Jeweled Necklace
                    ShopItem(itemId=2563, price=10, goldPrice=1, color1=30, color2=30, itemType="Necklace"), # Pumpkin Orange Bottle Cap Pendant
                    ShopItem(itemId=2553, price=10, goldPrice=1, color1=2, color2=2, itemType="Necklace"), # Clover Green Rainbow Necklace
                    ShopItem(itemId=2532, price=10, goldPrice=1, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Teardrop Necklace
                    ShopItem(itemId=2523, price=10, goldPrice=1, color1=208, color2=208, itemType="Necklace"), # Cerulean Blue Triple Bubble Necklace
                    ShopItem(itemId=2511, price=10, goldPrice=1, color1=35, color2=35, itemType="Necklace"), # Celery Green Multi-Sweetwrap Necklace
                    ShopItem(itemId=2622, price=10, goldPrice=1, color1=45, color2=45, itemType="Necklace"), # Strawberry Red Spider Web Necklace
                    ShopItem(itemId=2628, price=10, goldPrice=1, color1=207, color2=207, itemType="Necklace"), # Diamond Blue Frozen Flower Necklace
                    ShopItem(itemId=2579, price=10, goldPrice=1, color1=162, color2=162, itemType="Necklace"), # Sunglow Yellow Harvest Moon Necklace
                    ShopItem(itemId=2551, price=10, goldPrice=1, color1=129, color2=129, itemType="Necklace"), # Fig Purple Fringed Scarf
                    ShopItem(itemId=2552, price=10, goldPrice=1, color1=175, color2=175, itemType="Necklace"), # Creek Green Striped Scarf
                    ShopItem(itemId=2626, price=10, goldPrice=1, color1=840, color2=84, itemType="Necklace"), # Copper Brown Golden Acorn Necklace
                    ShopItem(itemId=2611, price=10, goldPrice=1, color1=267, color2=267, itemType="Necklace"), # Celestial Blue Silky Scarf
                    ShopItem(itemId=2601, price=10, goldPrice=1, color1=121, color2=121, itemType="Necklace"), # Daisy Pink Casual Scarf
                    ShopItem(itemId=2600, price=10, goldPrice=1, color1=265, color2=265, itemType="Necklace"), # Bright Sky Blue Puffball Necklace
                    ShopItem(itemId=2598, price=10, goldPrice=1, color1=10, color2=10, itemType="Necklace"), # Cantaloupe Orange Skinny Tie
                    ShopItem(itemId=2585, price=10, goldPrice=1, color1=230, color2=230, itemType="Necklace"), # Scarlet Red Fairy Friends Necklace
                    ShopItem(itemId=2576, price=10, goldPrice=1, color1=35, color2=35, itemType="Necklace"), # Celery Green Trinity Leaf Necklace
                    ShopItem(itemId=2546, price=10, goldPrice=1, color1=86, color2=86, itemType="Necklace"), # Nutmeg Brown Camp Pixie Dust Kerchief
                    ShopItem(itemId=2537, price=10, goldPrice=1, color1=129, color2=129, itemType="Necklace"), # Fig Purple Coiled Gear Necklace
                    ShopItem(itemId=2536, price=10, goldPrice=1, color1=69, color2=69, itemType="Necklace"), # Powder Blue Mermaid Shell Necklace
                    ShopItem(itemId=2529, price=10, goldPrice=1, color1=224, color2=224, itemType="Necklace"), # Ivory White Never Pearl Necklace
                    ShopItem(itemId=2522, price=10, goldPrice=1, color1=64, color2=64, itemType="Necklace"), # Emerald Green Cottonpuff Pendant
                    ShopItem(itemId=2514, price=10, goldPrice=1, color1=11, color2=11, itemType="Necklace"), # Marigold Yellow Stargazer Pendant
                    ShopItem(itemId=2510, price=10, goldPrice=1, color1=130, color2=130, itemType="Necklace"), # Orchid Pink Buttercup Pendant
                    ShopItem(itemId=2507, price=10, goldPrice=1, color1=277, color2=277, itemType="Necklace"), # Misty Purple Chain of Hearts
                    ShopItem(itemId=2506, price=10, goldPrice=1, color1=270, color2=270, itemType="Necklace"), # Horizon Blue Berry Bead Necklace
                    ShopItem(itemId=2504, price=10, goldPrice=1, color1=201, color2=201, itemType="Necklace"), # Velvet Red Rose Bud Pendant
                    ShopItem(itemId=2502, price=10, goldPrice=1, color1=11, color2=11, itemType="Necklace"), # Marigold Yellow Blossom Chain
                    ShopItem(itemId=2624, price=10, goldPrice=1, color1=18, color2=18, itemType="Necklace"), # Waterfall Blue Sparkly Wings Necklace

                ],
            ),

            ShopCollection(
                collectionId=29, # Belts
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=639, price=10, goldPrice=1, color1=200, color2=200, itemType="Belt"), # Ruby Pink Short Sarong
                    ShopItem(itemId=586, price=10, goldPrice=1, color1=35, color2=35, itemType="Belt"), # Celery Green Clover Belt
                    ShopItem(itemId=630, price=10, goldPrice=1, color1=152, color2=152, itemType="Belt"), # Pale Purple Gardening Utility Belt
                    ShopItem(itemId=642, price=10, goldPrice=1, color1=45, color2=45, itemType="Belt"), # Strawberry Red Spider Web Belt
                    ShopItem(itemId=648, price=10, goldPrice=1, color1=154, color2=154, itemType="Belt"), # Beetle Brown Autumn Leaves Belt
                    ShopItem(itemId=646, price=10, goldPrice=1, color1=154, color2=154, itemType="Belt"), # Beetle Brown Super Striped Belt
                    ShopItem(itemId=647, price=10, goldPrice=1, color1=126, color2=126, itemType="Belt"), # Raindrop Blue Lovely Links Belt
                    ShopItem(itemId=645, price=10, goldPrice=1, color1=28, color2=28, itemType="Belt"), # Cinnamon Brown Wonderful Woven Belt
                    ShopItem(itemId=591, price=10, goldPrice=1, color1=227, color2=227, itemType="Belt"), # Moonlight Gray Whisk Belt
                    ShopItem(itemId=589, price=10, goldPrice=1, color1=184, color2=184, itemType="Belt"), # Hummingbird Purple Raven Feather Belt
                    ShopItem(itemId=587, price=10, goldPrice=1, color1=91, color2=91, itemType="Belt"), # Coconut Brown Basic Belt
                    ShopItem(itemId=576, price=10, goldPrice=1, color1=183, color2=183, itemType="Belt"), # Vidia Purple Fast-Flying Feather
                    ShopItem(itemId=565, price=10, goldPrice=1, color1=139, color2=139, itemType="Belt"), # Seedling Green Artsy Floral Belt
                    ShopItem(itemId=545, price=10, goldPrice=1, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Pinecone Belt
                    ShopItem(itemId=544, price=10, goldPrice=1, color1=161, color2=161, itemType="Belt"), # Buried Treasure Brown Artists Clothing Belt
                    ShopItem(itemId=531, price=10, goldPrice=1, color1=121, color2=121, itemType="Belt"), # Daisy Pink Ruffled Myrtle Leaf Belt
                    ShopItem(itemId=521, price=10, goldPrice=1, color1=27, color2=27, itemType="Belt"), # Corn Cob Yellow Pleated Petal Sash
                    ShopItem(itemId=520, price=10, goldPrice=1, color1=69, color2=69, itemType="Belt"), # Powder Blue Spider Silk Tie Belt
                    ShopItem(itemId=519, price=10, goldPrice=1, color1=152, color2=152, itemType="Belt"), # Pale Purple Raindrop Sash
                    ShopItem(itemId=514, price=10, goldPrice=1, color1=258, color2=258, itemType="Belt"), # Spearmint Green Sunburst Petal Belt
                    ShopItem(itemId=513, price=10, goldPrice=1, color1=125, color2=125, itemType="Belt"), # Pine Green Stringbean Sash	
                    ShopItem(itemId=510, price=10, goldPrice=1, color1=10, color2=10, itemType="Belt"), # Cantaloupe Orange Starfire Sash
                    ShopItem(itemId=507, price=10, goldPrice=1, color1=139, color2=139, itemType="Belt"), # Seedling Green Wax Leaf Sash

                ],
            ),
            ShopCollection(
                collectionId=32, # Earrings and Anklets
                currencyId=FairiesConstants.SPIDER_SILK,
                items=[
                    ShopItem(itemId=2233, price=10, goldPrice=3, color1=136, color2=136, itemType="HeadItem"), # Peacock Blue Feather Earrings
                    ShopItem(itemId=2247, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Harvest Moon Earrings
                    ShopItem(itemId=2255, price=10, goldPrice=3, color1=274, color2=274, itemType="HeadItem"), # Bellflower Purple Beaded Row Earrings
                    ShopItem(itemId=2261, price=10, goldPrice=3, color1=30, color2=30, itemType="HeadItem"), # Pumpkin Orange Button Earrings
                    ShopItem(itemId=2264, price=10, goldPrice=3, color1=258, color2=258, itemType="HeadItem"), # Spearmint Green Bottlecap Earrings
                    ShopItem(itemId=2233, price=10, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Feather Earrings
                    ShopItem(itemId=2268, price=10, goldPrice=3, color1=35, color2=35, itemType="HeadItem"), # Celery Green Trinity Leaf Earrings
                    ShopItem(itemId=2368, price=10, goldPrice=3, color1=207, color2=207, itemType="HeadItem"), # Diamond Blue Frozen Flower Earrings
                    ShopItem(itemId=2366, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Darling Dandelion Earrings
                    ShopItem(itemId=2365, price=10, goldPrice=3, color1=27, color2=64, itemType="HeadItem"), # Corn Cob Yellow Sweet Wheat Earrings with Emerald Green Trim
                    ShopItem(itemId=2364, price=10, goldPrice=3, color1=199, color2=199, itemType="HeadItem"), # Cherryblossom Pink Maple Leaf Earrings
                    ShopItem(itemId=2363, price=10, goldPrice=3, color1=84, color2=84, itemType="HeadItem"), # Copper Brown Acorn Earrings
                    ShopItem(itemId=2251, price=10, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Bubble Earrings
                    ShopItem(itemId=2322, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Blooming Earrings
                    ShopItem(itemId=2321, price=10, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Pearly Flower Earrings
                    ShopItem(itemId=2258, price=10, goldPrice=3, color1=2, color2=2, itemType="HeadItem"), # Clover Green Lucky Rainbow Earrings
                    ShopItem(itemId=2320, price=10, goldPrice=3, color1=35, color2=35, itemType="HeadItem"), # Celery Green Beautiful Bud Earrings
                    ShopItem(itemId=2300, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Twirly Jeweled Earrings
                    ShopItem(itemId=2254, price=10, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Dewdrop Earrings
                    ShopItem(itemId=2446, price=10, goldPrice=3, color1=227, color2=227, itemType="HeadItem"), # Moonlight Gray Lost Spoon Danglies
                    ShopItem(itemId=2447, price=10, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Rose Pearl Danglies
                    ShopItem(itemId=2445, price=10, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Beaded Heart Danglies
                    ShopItem(itemId=2253, price=10, goldPrice=3, color1=126, color2=227, itemType="HeadItem"), # Raindrop Blue Raindrop Earrings with Moonlight Gray Trim
                    ShopItem(itemId=2426, price=10, goldPrice=3, color1=168, color2=168, itemType="HeadItem"), # Never Gold Simple Hoops
                    ShopItem(itemId=2424, price=10, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Heart-Shaped Hoops
                    ShopItem(itemId=2425, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Shimmery Hoops
                    ShopItem(itemId=3033, price=10, goldPrice=1, color1=121, color2=121, itemType="AnkleItem"), # Daisy Pink Friendship Anklet
                    ShopItem(itemId=3051, price=10, goldPrice=1, color1=45, color2=45, itemType="AnkleItem"), # Strawberry Red Licorice Twist Anklet
                    ShopItem(itemId=3032, price=10, goldPrice=1, color1=42, color2=42, itemType="AnkleItem"), # Blueberry Blue Rainbow Ankle Bands
                    ShopItem(itemId=3031, price=10, goldPrice=1, color1=126, color2=227, itemType="AnkleItem"), # Raindrop Blue Raindrop Anklet with Moonlight Gray Trim
                    ShopItem(itemId=3023, price=10, goldPrice=1, color1=180, color2=180, itemType="AnkleItem"), # Seashell Blue Clam Ribbon Anklet
                    ShopItem(itemId=3022, price=10, goldPrice=1, color1=152, color2=152, itemType="AnkleItem"), # Pale Purple Shell Anklet
                    ShopItem(itemId=3049, price=10, goldPrice=1, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Fine Feathered Anklet
                    ShopItem(itemId=3034, price=10, goldPrice=1, color1=13, color2=13, itemType="AnkleItem"), # Coral Pink Freesia Ankle Flounce
                    ShopItem(itemId=3021, price=10, goldPrice=1, color1=200, color2=200, itemType="AnkleItem"), # Ruby Pink Dear Droplets Anklet
                    ShopItem(itemId=3052, price=10, goldPrice=1, color1=162, color2=162, itemType="AnkleItem"), # Sunglow Yellow Twirly Jeweled Anklet
                    ShopItem(itemId=3036, price=10, goldPrice=1, color1=30, color2=30, itemType="AnkleItem"), # Pumpkin Orange Bottle Cap Anklet
                    ShopItem(itemId=3020, price=10, goldPrice=1, color1=126, color2=126, itemType="AnkleItem"), # Raindrop Blue Teardrop Anklet
                    ShopItem(itemId=3015, price=10, goldPrice=1, color1=69, color2=69, itemType="AnkleItem"), # Powder Blue Bubble Anklet
                    ShopItem(itemId=3008, price=10, goldPrice=1, color1=35, color2=35, itemType="AnkleItem"), # Celery Green Grass Wrap Anklet
                    ShopItem(itemId=3045, price=10, goldPrice=1, color1=162, color2=162, itemType="AnkleItem"), # Sunglow Yellow Harvest Moon Anklet
                    ShopItem(itemId=3043, price=10, goldPrice=1, color1=35, color2=35, itemType="AnkleItem"), # Celery Green Trinity Leaf Anklet
                    ShopItem(itemId=3024, price=10, goldPrice=1, color1=227, color2=227, itemType="AnkleItem"), # Moonlight Gray Tinkered Anklet
                    ShopItem(itemId=3006, price=10, goldPrice=1, color1=267, color2=267, itemType="AnkleItem"), # Celestial Blue Tropic Flower Anklet
                    ShopItem(itemId=3003, price=10, goldPrice=1, color1=152, color2=152, itemType="AnkleItem"), # Pale Purple Triple Blossom Anklet

                ]
            ),
        ]
    ),

    NPCShop(
        zone=ZoneConstants.SUMMIT_STYLE,
        shopId=2,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.DIVA_WINGS,
            position=(410, 450),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_DIVA_WINGS
        ),
        collections=[
            ShopCollection(
                collectionId=82, # Floral Collections
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2427, price=25, goldPrice=10, color1=201, color2=121, itemType="HeadItem"), # Velvet Red Hydrangea Barrette
                    ShopItem(itemId=1000058, price=45, goldPrice=16, color1=201, color2=121, itemType="Shirt"), # Velvet Red Hydrangea Top
                    ShopItem(itemId=1465, price=45, goldPrice=16, color1=201, color2=121, itemType="Skirt"), # Velvet Red Hydrangea Skirt
                    ShopItem(itemId=3846, price=25, goldPrice=10, color1=201, color2=121, itemType="Shoes"), # Velvet Red Hydrangea Heels
                    ShopItem(itemId=2284, price=25, goldPrice=10, color1=166, color2=1, itemType="HeadItem"), # Snow White Snowdrop Headband
                    ShopItem(itemId=343, price=45, goldPrice=16, color1=166, color2=1, itemType="Shirt"), # Snow White Snowdrop Top
                    ShopItem(itemId=629, price=15, goldPrice=6, color1=166, color2=1, itemType="Belt"), # Snow White Snowdrop Sash
                    ShopItem(itemId=1280, price=45, goldPrice=16, color1=166, color2=1, itemType="Skirt"), # Snow White Snowdrop Skirt
                    ShopItem(itemId=3704, price=25, goldPrice=10, color1=166, color2=1, itemType="Shoes"), # Snow White Snowdrop Shoes
                    ShopItem(itemId=2292, price=25, goldPrice=10, color1=208, color2=267, itemType="HeadItem"), # Cerulean Blue Hanami Headpiece
                    ShopItem(itemId=377, price=45, goldPrice=16, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Hanami Top
                    ShopItem(itemId=636, price=15, goldPrice=6, color1=209, color2=267, itemType="Belt"), # Deep Sea Blue Hanami Sash
                    ShopItem(itemId=1300, price=45, goldPrice=16, color1=208, color2=267, itemType="Skirt"), # Cerulean Blue Hanami Long Skirt
                    ShopItem(itemId=3717, price=25, goldPrice=16, color1=267, color2=98, itemType="Shoes"), # Celestial Blue Hanami Geta Shoes
                    ShopItem(itemId=2292, price=25, goldPrice=10, color1=81, color2=26, itemType="HeadItem"), # Crimson Red Hanami Headpiece
                    ShopItem(itemId=377, price=45, goldPrice=16, color1=199, color2=26, itemType="Shirt"), # Cherryblossom Pink Hanami Top
                    ShopItem(itemId=636, price=15, goldPrice=6, color1=81, color2=26, itemType="Belt"), # Crimson Red Hanami Sash
                    ShopItem(itemId=1295, price=45, goldPrice=16, color1=199, color2=26, itemType="Skirt"), # Cherryblossom Pink Hanami Short Skirt
                    ShopItem(itemId=3717, price=25, goldPrice=10, color1=81, color2=98, itemType="Shoes"), # Crimson Red Hanami Geta Shoes
                    ShopItem(itemId=2449, price=25, goldPrice=10, color1=267, color2=10, itemType="HeadItem"), # Celestial Blue Azalea Barrette
                    ShopItem(itemId=1000074, price=45, goldPrice=16, color1=10, color2=267, itemType="Shirt"), # Cantaloupe Orange Azalea Top
                    ShopItem(itemId=1481, price=45, goldPrice=16, color1=10, color2=267, itemType="Skirt"), # Cantaloupe Orange Azalea Skirt
                    ShopItem(itemId=3866, price=25, goldPrice=10, color1=10, color2=267, itemType="Shoes"), # Cantaloupe Orange Azalea Sandals
                    ShopItem(itemId=385, price=45, goldPrice=16, color1=287, color2=166, itemType="Shirt"), # Dianthus Red Dianthus Blouse
                    ShopItem(itemId=1305, price=45, goldPrice=16, color1=287, color2=166, itemType="Skirt"), # Dianthus Red Dianthus Skirt
                    ShopItem(itemId=3722, price=25, goldPrice=10, color1=287, color2=166, itemType="Shoes"), # Dianthus Red Dianthus Shoes
                    ShopItem(itemId=2336, price=25, goldPrice=10, color1=186, color2=230, itemType="HeadItem"), # Honeycomb Yellow Flame Lily Barrette
                    ShopItem(itemId=417, price=45, goldPrice=16, color1=186, color2=230, itemType="Shirt"), # Honeycomb Yellow Flame Lily Top
                    ShopItem(itemId=1335, price=45, goldPrice=16, color1=186, color2=230, itemType="Skirt"), # Honeycomb Yellow Flame Lily Skirt
                    ShopItem(itemId=3758, price=25, goldPrice=10, color1=186, color2=230, itemType="Shoes"), # Honeycomb Yellow Flame Lily Shoes
                    ShopItem(itemId=2348, price=25, goldPrice=10, color1=130, color2=81, itemType="HeadItem"), # Orchid Pink Chrysanthemum Beret
                    ShopItem(itemId=477, price=45, goldPrice=16, color1=224, color2=81, itemType="Shirt"), # Ivory White Chrysanthemum Top
                    ShopItem(itemId=640, price=15, goldPrice=6, color1=81, color2=130, itemType="Belt"), # Crimson Red Chrysanthemum Belt
                    ShopItem(itemId=1396, price=45, goldPrice=16, color1=206, color2=81, itemType="Skirt"), # Raven Black Chrysanthemum Skirt
                    ShopItem(itemId=3779, price=25, goldPrice=10, color1=81, color2=130, itemType="Shoes"), # Crimson Red Chrysanthemum Shoes
                    ShopItem(itemId=2356, price=25, goldPrice=10, color1=153, color2=162, itemType="HeadItem"), # Frostbunny Blue Bead Cascade Earrings
                    ShopItem(itemId=483, price=45, goldPrice=16, color1=118, color2=153, itemType="Shirt"), # Sapphire Blue Camellia Top
                    ShopItem(itemId=1400, price=45, goldPrice=16, color1=206, color2=118, itemType="Skirt"), # Raven Black Camellia Skirt
                    ShopItem(itemId=3782, price=25, goldPrice=10, color1=74, color2=74, itemType="Shoes"), # Papyrus Tan Camellia Boots
                    ShopItem(itemId=2386, price=25, goldPrice=10, color1=224, color2=153, itemType="HeadItem"), # Ivory White Snow Rose Barrettes with Frostbunny Blue Trim
                    ShopItem(itemId=1000024, price=45, goldPrice=16, color1=224, color2=153, itemType="Shirt"), # Ivory White Snow Rose Top with Frostbunny Blue Trim
                    ShopItem(itemId=1435, price=45, goldPrice=16, color1=153, color2=153, itemType="Skirt"), # Frostbunny Blue Snow Rose Skirt
                    ShopItem(itemId=3815, price=25, goldPrice=10, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Snow Rose Heels
                    ShopItem(itemId=2171, price=25, goldPrice=10, color1=211, color2=211, itemType="HeadItem"), # Gentian Purple Moth Orchid Headband
                    ShopItem(itemId=216, price=45, goldPrice=16, color1=51, color2=15, itemType="Shirt"), # Periwinkle Blue Moth Orchid Top
                    ShopItem(itemId=594, price=15, goldPrice=6, color1=211, color2=211, itemType="Belt"), # Gentian Purple Moth Orchid Leaf Sash
                    ShopItem(itemId=1183, price=45, goldPrice=16, color1=51, color2=211, itemType="Skirt"), # Periwinkle Blue Moth Orchid Bottom
                    ShopItem(itemId=3629, price=25, goldPrice=10, color1=51, color2=15, itemType="Shoes"), # Periwinkle Blue Moth Orchid Shoes
                    ShopItem(itemId=2172, price=25, goldPrice=10, color1=258, color2=125, itemType="HeadItem"), # Spearmint Green Dragon Arum Crown
                    ShopItem(itemId=217, price=45, goldPrice=16, color1=166, color2=18, itemType="Shirt"), # Snow White Dragon Arum Top
                    ShopItem(itemId=593, price=15, goldPrice=6, color1=258, color2=258, itemType="Belt"), # Spearmint Green Dragon Arum Sash
                    ShopItem(itemId=1185, price=45, goldPrice=16, color1=166, color2=18, itemType="Skirt"), # Snow White Dragon Arum Skirt
                    ShopItem(itemId=3630, price=25, goldPrice=10, color1=258, color2=125, itemType="Shoes"), # Spearmint Green Dragon Arum Shoes
                    ShopItem(itemId=2100, price=25, goldPrice=10, color1=153, color2=166, itemType="HeadItem"), # Frostbunny Blue Campanula Barrette
                    ShopItem(itemId=108, price=45, goldPrice=16, color1=153, color2=166, itemType="Shirt"), # Frostbunny Blue Campanula Top
                    ShopItem(itemId=1111, price=45, goldPrice=16, color1=153, color2=166, itemType="Skirt"), # Frostbunny Blue Campanula Skirt
                    ShopItem(itemId=3578, price=25, goldPrice=10, color1=153, color2=166, itemType="Shoes"), # Frostbunny Blue Campanula Shoes
                    ShopItem(itemId=2120, price=25, goldPrice=10, color1=199, color2=121, itemType="HeadItem"), # Cherryblossom Pink Campis Barrette
                    ShopItem(itemId=109, price=45, goldPrice=16, color1=199, color2=121, itemType="Shirt"), # Cherryblossom Pink Campis Top
                    ShopItem(itemId=1121, price=45, goldPrice=16, color1=199, color2=121, itemType="Skirt"), # Cherryblossom Pink Campis Skirt
                    ShopItem(itemId=3579, price=25, goldPrice=10, color1=199, color2=121, itemType="Shoes"), # Cherryblossom Pink Campis Shoes
                    ShopItem(itemId=2123, price=25, goldPrice=10, color1=152, color2=183, itemType="HeadItem"), # Pale Purple Lagerstroemia Hat
                    ShopItem(itemId=112, price=45, goldPrice=16, color1=152, color2=183, itemType="Shirt"), # Pale Purple Lagerstroemia Top
                    ShopItem(itemId=1124, price=45, goldPrice=16, color1=152, color2=183, itemType="Skirt"), # Pale Purple Lagerstroemia Skirt
                    ShopItem(itemId=3582, price=25, goldPrice=10, color1=152, color2=183, itemType="Shoes"), # Pale Purple Lagerstroemia Shoes
                    ShopItem(itemId=2586, price=15, goldPrice=6, color1=138, color2=138, itemType="Necklace"), # Persimmon Orange Marigold Necklace
                    ShopItem(itemId=333, price=45, goldPrice=16, color1=30, color2=10, itemType="Shirt"), # Pumpkin Orange Marigold Top
                    ShopItem(itemId=1270, price=45, goldPrice=16, color1=30, color2=10, itemType="Skirt"), # Pumpkin Orange Marigold Skirt
                    ShopItem(itemId=3695, price=25, goldPrice=10, color1=138, color2=138, itemType="Shoes"), # Persimmon Orange Marigold Shoes
                ],
            ),
            ShopCollection(
                collectionId=46, # Mainland Styles
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=1000031, price=45, goldPrice=16, color1=180, color2=195, itemType="Shirt"), # Seashell Blue Chic Tie-Dye Top
                    ShopItem(itemId=1442, price=45, goldPrice=16, color1=180, color2=195, itemType="Skirt"), # Seashell Blue Chic Tie-Dye Skirt
                    ShopItem(itemId=3822, price=25, goldPrice=10, color1=180, color2=195, itemType="Shoes"), # Seashell Blue Super Chic Sandals
                    ShopItem(itemId=1000037, price=45, goldPrice=16, color1=278, color2=110, itemType="Shirt"), # Aster Purple Fluttery Tie-Dye Top
                    ShopItem(itemId=1445, price=45, goldPrice=16, color1=278, color2=110, itemType="Skirt"), # Aster Purple Fluttery Tie-Dye Skirt
                    ShopItem(itemId=3822, price=25, goldPrice=10, color1=278, color2=110, itemType="Shoes"), # Aster Purple Super Chic Sandals
                    ShopItem(itemId=2423, price=25, goldPrice=10, color1=217, color2=267, itemType="HeadItem"), # Soft Gray Cute Cap
                    ShopItem(itemId=1000057, price=45, goldPrice=16, color1=217, color2=267, itemType="Shirt"), # Soft Gray Cardie Combo Top
                    ShopItem(itemId=1464, price=45, goldPrice=16, color1=217, color2=267, itemType="Skirt"), # Soft Gray Delightful Denim Skirt
                    ShopItem(itemId=3844, price=25, goldPrice=10, color1=217, color2=267, itemType="Shoes"), # Soft Gray Lovely Laceups
                    ShopItem(itemId=2634, price=15, goldPrice=6, color1=224, color2=267, itemType="Necklace"), # Ivory White Sweetheart Purse
                    ShopItem(itemId=1000055, price=45, goldPrice=16, color1=162, color2=224, itemType="Shirt"), # Sunglow Yellow Sweetheart Top
                    ShopItem(itemId=650, price=15, goldPrice=6, color1=267, color2=224, itemType="Belt"), # Celestial Blue Sweetheart Sash
                    ShopItem(itemId=1463, price=45, goldPrice=16, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sweetheart Skirt
                    ShopItem(itemId=3845, price=25, goldPrice=16, color1=162, color2=267, itemType="Shoes"), # Sunglow Yellow Sweetheart Sandals
                    ShopItem(itemId=2428, price=25, goldPrice=10, color1=135, color2=282, itemType="HeadItem"), # Boysenberry Purple Cute Cloud Earrings
                    ShopItem(itemId=1000061, price=45, goldPrice=16, color1=5, color2=152, itemType="Shirt"), # Wysteria Purple Rainy Day Top
                    ShopItem(itemId=1673, price=15, goldPrice=6, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Rainbow Umbrella
                    ShopItem(itemId=1468, price=45, goldPrice=16, color1=5, color2=152, itemType="Skirt"), # Wysteria Purple Rainy Day Skirt
                    ShopItem(itemId=3850, price=25, goldPrice=10, color1=135, color2=282, itemType="Shoes"), # Boysenberry Purple Cozy Rain Boots
                    ShopItem(itemId=1000052, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Soft Knit Sweater
                    ShopItem(itemId=1459, price=45, goldPrice=16, color1=141, color2=81, itemType="Skirt"), # Thundercloud Gray Pleasing Pleats Skirt
                    ShopItem(itemId=3840, price=25, goldPrice=10, color1=141, color2=224, itemType="Shoes"), # Thundercloud Gray Sweet Spring Laceups
                    ShopItem(itemId=2636, price=15, goldPrice=6, color1=105, color2=105, itemType="Necklace"), #  Siltstone Tan Sweet Beaded Necklace
                    ShopItem(itemId=1000063, price=45, goldPrice=16, color1=44, color2=123, itemType="Shirt"), # Plumblossom Pink Sweet Spring Hoodie
                    ShopItem(itemId=1470, price=45, goldPrice=16, color1=126, color2=123, itemType="Skirt"), # Raindrop Blue Layered Look Skirt
                    ShopItem(itemId=3855, price=25, goldPrice=10, color1=55, color2=224, itemType="Shoes"), # Pepper Black Cat Flats
                    ShopItem(itemId=1000080, price=45, goldPrice=16, color1=44, color2=134, itemType="Shirt"), #  Plumblossom Pink Stylish Hoodie
                    ShopItem(itemId=1487, price=45, goldPrice=16, color1=44, color2=134, itemType="Skirt"), # Plumblossom Pink Springy Skirt
                    ShopItem(itemId=3871, price=25, goldPrice=10, color1=44, color2=134, itemType="Shoes"), # Plumblossom Pink Perfect Plaid Loafers
                    ShopItem(itemId=2301, price=25, goldPrice=10, color1=11, color2=115, itemType="HeadItem"), # Marigold Yellow Folklorico Headband
                    ShopItem(itemId=386, price=45, goldPrice=16, color1=274, color2=149, itemType="Shirt"), # Bellflower Purple Folklorico Blouse
                    ShopItem(itemId=1306, price=45, goldPrice=16, color1=274, color2=149, itemType="Skirt"), # Bellflower Purple Folklorico Skirt
                    ShopItem(itemId=3726, price=25, goldPrice=10, color1=11, color2=149, itemType="Shoes"), # Marigold Yellow Folklorico Heels
                    ShopItem(itemId=1000114, price=45, goldPrice=16, color1=265, color2=17, itemType="Shirt"), # Bright Sky Blue Festive Floral Top
                    ShopItem(itemId=1001020, price=45, goldPrice=16, color1=265, color2=17, itemType="Skirt"), # Bright Sky Blue Festive Floral Skirt
                    ShopItem(itemId=3896, price=25, goldPrice=10, color1=17, color2=265, itemType="Shoes"), #  Tendershoot Green Pearl-Studded Sandals
                    ShopItem(itemId=1000122, price=45, goldPrice=16, color1=150, color2=18, itemType="Shirt"), # Dry Moss Green Summer Stripes Top
                    ShopItem(itemId=1001029, price=45, goldPrice=16, color1=150, color2=18, itemType="Skirt"), #  Dry Moss Green Summer Stripes Skirt
                    ShopItem(itemId=3904, price=25, goldPrice=10, color1=150, color2=18, itemType="Shoes"), # Dry Moss Green Summer Stripes Sandals
                    ShopItem(itemId=379, price=45, goldPrice=16, color1=189, color2=121, itemType="Shirt"), # Ladybug Red Breezy Ruffled Top
                    ShopItem(itemId=1299, price=45, goldPrice=16, color1=121, color2=189, itemType="Skirt"), # Daisy Pink Breezy Ruffled Skirt
                    ShopItem(itemId=3718, price=25, goldPrice=10, color1=206, color2=121, itemType="Shoes"), # Raven Black Ruffle Detail Shoes
                    ShopItem(itemId=2474, price=25, goldPrice=10, color1=84, color2=77, itemType="HeadItem"), # Copper Brown Hiking Hat
                    ShopItem(itemId=1000108, price=45, goldPrice=16, color1=224, color2=70, itemType="Shirt"), # Ivory White Hiking Gear
                    ShopItem(itemId=1001015, price=45, goldPrice=16, color1=209, color2=70, itemType="Skirt"), # Deep Sea Blue Hiking Shorts
                    ShopItem(itemId=3618, price=25, goldPrice=10, color1=78, color2=84, itemType="Shoes"), # Fawn Brown Woodchucks
                    ShopItem(itemId=145, price=45, goldPrice=16, color1=159, color2=170, itemType="Shirt"), # Tea Green Sporty Top
                    ShopItem(itemId=1048, price=45, goldPrice=16, color1=159, color2=170, itemType="Skirt"), # Tea Green Sports Shorts
                    ShopItem(itemId=3504, price=25, goldPrice=10, color1=170, color2=170, itemType="Shoes"), # Olive Green Striders
                    ShopItem(itemId=2466, price=25, goldPrice=10, color1=81, color2=224, itemType="HeadItem"), # Crimson Red Adventurer's Hat
                    ShopItem(itemId=1000112, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Adventurer Jacket
                    ShopItem(itemId=1001018, price=45, goldPrice=16, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Adventurer Leggings
                    ShopItem(itemId=3894, price=25, goldPrice=10, color1=81, color2=206, itemType="Shoes"), #  Crimson Red Adventurer's Boots
                    ShopItem(itemId=1000116, price=45, goldPrice=16, color1=203, color2=17, itemType="Shirt"), # Shadow Green Bold Summer Vest
                    ShopItem(itemId=1001022, price=45, goldPrice=16, color1=203, color2=17, itemType="Skirt"), # Shadow Green Bold Summer Skirt
                    ShopItem(itemId=3898, price=25, goldPrice=10, color1=91, color2=105, itemType="Shoes"), # Coconut Brown Bold Summer Boots
                    ShopItem(itemId=1000117, price=45, goldPrice=16, color1=166, color2=207, itemType="Shirt"), # Snow White Frills and Flounce Top
                    ShopItem(itemId=654, price=15, goldPrice=6, color1=286, color2=123, itemType="Belt"), #  Cherry Pink Striped Summer Sash
                    ShopItem(itemId=1001023, price=45, goldPrice=16, color1=166, color2=207, itemType="Skirt"), # Snow White Frills and Flounce Skirt
                    ShopItem(itemId=3673, price=25, goldPrice=16, color1=286, color2=123, itemType="Shoes"), # Cherry Pink Funky Wedges
                    ShopItem(itemId=294, price=45, goldPrice=16, color1=17, color2=165, itemType="Shirt"), #  Tendershoot Green Bow Sleeve Blouse
                    ShopItem(itemId=1246, price=45, goldPrice=16, color1=165, color2=17, itemType="Skirt"), # Spring Breeze Green Bow Belt Skirt
                    ShopItem(itemId=3626, price=25, goldPrice=10, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Ruffly Slippers
                    ShopItem(itemId=96, price=45, goldPrice=16, color1=121, color2=44, itemType="Shirt"), # Daisy Pink I-Heart-Mermaids Tee
                    ShopItem(itemId=1186, price=45, goldPrice=16, color1=121, color2=44, itemType="Skirt"), # Daisy Pink Ruffle Skirt
                    ShopItem(itemId=3619, price=25, goldPrice=10, color1=44, color2=121, itemType="Shoes"), # Plumblossom Pink Sparkly Slippers
                    ShopItem(itemId=2306, price=25, goldPrice=10, color1=189, color2=185, itemType="HeadItem"), # Ladybug Red Sunny Style Hat
                    ShopItem(itemId=394, price=45, goldPrice=16, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Sunny Style Top
                    ShopItem(itemId=1315, price=45, goldPrice=16, color1=185, color2=189, itemType="Skirt"), # Midnight Blue Sunny Style Skirt
                    ShopItem(itemId=3734, price=25, goldPrice=10, color1=206, color2=166, itemType="Shoes"), # Raven Black Sunny Style Boots
                    ShopItem(itemId=2084, price=25, goldPrice=10, color1=75, color2=84, itemType="HeadItem"), # Umber Brown Darling Fairy Crown
                    ShopItem(itemId=2531, price=15, goldPrice=6, color1=84, color2=75, itemType="Necklace"), # Copper Brown Darling Fairy Necklace
                    ShopItem(itemId=88, price=45, goldPrice=16, color1=84, color2=75, itemType="Shirt"), # Copper Brown Darling Fairy Combo Top
                    ShopItem(itemId=1089, price=45, goldPrice=16, color1=75, color2=84, itemType="Skirt"), # Umber Brown Darling Dance Drape
                    ShopItem(itemId=3565, price=25, goldPrice=10, color1=84, color2=75, itemType="Shoes"), # Copper Brown Darling Fairy Boots
                    ShopItem(itemId=2208, price=25, goldPrice=10, color1=78, color2=78, itemType="HeadItem"), #  Fawn Brown Nifty Knit Hat
                    ShopItem(itemId=320, price=45, goldPrice=16, color1=166, color2=151, itemType="Shirt"), # Snow White Carefree Sweater Top with Yellow Trim
                    ShopItem(itemId=1259, price=45, goldPrice=16, color1=118, color2=153, itemType="Skirt"), # Sapphire Blue Casual Crops with Light Blue Trim
                    ShopItem(itemId=3673, price=25, goldPrice=10, color1=78, color2=99, itemType="Shoes"), # Fawn Brown Funky Wedges
                    ShopItem(itemId=2392, price=25, goldPrice=10, color1=269, color2=207, itemType="HeadItem"), # Crisp White Knit Beret
                    ShopItem(itemId=1000025, price=45, goldPrice=16, color1=207, color2=215, itemType="Shirt"), # Diamond Blue Fluffy Puffer Top
                    ShopItem(itemId=1436, price=45, goldPrice=16, color1=215, color2=207, itemType="Skirt"), # Pewter Gray Cozy Stripes Skirt
                    ShopItem(itemId=3816, price=25, goldPrice=10, color1=207, color2=269, itemType="Shoes"), # Diamond Blue Fuzzy Ankle Boots
                    ShopItem(itemId=2310, price=25, goldPrice=10, color1=275, color2=72, itemType="HeadItem"), # Shadowy Purple Flower Knit Headwrap
                    ShopItem(itemId=1000023, price=45, goldPrice=16, color1=275, color2=72, itemType="Shirt"), # Shadowy Purple Neat Knit Top
                    ShopItem(itemId=1434, price=45, goldPrice=16, color1=275, color2=72, itemType="Skirt"), # Shadowy Purple Neat Knit Skirt
                    ShopItem(itemId=3814, price=25, goldPrice=10, color1=275, color2=72, itemType="Shoes"), # Shadowy Purple Coziest Boots
                ],
            ),
            ShopCollection(
                collectionId=84, # Themed Fashions
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2403, price=25, goldPrice=10, color1=18, color2=152, itemType="HeadItem"), # Waterfall Blue Northern Lights Tiara
                    ShopItem(itemId=2629, price=15, goldPrice=6, color1=152, color2=18, itemType="Necklace"), # Pale Purple Northern Lights Necklace
                    ShopItem(itemId=1000036, price=45, goldPrice=16, color1=18, color2=152, itemType="Shirt"), # Waterfall Blue Northern Lights Top
                    ShopItem(itemId=1444, price=45, goldPrice=16, color1=18, color2=152, itemType="Skirt"), # Waterfall Blue Northern Lights Skirt
                    ShopItem(itemId=3824, price=25, goldPrice=10, color1=18, color2=152, itemType="Shoes"), # Waterfall Blue Northern Lights Heels

                    ShopItem(itemId=2285, price=25, goldPrice=10, color1=200, color2=44, itemType="HeadItem"), # Ruby Pink Sweet Baker Hat
                    ShopItem(itemId=2591, price=15, goldPrice=6, color1=44, color2=44, itemType="Necklace"), # Plumblossom Pink Sweet Bow
                    ShopItem(itemId=344, price=45, goldPrice=16, color1=200, color2=44, itemType="Shirt"), # Ruby Pink Sweet Puff Top
                    ShopItem(itemId=631, price=15, goldPrice=6, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Sweet Bow Sash
                    ShopItem(itemId=1281, price=45, goldPrice=16, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Sweet Puff Skirt
                    ShopItem(itemId=3705, price=25, goldPrice=10, color1=200, color2=44, itemType="Shoes"), # Ruby Pink Sweet Bow Shoes

                    ShopItem(itemId=2101, price=25, goldPrice=10, color1=265, color2=45, itemType="HeadItem"), # Bright Sky Blue Straw and Blueberry Hat
                    ShopItem(itemId=248, price=45, goldPrice=16, color1=137, color2=265, itemType="Shirt"), # Lemon Yellow Serving-Talent Blouse
                    ShopItem(itemId=571, price=15, goldPrice=6, color1=45, color2=265, itemType="Belt"), # Strawberry Red Simple Apron with Bright Sky Blue Trim
                    ShopItem(itemId=1208, price=45, goldPrice=16, color1=265, color2=137, itemType="Skirt"), # Bright Sky Blue Tea-Brewer Skirt
                    ShopItem(itemId=3570, price=25, goldPrice=5, color1=265, color2=45 , itemType="Shoes"), # Bright Sky Blue Really Rainy Boots

                    ShopItem(itemId=2438, price=25, goldPrice=10, color1=121, color2=239, itemType="HeadItem"), # Daisy Pink Carnival Chic Top Hat
                    ShopItem(itemId=1000075, price=45, goldPrice=16, color1=121, color2=239, itemType="Shirt"), # Daisy Pink Carnival Chic Top
                    ShopItem(itemId=1482, price=45, goldPrice=16, color1=239, color2=121, itemType="Skirt"), # Coffee Black Carnival Chic Skirt
                    ShopItem(itemId=3867, price=25, goldPrice=10, color1=239, color2=239, itemType="Shoes"), # Coffee Black Carnival Chic Boots

                    ShopItem(itemId=1000072, price=45, goldPrice=16, color1=111, color2=225, itemType="Shirt"), # Sparkling Yellow Siren Style Top
                    ShopItem(itemId=1478, price=45, goldPrice=16, color1=225, color2=111, itemType="Skirt"), # Eggplant Purple Siren Style Skirt
                    ShopItem(itemId=3863, price=25, goldPrice=10, color1=225, color2=111, itemType="Shoes"), # Eggplant Purple Siren Style Sandals

                    ShopItem(itemId=1000113, price=45, goldPrice=16, color1=267, color2=159, itemType="Shirt"), # Celestial Blue Parrot Party Top
                    ShopItem(itemId=1001019, price=45, goldPrice=16, color1=267, color2=159, itemType="Skirt"), # Celestial Blue Parrot Party Skirt
                    ShopItem(itemId=3895, price=25, goldPrice=10, color1=159, color2=267, itemType="Shoes"), # Tea Green Parrot Party Heels

                    ShopItem(itemId=1000111, price=45, goldPrice=16, color1=204, color2=205, itemType="Shirt"), # Bamboo Green Sorceress Dress Top
                    ShopItem(itemId=1001017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Sorceress Dress Skirt
                    ShopItem(itemId=3893, price=25, goldPrice=10, color1=205, color2=204, itemType="Shoes"), # Myrtle Green Sorceress Heels

                    ShopItem(itemId=2299, price=25, goldPrice=10, color1=206, color2=287, itemType="HeadItem"), # Raven Black Flaptastic Cloche
                    ShopItem(itemId=383, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Flaptastic Top
                    ShopItem(itemId=1303, price=45, goldPrice=16, color1=206, color2=287, itemType="Skirt"), # Raven Black Flaptastic Skirt
                    ShopItem(itemId=3721, price=25, goldPrice=10, color1=206, color2=287, itemType="Shoes"), # Raven Black Flaptastic Shoes

                    ShopItem(itemId=2608, price=15, goldPrice=6, color1=110, color2=110, itemType="Necklace"), # Rosy Pink Sock Hop Scarf
                    ShopItem(itemId=399, price=45, goldPrice=16, color1=26, color2=110, itemType="Shirt"), # Raspberry Pink Sock Hop Top
                    ShopItem(itemId=1322, price=45, goldPrice=16, color1=26, color2=110, itemType="Skirt"), # Raspberry Pink Sock Hop Skirt
                    ShopItem(itemId=3746, price=25, goldPrice=10, color1=110, color2=26, itemType="Shoes"), # Rosy Pink Sock Hop Shoes

                    ShopItem(itemId=2111, price=25, goldPrice=10, color1=75, color2=265, itemType="HeadItem"), # Umber Brown Tiger Lily Head Piece
                    ShopItem(itemId=117, price=45, goldPrice=16, color1=75, color2=265, itemType="Shirt"), # Umber Brown Tiger Lily Top
                    ShopItem(itemId=1114, price=45, goldPrice=16, color1=75, color2=265, itemType="Skirt"), # Umber Brown Tassel Skirt
                    ShopItem(itemId=3585, price=25, goldPrice=10, color1=265, color2=75, itemType="Shoes"), # Bright Sky Blue Fire Dance Moccasins

                    ShopItem(itemId=341, price=45, goldPrice=16, color1=230, color2=8, itemType="Shirt"), # Scarlet Red Top 40 Jacket
                    ShopItem(itemId=1619, price=15, goldPrice=6, color1=8, color2=8, itemType="WristItem"), # Watermelon Pink Sassy Glove
                    ShopItem(itemId=1278, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Top 40 Pants
                    ShopItem(itemId=3702, price=25, goldPrice=10, color1=224, color2=230, itemType="Shoes"), # Ivory White Top 40 Sneakers

                    ShopItem(itemId=342, price=45, goldPrice=16, color1=239, color2=183, itemType="Shirt"), # Coffee Black Rock n' Roll Top
                    ShopItem(itemId=628, price=15, goldPrice=6, color1=239, color2=239, itemType="Belt"), # Coffee Black Rock n' Roll Chain Belt
                    ShopItem(itemId=1620, price=15, goldPrice=6, color1=239, color2=239, itemType="WristItem"), # Coffee Black Rock n' Roll Cuff
                    ShopItem(itemId=1279, price=45, goldPrice=16, color1=239, color2=183, itemType="Skirt"), # Coffee Black Rock n' Roll Skirt
                    ShopItem(itemId=3703, price=25, goldPrice=10, color1=239, color2=183, itemType="Shoes"), # Coffee Black Rock n' Roll Boots

                    ShopItem(itemId=2280, price=25, goldPrice=10, color1=286, color2=286, itemType="HeadItem"), # Cherry Pink Far Out Funky Earrings
                    ShopItem(itemId=339, price=25, goldPrice=16, color1=286, color2=226, itemType="Shirt"), # Cherry Pink Like, Totally! Top
                    ShopItem(itemId=1276, price=45, goldPrice=16, color1=229, color2=226, itemType="Skirt"), # Electric Indigo Radical Tutu
                    ShopItem(itemId=3701, price=25, goldPrice=10, color1=229, color2=226, itemType="Shoes"), # Electric Indigo Leg Warmer Shoes

                    ShopItem(itemId=399, price=45, goldPrice=16, color1=195, color2=226, itemType="Shirt"), # Electric Blue Sock Hop Top
                    ShopItem(itemId=1274, price=45, goldPrice=16, color1=226, color2=195, itemType="Skirt"), # Goldenrod Yellow Silly Tutu
                    ShopItem(itemId=3699, price=25, goldPrice=10, color1=226, color2=198, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks

                    ShopItem(itemId=2177, price=25, goldPrice=10, color1=70, color2=166, itemType="HeadItem"), # Tinker Blue Teatime Hat
                    ShopItem(itemId=250, price=45, goldPrice=16, color1=70, color2=166, itemType="Shirt"), # Tinker Blue Light and Lacy Tea Top
                    ShopItem(itemId=611, price=15, goldPrice=6, color1=166, color2=166, itemType="Belt"), # Snow White Light and Lacy Sash
                    ShopItem(itemId=1209, price=45, goldPrice=16, color1=70, color2=166, itemType="Skirt"), # Tinker Blue Light and Lacy Tea Skirt
                    ShopItem(itemId=3644, price=25, goldPrice=10, color1=70, color2=166, itemType="Shoes"), # Tinker Blue Light and Lacy Boots

                    ShopItem(itemId=2188, price=25, goldPrice=10, color1=44, color2=182, itemType="HeadItem"), # Plumblossom Pink Serving-Talent Hat with Twilight Blue Trim
                    ShopItem(itemId=248, price=45, goldPrice=16, color1=159, color2=182, itemType="Shirt"), # Tea Green Serving-Talent Blouse with Twilight Blue Trim
                    ShopItem(itemId=609, price=15, goldPrice=6, color1=182, color2=44, itemType="Belt"), #  Twilight Blue Serving-Talent Sash
                    ShopItem(itemId=1207, price=45, goldPrice=16, color1=159, color2=159, itemType="Skirt"), # Tea Green Serving-Talent Skirt
                    ShopItem(itemId=3696, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Petal Slippers

                    ShopItem(itemId=2176, price=25, goldPrice=10, color1=111, color2=130, itemType="HeadItem"), # Sparkling Yellow Tea-Brewer Cap
                    ShopItem(itemId=249, price=45, goldPrice=16, color1=130, color2=111, itemType="Shirt"), # Orchid Pink Tea-Brewer Top
                    ShopItem(itemId=610, price=15, goldPrice=6, color1=111, color2=226, itemType="Belt"), # Sparkling Yellow Tea-Brewer Apron
                    ShopItem(itemId=1208, price=45, goldPrice=16, color1=111, color2=130, itemType="Skirt"), # Sparkling Yellow Tea-Brewer Skirt
                    ShopItem(itemId=3696, price=25, goldPrice=10, color1=130, color2=130, itemType="Shoes"), # Orchid Pink Petal Slippers

                    ShopItem(itemId=2157, price=25, goldPrice=10, color1=166, color2=189, itemType="HeadItem"), # Snow White Baking Hat with Ladybug Red Trim
                    ShopItem(itemId=93, price=45, goldPrice=16, color1=189, color2=125, itemType="Shirt"), # Ladybug Red Desert Adventure Top
                    ShopItem(itemId=571, price=15, goldPrice=6, color1=45, color2=45, itemType="Belt"), # Strawberry Red Simple Apron
                    ShopItem(itemId=1520, price=15, goldPrice=6, color1=45, color2=166, itemType="WristItem"), # Strawberry Red Oven Mitt with Snow White Trim
                    ShopItem(itemId=1017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Grass Petal Pushers
                    ShopItem(itemId=3515, price=25, goldPrice=10, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Pea Pod Slippers
                ],
            ),
            ShopCollection(
                collectionId=95, # Princess Fashion
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2217, price=25, goldPrice=10, color1=162, color2=149, itemType="HeadItem"), # Sunglow Yellow Princess Headband
                    ShopItem(itemId=297, price=45, goldPrice=16, color1=162, color2=149, itemType="Shirt"), # Sunglow Yellow Poufy Princess Top
                    ShopItem(itemId=1247, price=45, goldPrice=16, color1=162, color2=149, itemType="Skirt"), # Sunglow Yellow Poufy Princess Skirt
                    ShopItem(itemId=3675, price=25, goldPrice=10, color1=149, color2=149, itemType="Shoes"), # Snowflake Blue Glittering Glass Slippers

                    ShopItem(itemId=2282, price=25, goldPrice=10, color1=206, color2=206, itemType="HeadItem"), # Raven Black Blossoming Rose Headband
                    ShopItem(itemId=340, price=45, goldPrice=16, color1=227, color2=206, itemType="Shirt"), # Moonlight Gray Dreamy Meadow Blouse
                    ShopItem(itemId=1277, price=45, goldPrice=16, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Dreamy Meadow Skirt
                    ShopItem(itemId=3696, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Splendid Petal Slippers

                    ShopItem(itemId=2397, price=25, goldPrice=10, color1=110, color2=110, itemType="HeadItem"), # Rosy Pink Lovely Blooms Crown
                    ShopItem(itemId=1000038, price=45, goldPrice=16, color1=52, color2=110, itemType="Shirt"), # Lavender Purple Lovely Blooms Top
                    ShopItem(itemId=1662, price=15, goldPrice=6, color1=116, color2=113, itemType="WristItem"), # Mushroom White Lovely Blooms Lantern
                    ShopItem(itemId=1446, price=45, goldPrice=16, color1=52, color2=110, itemType="Skirt"), # Lavender Purple Lovely Blooms Skirt
                    ShopItem(itemId=3826, price=25, goldPrice=10, color1=52, color2=110, itemType="Shoes"), # Lavender Purple Lovely Blooms Heels

                    ShopItem(itemId=2607, price=15, goldPrice=6, color1=69, color2=166, itemType="Necklace"), # Powder Blue Summer Breeze Necklace
                    ShopItem(itemId=397, price=45, goldPrice=16, color1=191, color2=113, itemType="Shirt"), # Vidia Black Summer Breeze Top
                    ShopItem(itemId=1640, price=15, goldPrice=6, color1=49, color2=166, itemType="WristItem"), # Robin Egg Blue Summer Breeze Bangles
                    ShopItem(itemId=1319, price=45, goldPrice=16, color1=191, color2=113, itemType="Skirt"), # Vidia Black Summer Breeze Pants
                    ShopItem(itemId=3745, price=25, goldPrice=10, color1=49, color2=166, itemType="Shoes"), # Robin Egg Blue Summer Moccassins

                    ShopItem(itemId=2323, price=25, goldPrice=10, color1=113, color2=38, itemType="HeadItem"), # Pale Rose Red Apple Headband
                    ShopItem(itemId=2585, price=15, goldPrice=6, color1=113, color2=118, itemType="Necklace"), # Pale Rose Red Fairy Friends Necklace
                    ShopItem(itemId=398, price=45, goldPrice=16, color1=38, color2=118, itemType="Shirt"), # Apple Green Wishing Apple Top
                    ShopItem(itemId=1320, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Wishing Apple Skirt
                    ShopItem(itemId=3696, price=25, goldPrice=10, color1=38, color2=38, itemType="Shoes"), # Apple Green Splendid Petal Slippers
                ],
            ),
        ]
    ),

    NPCShop(
        zone=ZoneConstants.GALES_OUTFITTERS,
        shopId=3,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.GALE,
            position=(434, 429),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_GALE
        ),
        collections=[
            ShopCollection(
            collectionId=41, # Gale's Favorites
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                 ShopItem(itemId=2037, price=10, goldPrice=3, color1=47, color2=47, itemType="HeadItem"), # Buttercup Yellow Gadgety Goggles
                 ShopItem(itemId=2003, price=10, goldPrice=3, color1=184, color2=184, itemType="HeadItem"), # Hummingbird Purple Grass Bow
                 ShopItem(itemId=40, price=17, goldPrice=5, color1=4, color2=128, itemType="Shirt"), # Bluebell Blue Down Feather Sweater
                 ShopItem(itemId=1047, price=17, goldPrice=5, color1=27, color2=157, itemType="Skirt"), # Corn Cob Yellow Sleepy Time Capris
                 ShopItem(itemId=3532, price=10, goldPrice=3, color1=163, color2=262, itemType="Shoes"), # Tundra Blue Bear Slippers
            ],
        ),
            ShopCollection(
            collectionId=78, # Pixie Party Dresses
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                ShopItem(itemId=1000129, price=40, goldPrice=13, color1=221, color2= 1, itemType="Shirt"), # Jade Green Tink's Pixie Party Top
                ShopItem(itemId=1001038, price=40, goldPrice=13, color1=221, color2= 1, itemType="Skirt"), # Jade Green Tink's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=221, color2= 1, itemType="Shoes"), # Jade Green Campanula Shoes

                ShopItem(itemId=1000126, price=40, goldPrice=13, color1=40, color2=207, itemType="Shirt"), # Candy Blue Peri's Pixie Party Top
                ShopItem(itemId=1001035, price=40, goldPrice=13, color1=40, color2=207, itemType="Skirt"), # Candy Blue Peri's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=40, color2=207, itemType="Shoes"), # Candy Blue Campanula Shoes

                ShopItem(itemId=1000124, price=40, goldPrice=13, color1=178, color2=10, itemType="Shirt"), # Fawn Orange Fawn's Pixie Party Top
                ShopItem(itemId=1001032, price=40, goldPrice=13, color1=178, color2=10, itemType="Skirt"), # Fawn Orange Fawn's Pixie Party Skirt
                ShopItem(itemId=3768, price=33, goldPrice=11, color1=178, color2=10, itemType="Shoes"), # Fawn Orange Autumn Leaf Boots

                ShopItem(itemId=1000127, price=40, goldPrice=13, color1=286, color2=286, itemType="Shirt"), # Cherry Pink Rosetta's Pixie Party Top
                ShopItem(itemId=1001036, price=40, goldPrice=13, color1=286, color2=286, itemType="Skirt"), # Cherry Pink Rosetta's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=286, color2=286, itemType="Shoes"), # Cherry Pink Campanula Shoes

                ShopItem(itemId=1000128, price=40, goldPrice=13, color1=208, color2=126, itemType="Shirt"), # Cerulean Blue Sil's Pixie Party Top
                ShopItem(itemId=1001037, price=40, goldPrice=13, color1=208, color2=126, itemType="Skirt"), # Cerulean Blue Sil's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=208, color2=126, itemType="Shoes"), # Cerulean Blue Campanula Shoes

                ShopItem(itemId=1000125, price=40, goldPrice=13, color1=228, color2=248, itemType="Shirt"), # Duckbill Orange Dessa's Pixie Party Top
                ShopItem(itemId=1001033, price=40, goldPrice=13, color1=228, color2=248, itemType="Skirt"), # Duckbill Orange Dessa's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=248, color2=248, itemType="Shoes"), # Saffron Yellow Campanula Shoes

                ShopItem(itemId=1000130, price=40, goldPrice=13, color1=225, color2=131, itemType="Shirt"), # Eggplant Purple Vidia's Pixie Party Top
                ShopItem(itemId=1001039, price=40, goldPrice=13, color1=225, color2=131, itemType="Skirt"), # Eggplant Purple Vidia's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=225, color2=131, itemType="Shoes"), # Eggplant Purple Campanula Shoes
            ],
        ),  
            ShopCollection(
            collectionId=97, # Famous Fairy Collection
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                ShopItem(itemId=185, price=40, goldPrice=16, color1=145, color2=145, itemType="Shirt"), # Tinker Bell Green Tink's Summer Top
                ShopItem(itemId=1167, price=40, goldPrice=16, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Tink's Summer Skirt
                ShopItem(itemId=3568, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tie Dye Sandals with White Trim

                ShopItem(itemId=168, price=40, goldPrice=16, color1=174, color2=174, itemType="Shirt"), # Rosetta Red Rosetta's Summer Top
                ShopItem(itemId=1154, price=40, goldPrice=16, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Rosetta's Summer Skirt
                ShopItem(itemId=3626, price=25, goldPrice=10, color1=174, color2=174, itemType="Shoes"), # Rosetta Red Ruffly Slippers

                ShopItem(itemId=184, price=40, goldPrice=16, color1=176, color2=27, itemType="Shirt"), # Silvermist Blue Sil's Summer Top
                ShopItem(itemId=1166, price=40, goldPrice=16, color1=176, color2=27, itemType="Skirt"), # Silvermist Blue Sil's Summer Skirt
                ShopItem(itemId=3608, price=25, goldPrice=10, color1=176, color2=27, itemType="Shoes"), # Silvermist Blue Strappy Sandal

                ShopItem(itemId=182, price=40, goldPrice=16, color1=178, color2=123, itemType="Shirt"), # Fawn Orange Fawn's Summer Tank
                ShopItem(itemId=1164, price=40, goldPrice=16, color1=178, color2=123, itemType="Skirt"), # Fawn Orange Fawn's Summer Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=178, color2=123, itemType="Shoes"), # Fawn Orange Sparkle Slippers

                ShopItem(itemId=183, price=40, goldPrice=16, color1=226, color2=29, itemType="Shirt"), # Goldenrod Yellow Dessa's Summer Tank
                ShopItem(itemId=1165, price=40, goldPrice=16, color1=226, color2=29, itemType="Skirt"), # Goldenrod Yellow Dessa's Summer Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=29, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers

                ShopItem(itemId=2077, price=25, goldPrice=10, color1=145, color2=224, itemType="HeadItem"), # Tinker Bell Green Adventure Bonnet with White Trim
                ShopItem(itemId=2533, price=15, goldPrice=6, color1=145, color2=145, itemType="Necklace"), # Tinker Bell Green Ruffle Neck Wrap
                ShopItem(itemId=80, price=40, goldPrice=16, color1=35, color2=35, itemType="Shirt"), # Celery Green Tink's Travel Top
                ShopItem(itemId=542, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Grass-braided Belt
                ShopItem(itemId=1082, price=40, goldPrice=16, color1=145, color2=1, itemType="Skirt"), # Tinker Bell Green Tink's Travel Skirt
                ShopItem(itemId=3562, price=25, goldPrice=10, color1=145, color2=145, itemType="Shoes"), # Tinker Bell Green Puffie Toe Boots

                ShopItem(itemId=85, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Fluffy Ruff Top
                ShopItem(itemId=1086, price=40, goldPrice=16, color1=174, color2=121, itemType="Skirt"), # Rosetta Red Bellflower Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes

                ShopItem(itemId=84, price=40, goldPrice=16, color1=126, color2=269, itemType="Shirt"), # Raindrop Blue Waterfall Top
                ShopItem(itemId=1087, price=40, goldPrice=16, color1=126, color2=269, itemType="Skirt"), # Raindrop Blue Waterfall Wrap
                ShopItem(itemId=3537, price=25, goldPrice=10, color1=126, color2=269, itemType="Shoes"), # Raindrop Blue Iris Boots

                ShopItem(itemId=82, price=40, goldPrice=16, color1=84, color2=178, itemType="Shirt"), # Copper Brown Feather Fun Top
                ShopItem(itemId=543, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Fawn Adventure Belt
                ShopItem(itemId=1084, price=40, goldPrice=16, color1=84, color2=178, itemType="Skirt"), # Copper Brown Critter Comfort Skirt
                ShopItem(itemId=3514, price=25, goldPrice=10, color1=178, color2=178, itemType="Shoes"), # Fawn Orange Ivy Ankle Boots

                ShopItem(itemId=2042, price=25, goldPrice=10, color1=231, color2=226, itemType="HeadItem"), # Sunny Orange Athletic Headband
                ShopItem(itemId=83, price=40, goldPrice=16, color1=226, color2=231, itemType="Shirt"), # Goldenrod Yellow Light Bright Top
                ShopItem(itemId=1085, price=40, goldPrice=16, color1=226, color2=231, itemType="Skirt"), # Goldenrod Yellow Light Bright Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=231, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers

                ShopItem(itemId=1000009, price=40, goldPrice=16, color1=145, color2=224, itemType="Shirt"), # Tinker Bell Green Tink's Frosty Top
                ShopItem(itemId=1423, price=40, goldPrice=16, color1=145, color2=224, itemType="Skirt"), # Tinker Bell Green Tink's Frosty Skirt
                ShopItem(itemId=3798, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tink's Frosty Boots

                ShopItem(itemId=1000008, price=40, goldPrice=16, color1=149, color2=166, itemType="Shirt"), # Snowflake Blue Periwinkle's Frosty Top
                ShopItem(itemId=1422, price=40, goldPrice=16, color1=149, color2=166, itemType="Skirt"), # Snowflake Blue Periwinkle's Frosty Skirt
                ShopItem(itemId=3797, price=25, goldPrice=10, color1=149, color2=166, itemType="Shoes"), # Snowflake Blue Periwinkle's Frosty Flats

                ShopItem(itemId=2371, price=25, goldPrice=10, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Rosetta's Headwrap
                ShopItem(itemId=1000004, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Rosetta's Winter Top
                ShopItem(itemId=1658, price=15, goldPrice=6, color1=84, color2=166, itemType="Wristitem"), # Copper Brown Cottonpuff Clutch
                ShopItem(itemId=1419, price=40, goldPrice=16, color1=224, color2=174, itemType="Skirt"), # Ivory White Rosetta's Winter Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=217, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes with Gray Trim

                ShopItem(itemId=2372, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Sil's Winter Hat
                ShopItem(itemId=1000005, price=40, goldPrice=16, color1=126, color2=224, itemType="Shirt"), # Raindrop Blue Sil's Winter Top
                ShopItem(itemId=1420, price=40, goldPrice=16, color1=135, color2=126, itemType="Skirt"), # Boysenberry Purple Sil's Winter Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=126, color2=135, itemType="Shoes"), # Raindrop Blue Slim Leaf Shoes with Boysenberry Purple Trim

                ShopItem(itemId=1000001, price=40, goldPrice=16, color1=238, color2=123, itemType="Shirt"), #  Zesty Orange Fawn's Winter Top
                ShopItem(itemId=1417, price=40, goldPrice=16, color1=79, color2=238, itemType="Skirt"), # Sienna Brown Fawn's Winter Skirt with Zesty Orange Trim
                ShopItem(itemId=3802, price=25, goldPrice=10, color1=238, color2=224, itemType="Shoes"), # Zesty Orange Fawn's Winter Boots

                ShopItem(itemId=2370, price=25, goldPrice=10, color1=84, color2=224, itemType="HeadItem"), # Copper Brown Iridessa's Earmuffs
                ShopItem(itemId=1000003, price=40, goldPrice=16, color1=84, color2=171, itemType="Shirt"), # Copper Brown Iridessa's Winter Top
                ShopItem(itemId=1418, price=40, goldPrice=16, color1=171, color2=84, itemType="Skirt"), # Sunrise Yellow Iridessa's Winter Skirt
                ShopItem(itemId=3795, price=25, goldPrice=10, color1=84, color2=224, itemType="Shoes"), # Copper Brown Iridessa's Winter Boots

                ShopItem(itemId=2373, price=25, goldPrice=10, color1=135, color2=5, itemType="HeadItem"), # Boysenberry Purple Vidia's Headwrap
                ShopItem(itemId=1000006, price=40, goldPrice=16, color1=5, color2=135, itemType="Shirt"), # Wysteria Purple Vidia's Winter Top
                ShopItem(itemId=1424, price=40, goldPrice=16, color1=5, color2=135, itemType="Skirt"), # Wysteria Purple Vidia's Winter Skirt
                ShopItem(itemId=3799, price=25, goldPrice=10, color1=135, color2=5, itemType="Shoes"), # Boysenberry Purple Vidia's Winter Boots

            ],
        ),
            ShopCollection(
            collectionId=79, # Floral Collections
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                ShopItem(itemId=2140, price=10, goldPrice=3, color1=10, color2=30, itemType="HeadItem"), # Cantaloupe Orange Citrus Barrette
                ShopItem(itemId=158, price=17, goldPrice=5, color1=10, color2=30, itemType="Shirt"), # Cantaloupe Orange Citrus Layer Top
                ShopItem(itemId=1144, price=17, goldPrice=5, color1=10, color2=30, itemType="Skirt"), # Cantaloupe Orange Citrus Peel Wrap
                ShopItem(itemId=3603, price=10, goldPrice=3, color1=30, color2=10, itemType="Shoes"), # Pumpkin Orange Citrus Peel Heels

                ShopItem(itemId=2139, price=10, goldPrice=3, color1=18, color2=27, itemType="HeadItem"), # Waterfall Blue Strawberry Barrette with Yellow Trim
                ShopItem(itemId=159, price=17, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Strawberry Top
                ShopItem(itemId=569, price=3, goldPrice=1, color1=139, color2=18, itemType="Belt"), # Seedling Green Strawberry Sash with Waterfall Blue Trim
                ShopItem(itemId=1142, price=17, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Strawberry Skirt
                ShopItem(itemId=3602, price=10, goldPrice=3, color1=139, color2=45, itemType="Shoes"), # Seedling Green Strawberry Low Heels with Strawberry Red Trim

                ShopItem(itemId=2058, price=10, goldPrice=3, color1=17, color2=0, itemType="HeadItem"), # Tendershoot Green Clover Headband
                ShopItem(itemId=59, price=17, goldPrice=5, color1=2, color2=17, itemType="Shirt"), # Clover Green Clover Top with Tendershoot Green Trim
                ShopItem(itemId=1064, price=17, goldPrice=5, color1=2, color2=17, itemType="Skirt"), # Clover Green Clover Skirt with Tendershoot Green Trim
                ShopItem(itemId=3546, price=10, goldPrice=3, color1=2, color2=17, itemType="Shoes"), # Clover Green Clover Slippers with Tendershoot Green Trim

                ShopItem(itemId=2067, price=10, goldPrice=3, color1=195, color2=209, itemType="HeadItem"), # Electric Blue Helenium Headband with Deep Sea Blue Trim
                ShopItem(itemId=68, price=17, goldPrice=5, color1=209, color2=195, itemType="Shirt"), # Deep Sea Blue Helenium Top
                ShopItem(itemId=1073, price=17, goldPrice=5, color1=209, color2=195, itemType="Skirt"), # Deep Sea Blue Helenium Skirt
                ShopItem(itemId=3555, price=10, goldPrice=3, color1=209, color2=195, itemType="Shoes"), # Deep Sea Blue Helenium Boots

                ShopItem(itemId=155, price=17, goldPrice=5, color1=152, color2=129, itemType="Shirt"), # Pale Purple Plumeria Top with Dark Purple Trim
                ShopItem(itemId=568, price=3, goldPrice=1, color1=69, color2=69, itemType="Belt"), # Powder Blue Plumeria Garland
                ShopItem(itemId=1140, price=17, goldPrice=5, color1=152, color2=129, itemType="Skirt"), # Pale Purple Plumeria Sarong with Dark Purple Trim
                ShopItem(itemId=3608, price=10, goldPrice=3, color1=69, color2=69, itemType="Shoes"), # Powder Blue Strappy Sandal

                ShopItem(itemId=2047, price=10, goldPrice=3, color1=265, color2=258, itemType="HeadItem"), # Bright Sky Blue Lantana Headband
                ShopItem(itemId=48, price=17, goldPrice=5, color1=265, color2=258, itemType="Shirt"), # Bright Sky Blue Lantana Top
                ShopItem(itemId=1053, price=17, goldPrice=5, color1=265, color2=258, itemType="Skirt"), # Bright Sky Blue Lantana Skirt
                ShopItem(itemId=3535, price=10, goldPrice=3, color1=258, color2=258, itemType="Shoes"), # Spearmint Green Lantana Slippers

                ShopItem(itemId=2057, price=10, goldPrice=3, color1=230, color2=121, itemType="HeadItem"), # Scarlet Red Ginkgo Headband
                ShopItem(itemId=58, price=17, goldPrice=5, color1=230, color2=121, itemType="Shirt"), # Scarlet Red Ginkgo Top
                ShopItem(itemId=1063, price=17, goldPrice=5, color1=230, color2=121, itemType="Skirt"), # Scarlet Red Ginkgo Skirt
                ShopItem(itemId=3545, price=10, goldPrice=3, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Ginkgo Slippers 

                ShopItem(itemId=2060, price=10, goldPrice=3, color1=152, color2=73, itemType="HeadItem"), # Pale Purple Lemon Balm Headband with Grape Purple Trim
                ShopItem(itemId=61, price=17, goldPrice=5, color1=152, color2=73, itemType="Shirt"), # Pale Purple Lemon Balm Top with Grape Purple Trim
                ShopItem(itemId=1066, price=17, goldPrice=5, color1=73, color2=152, itemType="Skirt"), # Grape Purple Lemon Balm Skirt
                ShopItem(itemId=3548, price=10, goldPrice=3, color1=73, color2=152, itemType="Shoes"), # Grape Purple Lemon Balm Boots

                ShopItem(itemId=2052, price=10, goldPrice=3, color1=226, color2=208, itemType="HeadItem"), # Goldenrod Yellow Saffron Headband
                ShopItem(itemId=53, price=17, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Saffron Top
                ShopItem(itemId=1058, price=17, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Saffron Skirt
                ShopItem(itemId=3540, price=10, goldPrice=3, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Saffron Slippers

                ShopItem(itemId=2061, price=10, goldPrice=3, color1=45, color2=139, itemType="HeadItem"), # Strawberry Red Poinsettia Headband with Seedling Green Trim
                ShopItem(itemId=62, price=17, goldPrice=5, color1=139, color2=45, itemType="Shirt"), # Seedling Green Poinsettia Top
                ShopItem(itemId=1067, price=17, goldPrice=5, color1=139, color2=45, itemType="Skirt"), # Seedling Green Poinsettia Skirt
                ShopItem(itemId=3549, price=10, goldPrice=3, color1=139, color2=45, itemType="Shoes"), # Seedling Green Poinsettia Boots

                ShopItem(itemId=2051, price=10, goldPrice=3, color1=18, color2=18, itemType="HeadItem"), # Waterfall Blue White Rose Headband
                ShopItem(itemId=52, price=17, goldPrice=5, color1=166, color2=18, itemType="Shirt"), # Snow White White Rose Top
                ShopItem(itemId=1057, price=17, goldPrice=5, color1=166, color2=18, itemType="Skirt"), # Snow White White Rose Skirt
                ShopItem(itemId=3539, price=10, goldPrice=3, color1=18, color2=18, itemType="Shoes"), # Waterfall Blue White Rose Slippers

                ShopItem(itemId=2054, price=10, goldPrice=3, color1=287, color2=121, itemType="HeadItem"), # Dianthus Red Cosmos Headband
                ShopItem(itemId=55, price=17, goldPrice=5, color1=287, color2=121, itemType="Shirt"), # Dianthus Red Cosmos Top
                ShopItem(itemId=1060, price=17, goldPrice=5, color1=287, color2=287, itemType="Skirt"), # Dianthus Red Cosmos Skirt
                ShopItem(itemId=3542, price=10, goldPrice=3, color1=287, color2=121, itemType="Shoes"), # Dianthus Red Cosmos Boots

                ShopItem(itemId=2049, price=10, goldPrice=3, color1=136, color2=125, itemType="HeadItem"), # Peacock Blue Iris Headband
                ShopItem(itemId=50, price=17, goldPrice=5, color1=136, color2=136, itemType="Shirt"), # Peacock Blue Iris Top
                ShopItem(itemId=1055, price=17, goldPrice=5, color1=136, color2=136, itemType="Skirt"), # Peacock Blue Iris Skirt
                ShopItem(itemId=3537, price=10, goldPrice=3, color1=136, color2=136, itemType="Shoes"), # Peacock Blue Iris Boots

                ShopItem(itemId=2046, price=10, goldPrice=3, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Nerine Headband
                ShopItem(itemId=47, price=17, goldPrice=5, color1=277, color2=144, itemType="Shirt"), # Misty Purple Nerine Top
                ShopItem(itemId=1052, price=17, goldPrice=5, color1=277, color2=144, itemType="Skirt"), # Misty Purple Nerine Skirt
                ShopItem(itemId=3534, price=10, goldPrice=3, color1=277, color2=144, itemType="Shoes"), # Misty Purple Nerine Boots

                ShopItem(itemId=2065, price=10, goldPrice=3, color1=223, color2=223, itemType="HeadItem"), # Teal Blue Euphorbia Headband
                ShopItem(itemId=66, price=17, goldPrice=5, color1=68, color2=223, itemType="Shirt"), # Huckleberry Blue Euphorbia Top
                ShopItem(itemId=1071, price=17, goldPrice=5, color1=223, color2=68, itemType="Skirt"), # Teal Blue Euphorbia Skirt
                ShopItem(itemId=3553, price=10, goldPrice=3, color1=223, color2=68, itemType="Shoes"), # Teal Blue Euphorbia Boots

                ShopItem(itemId=2053, price=10, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Dahlia Headband
                ShopItem(itemId=54, price=17, goldPrice=5, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Dahlia Top
                ShopItem(itemId=1059, price=17, goldPrice=5, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Dahlia Skirt
                ShopItem(itemId=3541, price=10, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Dahlia Slippers

                ShopItem(itemId=2059, price=10, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Geranium Headband
                ShopItem(itemId=60, price=17, goldPrice=5, color1=44, color2=130, itemType="Shirt"), # Plumblossom Pink Geranium Top
                ShopItem(itemId=1065, price=17, goldPrice=5, color1=44, color2=130, itemType="Skirt"), # Plumblossom Pink Geranium Skirt
                ShopItem(itemId=3547, price=10, goldPrice=3, color1=44, color2=130, itemType="Shoes"), # Plumblossom Pink Geranium Slippers

                ShopItem(itemId=2048, price=10, goldPrice=3, color1=258, color2=264, itemType="HeadItem"), # Spearmint Green Bougainvillea Headband
                ShopItem(itemId=49, price=17, goldPrice=5, color1=264, color2=258, itemType="Shirt"), # Jungle Green Bougainvillea Top
                ShopItem(itemId=1054, price=17, goldPrice=5, color1=264, color2=258, itemType="Skirt"), # Jungle Green Bougainvillea Skirt
                ShopItem(itemId=3536, price=10, goldPrice=3, color1=264, color2=258, itemType="Shoes"), # Jungle Green Bougainvillea Slippers

                ShopItem(itemId=2056, price=10, goldPrice=3, color1=51, color2=55, itemType="HeadItem"), # Periwinkle Blue Aster Headband
                ShopItem(itemId=57, price=17, goldPrice=5, color1=51, color2=55, itemType="Shirt"), #  Periwinkle Blue Aster Top
                ShopItem(itemId=1062, price=17, goldPrice=5, color1=51, color2=55, itemType="Skirt"), # Periwinkle Blue Aster Skirt
                ShopItem(itemId=3544, price=10, goldPrice=3, color1=51, color2=55, itemType="Shoes"), # Periwinkle Blue Aster Boots

                ShopItem(itemId=2121, price=10, goldPrice=3, color1=27, color2=26, itemType="HeadItem"), # Corn Cob Yellow Commelina Band
                ShopItem(itemId=110, price=17, goldPrice=5, color1=27, color2=26, itemType="Shirt"), # Corn Cob Yellow Commelina Top
                ShopItem(itemId=1122, price=17, goldPrice=5, color1=27, color2=26, itemType="Skirt"), #  Corn Cob Yellow Commelina Skirt
                ShopItem(itemId=3580, price=10, goldPrice=3, color1=27, color2=27, itemType="Shoes"), #  Corn Cob Yellow Commelina Shoes
            ],    
        ),
            ShopCollection(
            collectionId=28, # Animal-Inspired Fashions
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                ShopItem(itemId=2073, price=10, goldPrice=3, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
                ShopItem(itemId=76, price=17, goldPrice=5, color1=206, color2=142, itemType="Shirt"), # Raven Black Buzzy Bee Striped Wrap
                ShopItem(itemId=1003, price=17, goldPrice=5, color1=142, color2=142, itemType="Skirt"), # Bumble Bee Yellow Leafy Bubble Skirt
                ShopItem(itemId=3501, price=10, goldPrice=3, color1=142, color2=142, itemType="Shoes"), # Bumble Bee Yellow Petal Slippers

                ShopItem(itemId=2071, price=10, goldPrice=3, color1=44, color2=257, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
                ShopItem(itemId=91, price=17, goldPrice=5, color1=44, color2=44, itemType="Shirt"), # Plumblossom Pink Little Light Top
                ShopItem(itemId=1091, price=17, goldPrice=5, color1=44, color2=257, itemType="Skirt"), #  Plumblossom Pink Little Light Mini
                ShopItem(itemId=3501, price=10, goldPrice=3, color1=44, color2=44, itemType="Shoes"), #  Plumblossom Pink Petal Slippers

                ShopItem(itemId=2071, price=10, goldPrice=3, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
                ShopItem(itemId=172, price=17, goldPrice=5, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tank
                ShopItem(itemId=1156, price=17, goldPrice=5, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Skirt
                ShopItem(itemId=3501, price=10, goldPrice=3, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Petal Slippers

                ShopItem(itemId=2151, price=10, goldPrice=3, color1=1, color2=1, itemType="HeadItem"), # Mint Green Dragonfly Mask
                ShopItem(itemId=186, price=17, goldPrice=5, color1=1, color2=1, itemType="Shirt"), # Mint Green Dragonfly Top
                ShopItem(itemId=1168, price=17, goldPrice=5, color1=1, color2=1, itemType="Skirt"), # Mint Green Dragonfly Skirt
                ShopItem(itemId=3501, price=10, goldPrice=3, color1=1, color2=1, itemType="Shoes"), # Mint Green Petal Slippers

                ShopItem(itemId=2150, price=10, goldPrice=3, color1=267, color2=186, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                ShopItem(itemId=187, price=17, goldPrice=5, color1=267, color2=186, itemType="Shirt"), # Celestial Blue Hummingbird Top
                ShopItem(itemId=1169, price=17, goldPrice=5, color1=267, color2=186, itemType="Skirt"), # Celestial Blue Hummingbird Skirt
                ShopItem(itemId=3501, price=10, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Petal Slippers

                ShopItem(itemId=2033, price=10, goldPrice=3, color1=175, color2=159, itemType="HeadItem"), # Creek Green Firefly Spotlight Barrette
                ShopItem(itemId=2524, price=3, goldPrice=1, color1=175, color2=159, itemType="Necklace"), # Creek Green Firefly Glow Choker
                ShopItem(itemId=29, price=17, goldPrice=5, color1=175, color2=159, itemType="Shirt"), # Creek Green Orchid Firefly Wrap
                ShopItem(itemId=1032, price=17, goldPrice=5, color1=175, color2=159, itemType="Skirt"), # Creek Green Slit Satin Firefly Skirt
                ShopItem(itemId=3519, price=10, goldPrice=3, color1=175, color2=159, itemType="Shoes"), # Creek Green Firefly Glow Toes Slippers

                ShopItem(itemId=90, price=17, goldPrice=5, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Fanciful Flutter Top with White Trim
                ShopItem(itemId=548, price=3, goldPrice=1, color1=63, color2=166, itemType="Belt"), # Butterfly Blue Fanciful Flutter Sash with White Trim
                ShopItem(itemId=1090, price=17, goldPrice=5, color1=63, color2=166, itemType="Skirt"), # Butterfly Blue Fanciful Flutter Gown with White Trim
                ShopItem(itemId=3559, price=10, goldPrice=3, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Fanciful Flutter Flats with White Trim

                ShopItem(itemId=376, price=17, goldPrice=5, color1=189, color2=206, itemType="Shirt"), # Ladybug Red Morpho Butterfly Top with Raven Black Trim
                ShopItem(itemId=635, price=3, goldPrice=1, color1=189, color2=189, itemType="Belt"), # Ladybug Red Morpho Butterfly Sash
                ShopItem(itemId=1294, price=17, goldPrice=5, color1=30, color2=206, itemType="Skirt"), # Pumpkin Orange Morpho Butterfly Skirt with Raven Black Trim
                ShopItem(itemId=3716, price=10, goldPrice=3, color1=206, color2=189, itemType="Shoes"), # Raven Black Morpho Butterfly Shoes

                ShopItem(itemId=2367, price=10, goldPrice=3, color1=216, color2=216, itemType="HeadItem"), # Slate Gray Raven Mask
                ShopItem(itemId=499, price=17, goldPrice=5, color1=206, color2=216, itemType="Shirt"), # Raven Black Raven Costume Top with Slate Gray Trim
                ShopItem(itemId=1415, price=17, goldPrice=5, color1=206, color2=216, itemType="Skirt"), # Raven Black Raven Skirt with Slate Gray Trim
                ShopItem(itemId=3794, price=10, goldPrice=3, color1=206, color2=216, itemType="Shoes"), # Raven Black Raven Heels with Slate Gray Trim

                ShopItem(itemId=2347, price=10, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Fox Mask
                ShopItem(itemId=1000011, price=17, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Fox Top
                ShopItem(itemId=1395, price=17, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Fox Skirt
                ShopItem(itemId=3801, price=10, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Furry Critter Boots

                ShopItem(itemId=2360, price=10, goldPrice=3, color1=206, color2=169, itemType="HeadItem"), # Raven Black Raccoon Mask
                ShopItem(itemId=481, price=17, goldPrice=5, color1=169, color2=206, itemType="Shirt"), # Squirrel Gray Raccoon Top
                ShopItem(itemId=1398, price=17, goldPrice=5, color1=169, color2=206, itemType="Skirt"), # Squirrel Gray Raccoon Skirt
                ShopItem(itemId=3801, price=10, goldPrice=3, color1=206, color2=169, itemType="Shoes"), # Raven Black Furry Critter Boots

                ShopItem(itemId=2440, price=10, goldPrice=3, color1=212, color2=194, itemType="HeadItem"), # Indigo Purple Songbird Headband
                ShopItem(itemId=1000078, price=17, goldPrice=5, color1=194, color2=212, itemType="Shirt"), # Electric Pink Songbird Top
                ShopItem(itemId=1484, price=17, goldPrice=5, color1=212, color2=194, itemType="Skirt"), # Indigo Purple Songbird Skirt
                ShopItem(itemId=3869, price=10, goldPrice=3, color1=212, color2=194, itemType="Shoes"), # Indigo Purple Songbird Heels
            ],
        ),   
            ShopCollection(
            collectionId=40, # Casual and Sporty Wear
            currencyId=FairiesConstants.PINE_NEEDLES,
            items=[
                ShopItem(itemId=303, price=17, goldPrice=5, color1=166, color2=286, itemType="Shirt"), # Snow White Snowbound Ski Jacket with Cherry Pink Trim
                ShopItem(itemId=1253, price=17, goldPrice=5, color1=166, color2=286, itemType="Skirt"), # Snow White Warm Ski Pants with Cherry Pink Trim
                ShopItem(itemId=3682, price=10, goldPrice=3, color1=105, color2=286, itemType="Shoes"), # Siltstone Tan Swift Skis with Cherry Pink Trim

                ShopItem(itemId=197, price=17, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Rainbow Tee
                ShopItem(itemId=588, price=3, goldPrice=1, color1=141, color2=141, itemType="Belt"), # Thundercloud Gray Studded Belt
                ShopItem(itemId=1143, price=17, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Denim Flyers
                ShopItem(itemId=3849, price=10, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Rainbow Sneakers

                ShopItem(itemId=145, price=17, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Sporty Top
                ShopItem(itemId=1048, price=17, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sports Shorts
                ShopItem(itemId=3504, price=10, goldPrice=3, color1=162, color2=162, itemType="Shoes"), # Sunglow Yellow Striders

                ShopItem(itemId=214, price=17, goldPrice=5, color1=121, color2=282, itemType="Shirt"), # Daisy Pink Pretty Plaid Top
                ShopItem(itemId=1187, price=17, goldPrice=5, color1=121, color2=121, itemType="Skirt"), # Daisy Pink Stitched Leaf Skirt
                ShopItem(itemId=3620, price=10, goldPrice=3, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Pretty Plaid Flats

                ShopItem(itemId=283, price=17, goldPrice=5, color1=211, color2=5, itemType="Shirt"), # Gentian Purple Sporty Tankini
                ShopItem(itemId=1233, price=17, goldPrice=5, color1=211, color2=5, itemType="Skirt"), # Gentian Purple Sporty Swim Skirt
                ShopItem(itemId=3757, price=10, goldPrice=3, color1=211, color2=5, itemType="Shoes"), # Gentian Purple Summer Splash Shoes with Wysteria Purple Trim

                ShopItem(itemId=2335, price=10, goldPrice=3, color1=267, color2=166, itemType="HeadItem"), # Celestial Blue Summer Splash Hat
                ShopItem(itemId=415, price=17, goldPrice=5, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Summer Splash Top
                ShopItem(itemId=1334, price=17, goldPrice=5, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Summer Splash Skirt
                ShopItem(itemId=3757, price=10, goldPrice=3, color1=166, color2=267, itemType="Shoes"), # Snow White Summer Splash Shoes

                ShopItem(itemId=2043, price=10, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Sunny Days Hat
                ShopItem(itemId=45, price=17, goldPrice=5, color1=17, color2=175, itemType="Shirt"), # Tendershoot Green Sunshine Top
                ShopItem(itemId=1050, price=17, goldPrice=5, color1=35, color2=175, itemType="Skirt"), # Celery Green Sunshine Skirt
                ShopItem(itemId=3610, price=10, goldPrice=3, color1=17, color2=175, itemType="Shoes"), # Tendershoot Green Fresh Petal Pumps

                ShopItem(itemId=46, price=17, goldPrice=5, color1=278, color2=135, itemType="Shirt"), # Aster Purple Tropical Top
                ShopItem(itemId=539, price=3, goldPrice=1, color1=135, color2=135, itemType="Belt"), # Boysenberry Purple Tropical Belt
                ShopItem(itemId=1051, price=17, goldPrice=5, color1=278, color2=135, itemType="Skirt"), # Aster Purple Tropical Sarong
                ShopItem(itemId=3568, price=10, goldPrice=3, color1=135, color2=278, itemType="Shoes"), # Boysenberry Purple Tie Dye Sandals

                ShopItem(itemId=28, price=17, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Bubble Button Top
                ShopItem(itemId=532, price=3, goldPrice=1, color1=69, color2=208, itemType="Belt"), # Powder Blue Triple Bubble Belt
                ShopItem(itemId=1010, price=17, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Lily Pad Bubble Skirt
                ShopItem(itemId=3520, price=10, goldPrice=3, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Bubble Top Slippers
            ],    
        ),    
        ShopCollection(
            collectionId=9, # Berry
            currencyId=FairiesConstants.PINE_NEEDLES,
            outfits=[
                ShopOutfit(
                    outfitId=2005, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=2009, price=20, goldPrice=8, color1=42, color2=51, itemType="HeadItem"), 
                        OutfitItem(itemId=480, price=35, goldPrice=13, color1=42, color2=51, itemType="Shirt"),
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=42, color2=42, itemType="Belt"),
                        OutfitItem(itemId=1377, price=35, goldPrice=13, color1=42, color2=51, itemType="Skirt"),
                        OutfitItem(itemId=3778, price=20, goldPrice=8, color1=42, color2=51, itemType="Shoes"),
                ],
            ),
                ShopOutfit(
                    outfitId=2006, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=1000073, price=35, goldPrice=13, color1=199, color2=26, itemType="Shirt"),
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=26, color2=26, itemType="Belt"),
                        OutfitItem(itemId=1077, price=35, goldPrice=13, color1=130, color2=26, itemType="Skirt"),
                        OutfitItem(itemId=3845, price=15, goldPrice=8, color1=199, color2=26, itemType="Shoes"),
                    ],
                ),
            ],
        ),
    ],
),




    NPCShop(
        zone=ZoneConstants.CASSIES_COSTUME_SHOP,
        shopId=4,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.CASSIE,
            position=(500, 350),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_CASSIE
        ),
        collections=[
            ShopCollection(
                collectionId=39, # Troop Uniforms
                currencyId=FairiesConstants.MEADOW_GRASS,
                items=[
                    # Rabbit - Fairies
                    ShopItem(itemId=2126, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                    ShopItem(itemId=1000088, price=37, goldPrice=11, color1=178, color2=237, itemType="Shirt"), # Fawn Orange, Melon Orange
                    ShopItem(itemId=1496, price=33, goldPrice=10, color1=178, color2=237, itemType="Skirt"), # Fawn Orange, Melon Orange
                    ShopItem(itemId=3595, price=33, goldPrice=10, color1=178, color2=237, itemType="Shoes"), # Fawn Orange, Melon Orange
                    # Butterfly - Fairies
                    ShopItem(itemId=2126, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                    ShopItem(itemId=1000084, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red, Daisy Pink
                    ShopItem(itemId=1491, price=33, goldPrice=10, color1=174, color2=121, itemType="Skirt"), # Rosetta Red, Daisy Pink
                    ShopItem(itemId=3595, price=33, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red, Daisy Pink
                    # Otter - Fairies
                    ShopItem(itemId=2126, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                    ShopItem(itemId=1000087, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue, Crystal Blue
                    ShopItem(itemId=1494, price=33, goldPrice=10, color1=176, color2=219, itemType="Skirt"), # Silvermist Blue, Crystal Blue
                    ShopItem(itemId=3595, price=33, goldPrice=10, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue, Crystal Blue
                    # Turtle - Fairies
                    ShopItem(itemId=2126, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                    ShopItem(itemId=1000089, price=37, goldPrice=11, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green, Caramel Tan
                    ShopItem(itemId=1495, price=33, goldPrice=10, color1=145, color2=250, itemType="Skirt"), # Tinker Bell Green, Caramel Tan
                    ShopItem(itemId=3595, price=33, goldPrice=10, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green, Caramel Tan
                    # Gloworm - Fairies
                    ShopItem(itemId=2126, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                    ShopItem(itemId=1000085, price=37, goldPrice=11, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow, Lemon Yellow
                    ShopItem(itemId=1492, price=33, goldPrice=10, color1=179, color2=137, itemType="Skirt"), # Iridessa Yellow, Lemon Yellow
                    ShopItem(itemId=3595, price=33, goldPrice=10, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow, Lemon Yellow
                    # Rabbit - Sparrowmen
                    ShopItem(itemId=2127, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                    ShopItem(itemId=142, price=17, goldPrice=5, color1=237, color2=78, itemType="Shirt"), # Melon Orange Animal-Talent Tee 
                    ShopItem(itemId=1193, price=17, goldPrice=5, color1=178, color2=178, itemType="Skirt"), # Fawn Orange Sporty Shorts
                    ShopItem(itemId=3597, price=10, goldPrice=3, color1=178, color2=237, itemType="Shoes"), # Fawn Orange Camp Referee Shoes with Melon Orange Trim
                    # Butterfly - Sparrowmen
                    ShopItem(itemId=2127, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                    ShopItem(itemId=139, price=17, goldPrice=5, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Garden-Talent Tee 
                    ShopItem(itemId=1193, price=17, goldPrice=5, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Sporty Shorts
                    ShopItem(itemId=3597, price=10, goldPrice=3, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Camp Referee Shoes with Daisy Pink Trim
                    # Otters - Sparrowmen
                    ShopItem(itemId=2127, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                    ShopItem(itemId=141, price=17, goldPrice=5, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue Water-Talent Tee
                    ShopItem(itemId=1193, price=17, goldPrice=5, color1=176, color2=176, itemType="Skirt"), # Silvermist Blue Sporty Shorts
                    ShopItem(itemId=3597, price=10, goldPrice=3, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue Camp Referee Shoes with Crystal Blue Trim
                    # Turtle - Sparrowmen
                    ShopItem(itemId=2127, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                    ShopItem(itemId=143, price=17, goldPrice=5, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green Tinker-Talent Tee
                    ShopItem(itemId=1193, price=17, goldPrice=5, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Sporty Shorts
                    ShopItem(itemId=3597, price=10, goldPrice=3, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green Camp Referee Shoes with Caramel Tan Trim 
                    # Gloworm - Sparrowmen
                    ShopItem(itemId=2127, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                    ShopItem(itemId=140, price=17, goldPrice=5, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow Light-Talent Tee 
                    ShopItem(itemId=1193, price=17, goldPrice=5, color1=179, color2=179, itemType="Skirt"), # Iridessa Yellow Sporty Shorts
                    ShopItem(itemId=3597, price=10, goldPrice=3, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow Camp Referee Shoes with Lemon Yellow Trim
                ],
            ),
            ShopCollection(
                collectionId=133, # Lobster
                currencyId=FairiesConstants.MEADOW_GRASS,
                items=[
                    ShopItem(itemId=2286, price=10, goldPrice=3, color1=189, color2=7, itemType="HeadItem"), # Lobster Mask
                    ShopItem(itemId=347, price=17, goldPrice=5, color1=189, color2=7, itemType="Shirt"), # Lobster Top
                    ShopItem(itemId=1293, price=17, goldPrice=5, color1=189, color2=7, itemType="Skirt"),
                ],
            ),
        ],
    ),
          



    NPCShop(
        zone=ZoneConstants.COALS_CLOTHIERS,
        shopId=5,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.COAL,
            position=(420, 420),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_COAL,
            gender=2
        ),
        collections=[
            ShopCollection(
                collectionId=83, # Mainland Styles
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=484, price=30, goldPrice=5, color1=45, color2=248, itemType="Shirt"), # Strawberry Red Varsity Jacket
                    ShopItem(itemId=1651, price=10, goldPrice=2, color1=78, color2=224, itemType="WristItem"), # Fawn Brown Football
                    ShopItem(itemId=1172, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Dry Leaf Trousers
                    ShopItem(itemId=3625, price=15, goldPrice=3, color1=78, color2=224, itemType="Shoes"), # Fawn Brown Woodchucks with White Trim

                    ShopItem(itemId=478, price=25, goldPrice=5, color1=126, color2=208, itemType="Shirt"), # Raindrop Blue Splish-Splash Tank
                    ShopItem(itemId=1394, price=25, goldPrice=5, color1=126, color2=208, itemType="Skirt"), # Raindrop Blue Splish-Splash Shorts
                    ShopItem(itemId=3604, price=15, goldPrice=3, color1=208, color2=126, itemType="Shoes"), # Cerulean Blue Tick Tock

                    ShopItem(itemId=286, price=25, goldPrice=5, color1=162, color2=161, itemType="Shirt"), # Sunglow Yellow Plenty Plaid Top
                    ShopItem(itemId=1133, price=25, goldPrice=5, color1=161, color2=161, itemType="Skirt"), # Buried Treasure Brown Cuffed Leaf Shorts
                    ShopItem(itemId=3671, price=15, goldPrice=3, color1=161, color2=162, itemType="Shoes"), # Buried Treasure Brown Plenty Plaid Deck Shoes

                    ShopItem(itemId=244, price=25, goldPrice=5, color1=166, color2=206, itemType="Shirt"), # Snow White Best Dressed Suspenders
                    ShopItem(itemId=1204, price=25, goldPrice=5, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Best Dressed Slacks
                    ShopItem(itemId=3641, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Best Dressed Loafers

                    ShopItem(itemId=2155, price=15, goldPrice=3, color1=27, color2=75, itemType="HeadItem"), # Corn Cob Yellow Sparrow Snow Cap
                    ShopItem(itemId=2578, price=5, goldPrice=1, color1=27, color2=27, itemType="Necklace"), # Corn Cob Yellow Twisty Winter Warmer
                    ShopItem(itemId=304, price=25, goldPrice=5, color1=75, color2=27, itemType="Shirt"), # Umber Brown Snowbound Ski Jacket
                    ShopItem(itemId=1592, price=10, goldPrice=2, color1=93, color2=27, itemType="WristItem"), # Maple Brown Ski Poles
                    ShopItem(itemId=1254, price=25, goldPrice=5, color1=75, color2=27, itemType="Skirt"), # Umber Brown Warm Ski Pants
                    ShopItem(itemId=3677, price=15, goldPrice=3, color1=93, color2=27, itemType="Shoes"), # Maple Brown Swift Skis

                    ShopItem(itemId=222, price=25, goldPrice=5, color1=224, color2=3, itemType="Shirt"), # Ivory White Scholarly Vest
                    ShopItem(itemId=1172, price=25, goldPrice=5, color1=91, color2=91, itemType="Skirt"), # Coconut Brown Dry Leaf Trousers
                    ShopItem(itemId=3588, price=15, goldPrice=3, color1=74, color2=236, itemType="Shoes"), # Soil Brown Bark Layer Shoes

                    ShopItem(itemId=220, price=25, goldPrice=5, color1=60, color2=129, itemType="Shirt"), # Tyrian Purple Simple Cardie with Purple Trim
                    ShopItem(itemId=1145, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Denim Flyers
                    ShopItem(itemId=3587, price=15, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Bark Sole Dress Shoes

                    ShopItem(itemId=268, price=25, goldPrice=5, color1=113, color2=161, itemType="Shirt"), # Pale Rose Red Easy Style Henley with Buried Treasure Brown Trim
                    ShopItem(itemId=1217, price=25, goldPrice=5, color1=161, color2=161, itemType="Skirt"), # Buried Treasure Brown Easy Style Jeans
                    ShopItem(itemId=3654, price=15, goldPrice=3, color1=78, color2=161, itemType="Shoes"), # Fawn Brown Easy Style Sneaks

                    ShopItem(itemId=2330, price=15, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Keen Comb
                    ShopItem(itemId=407, price=25, goldPrice=5, color1=206, color2=166, itemType="Shirt"), # Raven Black Sock Hop Jacket
                    ShopItem(itemId=1330, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Sock Hop Pants
                    ShopItem(itemId=3749, price=15, goldPrice=3, color1=206, color2=166, itemType="Shoes"), # Raven Black Cool Moto Boots

                    ShopItem(itemId=277, price=25, goldPrice=5, color1=172, color2=122, itemType="Shirt"), # Forest Green Cool Breeze Roll-Up Top
                    ShopItem(itemId=1227, price=25, goldPrice=5, color1=118, color2=206, itemType="Skirt"), # Sapphire Blue Breezy Casual Shorts
                    ShopItem(itemId=3625, price=15, goldPrice=3, color1=78, color2=236, itemType="Shoes"), # Fawn Brown Woodchucks with Tan Trim

                    ShopItem(itemId=2326, price=15, goldPrice=3, color1=224, color2=141, itemType="HeadItem"), # Ivory White Too Cool Hat
                    ShopItem(itemId=406, price=25, goldPrice=5, color1=224, color2=141, itemType="Shirt"), # Ivory White Hip Zip Sweater
                    ShopItem(itemId=1311, price=25, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Neat and Trim Trousers
                    ShopItem(itemId=3714, price=15, goldPrice=3, color1=141, color2=224, itemType="Shoes"), # Thundercloud Gray Fast-Flying Sneakers

                    ShopItem(itemId=287, price=25, goldPrice=5, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Beach Breezy Top
                    ShopItem(itemId=1239, price=25, goldPrice=5, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Beach Breezy Shorts
                    ShopItem(itemId=3672, price=15, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Easy Walker

                    ShopItem(itemId=285, price=25, goldPrice=5, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Casual Flyer Coat
                    ShopItem(itemId=1238, price=25, goldPrice=5, color1=63, color2=63, itemType="Skirt"), # Butterfly Blue Casual Flyer Pants
                    ShopItem(itemId=3670, price=15, goldPrice=3, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Casual Flyer Shoes

                    ShopItem(itemId=299, price=25, goldPrice=5, color1=166, color2=169, itemType="Shirt"), # Snow White Polished Pinstripe Vest with Squirrel Gray Trim
                    ShopItem(itemId=1249, price=25, goldPrice=5, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Polished Pinstripe Pants
                    ShopItem(itemId=3679, price=15, goldPrice=3, color1=141, color2=169, itemType="Shoes"), # Thundercloud Gray Luxurious Lace-Ups

                    ShopItem(itemId=218, price=25, goldPrice=5, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Rain Hoodie
                    ShopItem(itemId=1131, price=25, goldPrice=5, color1=78, color2=78, itemType="Skirt"), # Fawn Brown Tailored Leaf Jeans
                    ShopItem(itemId=3627, price=15, goldPrice=3, color1=78, color2=78, itemType="Shoes"), #  Fawn Brown Sturdy Galoshes

                    ShopItem(itemId=147, price=25, goldPrice=5, color1=127, color2=17, itemType="Shirt"), # Grasshopper Green Sporty Top
                    ShopItem(itemId=1193, price=25, goldPrice=5, color1=127, color2=127, itemType="Skirt"), # Grasshopper Green Sporty Shorts
                    ShopItem(itemId=3633, price=15, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Sporty Shoes
                
                ],
            ),
            ShopCollection(
                collectionId=56, # Themed Fashions
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2294, price=15, goldPrice=3, color1=154, color2=45, itemType="HeadItem"), # Beetle Brown Gardening Hat
                    ShopItem(itemId=380, price=25, goldPrice=5, color1=118, color2=45, itemType="Shirt"), # Sapphire Blue Gardening Overall Top
                    ShopItem(itemId=1298, price=25, goldPrice=5, color1=209, color2=141, itemType="Skirt"), # Deep Sea Blue Gardening Jeans
                    ShopItem(itemId=3627, price=15, goldPrice=3, color1=141, color2=214, itemType="Shoes"), # Thundercloud Gray Sturdy Galoshes with Gray Trim

                    ShopItem(itemId=2275, price=15, goldPrice=3, color1=239, color2=216, itemType="HeadItem"), # Coffee Black Ninja Hood
                    ShopItem(itemId=336, price=25, goldPrice=5, color1=239, color2=216, itemType="Shirt"), # Coffee Black Ninja Shinobi Top
                    ShopItem(itemId=1272, price=25, goldPrice=5, color1=239, color2=216, itemType="Skirt"), # Coffee Black Ninja Shinobi Pants
                    ShopItem(itemId=3697, price=15, goldPrice=3, color1=239, color2=141, itemType="Shoes"), #  Coffee Black Ninja Tabi Shoes

                    ShopItem(itemId=2297, price=15, goldPrice=3, color1=239, color2=168, itemType="HeadItem"), # Coffee Black Folklorico Hat
                    ShopItem(itemId=381, price=25, goldPrice=5, color1=239, color2=168, itemType="Shirt"), # Coffee Black Folklorico Jacket
                    ShopItem(itemId=1301, price=25, goldPrice=5, color1=239, color2=168, itemType="Skirt"), # Coffee Black Folklorico Trousers
                    ShopItem(itemId=3719, price=15, goldPrice=3, color1=239, color2=168, itemType="Shoes"), # Coffee Black Folklorico Shoes

                    ShopItem(itemId=352, price=25, goldPrice=5, color1=206, color2=236, itemType="Shirt"), #  Raven Black Woodsman Top
                    ShopItem(itemId=633, price=5, goldPrice=1, color1=206, color2=245, itemType="Belt"), # Raven Black Woodsman's Belt
                    ShopItem(itemId=1287, price=25, goldPrice=5, color1=239, color2=239, itemType="Skirt"), # Coffee Black Woodsman Trousers
                    ShopItem(itemId=3712, price=15, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Woodsman Boots

                    ShopItem(itemId=2157, price=15, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Baking Hat
                    ShopItem(itemId=189, price=25, goldPrice=5, color1=171, color2=224, itemType="Shirt"), # Sunrise Yellow Chef's Jacket
                    ShopItem(itemId=1171, price=25, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Chef's Apron Pants
                    ShopItem(itemId=3592, price=15, goldPrice=3, color1=75, color2=75, itemType="Shoes"), # Umber Brown Round Toe Shoes

                    ShopItem(itemId=2184, price=15, goldPrice=3, color1=224, color2=105, itemType="HeadItem"), # Ivory White Serving-Talent Hat
                    ShopItem(itemId=237, price=25, goldPrice=5, color1=224, color2=105, itemType="Shirt"), # Ivory White Serving-Talent Vest
                    ShopItem(itemId=1172, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Dry Leaf Trousers
                    ShopItem(itemId=3623, price=15, goldPrice=3, color1=141, color2=206, itemType="Shoes"), # Thundercloud Gray Later Skaters with Black Trim

                    ShopItem(itemId=2179, price=15, goldPrice=3, color1=209, color2=180, itemType="HeadItem"), # Deep Sea Blue Teatime Top Hat
                    ShopItem(itemId=2569, price=2, goldPrice=1, color1=209, color2=209, itemType="Necklace"), # Deep Sea Blue Mad Tea Party Scarf
                    ShopItem(itemId=247, price=25, goldPrice=5, color1=209, color2=180, itemType="Shirt"), # Deep Sea Blue Mad Tea Party Attire
                    ShopItem(itemId=1204, price=25, goldPrice=5, color1=185, color2=180, itemType="Skirt"), # Midnight Blue Best Dressed Slacks
                    ShopItem(itemId=3641, price=15, goldPrice=3, color1=209, color2=180, itemType="Shoes"), # Deep Sea Blue Best Dressed Loafers

                    ShopItem(itemId=2588, price=2, goldPrice=1, color1=227, color2=227, itemType="Necklace"), # Moonlight Gray Top 40 Necklace
                    ShopItem(itemId=335, price=25, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Top 40 Vest
                    ShopItem(itemId=1608, price=2, goldPrice=1, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Top 40 Wrist Cuff
                    ShopItem(itemId=1132, price=25, goldPrice=5, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Tailored Spider Silk Jeans
                    ShopItem(itemId=3633, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Sporty Shoes

                    ShopItem(itemId=2287, price=15, goldPrice=3, color1=92, color2=92, itemType="HeadItem"), # Hawk Brown Rockin' Hair
                    ShopItem(itemId=2592, price=5, goldPrice=1, color1=169, color2=169, itemType="Necklace"), # Squirrel Gray Rockin' Necklace
                    ShopItem(itemId=349, price=25, goldPrice=5, color1=55, color2=55, itemType="Shirt"), # Pepper Black Rockin' Jacket
                    ShopItem(itemId=632, price=5, goldPrice=1, color1=45, color2=45, itemType="Belt"), # Strawberry Red Rockin' Belt
                    ShopItem(itemId=1285, price=25, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Rockin' Pants
                    ShopItem(itemId=3709, price=15, goldPrice=3, color1=55, color2=55, itemType="Shoes"), # Pepper Black Rockin' Boots

                    ShopItem(itemId=351, price=25, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Glitz and Glam Top
                    ShopItem(itemId=1297, price=25, goldPrice=5, color1=226, color2=226, itemType="Skirt"), # Goldenrod Yellow Glitz and Glam Pants
                    ShopItem(itemId=3711, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Glitz and Glam Boots

                    ShopItem(itemId=324, price=25, goldPrice=5, color1=116, color2=116, itemType="Shirt"), # Mushroom White Royal Jacket
                    ShopItem(itemId=1262, price=25, goldPrice=5, color1=26, color2=26, itemType="Skirt"), # Raspberry Red Princely Trousers
                    ShopItem(itemId=3683, price=15, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Princely Boots

                    ShopItem(itemId=337, price=25, goldPrice=5, color1=170, color2=170, itemType="Shirt"), # Olive Green Agave Top
                    ShopItem(itemId=1610, price=10, goldPrice=2, color1=170, color2=170, itemType="WristItem"), # Olive Green Agave Cuff
                    ShopItem(itemId=1273, price=25, goldPrice=5, color1=170, color2=170, itemType="Skirt"), # Olive Green Agave Shorts
                    ShopItem(itemId=3698, price=15, goldPrice=3, color1=170, color2=170, itemType="Shoes"), # Olive Green Agave Shoes

                    ShopItem(itemId=2131, price=15, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Camp Referee Visor
                    ShopItem(itemId=146, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Camp Referee Top
                    ShopItem(itemId=1137, price=25, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Camp Referee Shorts
                    ShopItem(itemId=3597, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Camp Referee Shoes

                    ShopItem(itemId=361, price=25, goldPrice=5, color1=183, color2=183, itemType="Shirt"), # Vidia Purple Fast-Flying Tee
                    ShopItem(itemId=1291, price=25, goldPrice=5, color1=183, color2=183, itemType="Skirt"), # Vidia Purple Fast-Flying Pants
                    ShopItem(itemId=3714, price=15, goldPrice=3, color1=60, color2=60, itemType="Shoes"), # Tyrian Purple Fast-Flying Sneakers

                    ShopItem(itemId=2290, price=15, goldPrice=3, color1=60, color2=60, itemType="HeadItem"), # Tyrian Purple Fast-Flying Headband
                    ShopItem(itemId=362, price=25, goldPrice=5, color1=183, color2=183, itemType="Shirt"), # Vidia Purple Fast-Flying Tunic
                    ShopItem(itemId=634, price=5, goldPrice=1, color1=183, color2=183, itemType="Belt"), # Vidia Purple Fast-Flying Belt
                    ShopItem(itemId=1292, price=25, goldPrice=5, color1=183, color2=183, itemType="Skirt"), # Vidia Purple Fast-Flying Pants
                    ShopItem(itemId=3715, price=15, goldPrice=3, color1=183, color2=183, itemType="Shoes"), # Vidia Purple Fast-Flying Laceups

                    ShopItem(itemId=2276, price=15, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Wacky Rainbow Wig
                    ShopItem(itemId=131, price=25, goldPrice=5, color1=226, color2=226, itemType="Shirt"), # Goldenrod Yellow Cap Sleeve Meadow Tee
                    ShopItem(itemId=1288, price=25, goldPrice=5, color1=228, color2=228, itemType="Skirt"), # Duckbill Orange Silly Parachute Pants
                    ShopItem(itemId=3713, price=15, goldPrice=3, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks

                ]
            ),
             ShopCollection(
                 collectionId=58, # Animal Friend Costumes
                 currencyId=FairiesConstants.MAPLE_LEAVES,
                 items=[
                    ShopItem(itemId=2073, price=15, goldPrice=3, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
                    ShopItem(itemId=230, price=25, goldPrice=5, color1=142, color2=206, itemType="Shirt"), # Bumble Bee Yellow Buzzy Bee Top
                    ShopItem(itemId=1170, price=25, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Pocket Pants
                    ShopItem(itemId=3577, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots

                    ShopItem(itemId=2071, price=15, goldPrice=3, color1=44, color2=190, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
                    ShopItem(itemId=175, price=25, goldPrice=5, color1=44, color2=190, itemType="Shirt"), # Plumblossom Pink Firefly Wrap
                    ShopItem(itemId=1195, price=25, goldPrice=5, color1=190, color2=190, itemType="Skirt"), # Firefly Green Dry Leaf Shorts
                    ShopItem(itemId=3577, price=15, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Ivy Lace Work Boots

                    ShopItem(itemId=2071, price=15, goldPrice=3, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
                    ShopItem(itemId=177, price=25, goldPrice=5, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tee
                    ShopItem(itemId=1175, price=25, goldPrice=5, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Shorts
                    ShopItem(itemId=3577, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots

                    ShopItem(itemId=2149, price=15, goldPrice=3, color1=193, color2=175, itemType="HeadItem"), # Electric Green Dragonfly Mask
                    ShopItem(itemId=178, price=25, goldPrice=5, color1=175, color2=175, itemType="Shirt"), # Creek Green Dragonfly Top 
                    ShopItem(itemId=1173, price=25, goldPrice=5, color1=175, color2=193, itemType="Skirt"), # Creek Green Dragonfly Trousers
                    ShopItem(itemId=3577, price=15, goldPrice=3, color1=175, color2=175, itemType="Shoes"), # Creek Green Ivy Lace Work Boots

                    ShopItem(itemId=2153, price=15, goldPrice=3, color1=267, color2=27, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                    ShopItem(itemId=190, price=25, goldPrice=5, color1=267, color2=27, itemType="Shirt"), # Celestial Blue Hummingbird Top 
                    ShopItem(itemId=1174, price=25, goldPrice=5, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Hummingbird Trousers
                    ShopItem(itemId=3577, price=15, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Ivy Lace Work Boots
                 ]
             ),
             ShopCollection(
                 collectionId=62, # Sparrow Shirts and Jackets
                 currencyId=FairiesConstants.MAPLE_LEAVES,
                 items=[
                    ShopItem(itemId=1000033, price=25, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Sunburst Tie-Dye Tee
                    ShopItem(itemId=1000034, price=25, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Striped Tie-Dye Tee
                    ShopItem(itemId=1000035, price=25, goldPrice=5, color1=129, color2=129, itemType="Shirt"), # Fig Purple Speckled Tie-Dye Tee
                    ShopItem(itemId=354, price=25, goldPrice=5, color1=90, color2=90, itemType="Shirt"), # Custard Yellow Horizontal Leaf Hoodie with Tan Trim
                    ShopItem(itemId=355, price=25, goldPrice=5, color1=221, color2=221, itemType="Shirt"), # Jade Green Colorblock Stripe Hoodie

                    ShopItem(itemId=353, price=25, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Vertical Leaf Hoodie
                    ShopItem(itemId=356, price=25, goldPrice=5, color1=216, color2=216, itemType="Shirt"), # Slate Gray Layered Blazer
                    ShopItem(itemId=357, price=25, goldPrice=5, color1=161, color2=161, itemType="Shirt"), # Buried Treasure Brown Casual Plaid Shirt
                    ShopItem(itemId=358, price=25, goldPrice=5, color1=209, color2=209, itemType="Shirt"), # Deep Sea Blue Denim Jacket
                    ShopItem(itemId=359, price=25, goldPrice=5, color1=78, color2=78, itemType="Shirt"), # Fawn Brown Casual Denim Shirt

                    ShopItem(itemId=150, price=25, goldPrice=5, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Birdy Button Down
                    ShopItem(itemId=151, price=25, goldPrice=5, color1=265, color2=265, itemType="Shirt"), # Bright Sky Blue Palm Tree Button Down
                    ShopItem(itemId=152, price=25, goldPrice=5, color1=81, color2=81, itemType="Shirt"), # Crimson Red Wave Button Down
                    ShopItem(itemId=402, price=25, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Triple Stripes Polo

                    ShopItem(itemId=403, price=25, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Neat Stripes Polo
                    ShopItem(itemId=404, price=25, goldPrice=5, color1=148, color2=148, itemType="Shirt"), # Pots'n'Pans Purple Super Stripes Polo
                    ShopItem(itemId=224, price=25, goldPrice=5, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Zip Up Hoodie
                    ShopItem(itemId=128, price=25, goldPrice=5, color1=172, color2=172, itemType="Shirt"), # Forest Green Cottonpuff Pullover
                    ShopItem(itemId=366, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Vine Tee
                    
                    ShopItem(itemId=367, price=25, goldPrice=5, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Twisty Print Tee
                    ShopItem(itemId=364, price=25, goldPrice=5, color1=221, color2=221, itemType="Shirt"), # Jade Green Sideswept Swirl Tee
                    ShopItem(itemId=368, price=25, goldPrice=5, color1=180, color2=180, itemType="Shirt"), # Seashell Blue Star Print Tee
                    ShopItem(itemId=371, price=25, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Nifty Print Tee
                    ShopItem(itemId=370, price=25, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Twisty Tree Tee
                 ]
             ),
             ShopCollection(
                 collectionId=63, # Sparrow Man Accessories
                 currencyId=FairiesConstants.MAPLE_LEAVES,
                 items=[
                    ShopItem(itemId=2125, price=15, goldPrice=3, color1=214, color2=214, itemType="HeadItem"), # Smokey Gray Mainland Fedora
                    ShopItem(itemId=2182, price=15, goldPrice=3, color1=46, color2=46, itemType="HeadItem"), # Bark Brown Round Up Hat
                    ShopItem(itemId=2132, price=15, goldPrice=3, color1=109, color2=109, itemType="HeadItem"), # Soft Orange Summer Wave Hat
                    ShopItem(itemId=2205, price=15, goldPrice=3, color1=91, color2=91, itemType="HeadItem"), # Coconut Brown Straw Brim Hat
                    ShopItem(itemId=2206, price=15, goldPrice=3, color1=172, color2=141, itemType="HeadItem"), # Forest Green Linen Sun Hat with Gray Trim
                    ShopItem(itemId=2154, price=15, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Lined Winter Hat
                    ShopItem(itemId=2178, price=15, goldPrice=3, color1=73, color2=73, itemType="HeadItem"), # Grape Purple Tea-brewer Cap
                    ShopItem(itemId=2165, price=15, goldPrice=3, color1=180, color2=180, itemType="HeadItem"), # Seashell Blue Seashell Cap
                    ShopItem(itemId=2174, price=15, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Leaf Embroidered Cap
                    ShopItem(itemId=2190, price=15, goldPrice=3, color1=141, color2=136, itemType="HeadItem"), # Thundercloud Gray Conductor Cap with Blue Trim
                    ShopItem(itemId=2175, price=15, goldPrice=3, color1=169, color2=169, itemType="HeadItem"), # Squirrel Gray Easy Style Cap
                    ShopItem(itemId=2130, price=15, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Sporty Sparrow Band
                    ShopItem(itemId=2135, price=15, goldPrice=3, color1=207, color2=207, itemType="HeadItem"), # Diamond Blue Sparrow Sun-Shades
                    ShopItem(itemId=2279, price=15, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Peppermint Swirl Glasses
                    ShopItem(itemId=2230, price=15, goldPrice=3, color1=168, color2=168, itemType="HeadItem"), # Never Gold Merry Monocle

                    ShopItem(itemId=2552, price=5, goldPrice=1, color1=175, color2=175, itemType="Necklace"), # Creek Green Striped Scarf
                    ShopItem(itemId=2558, price=5, goldPrice=1, color1=230, color2=230, itemType="Necklace"), # Scarlet Red Fringed Scarf
                    ShopItem(itemId=2542, price=5, goldPrice=1, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Meadowland Neck Band
                    ShopItem(itemId=2596, price=5, goldPrice=1, color1=206, color2=111, itemType="Necklace"), # Raven Black Sunburst Necklace with Yellow Trim
                    ShopItem(itemId=2583, price=5, goldPrice=1, color1=221, color2=221, itemType="Necklace"), # Jade Green Ivy Necklace
                    ShopItem(itemId=2582, price=5, goldPrice=1, color1=109, color2=230, itemType="Necklace"), # Soft Orange Bamboo Necklace with Scarlet Red Trim
                    ShopItem(itemId=2541, price=5, goldPrice=1, color1=30, color2=30, itemType="Necklace"), # Pumpkin Orange Triple Gem Neck Ring
                    ShopItem(itemId=2540, price=5, goldPrice=1, color1=60, color2=60, itemType="Necklace"), # Tyrian Purple Neverberry Neck Band
                    ShopItem(itemId=2544, price=5, goldPrice=1, color1=266, color2=266, itemType="Necklace"), # Ocean Blue Gavin's 3-2 Neck Band
                    ShopItem(itemId=2577, price=5, goldPrice=1, color1=221, color2=221, itemType="Necklace"), # Jade Green Trinity Leaf Torc

                    ShopItem(itemId=585, price=5, goldPrice=1, color1=78, color2=78, itemType="Belt"), # Fawn Brown Studded Belt
                    ShopItem(itemId=584, price=5, goldPrice=1, color1=170, color2=170, itemType="Belt"), # Olive Green Clover Belt
                    ShopItem(itemId=583, price=5, goldPrice=1, color1=154, color2=154, itemType="Belt"), # Beetle Brown Basic Belt
                    ShopItem(itemId=598, price=5, goldPrice=1, color1=227, color2=227, itemType="Belt"), # Moonlight Gray Triple Gear Belt
                    ShopItem(itemId=597, price=5, goldPrice=1, color1=75, color2=75, itemType="Belt"), # Umber Brown Gear Buckle Belt
                    ShopItem(itemId=578, price=5, goldPrice=1, color1=28, color2=28, itemType="Belt"), # Cinnamon Brown Acorn Buckle Belt
                    ShopItem(itemId=562, price=5, goldPrice=1, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Sash Belt
                    ShopItem(itemId=563, price=5, goldPrice=1, color1=148, color2=148, itemType="Belt"), # Pots'n'Pans Purple Cross-Stitch Belt
                    ShopItem(itemId=564, price=5, goldPrice=1, color1=83, color2=83, itemType="Belt"), # Cherry Brown Bark Braid Belt
                    ShopItem(itemId=561, price=5, goldPrice=1, color1=75, color2=75, itemType="Belt"), # Umber Brown Seed Band Belt
                    ShopItem(itemId=627, price=5, goldPrice=1, color1=166, color2=166, itemType="Belt"), # Snow White Peppermint Swirl Belt
                    ShopItem(itemId=637, price=5, goldPrice=1, color1=206, color2=111, itemType="Belt"), # Raven Black Sunburst Belt with Yellow Trim
                    ShopItem(itemId=582, price=5, goldPrice=1, color1=180, color2=180, itemType="Belt"), # Seashell Blue Scallop Shell Belt
                    ShopItem(itemId=581, price=5, goldPrice=1, color1=209, color2=209, itemType="Belt"), # Deep Sea Blue Seashell Belt
                    ShopItem(itemId=592, price=5, goldPrice=1, color1=191, color2=191, itemType="Belt"), # Vidia Black Feather Friendship Belt

                    ShopItem(itemId=1540, price=10, goldPrice=2, color1=185, color2=185, itemType="WristItem"), # Midnight Blue Ever Never-Friend Bracelet
                    ShopItem(itemId=1559, price=10, goldPrice=2, color1=45, color2=185, itemType="WristItem"), # Strawberry Red Friendship Cuff with Midnight Blue Trim
                    ShopItem(itemId=1595, price=10, goldPrice=2, color1=221, color2=221, itemType="WristItem"), # Jade Green Ivy Bracelet
                    ShopItem(itemId=1630, price=10, goldPrice=2, color1=206, color2=111, itemType="WristItem"), # Raven Black Sunburst Cuff with Yellow Trim
                    ShopItem(itemId=1536, price=10, goldPrice=2, color1=138, color2=138, itemType="WristItem"), # Persimmon Orange Meadow Grass Wrist Wrap
                    ShopItem(itemId=1531, price=10, goldPrice=2, color1=126, color2=126, itemType="WristItem"), # Raindrop Blue Shield Brace
                    ShopItem(itemId=1530, price=10, goldPrice=2, color1=148, color2=148, itemType="WristItem"), # Pots'n'Pans Purple Winding Wrist Wrap
                    ShopItem(itemId=1529, price=10, goldPrice=2, color1=168, color2=168, itemType="WristItem"), # Never Gold Quick Brace
                    ShopItem(itemId=1596, price=10, goldPrice=2, color1=109, color2=98, itemType="WristItem"), # Soft Orange Bamboo Bracelet with Tan Trim
                    ShopItem(itemId=1535, price=10, goldPrice=2, color1=215, color2=215, itemType="WristItem"), # Pewter Gray X-Band Wrist Wrap
                    ShopItem(itemId=1537, price=10, goldPrice=2, color1=208, color2=208, itemType="WristItem"), # Cerulean Blue Grassblade Wrist Wrap
                    ShopItem(itemId=1538, price=10, goldPrice=2, color1=175, color2=175, itemType="WristItem"), # Creek Green Triple Tie Wrist Wrap
                    ShopItem(itemId=1534, price=10, goldPrice=2, color1=220, color2=220, itemType="WristItem"), # Dusty Pink Triple Cuff
                    ShopItem(itemId=1532, price=10, goldPrice=2, color1=183, color2=183, itemType="WristItem"), # Vidia Purple Pinfeather Brace
                    ShopItem(itemId=1584, price=10, goldPrice=2, color1=221, color2=221, itemType="WristItem"), # Jade Green Trinity Leaf Bracelet

                    ShopItem(itemId=3044, price=5, goldPrice=1, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Trinity Leaf Anklet
                    ShopItem(itemId=3029, price=5, goldPrice=1, color1=208, color2=208, itemType="AnkleItem"), # Cerulean Blue Vine Duo Anklet
                    ShopItem(itemId=3047, price=5, goldPrice=1, color1=230, color2=230, itemType="AnkleItem"), # Scarlet Red Bamboo Anklet
                    ShopItem(itemId=3046, price=5, goldPrice=1, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Ivy Anklet

                    ShopItem(itemId=3663, price=15, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Socks'n'Sandal Combo
                    ShopItem(itemId=3665, price=15, goldPrice=3, color1=113, color2=113, itemType="Shoes"), # Pale Rose Red Super Sports Foot Gear
                    ShopItem(itemId=3664, price=15, goldPrice=3, color1=175, color2=175, itemType="Shoes"), # Creek Green Fun Run Foot Gear
                    ShopItem(itemId=3572, price=15, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Tall Tied Boots
                    ShopItem(itemId=3616, price=15, goldPrice=3, color1=118, color2=118, itemType="Shoes"), # Sapphire Blue Short Sturdy Boots
                    ShopItem(itemId=3615, price=15, goldPrice=3, color1=10, color2=10, itemType="Shoes"), # Cantaloupe Orange Tall Sturdy Boots
                    ShopItem(itemId=3692, price=15, goldPrice=3, color1=105, color2=105, itemType="Shoes"), # Siltstone Tan Bamboo Sandals
                    ShopItem(itemId=3575, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Cross-Stitch Work Boots  
                 ],
             ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.ZEPHYRS_ZOOM_ROOM,
        shopId=7,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.ZEPHYR,
            position=(408, 452),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_ZEPHYR
        ),
        collections=[
            ShopCollection(
                collectionId=1, # Rapid Racer - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2219, price=10, goldPrice=4, color1=191, color2=72, itemType="HeadItem"), # Vidia Black Racing Goggles
                    ShopItem(itemId=302, price=18, goldPrice=7, color1=129, color2=72, itemType="Shirt"), # Fig Purple Rapid Racer Top
                    ShopItem(itemId=1264, price=18, goldPrice=7, color1=129, color2=72, itemType="Skirt"), # Fig Purple Rapid Racer Knickers
                    ShopItem(itemId=3678, price=13, goldPrice=5, color1=72, color2=191, itemType="Shoes"), # Mauve Purple Riding Boots

                    ShopItem(itemId=2219, price=10, goldPrice=4, color1=55, color2=48, itemType="HeadItem"), # Pepper Black Racing Goggles
                    ShopItem(itemId=302, price=18, goldPrice=7, color1=48, color2=41, itemType="Shirt"), # Sea Green Rapid Racer Top
                    ShopItem(itemId=1264, price=18, goldPrice=7, color1=41, color2=48, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                    ShopItem(itemId=3678, price=13, goldPrice=5, color1=55, color2=48, itemType="Shoes"), # Sea Green Riding Boots
                ],
            ),
            ShopCollection(
                collectionId=42, # Rapid Racer - Sparrows
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2225, price=10, goldPrice=4, color1=55, color2=48, itemType="HeadItem"), # Pepper Black Racing Goggles
                    ShopItem(itemId=306, price=18, goldPrice=7, color1=48, color2=41, itemType="Shirt"), # Sea Green Rapid Racer Top
                    ShopItem(itemId=1255, price=18, goldPrice=7, color1=41, color2=48, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                    ShopItem(itemId=3681, price=13, goldPrice=5, color1=55, color2=48, itemType="Shoes"), # Pepper Black Riding Boots with Sea Green Trim

                    ShopItem(itemId=2225, price=10, goldPrice=4, color1=191, color2=189, itemType="HeadItem"), # Vidia Black Racing Goggles
                    ShopItem(itemId=306, price=18, goldPrice=7, color1=189, color2=113, itemType="Shirt"), # Ladybug Red Rapid Racer Top
                    ShopItem(itemId=1255, price=18, goldPrice=7, color1=191, color2=189, itemType="Skirt"), # Vidia Black Rapid Racer Knickers
                    ShopItem(itemId=3681, price=13, goldPrice=5, color1=75, color2=189, itemType="Shoes"), # Umber Brown Riding Boots
                ],
            ),
            ShopCollection(
                collectionId=69, # Super Speedster - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=323, price=18, goldPrice=5, color1=8, color2=81, itemType="Shirt"), # Watermelon Pink Super Speedster Jacket
                    ShopItem(itemId=1263, price=18, goldPrice=7, color1=8, color2=81, itemType="Skirt"), # Watermelon Pink Super Speedster Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=81, color2=8, itemType="Shoes"), # Crimson Red Finish Line Shoes

                    ShopItem(itemId=323, price=18, goldPrice=7, color1=151, color2=111, itemType="Shirt"), # Peanut Yellow Super Speedster Jacket
                    ShopItem(itemId=1263, price=18, goldPrice=7, color1=151, color2=111, itemType="Skirt"), # Peanut Yellow Super Speedster Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=151, color2=111, itemType="Shoes"), # Peanut Yellow Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=70, # Super Speedster - Sparrow
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=318, price=18, goldPrice=7, color1=74, color2=92, itemType="Shirt"), # Soil Brown Super Speedster Jacket
                    ShopItem(itemId=1257, price=18, goldPrice=7, color1=74, color2=92, itemType="Skirt"), # Soil Brown Super Speedster Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=74, color2=92, itemType="Shoes"), # Soil Brown Finish Line Shoes

                    ShopItem(itemId=318, price=18, goldPrice=7, color1=172, color2=125, itemType="Shirt"), # Forest Green Super Speedster Jacket
                    ShopItem(itemId=1257, price=18, goldPrice=7, color1=125, color2=172, itemType="Skirt"), # Pine Green Super Speedster Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=125, color2=172, itemType="Shoes"), # Pine Green Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=71, # Fast Flash Racer - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=322, price=18, goldPrice=7, color1=130, color2=181, itemType="Shirt"), # Orchid Pink Fast Flash Racing Top
                    ShopItem(itemId=1260, price=18, goldPrice=7, color1=130, color2=181, itemType="Skirt"), # Orchid Pink Fast Flash Racing Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=181, color2=130, itemType="Shoes"), # Cupcake Pink Finish Line Shoes

                    ShopItem(itemId=322, price=18, goldPrice=7, color1=24, color2=185, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                    ShopItem(itemId=1260, price=18, goldPrice=7, color1=24, color2=185, itemType="Skirt"), # Sky Blue Fast Flash Racing Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=185, color2=24, itemType="Shoes"), # Midnight Blue Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=72, # Fast Flash Racer - Sparrow
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=319, price=18, goldPrice=7, color1=24, color2=185, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                    ShopItem(itemId=1258, price=18, goldPrice=7, color1=185, color2=24, itemType="Skirt"), # Midnight Blue Fast Flash Racing Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=185, color2=24, itemType="Shoes"), # Midnight Blue Finish Line Shoes

                    ShopItem(itemId=319, price=18, goldPrice=7, color1=12, color2=138, itemType="Shirt"), # Tangerine Orange Fast Flash Racing Top
                    ShopItem(itemId=1258, price=18, goldPrice=7, color1=138, color2=12, itemType="Skirt"), # Persimmon Orange Fast Flash Racing Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=138, color2=12, itemType="Shoes"), # Persimmon Orange Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=18, # Riding Helmets
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2223, price=8, goldPrice=3, color1=105, color2=92, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                    ShopItem(itemId=2223, price=8, goldPrice=3, color1=61, color2=55, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                    ShopItem(itemId=2220, price=13, goldPrice=5, color1=52, color2=129, itemType="HeadItem"), # Lavender Purple Rapid Racer Helmet
                    ShopItem(itemId=2220, price=13, goldPrice=5, color1=48, color2=41, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                    ShopItem(itemId=2242, price=13, goldPrice=5, color1=130, color2=181, itemType="HeadItem"), # Orchid Pink Vintage Racer Helmet
                    ShopItem(itemId=2242, price=13, goldPrice=5, color1=24, color2=185, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet

                    # Sparrows \/
                    ShopItem(itemId=2229, price=8, goldPrice=3, color1=105, color2=92, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                    ShopItem(itemId=2229, price=8, goldPrice=3, color1=61, color2=55, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                    ShopItem(itemId=2226, price=13, goldPrice=5, color1=48, color2=41, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                    ShopItem(itemId=2226, price=13, goldPrice=5, color1=113, color2=189, itemType="HeadItem"), # Pale Rose Red Rapid Racer Helmet
                    ShopItem(itemId=2244, price=13, goldPrice=5, color1=24, color2=185, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet
                    ShopItem(itemId=2244, price=13, goldPrice=5, color1=12, color2=138, itemType="HeadItem"), # Tangerine Orange Vintage Racer Helmet

                    # Both \/
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=81, color2=8, itemType="HeadItem"), # Crimson Red Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=151, color2=111, itemType="HeadItem"), # Peanut Yellow Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=172, color2=172, itemType="HeadItem"), # Forest Green Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=74, color2=74, itemType="HeadItem"), # Soil Brown Dustkicker Helmet
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.PIXIE_POST_OFFICE,
        shopId=8,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SPRING,
            position=(500, 350),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_SPRING
        ),
        collections=[
            ShopCollection(
                collectionId=5, # Floral Giftsets
                items=[
                    ShopItem(itemId=2262, price=5, goldPrice=3, color1=210, color2=210, itemType="HeadItem"), # Lotus Purple Tillandsia Headband
                    ShopItem(itemId=329, price=9, goldPrice=5, color1=210, color2=210, itemType="Shirt"), # Lotus Purple Tillandsia Top
                    ShopItem(itemId=625, price=2, goldPrice=1, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Tillandsia Sash
                    ShopItem(itemId=1266, price=9, goldPrice=5, color1=210, color2=210, itemType="Skirt"), # Lotus Purple Tillandsia Skirt
                    ShopItem(itemId=3689, price=5, goldPrice=3, color1=210, color2=210, itemType="Shoes"), # Lotus Purple Tillandsia Flats
                    ShopItem(itemId=2263, price=5, goldPrice=3, color1=30, color2=30, itemType="HeadItem"), # Pumpkin Orange Pumpkin Headband
                    ShopItem(itemId=330, price=9, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Pumpkin Bodice
                    ShopItem(itemId=1267, price=9, goldPrice=5, color1=30, color2=30, itemType="Skirt"), # Pumpkin Orange Pumpkin Skirt
                    ShopItem(itemId=3690, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Pumpkin Boots
                    ShopItem(itemId=2062, price=5, goldPrice=3, color1=140, color2=140, itemType="HeadItem"), # Bunnynose Pink Curcuma Headband
                    ShopItem(itemId=332, price=9, goldPrice=5, color1=162, color2=140, itemType="Shirt"), # Sunglow Yellow Curcuma Top
                    ShopItem(itemId=1269, price=9, goldPrice=5, color1=162, color2=140, itemType="Skirt"), # Sunglow Yellow Curcuma Skirt
                    ShopItem(itemId=3694, price=5, goldPrice=3, color1=162, color2=140, itemType="Shoes"), # Sunglow Yellow Curcuma Shoes
                    ShopItem(itemId=2148, price=5, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Fresh Petal Barrette
                    ShopItem(itemId=173, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Fresh Petal Bodice
                    ShopItem(itemId=1157, price=9, goldPrice=5, color1=27, color2=27, itemType="Skirt"), # Corn Cob Yellow Fresh Petal Skirt
                    ShopItem(itemId=3610, price=5, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Fresh Petal Pumps
                    ShopItem(itemId=2063, price=5, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Pansy Headband
                    ShopItem(itemId=64, price=9, goldPrice=5, color1=247, color2=247, itemType="Shirt"), # Jasmine Yellow Pansy Top
                    ShopItem(itemId=1069, price=9, goldPrice=5, color1=247, color2=247, itemType="Skirt"), # Jasmine Yellow Pansy Skirt
                    ShopItem(itemId=3551, price=5, goldPrice=3, color1=113, color2=113, itemType="Shoes"), # Pale Rose Red Pansy Slippers
                    ShopItem(itemId=2122, price=5, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Delphinium Barrette
                    ShopItem(itemId=111, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Delphinium Top
                    ShopItem(itemId=1123, price=9, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Delphinium Skirt
                    ShopItem(itemId=3581, price=5, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Delphinium Shoes
                    ShopItem(itemId=2050, price=5, goldPrice=3, color1=201, color2=201, itemType="HeadItem"), # Velvet Red Gentian Original Headband
                    ShopItem(itemId=331, price=9, goldPrice=5, color1=201, color2=201, itemType="Shirt"), # Velvet Red Gentian Top
                    ShopItem(itemId=1268, price=9, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Gentian Skirt
                    ShopItem(itemId=3691, price=5, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Gentian Shoes
                    ShopItem(itemId=2421, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Cheery Cherry Headband
                    ShopItem(itemId=1000054, price=9, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Cheery Cherry Top
                    ShopItem(itemId=1669, price=2, goldPrice=1, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Cheery Cherry Clutch
                    ShopItem(itemId=1461, price=9, goldPrice=5, color1=230, color2=230, itemType="Skirt"), # Scarlet Red Cheery Cherry Skirt
                    ShopItem(itemId=3842, price=5, goldPrice=3, color1=230, color2=230, itemType="Shoes"), # Scarlet Red Cheery Cherry Heels
                    ShopItem(itemId=2429, price=5, goldPrice=3, color1=226, color2=226, itemType="HeadItem"), # Goldenrod Yellow Starfruit Earrings
                    ShopItem(itemId=1000062, price=9, goldPrice=5, color1=226, color2=226, itemType="Shirt"), # Goldenrod Yellow Starfruit Top
                    ShopItem(itemId=1469, price=9, goldPrice=5, color1=226, color2=226, itemType="Skirt"), # Goldenrod Yellow Starfruit Skirt
                    ShopItem(itemId=3854, price=5, goldPrice=3, color1=267, color2=226, itemType="Shoes"), # Celestial Blue Starfruit Heels with Goldenrod Yellow Trim
                    ShopItem(itemId=2010, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Fanned Flower Clip
                    ShopItem(itemId=284, price=9, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Layered Petal Top
                    ShopItem(itemId=1234, price=9, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Layered Petal Skirt
                    ShopItem(itemId=3539, price=5, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink White Rose Slippers
                    ShopItem(itemId=2173, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Blooming Rose Headband
                    ShopItem(itemId=295, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Formal Ruffle Top
                    ShopItem(itemId=1236, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Formal Ruffle Skirt
                    ShopItem(itemId=3718, price=5, goldPrice=3, color1=139, color2=139, itemType="Shoes"), # Seedling Green Ruffle Detail Shoes
                    ShopItem(itemId=2639, price=5, goldPrice=3, color1=121, color2=121, itemType="Necklace"), # Daisy Pink Spring Rose Choker
                    ShopItem(itemId=1000073, price=9, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Spring Rose Top
                    ShopItem(itemId=653, price=2, goldPrice=1, color1=121, color2=121, itemType="Belt"), # Daisy Pink Spring Rose Sash
                    ShopItem(itemId=1480, price=9, goldPrice=5, color1=207, color2=207, itemType="Skirt"), # Diamond Blue Spring Rose Skirt
                    ShopItem(itemId=3865, price=5, goldPrice=3, color1=207, color2=207, itemType="Shoes"), # Diamond Blue Spring Rose Shoes
                    ShopItem(itemId=2465, price=5, goldPrice=3, color1=264, color2=264, itemType="HeadItem"), # Jungle Green Posh Pineapple Fascinator
                    ShopItem(itemId=1000109, price=9, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Posh Pineapple Top
                    ShopItem(itemId=1001016, price=9, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Posh Pineapple Skirt
                    ShopItem(itemId=3892, price=5, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Posh Pineapple Pumps
                    ShopItem(itemId=2448, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Sycamore Blossom Earrings
                    ShopItem(itemId=1000077, price=9, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Sycamore Leaf Top
                    ShopItem(itemId=1483, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Sycamore Leaf Skirt
                    ShopItem(itemId=3868, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Sycamore Leaf Shoes
                    ShopItem(itemId=1000115, price=9, goldPrice=5, color1=17, color2=17, itemType="Shirt"), # Tendershoot Green Sweet Pea Petal Top
                    ShopItem(itemId=1001021, price=9, goldPrice=5, color1=17, color2=17, itemType="Skirt"), # Tendershoot Green Sweet Pea Petal Skirt
                    ShopItem(itemId=3897, price=5, goldPrice=3, color1=17, color2=17, itemType="Shoes"), # Tendershoot Green Sweet Pea Petal Shoes

                ],
            ),
            ShopCollection(
                collectionId=26, # Mainland Style Gift Sets
                items=[
                    ShopItem(itemId=396, price=9, goldPrice=5, color1=224, color2=206, itemType="Shirt"), # Ivory White Unstoppable Top
                    ShopItem(itemId=638, price=2, goldPrice=1, color1=206, color2=206, itemType="Belt"), # Raven Black Unstoppable Belt
                    ShopItem(itemId=1321, price=9, goldPrice=5, color1=45, color2=206, itemType="Skirt"), # Strawberry Red Unstoppable Skirt
                    ShopItem(itemId=3747, price=5, goldPrice=3, color1=206, color2=224, itemType="Shoes"), # Raven Black Sky High Laceups
                    ShopItem(itemId=2327, price=5, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Alluring Elegance Hat
                    ShopItem(itemId=408, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Alluring Elegance Dress Top
                    ShopItem(itemId=1327, price=9, goldPrice=5, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Alluring Elegance Dress Bottom
                    ShopItem(itemId=3750, price=5, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Alluring Elegance Sandals
                    ShopItem(itemId=2187, price=5, goldPrice=3, color1=82, color2=82, itemType="HeadItem"), # Raspberry Red Button Headband
                    ShopItem(itemId=401, price=9, goldPrice=5, color1=27, color2=27, itemType="Shirt"), # Corn Cob Yellow Bitsy Buttons Top
                    ShopItem(itemId=1324, price=9, goldPrice=5, color1=27, color2=27, itemType="Skirt"), # Corn Cob Yellow Bitsy Buttons Skirt
                    ShopItem(itemId=3656, price=5, goldPrice=3, color1=82, color2=82, itemType="Shoes"), # Raspberry Red One-Button Boots
                    ShopItem(itemId=2621, price=2, goldPrice=1, color1=141, color2=141, itemType="Necklace"), # Thundercloud Gray Art Deco Necklace
                    ShopItem(itemId=480, price=9, goldPrice=5, color1=182, color2=182, itemType="Shirt"), # Twilight Blue Sleek and Stylish Top
                    ShopItem(itemId=1397, price=9, goldPrice=5, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Peplum Skirt
                    ShopItem(itemId=3780, price=5, goldPrice=3, color1=182, color2=182, itemType="Shoes"), # Twilight Blue Stripey Wedges
                    ShopItem(itemId=2208, price=5, goldPrice=3, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Nifty Knit Hat
                    ShopItem(itemId=479, price=9, goldPrice=5, color1=81, color2=81, itemType="Shirt"), # Crimson Red Funky Striped Tee
                    ShopItem(itemId=1199, price=9, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Knitted Gala Skirt
                    ShopItem(itemId=3505, price=5, goldPrice=3, color1=75, color2=75, itemType="Shoes"), # Umber Brown Twirly Boots
                    ShopItem(itemId=2398, price=5, goldPrice=3, color1=274, color2=274, itemType="HeadItem"), #  Bellflower Purple Trendy Accessory Set
                    ShopItem(itemId=1000032, price=9, goldPrice=5, color1=274, color2=274, itemType="Shirt"), # Bellflower Purple Trendy Tied Shirt
                    ShopItem(itemId=1660, price=2, goldPrice=1, color1=274, color2=274, itemType="WristItem"), # Bellflower Purple Multi-Bead Bracelet
                    ShopItem(itemId=1443, price=9, goldPrice=5, color1=274, color2=274, itemType="Skirt"), # Bellflower Purple Buttoned Up Leggings
                    ShopItem(itemId=3823, price=5, goldPrice=3, color1=274, color2=274, itemType="Shoes"), # Bellflower Purple Glitter Sneakers
                    ShopItem(itemId=2346, price=5, goldPrice=3, color1=219, color2=219, itemType="HeadItem"), # Crystal Blue Fun Flower Headband
                    ShopItem(itemId=1000060, price=9, goldPrice=5, color1=199, color2=199, itemType="Shirt"), # Cherryblossom Pink Flower Power Top
                    ShopItem(itemId=651, price=2, goldPrice=1, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Flower Power Belt
                    ShopItem(itemId=1466, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Flower Power Skirt
                    ShopItem(itemId=3847, price=5, goldPrice=3, color1=46, color2=46, itemType="Shoes"), # Bark Brown Moccasin Boots
                    ShopItem(itemId=1000079, price=9, goldPrice=5, color1=218, color2=218, itemType="Shirt"), # Laurel Green Ruffled Petal Bolero
                    ShopItem(itemId=1682, price=2, goldPrice=1, color1=265, color2=265, itemType="WristItem"), # Bright Sky Blue Ruffled Petal Purse
                    ShopItem(itemId=1380, price=9, goldPrice=5, color1=258, color2=258, itemType="Skirt"), # Spearmint Green Single Ruffle Skirt
                    ShopItem(itemId=3870, price=5, goldPrice=3, color1=265, color2=265, itemType="Shoes"), # Bright Sky Blue Strappy Platforms
                    ShopItem(itemId=2443, price=5, goldPrice=3, color1=171, color2=171, itemType="HeadItem"), # Sunrise Yellow Sassy Chic Fedora
                    ShopItem(itemId=1000090, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Sassy Chic Top
                    ShopItem(itemId=1497, price=9, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Sassy Chic Skirt
                    ShopItem(itemId=3875, price=5, goldPrice=3, color1=171, color2=171, itemType="Shoes"), # Sunrise Yellow Sassy Chic Boots
                    ShopItem(itemId=2610, price=2, goldPrice=1, color1=134, color2=134, itemType="Necklace"), # Heather Purple Beaded Bud Necklace
                    ShopItem(itemId=416, price=9, goldPrice=5, color1=134, color2=134, itemType="Shirt"), # Heather Purple Lace Flower Top
                    ShopItem(itemId=1336, price=9, goldPrice=5, color1=134, color2=134, itemType="Skirt"), # Heather Purple Lace Flower Skirt
                    ShopItem(itemId=3759, price=5, goldPrice=3, color1=134, color2=134, itemType="Shoes"), # Heather Purple Lace Flower Wedges
                    ShopItem(itemId=2240, price=5, goldPrice=3, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Fancy Floral Headband
                    ShopItem(itemId=298, price=9, goldPrice=5, color1=277, color2=277, itemType="Shirt"), # Misty Purple Fancy Formal Top
                    ShopItem(itemId=1248, price=9, goldPrice=5, color1=277, color2=277, itemType="Skirt"), # Misty Purple Fancy Floral Skirt
                    ShopItem(itemId=3676, price=5, goldPrice=3, color1=277, color2=277, itemType="Shoes"), # Misty Purple Fancy Formal Boots
                    ShopItem(itemId=2391, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Cute and Cozy Cap
                    ShopItem(itemId=1000026, price=9, goldPrice=5, color1=201, color2=201, itemType="Shirt"), # Velvet Red Stylish Buckle Vest
                    ShopItem(itemId=1437, price=9, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Twist and Twirl Skirt
                    ShopItem(itemId=3817, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Funky Laceup Boots
                    ShopItem(itemId=2418, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Sailor Cloche
                    ShopItem(itemId=1000053, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Sailor Top
                    ShopItem(itemId=1460, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Sailor Striped Skirt
                    ShopItem(itemId=3841, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Sailor Slippers
                    ShopItem(itemId=2422, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Lovely Hearts Headband
                    ShopItem(itemId=1000056, price=9, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Heart Keyhole Top
                    ShopItem(itemId=1670, price=2, goldPrice=1, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Lovely Heart Purse
                    ShopItem(itemId=1462, price=9, goldPrice=5, color1=230, color2=230, itemType="Skirt"), # Scarlet Red Lovely Hearts Skirt
                    ShopItem(itemId=3843, price=5, goldPrice=3, color1=230, color2=230, itemType="Shoes"), # Scarlet Red Heart Buckle Boots
                ],
            ),


            ShopCollection(
                collectionId=3, # Tailoring Gift Sets - Sparrow men
                items=[
                    ShopItem(itemId=2195, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Buckingham Fur Hat
                    ShopItem(itemId=254, price=9, goldPrice=5, color1=82, color2=82, itemType="Shirt"), # Raspberry Red Buckingham Fur Coat
                    ShopItem(itemId=616, price=2, goldPrice=1, color1=116, color2=116, itemType="Belt"), # Mushroom White Buckingham Belt
                    ShopItem(itemId=1214, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Buckingham Fur Pants
                    ShopItem(itemId=3648, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Buckingham Fur Boots
                    ShopItem(itemId=233, price=9, goldPrice=5, color1=172, color2=172, itemType="Shirt"), # Forest Green Fur Trainer Jacket
                    ShopItem(itemId=600, price=2, goldPrice=1, color1=56, color2=56, itemType="Belt"), # Bole Brown Fur Trainer Belt
                    ShopItem(itemId=1197, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Fur Trainer Pants
                    ShopItem(itemId=3635, price=5, goldPrice=3, color1=56, color2=56, itemType="Shoes"), # Bole Brown Fur Trainer Boots
                    ShopItem(itemId=264, price=9, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Striking Fur Top
                    ShopItem(itemId=615, price=2, goldPrice=1, color1=59, color2=59, itemType="Belt"), # Bunny Brown Striking Fur Belt
                    ShopItem(itemId=1213, price=9, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Striking Fur Pants
                    ShopItem(itemId=3649, price=5, goldPrice=3, color1=206, color2=186, itemType="Shoes"), # Raven Black Striking Fur Boots with Yellow Trim
                    ShopItem(itemId=2192, price=5, goldPrice=3, color1=60, color2=60, itemType="HeadItem"), # Tyrian Purple Birdie Best Cap
                    ShopItem(itemId=245, price=9, goldPrice=5, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Birdie Best Top
                    ShopItem(itemId=607, price=2, goldPrice=1, color1=169, color2=169, itemType="Belt"), # Squirrel Gray Birdie Best Belt
                    ShopItem(itemId=3642, price=5, goldPrice=3, color1=169, color2=169, itemType="Shoes"), # Squirrel Gray Birdie Best Shoes
                    ShopItem(itemId=240, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Tailor's Top
                    ShopItem(itemId=606, price=2, goldPrice=1, color1=13, color2=13, itemType="Belt"), # Coral Pink Tailor's Utility Belt
                    ShopItem(itemId=1203, price=9, goldPrice=5, color1=73, color2=73, itemType="Skirt"), # Grape Purple Tailor's Trousers
                    ShopItem(itemId=3637, price=5, goldPrice=3, color1=87, color2=87, itemType="Shoes"), # Driftwood Brown Tailor's Boots
                    ShopItem(itemId=267, price=9, goldPrice=5, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Knit Messenger Top
                    ShopItem(itemId=620, price=2, goldPrice=1, color1=177, color2=177, itemType="Belt"), # Mud Brown Knit Messenger Belt
                    ShopItem(itemId=1216, price=9, goldPrice=5, color1=93, color2=93, itemType="Skirt"), # Maple Brown Knit Messenger Pants
                    ShopItem(itemId=3653, price=5, goldPrice=3, color1=177, color2=177, itemType="Shoes"), # Mud Brown Knit Messenger Slippers
                    ShopItem(itemId=241, price=9, goldPrice=5, color1=161, color2=161, itemType="Shirt"), # Buried Treasure Brown Lightning Bead Coat
                    ShopItem(itemId=1202, price=9, goldPrice=5, color1=91, color2=91, itemType="Skirt"), # Coconut Brown Lightning Bead Pants
                    ShopItem(itemId=3593, price=5, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Ivy Wrap Slippers
                    ShopItem(itemId=2189, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White All Buttons Visor
                    ShopItem(itemId=234, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Button Down Jacket
                    ShopItem(itemId=1198, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Button Down Pants
                    ShopItem(itemId=3636, price=5, goldPrice=3, color1=215, color2=215, itemType="Shoes"), # Pewter Gray Button Down Shoes
                ],
            ),
            ShopCollection(
                collectionId=19, # Costume Gift Sets
                items=[
                    ShopItem(itemId=2193, price=5, goldPrice=3, color1=75, color2=75, itemType="HeadItem"), # Umber Brown Never West Round Up Hat
                    ShopItem(itemId=2568, price=2, goldPrice=1, color1=171, color2=171, itemType="Necklace"), # Sunrise Yellow Never West Necklace
                    ShopItem(itemId=246, price=9, goldPrice=5, color1=92, color2=92, itemType="Shirt"), # Hawk Brown Never West Shirt
                    ShopItem(itemId=608, price=2, goldPrice=1, color1=171, color2=171, itemType="Belt"), # Sunrise Yellow Never West Belt
                    ShopItem(itemId=1206, price=9, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Never West Trousers
                    ShopItem(itemId=3643, price=5, goldPrice=3, color1=171, color2=171, itemType="Shoes"), # Sunrise Yellow Never West Boots
                    ShopItem(itemId=2415, price=5, goldPrice=3, color1=172, color2=172, itemType="HeadItem"), # Forest Green Calla Lily Hat
                    ShopItem(itemId=1000050, price=9, goldPrice=5, color1=172, color2=172, itemType="Shirt"), # Forest Green Calla Lily Top
                    ShopItem(itemId=649, price=2, goldPrice=1, color1=76, color2=76, itemType="Belt"), # Chocolate Brown Calla Lily Belt
                    ShopItem(itemId=1457, price=9, goldPrice=5, color1=76, color2=76, itemType="Skirt"), # Chocolate Brown Calla Lily Pants
                    ShopItem(itemId=3838, price=5, goldPrice=3, color1=172, color2=172, itemType="Shoes"), # Forest Green Calla Lily Boots
                    ShopItem(itemId=2289, price=5, goldPrice=3, color1=1, color2=1, itemType="HeadItem"), # Mint Green Clover Hat
                    ShopItem(itemId=2593, price=2, goldPrice=1, color1=1, color2=1, itemType="Necklace"), # Mint Green Clover Bowtie
                    ShopItem(itemId=350, price=9, goldPrice=5, color1=1, color2=1, itemType="Shirt"), # Mint Green Clover Vest
                    ShopItem(itemId=1286, price=9, goldPrice=5, color1=1, color2=1, itemType="Skirt"), # Mint Green Clover Knickers
                    ShopItem(itemId=3710, price=5, goldPrice=3, color1=1, color2=1, itemType="Shoes"), # Mint Green Clover Boots
                    ShopItem(itemId=2361, price=5, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Wizard Beard
                    ShopItem(itemId=498, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Wizard Top
                    ShopItem(itemId=1414, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Wizard Robe
                    ShopItem(itemId=3792, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Wizard Boots
                    ShopItem(itemId=291, price=9, goldPrice=5, color1=145, color2=145, itemType="Shirt"), #  Tinker Bell Green Tinker Training Jersey
                    ShopItem(itemId=1245, price=9, goldPrice=5, color1=186, color2=186, itemType="Skirt"), # Honeycomb Yellow Tinker Training Shorts
                    ShopItem(itemId=3668, price=5, goldPrice=3, color1=166, color2=145, itemType="Shoes"), #  Snow White All-Terrain Training Shoes with Tinker Bell Green Trim
                    ShopItem(itemId=289, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Garden Training Jersey
                    ShopItem(itemId=1242, price=9, goldPrice=5, color1=174, color2=166, itemType="Skirt"), # Rosetta Red Garden Training Shorts with Snow White Trim
                    ShopItem(itemId=3668, price=5, goldPrice=3, color1=174, color2=174, itemType="Shoes"), #  Rosetta Red All-Terrain Training Shoes
                    ShopItem(itemId=292, price=9, goldPrice=5, color1=176, color2=126, itemType="Shirt"), # Silvermist Blue Water Training Jersey with Raindrop Blue Trim
                    ShopItem(itemId=1244, price=9, goldPrice=5, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue Water Training Shorts
                    ShopItem(itemId=3668, price=5, goldPrice=3, color1=176, color2=176, itemType="Shoes"), #  Silvermist Blue All-Terrain Training Shoes
                    ShopItem(itemId=288, price=9, goldPrice=5, color1=178, color2=237, itemType="Shirt"), # Fawn Orange Animal Training Jersey with Cantaloupe Orange Trim
                    ShopItem(itemId=1241, price=9, goldPrice=5, color1=237, color2=237, itemType="Skirt"), # Cantaloupe Orange Animal Training Shorts
                    ShopItem(itemId=3666, price=5, goldPrice=3, color1=178, color2=178, itemType="Shoes"), # Fawn Orange Super Winged Sneakers
                    ShopItem(itemId=290, price=9, goldPrice=5, color1=47, color2=111, itemType="Shirt"), # Iridessa Yellow Light Training Jersey with Sparkling Yellow Trim
                    ShopItem(itemId=1243, price=9, goldPrice=5, color1=111, color2=111, itemType="Skirt"), # Sparkling Yellow Light Training Shorts
                    ShopItem(itemId=3668, price=5, goldPrice=3, color1=47, color2=47, itemType="Shoes"), # Iridessa Yellow All-Terrain Training Shoes
                    ShopItem(itemId=2278, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Soft-Serve Hat
                    ShopItem(itemId=348, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Candy Fanatic Marshmallow Top
                    ShopItem(itemId=1284, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Candy Fanatic Licorice Shorts
                    ShopItem(itemId=3708, price=5, goldPrice=3, color1=45, color2=45, itemType="Shoes"), # Strawberry Red Candy Fanatic Jellybean Shoes
                    ShopItem(itemId=2362, price=5, goldPrice=3, color1=114, color2=114, itemType="HeadItem"), # Foxtail Orange Fox Mask
                    ShopItem(itemId=497, price=9, goldPrice=5, color1=143, color2=143, itemType="Shirt"), # June Bug Green Fox Costume Top
                    ShopItem(itemId=1413, price=9, goldPrice=5, color1=143, color2=143, itemType="Skirt"), # June Bug Green Fox Trousers
                    ShopItem(itemId=3793, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Fox Boots
                ],
            ),
            ShopCollection(
                collectionId=33, # Famous Fairy Gift Sets
                items=[
                    ShopItem(itemId=176, price=9, goldPrice=5, color1=75, color2=75, itemType="Shirt"), # Umber Brown Terence's Top
                    ShopItem(itemId=1160, price=9, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Terence's Trunks
                    ShopItem(itemId=3613, price=5, goldPrice=3, color1=86, color2=86, itemType="Shoes"), # Nutmeg Brown Terence's Shoes
                    ShopItem(itemId=2152, price=5, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Bobble's Goggles
                    ShopItem(itemId=179, price=9, goldPrice=5, color1=65, color2=65, itemType="Shirt"), # Summer Green Bobble Vest
                    ShopItem(itemId=575, price=2, goldPrice=1, color1=46, color2=46, itemType="Belt"), # Bark Brown Bobble Belt
                    ShopItem(itemId=1161, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Bobble Trunks
                    ShopItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                    ShopItem(itemId=180, price=9, goldPrice=5, color1=64, color2=64, itemType="Shirt"), # Emerald Green Clank's Top
                    ShopItem(itemId=1162, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Clank's Trunks
                    ShopItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                    ShopItem(itemId=1000010, price=9, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Sled's Top
                    ShopItem(itemId=1425, price=9, goldPrice=5, color1=216, color2=216, itemType="Skirt"), # Slate Gray Sled's Trousers
                    ShopItem(itemId=3800, price=5, goldPrice=3, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Sled's Shoes
                ],
            ),
        


            ShopCollection(
                collectionId=27, # Costume Gift Sets
                items=[
                    ShopItem(itemId=2216, price=5, goldPrice=3, color1=206, color2=167, itemType="HeadItem"), # Raven Black Bewitching Hat with Never Silver Trim
                    ShopItem(itemId=482, price=9, goldPrice=5, color1=206, color2=167, itemType="Shirt"), # Raven Black Bewitching Top with Never Silver Trim
                    ShopItem(itemId=1586, price=2, goldPrice=1, color1=206, color2=167, itemType="WristItem"), # Buried Treasure Brown Bewitching Twig Broom
                    ShopItem(itemId=1399, price=9, goldPrice=5, color1=206, color2=167, itemType="Skirt"), # Raven Black Bewitching Skirt with Never Silver Trim
                    ShopItem(itemId=3674, price=5, goldPrice=3, color1=206, color2=167, itemType="Shoes"), # Raven Black Bewitching Boots with Never Silver Trim
                    ShopItem(itemId=2238, price=5, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Spring Peacock Headband
                    ShopItem(itemId=317, price=9, goldPrice=5, color1=221, color2=221, itemType="Shirt"), # Jade Green Spring Peacock Top
                    ShopItem(itemId=1256, price=9, goldPrice=5, color1=221, color2=221, itemType="Skirt"), # Jade Green Spring Peacock Skirt
                    ShopItem(itemId=3684, price=5, goldPrice=3, color1=221, color2=221, itemType="Shoes"), # Jade Green Spring Peacock Shoes
                    ShopItem(itemId=2239, price=5, goldPrice=3, color1=169, color2=169, itemType="HeadItem"), # Squirrel Gray Fluffy Owl Fascinator
                    ShopItem(itemId=321, price=9, goldPrice=5, color1=166, color2=169, itemType="Shirt"), # Snow White Feather Accent Capelet with Squirrel Gray Trim
                    ShopItem(itemId=1261, price=9, goldPrice=5, color1=166, color2=169, itemType="Skirt"), # Snow White Layered Feather Skirt with Squirrel Gray Trim
                    ShopItem(itemId=3687, price=5, goldPrice=3, color1=166, color2=169, itemType="Shoes"), # Snow White Feathered Ankle Boots with Squirrel Gray Trim
                    ShopItem(itemId=2017, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Tulip Petal Bow
                    ShopItem(itemId=327, price=9, goldPrice=5, color1=126, color2=126, itemType="Shirt"), # Raindrop Blue Wonderland Top
                    ShopItem(itemId=1265, price=9, goldPrice=5, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue Wonderland Skirt
                    ShopItem(itemId=3688, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Wonderland Shoes
                    ShopItem(itemId=2083, price=5, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Mer-Made Crown
                    ShopItem(itemId=400, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Magical Mermaid Top
                    ShopItem(itemId=1323, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Magical Mermaid Skirt
                    ShopItem(itemId=3675, price=5, goldPrice=3, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Glittering Glass Slippers
                ],
            ),
            ShopCollection(
                collectionId=30, # Fashion Boutique Gift Sets
                items=[
                    ShopItem(itemId=447, price=9, goldPrice=5, color1=200, color2=200, itemType="Shirt"), # Ruby Pink Tri-Color Top
                    ShopItem(itemId=1642, price=2, goldPrice=1, color1=200, color2=200, itemType="WristItem"), #  Ruby Pink Spangled Clutch
                    ShopItem(itemId=1360, price=9, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Tri-Color Skirt
                    ShopItem(itemId=3716, price=5, goldPrice=3, color1=27, color2=27, itemType="Shoes"), # Corn Cob Yellow Morpho Butterfly Shoes
                    ShopItem(itemId=460, price=9, goldPrice=5, color1=180, color2=180, itemType="Shirt"), # Seashell Blue Furry Vest
                    ShopItem(itemId=1377, price=9, goldPrice=5, color1=180, color2=180, itemType="Skirt"), # Seashell Blue Sweet Stripey Skirt
                    ShopItem(itemId=3778, price=5, goldPrice=3, color1=180, color2=180, itemType="Shoes"), #  Seashell Blue Colorblock Wedges
                    ShopItem(itemId=427, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Sweater Dress Top
                    ShopItem(itemId=1347, price=9, goldPrice=5, color1=69, color2=69, itemType="Skirt"), # Powder Blue Sweater Dress Skirt
                    ShopItem(itemId=3739, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), #  Ivory White Casual Moccasins
                    ShopItem(itemId=426, price=9, goldPrice=5, color1=266, color2=266, itemType="Shirt"), # Ocean Blue Cozy Coat
                    ShopItem(itemId=1343, price=9, goldPrice=5, color1=225, color2=225, itemType="Skirt"), # Eggplant Purple Skinny Jeans
                    ShopItem(itemId=3773, price=5, goldPrice=3, color1=236, color2=236, itemType="Shoes"), # Dusty Brown Comfy Slip-Ons
                    ShopItem(itemId=424, price=9, goldPrice=5, color1=211, color2=211, itemType="Shirt"), # Gentian Purple Cropped Cardigan
                    ShopItem(itemId=1345, price=9, goldPrice=5, color1=275, color2=275, itemType="Skirt"), # Shadowy Purple Big Bow Skirt
                    ShopItem(itemId=3767, price=5, goldPrice=3, color1=74, color2=74, itemType="Shoes"), # Soil Brown Knee Boots
                    ShopItem(itemId=2317, price=5, goldPrice=3, color1=45, color2=239, itemType="HeadItem"), # Strawberry Red Blooming Headband with Coffee Black Trim
                    ShopItem(itemId=464, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Charleston Top
                    ShopItem(itemId=1383, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Charleston Skirt
                    ShopItem(itemId=3777, price=5, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Charleston Heels
                    ShopItem(itemId=433, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Zippy Top
                    ShopItem(itemId=1351, price=9, goldPrice=5, color1=268, color2=268, itemType="Skirt"), # Navy Blue Zippy Skirt
                    ShopItem(itemId=3774, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Roller Skates
                    ShopItem(itemId=456, price=9, goldPrice=5, color1=282, color2=282, itemType="Shirt"), # Magnolia White Sassy Suspender Top
                    ShopItem(itemId=1372, price=9, goldPrice=5, color1=165, color2=165, itemType="Skirt"), # Spring Breeze Green Layered Shorts
                    ShopItem(itemId=3760, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Trinket Toe Flats
                    ShopItem(itemId=469, price=9, goldPrice=5, color1=285, color2=285, itemType="Shirt"), # Jazzberry Red Cropped Sweater
                    ShopItem(itemId=1356, price=9, goldPrice=5, color1=266, color2=266, itemType="Skirt"), # Ocean Blue Sparkly Dotted Mini
                    ShopItem(itemId=3772, price=5, goldPrice=3, color1=285, color2=285, itemType="Shoes"), # Jazzberry Red Platform Espadrilles
                    ShopItem(itemId=448, price=9, goldPrice=5, color1=195, color2=195, itemType="Shirt"), # Electric Blue Fabulous Fishy Top
                    ShopItem(itemId=1361, price=9, goldPrice=5, color1=195, color2=195, itemType="Skirt"), # Electric Blue Fabulous Fishy Skirt
                    ShopItem(itemId=3764, price=5, goldPrice=3, color1=195, color2=195, itemType="Shoes"), # Electric Blue Spider Web Heels
                    ShopItem(itemId=420, price=9, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Clever Cutout Tank
                    ShopItem(itemId=1359, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Mermaid Skirt
                    ShopItem(itemId=3763, price=5, goldPrice=3, color1=45, color2=45, itemType="Shoes"), # Strawberry Red Banded Sandals
                    ShopItem(itemId=444, price=9, goldPrice=5, color1=165, color2=165, itemType="Shirt"), # Spring Breeze Green Grecian Top
                    ShopItem(itemId=1357, price=9, goldPrice=5, color1=165, color2=152, itemType="Skirt"), # Spring Breeze Green Grecian Skirt with Pale Purple Trim
                    ShopItem(itemId=3737, price=5, goldPrice=3, color1=152, color2=152, itemType="Shoes"), # Pale Purple Sweet Strappy Shoes
                    ShopItem(itemId=445, price=9, goldPrice=5, color1=235, color2=235, itemType="Shirt"), #  Tawny Orange Autumn Leaf Top
                    ShopItem(itemId=1358, price=9, goldPrice=5, color1=235, color2=235, itemType="Skirt"), # Tawny Orange Autumn Leaf Skirt
                    ShopItem(itemId=3768, price=5, goldPrice=3, color1=235, color2=235, itemType="Shoes"), #  Tawny Orange Autumn Leaf Boots
                    ShopItem(itemId=465, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Crocheted Vest
                    ShopItem(itemId=1390, price=9, goldPrice=5, color1=18, color2=18, itemType="Skirt"), # Waterfall Blue Patchwork Skirt
                    ShopItem(itemId=3759, price=5, goldPrice=3, color1=152, color2=152, itemType="Shoes"), # Pale Purple Lace Flower Wedges
                    ShopItem(itemId=2341, price=5, goldPrice=3, color1=220, color2=165, itemType="HeadItem"), # Dusty Pink Rose Crown with Spring Breeze Green Trim
                    ShopItem(itemId=461, price=9, goldPrice=5, color1=239, color2=220, itemType="Shirt"), # Coffee Black Bitsy Bolero Top with Dusty Pink Trim
                    ShopItem(itemId=1374, price=9, goldPrice=5, color1=220, color2=220, itemType="Skirt"), # Dusty Pink Bubble Skirt
                    ShopItem(itemId=3769, price=5, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Desert Rose Boots
                    ShopItem(itemId=440, price=9, goldPrice=5, color1=282, color2=282, itemType="Shirt"), # Magnolia White Heart Tee
                    ShopItem(itemId=1362, price=9, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Fitted Formal Skirt
                    ShopItem(itemId=3765, price=5, goldPrice=3, color1=200, color2=200, itemType="Shoes"), # Ruby Pink Ankle Warmer Heels
                    ShopItem(itemId=2344, price=5, goldPrice=3, color1=118, color2=118, itemType="HeadItem"), # Sapphire Blue Sailor Hat
                    ShopItem(itemId=443, price=9, goldPrice=5, color1=63, color2=63, itemType="Shirt"), # Butterfly Blue Chevron Blouse
                    ShopItem(itemId=1384, price=9, goldPrice=5, color1=63, color2=63, itemType="Skirt"), # Butterfly Blue Sailor Pants
                    ShopItem(itemId=3775, price=5, goldPrice=3, color1=118, color2=118, itemType="Shoes"), # Sapphire Blue Bow Toe Flats
                    ShopItem(itemId=449, price=9, goldPrice=5, color1=10, color2=10, itemType="Shirt"), # Cantaloupe Orange Chandelier Top
                    ShopItem(itemId=1364, price=9, goldPrice=5, color1=10, color2=10, itemType="Skirt"), # Cantaloupe Orange Chandelier Skirt
                    ShopItem(itemId=3738, price=5, goldPrice=3, color1=234, color2=234, itemType="Shoes"), # Flame Orange Bow Heels
                    ShopItem(itemId=2316, price=5, goldPrice=3, color1=282, color2=282, itemType="HeadItem"), # Magnolia White Pixie Diamond Headband
                    ShopItem(itemId=475, price=9, goldPrice=5, color1=277, color2=277, itemType="Shirt"), # Misty Purple Pixie Diamonds Gown
                    ShopItem(itemId=1392, price=9, goldPrice=5, color1=212, color2=212, itemType="Skirt"), # Indigo Purple Pixie Diamonds Skirt
                    ShopItem(itemId=3740, price=5, goldPrice=3, color1=282, color2=282, itemType="Shoes"), # Magnolia White Pixie Diamond Heels
                    ShopItem(itemId=474, price=9, goldPrice=5, color1=165, color2=165, itemType="Shirt"), # Spring Breeze Green Striking Twelve Top
                    ShopItem(itemId=1389, price=9, goldPrice=5, color1=165, color2=165, itemType="Skirt"), # Spring Breeze Green Striking Twelve Skirt
                    ShopItem(itemId=3675, price=5, goldPrice=3, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Glittering Glass Slippers
                ],
            ),

            ShopCollection(
                collectionId=43, # Post Office Accessories
                items=[
                    ShopItem(itemId=2581, price=2, goldPrice=1, color1=230, color2=230, itemType="Necklace"), # Scarlet Red Flying V Guitar
                    ShopItem(itemId=2589, price=2, goldPrice=1, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Keytar
                    ShopItem(itemId=2590, price=2, goldPrice=1, color1=206, color2=206, itemType="Necklace"), # Raven Black Electric Guitar
                    ShopItem(itemId=2554, price=2, goldPrice=1, color1=180, color2=180, itemType="Necklace"), # Seashell Blue Giant Bow Tie
                    ShopItem(itemId=2040, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Silly Spectacles
                    ShopItem(itemId=2180, price=5, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Stars Are Out Cap
                    ShopItem(itemId=1583, price=2, goldPrice=1, color1=30, color2=30, itemType="WristItem"), # Pumpkin Orange Trick or Treat Basket
                    ShopItem(itemId=2213, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Wayfairy Glasses
                    ShopItem(itemId=2214, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Fairy Spotter Specs
                    ShopItem(itemId=2241, price=5, goldPrice=3, color1=197, color2=197, itemType="HeadItem"), # Electric Purple Fly Shutter Shades
                    ShopItem(itemId=2038, price=5, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Cold Weather Hat
                    ShopItem(itemId=2296, price=5, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Stripey Sleep Cap
                    ShopItem(itemId=2137, price=5, goldPrice=3, color1=10, color2=10, itemType="HeadItem"), # Cantaloupe Orange Summer Snorkel
                    ShopItem(itemId=1602, price=2, goldPrice=1, color1=2, color2=168, itemType="WristItem"), # Clover Green Tinkered Clover Sundial with Never Gold Trim
                    ShopItem(itemId=1603, price=2, goldPrice=1, color1=152, color2=161, itemType="WristItem"), # Pale Purple Tinkered Leaf Sundial with Buried Treasure Brown Trim
                    ShopItem(itemId=1605, price=2, goldPrice=1, color1=267, color2=267, itemType="WristItem"), # Celestial Blue Tinkered Jewel Sundial
                    ShopItem(itemId=2163, price=5, goldPrice=3, color1=170, color2=230, itemType="HeadItem"), # Olive Green Silly Top Hat with Red Trim
                    ShopItem(itemId=2627, price=2, goldPrice=1, color1=105, color2=108, itemType="Necklace"), # Siltstone Tan Acoustic Guitar with Tan Trim
                    ShopItem(itemId=2399, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Painter's Beret
                    ShopItem(itemId=1661, price=2, goldPrice=1, color1=108, color2=108, itemType="WristItem"), # Creamy Tan Painter's Palette
                    ShopItem(itemId=263, price=2, goldPrice=1, color1=168, color2=168, itemType="Necklace"), # Never Gold Winged Heart Necklace
                    ShopItem(itemId=2276, price=5, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Wacky Rainbow Wig
                    ShopItem(itemId=1573, price=2, goldPrice=1, color1=264, color2=264, itemType="WristItem"), # Jungle Green Tea Tray
                ],
            ),
            ShopCollection(
                collectionId=5,
                outfits=[
                    ShopOutfit(
                        outfitId=2001, # Outfit of the Month
                        items=[
  			                OutfitItem(itemId=2388, goldPrice=30, color1=41, color2=209, itemType="HeadItem"),
                            OutfitItem(itemId=1000090, goldPrice=0, color1=209, color2=40, itemType="Shirt"),
                            OutfitItem(itemId=1077, goldPrice=0, color1=49, color2=40, itemType="Skirt"),
                            OutfitItem(itemId=647, goldPrice=0, color1=41, color2=40, itemType="Belt"),
                            OutfitItem(itemId=3870, goldPrice=0, color1=41, color2=40, itemType="Shoes"),
                        ],
                    ),

                    ShopOutfit(
                        outfitId=2002, # Tillandsia Dress
                        items=[
                            OutfitItem(itemId=2262, goldPrice=20, color1=210, color2=210, itemType="HeadItem"),
                            OutfitItem(itemId=329, goldPrice=0, color1=210, color2=44, itemType="Shirt"),
                            OutfitItem(itemId=1266, goldPrice=0, color1=210, color2=44, itemType="Skirt"),
                            OutfitItem(itemId=625, goldPrice=0, color1=44, color2=44, itemType="Belt"),
                            OutfitItem(itemId=3689, goldPrice=0, color1=210, color2=210, itemType="Shoes"),
                        ],
                    ),
                    ShopOutfit(
                        outfitId=2003, # Pumpkim' Dress
                        items=[
                            OutfitItem(itemId=2263, goldPrice=20, color1=30, color2=30, itemType="HeadItem"),
                            OutfitItem(itemId=330, goldPrice=0, color1=206, color2=30, itemType="Shirt"),
                            OutfitItem(itemId=1267, goldPrice=0, color1=30, color2=30, itemType="Skirt"),
                            OutfitItem(itemId=3690, goldPrice=0, color1=206, color2=30, itemType="Shoes"),
                        ],
                    ),
                    ShopOutfit(
                        outfitId=2004, # Curcuma Dress
                        items=[
                            OutfitItem(itemId=2062, goldPrice=20, color1=140, color2=0, itemType="HeadItem"),
                            OutfitItem(itemId=332, goldPrice=0, color1=162, color2=140, itemType="Shirt"),
                            OutfitItem(itemId=1269, goldPrice=0, color1=162, color2=140, itemType="Skirt"),
                            OutfitItem(itemId=3694, goldPrice=0, color1=162, color2=140, itemType="Shoes"),
                        ],
                    ),
                ],
            ),
        ],
    ),


  

    


            

    NPCShop(
        zone=ZoneConstants.QUEENS_BOUTIQUE,
        shopId=9,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.ERICA,
            position=(417, 455),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_ERICA
        ),
        collections=[
            ShopCollection(
                collectionId=2, # The Queen's Collections (Red)
                outfits=[
                    ShopOutfit(
                        outfitId=1000, # Ravishing Rosette Gown
                        items=[
                            OutfitItem(itemId=2357, goldPrice=75, itemType="HeadItem"),
                            OutfitItem(itemId=486, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1402, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=643, goldPrice=0, itemType="Belt"),
                            OutfitItem(itemId=3784, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1001, # Chic Crimson Gown
                        items=[
                            OutfitItem(itemId=487, goldPrice=80, itemType="Shirt"),
                            OutfitItem(itemId=1403, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3785, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1002, # Resplendent Ruby Gown
                        items=[
                            OutfitItem(itemId=2376, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=1000002, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1416, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3803, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1003, # Blooming Couture Gown
                        items=[
                            OutfitItem(itemId=2408, goldPrice=120, itemType="HeadItem"),
                            OutfitItem(itemId=1000041, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1449, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3829, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1004, # Princess of Hearts Gown
                        items=[
                            OutfitItem(itemId=2453, goldPrice=150, itemType="HeadItem"),
                            OutfitItem(itemId=1000095, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001003, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3880, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1005, # Bewitching Blossoms Gown
                        items=[
                            OutfitItem(itemId=2454, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=1000096, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001004, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3881, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1006, # Flowing Floral Gown
                        items=[
                            OutfitItem(itemId=2463, goldPrice=130, itemType="HeadItem"),
                            OutfitItem(itemId=1000106, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001014, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3890, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=106, # The Queen's Collections (Orange)
                outfits=[
                    ShopOutfit(
                        outfitId=1007, # Delicate Dahlia Gown
                        items=[
                            OutfitItem(itemId=2329, goldPrice=85, itemType="HeadItem"),
                            OutfitItem(itemId=410, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1325, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3752, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1008, # Perfect Peacock Gown
                        items=[
                            OutfitItem(itemId=2378, goldPrice=100, itemType="HeadItem"),
                            OutfitItem(itemId=1000014, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1428, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3805, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1009, # Autumn Couture Gown
                        items=[
                            OutfitItem(itemId=2380, goldPrice=100, itemType="HeadItem"),
                            OutfitItem(itemId=1000016, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1430, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3807, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1010, # Critterific Couture
                        items=[
                            OutfitItem(itemId=2409, goldPrice=130, itemType="HeadItem"),
                            OutfitItem(itemId=1000042, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1450, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3830, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1011, # Sensational Sparkle Gown
                        items=[
                            OutfitItem(itemId=2436, goldPrice=130, itemType="HeadItem"),
                            OutfitItem(itemId=1000071, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1479, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3864, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1012, # Autumn Revelry Gown
                        items=[
                            OutfitItem(itemId=2460, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=1000103, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001011, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3887, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1013, # Savannah Sunset Gown
                        items=[
                            OutfitItem(itemId=2471, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=1000119, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001026, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3901, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1014, # Perfect Poinsettia Gown
                        items=[
                            OutfitItem(itemId=2458, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=1000100, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001008, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3885, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=108, # The Queen's Collections (Yellow)
                outfits=[
                    ShopOutfit(
                        outfitId=1015, # Soverign Hearts Gown
                        items=[
                            OutfitItem(itemId=2451, goldPrice=160, itemType="HeadItem"),
                            OutfitItem(itemId=2641, goldPrice=0, itemType="Necklace"),
                            OutfitItem(itemId=1000093, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001001, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=1683, goldPrice=0, itemType="WristItem"),
                            OutfitItem(itemId=3878, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1016, # Sublime Splendor Gown
                        items=[
                            OutfitItem(itemId=2307, goldPrice=85, itemType="HeadItem"),
                            OutfitItem(itemId=392, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1314, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3731, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1017, # Gilded Glamour Gown
                        items=[
                            OutfitItem(itemId=2332, goldPrice=80, itemType="HeadItem"),
                            OutfitItem(itemId=412, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1331, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3754, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1018, # Golden Flutter Gown
                        items=[
                            OutfitItem(itemId=2430, goldPrice=120, itemType="HeadItem"),
                            OutfitItem(itemId=1000064, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1471, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3856, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1019, # Royal Couture Gown
                        items=[
                            OutfitItem(itemId=2432, goldPrice=150, itemType="HeadItem"),
                            OutfitItem(itemId=1000066, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1473, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3858, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1020, # Radiant Rosebud Gown
                        items=[
                            OutfitItem(itemId=2433, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=1000068, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1475, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3860, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1021, # Golden Roses Gown
                        items=[
                            OutfitItem(itemId=2298, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=384, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1304, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3720, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1022, # Vivacious Vines Gown
                        items=[
                            OutfitItem(itemId=2328, goldPrice=85, itemType="HeadItem"),
                            OutfitItem(itemId=409, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1328, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3751, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=109, # The Queen's Collections (Green)
                outfits=[
                    ShopOutfit(
                        outfitId=1023, # Emerald Dreams Gown
                        items=[
                            OutfitItem(itemId=395, goldPrice=70, itemType="Shirt"),
                            OutfitItem(itemId=1316, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3735, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1024, # Fanciful Feathers Gown
                        items=[
                            OutfitItem(itemId=2381, goldPrice=90, itemType="HeadItem"),
                            OutfitItem(itemId=1000017, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1431, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3808, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1025, # Tinkered Couture
                        items=[
                            OutfitItem(itemId=2395, goldPrice=130, itemType="HeadItem"),
                            OutfitItem(itemId=2625, goldPrice=0, itemType="Necklace"),
                            OutfitItem(itemId=1000029, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1440, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3820, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1026, # Feathered Fringe Gown
                        items=[
                            OutfitItem(itemId=2459, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=2642, goldPrice=0, itemType="Necklace"),
                            OutfitItem(itemId=1000101, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001009, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3886, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1027, # Alluring Artisan Gown
                        items=[
                            OutfitItem(itemId=2470, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=2644, goldPrice=0, itemType="Necklace"),
                            OutfitItem(itemId=1000118, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001025, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3900, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1028, # Chic Sari
                        items=[
                            OutfitItem(itemId=2473, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=1000121, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001028, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3903, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1029, # Splendid Solstice Gown
                        items=[
                            OutfitItem(itemId=2407, goldPrice=140, itemType="HeadItem"),
                            OutfitItem(itemId=1000040, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1448, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3825, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=114, # The Queen's Collections (Blue)
                outfits=[
                    ShopOutfit(
                        outfitId=1030, # Fine Flowing Gown
                        items=[
                            OutfitItem(itemId=387, goldPrice=75, itemType="Shirt"),
                            OutfitItem(itemId=1313, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3730, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1031, # Grand and Graceful Gown
                        items=[
                            OutfitItem(itemId=391, goldPrice=70, itemType="Shirt"),
                            OutfitItem(itemId=1307, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3729, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1032, # Stunning Seafoam Gown
                        items=[
                            OutfitItem(itemId=2333, goldPrice=90, itemType="HeadItem"),
                            OutfitItem(itemId=413, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1332, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3755, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1033, # Gossamer Gown
                        items=[
                            OutfitItem(itemId=2334, goldPrice=85, itemType="HeadItem"),
                            OutfitItem(itemId=414, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1333, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3756, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1034, # Spectacular Swirl
                        items=[
                            OutfitItem(itemId=2379, goldPrice=95, itemType="HeadItem"),
                            OutfitItem(itemId=1000015, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1429, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3806, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1035, # Smashing Splash Gown
                        items=[
                            OutfitItem(itemId=2393, goldPrice=70, itemType="HeadItem"),
                            OutfitItem(itemId=1000027, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1438, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3818, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1036, # Winter Couture Gown
                        items=[
                            OutfitItem(itemId=2405, goldPrice=115, itemType="HeadItem"),
                            OutfitItem(itemId=1000039, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1447, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3828, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1037, # Pretty Panache Gown
                        items=[
                            OutfitItem(itemId=2384, goldPrice=115, itemType="HeadItem"),
                            OutfitItem(itemId=1000022, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1432, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3809, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1038, # Majestic Charm Gown
                        items=[
                            OutfitItem(itemId=2377, goldPrice=90, itemType="HeadItem"),
                            OutfitItem(itemId=1000013, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1427, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3804, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1039, # Finely Feathered Gown
                        items=[
                            OutfitItem(itemId=2452, goldPrice=120, itemType="HeadItem"),
                            OutfitItem(itemId=1000094, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001002, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3879, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1040, # Mystical Mist Gown
                        items=[
                            OutfitItem(itemId=2455, goldPrice=135, itemType="HeadItem"),
                            OutfitItem(itemId=1000097, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001005, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3882, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1041, # Riverine Elegance Gown
                        items=[
                            OutfitItem(itemId=2472, goldPrice=135, itemType="HeadItem"),
                            OutfitItem(itemId=1000120, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001027, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3902, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1042, # Radiant Regalia
                        items=[
                            OutfitItem(itemId=2476, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=1000131, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001040, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3905, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1043, # Summer Couture Gown
                        items=[
                            OutfitItem(itemId=390, goldPrice=90, itemType="Shirt"),
                            OutfitItem(itemId=1310, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3727, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=115, # The Queen's Collections (Purple)
                outfits=[
                    ShopOutfit(
                        outfitId=1044, # Morning Glory Gown
                        items=[
                            OutfitItem(itemId=2331, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=411, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1326, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3058, goldPrice=0, itemType="AnkleItem"),
                            OutfitItem(itemId=3753, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1045, # Moonlight Magic Gown
                        items=[
                            OutfitItem(itemId=2359, goldPrice=80, itemType="HeadItem"),
                            OutfitItem(itemId=490, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1406, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3788, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1046, # Fast-Flying Couture
                        items=[
                            OutfitItem(itemId=2394, goldPrice=100, itemType="HeadItem"),
                            OutfitItem(itemId=1000028, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1439, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3819, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1047, # Petal Twirl Gown
                        items=[
                            OutfitItem(itemId=2435, goldPrice=100, itemType="HeadItem"),
                            OutfitItem(itemId=1000070, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1477, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3862, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1048, # Magnificent Evening Gown
                        items=[
                            OutfitItem(itemId=2457, goldPrice=150, itemType="HeadItem"),
                            OutfitItem(itemId=1000099, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001007, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=1684, goldPrice=0, itemType="WristItem"),
                            OutfitItem(itemId=3884, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1049, # Irresistible Indigo Gown
                        items=[
                            OutfitItem(itemId=2461, goldPrice=105, itemType="HeadItem"),
                            OutfitItem(itemId=1000104, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1001012, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3888, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            ),
            ShopCollection(
                collectionId=116, # The Queen's Collections (Other)
                outfits=[
                    ShopOutfit(
                        outfitId=1050, # Incredible Iris Dress
                        items=[
                            OutfitItem(itemId=2303, goldPrice=80, itemType="HeadItem"),
                            OutfitItem(itemId=393, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1312, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3732, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1051, # Marvelous Magenta Gown
                        items=[
                            OutfitItem(itemId=488, goldPrice=70, itemType="Shirt"),
                            OutfitItem(itemId=1404, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3786, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1052, # Graceful Glamor Gown
                        items=[
                            OutfitItem(itemId=2358, goldPrice=85, itemType="HeadItem"),
                            OutfitItem(itemId=489, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1405, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3787, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1053, # Amethyst Flutter Gown
                        items=[
                            OutfitItem(itemId=2431, goldPrice=120, itemType="HeadItem"),
                            OutfitItem(itemId=1000065, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=1472, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3857, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                    ShopOutfit(
                        outfitId=1054, # Plush Plumes Gown
                        items=[
                            OutfitItem(itemId=2434, goldPrice=130, itemType="HeadItem"),
                            OutfitItem(itemId=1000069, goldPrice=0, itemType="Shirt"),
                            OutfitItem(itemId=652, goldPrice=0, itemType="Belt"),
                            OutfitItem(itemId=1476, goldPrice=0, itemType="Skirt"),
                            OutfitItem(itemId=3861, goldPrice=0, itemType="Shoes")
                        ]
                    ),
                ]
            )
        ]
    ),

    NPCShop(
        zone=ZoneConstants.EMBERS_ESSENTIALS,
        shopId=1002,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.EMBER,
            position=(433, 432),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_EMBER
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.TREETOP_HOUSEWARES,
        shopId=1002,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.TRINKET,
            position=(425, 444),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_TRINKET
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.DAISYS_DYES,
        shopId=2000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.DAISY,
            position=(390, 434),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_DAISY
        ),
        # Dye Bottle Item IDs are 14000 + Color ID in colorAssets.xml
        collections=[
            ShopCollection(
                collectionId=2003, # Seasonal Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14034, price=10, goldPrice=2), # Primrose Pink
                    ShopItem(itemId=14231, price=10, goldPrice=2), # Sunny Orange
                    ShopItem(itemId=14255, price=10, goldPrice=2), # Canary Yellow
                    ShopItem(itemId=14259, price=10, goldPrice=2), # Kiwi Green
                    ShopItem(itemId=14069, price=10, goldPrice=2), # Powder Blue
                    ShopItem(itemId=14208, price=10, goldPrice=2), # Cerulean Blue
                    ShopItem(itemId=14274, price=10, goldPrice=2), # Bellflower Purple
                    ShopItem(itemId=14285, price=10, goldPrice=2), # Jazzberry Red
                ],
            ),
            ShopCollection(
                collectionId=2020, # Red & Purple Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 57
                    ShopItem(itemId=14110, price=5, goldPrice=1), # Rosy Pink
                    ShopItem(itemId=14121, price=5, goldPrice=1), # Daisy Pink
                    ShopItem(itemId=14016, price=5, goldPrice=1), # Camellia Pink
                    ShopItem(itemId=14194, price=5, goldPrice=1), # Electric Pink
                    ShopItem(itemId=14008, price=5, goldPrice=1), # Watermelon Pink
                    ShopItem(itemId=14013, price=5, goldPrice=1), # Coral Pink
                    ShopItem(itemId=14026, price=5, goldPrice=1), # Raspberry Pink
                    ShopItem(itemId=14286, price=5, goldPrice=1), # Cherry Pink
                    ShopItem(itemId=14113, price=5, goldPrice=1), # Pale Rose Red
                    ShopItem(itemId=14045, price=5, goldPrice=1), # Strawberry Red
                    ShopItem(itemId=14082, price=5, goldPrice=1), # Raspberry Red
                    ShopItem(itemId=14230, price=5, goldPrice=1), # Scarlet Red
                    ShopItem(itemId=14201, price=5, goldPrice=1), # Velvet Red
                    ShopItem(itemId=14044, price=5, goldPrice=1), # Plumblossom Pink
                    ShopItem(itemId=14045, price=5, goldPrice=1), # Hyacinth Pink
                    ShopItem(itemId=14081, price=5, goldPrice=1), # Crimson Red
                    ShopItem(itemId=14130, price=5, goldPrice=1), # Orchid Pink
                    ShopItem(itemId=14140, price=5, goldPrice=1), # Bunnynose Pink
                    ShopItem(itemId=14144, price=5, goldPrice=1), # Petal Pink
                    ShopItem(itemId=14156, price=5, goldPrice=1), # Friendship Pink
                    ShopItem(itemId=14181, price=5, goldPrice=1), # Cupcake Pink
                    ShopItem(itemId=14174, price=5, goldPrice=1), # Rosetta Red
                    ShopItem(itemId=14189, price=5, goldPrice=1), # Ladybug Red
                    ShopItem(itemId=14199, price=5, goldPrice=1), # Cherryblossom Pink
                    ShopItem(itemId=14200, price=5, goldPrice=1), # Ruby Pink
                    ShopItem(itemId=14220, price=5, goldPrice=1), # Dusty Pink
                    ShopItem(itemId=14283, price=5, goldPrice=1), # Thistle Pink
                    ShopItem(itemId=14287, price=5, goldPrice=1), # Dianthus Red
                    ShopItem(itemId=14005, price=5, goldPrice=1), # Wysteria Purple
                    ShopItem(itemId=14014, price=5, goldPrice=1), # Plum Purple
                    ShopItem(itemId=14073, price=5, goldPrice=1), # Grape Purple
                    ShopItem(itemId=14061, price=5, goldPrice=1), # Pale Lilac Purple
                    ShopItem(itemId=14072, price=5, goldPrice=1), # Mauve Purple
                    ShopItem(itemId=14135, price=5, goldPrice=1), # Boysenberry Purple
                    ShopItem(itemId=14183, price=5, goldPrice=1), # Vidia Purple
                    ShopItem(itemId=14184, price=5, goldPrice=1), # Hummingbird Purple
                    ShopItem(itemId=14210, price=5, goldPrice=1), # Lotus Purple
                    ShopItem(itemId=14211, price=5, goldPrice=1), # Gentian Purple
                    ShopItem(itemId=14212, price=5, goldPrice=1), # Indigo Purple
                    ShopItem(itemId=14225, price=5, goldPrice=1), # Eggplant Purple
                    ShopItem(itemId=14229, price=5, goldPrice=1), # Electric Indigo
                    ShopItem(itemId=14276, price=5, goldPrice=1), # Dusk Purple
                    ShopItem(itemId=14129, price=5, goldPrice=1), # Fig Purple
                    ShopItem(itemId=14134, price=5, goldPrice=1), # Heather Purple
                    ShopItem(itemId=14278, price=5, goldPrice=1), # Aster Purple
                    ShopItem(itemId=14277, price=5, goldPrice=1), # Misty Purple
                    ShopItem(itemId=14117, price=5, goldPrice=1), # Amethyst Purple
                    ShopItem(itemId=14033, price=5, goldPrice=1), # Iris Purple
                    ShopItem(itemId=14197, price=5, goldPrice=1), # Electric Purple
                    ShopItem(itemId=14032, price=5, goldPrice=1), # Mulberry Purple
                    ShopItem(itemId=14275, price=5, goldPrice=1), # Shadowy Purple
                    ShopItem(itemId=14152, price=5, goldPrice=1), # Pale Purple
                    ShopItem(itemId=14192, price=5, goldPrice=1), # Royal Purple
                    ShopItem(itemId=14279, price=5, goldPrice=1), # Kingfisher Purple
                    ShopItem(itemId=14135, price=5, goldPrice=1), # Berry Purple
                    ShopItem(itemId=14281, price=5, goldPrice=1), # Deep Violet Purple
                    ShopItem(itemId=14284, price=5, goldPrice=1), # Deep Magenta Purple
                ],
            ),
            ShopCollection(
                collectionId=2001, # Orange & Yellow Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 43
                    ShopItem(itemId=14025, price=5, goldPrice=1), # Peachy Orange
                    ShopItem(itemId=14031, price=5, goldPrice=1), # Sunset Orange
                    ShopItem(itemId=14138, price=5, goldPrice=1), # Persimmon Orange
                    ShopItem(itemId=14109, price=5, goldPrice=1), # Soft Orange
                    ShopItem(itemId=14123, price=5, goldPrice=1), # Squash Orange
                    ShopItem(itemId=14010, price=5, goldPrice=1), # Cantaloupe Orange
                    ShopItem(itemId=14237, price=5, goldPrice=1), # Melon Orange
                    ShopItem(itemId=14187, price=5, goldPrice=1), # Maple Orange
                    ShopItem(itemId=14196, price=5, goldPrice=1), # Electric Orange
                    ShopItem(itemId=14228, price=5, goldPrice=1), # Duckbill Orange
                    ShopItem(itemId=14234, price=5, goldPrice=1), # Flame Orange
                    ShopItem(itemId=14232, price=5, goldPrice=1), # Rusty orange
                    ShopItem(itemId=14233, price=5, goldPrice=1), # Apricot Orange
                    ShopItem(itemId=14030, price=5, goldPrice=1), # Pumpkin Orange
                    ShopItem(itemId=14114, price=5, goldPrice=1), # Foxtail Orange
                    ShopItem(itemId=14173, price=5, goldPrice=1), # Carrot Orange
                    ShopItem(itemId=14238, price=5, goldPrice=1), # Zesty Orange
                    ShopItem(itemId=14178, price=5, goldPrice=1), # Fawn Orange
                    ShopItem(itemId=14235, price=5, goldPrice=1), # Tawny Orange
                    ShopItem(itemId=14111, price=5, goldPrice=1), # Sparkling Yellow
                    ShopItem(itemId=14047, price=5, goldPrice=1), # Buttercup Yellow
                    ShopItem(itemId=14142, price=5, goldPrice=1), # Bumble Bee Yellow
                    ShopItem(itemId=14162, price=5, goldPrice=1), # Sunglow Yellow
                    ShopItem(itemId=14252, price=5, goldPrice=1), # Starshine Yellow
                    ShopItem(itemId=14090, price=5, goldPrice=1), # Custard Yellow
                    ShopItem(itemId=14247, price=5, goldPrice=1), # Jasmine Yellow
                    ShopItem(itemId=14027, price=5, goldPrice=1), # Corn Cob Yellow
                    ShopItem(itemId=14253, price=5, goldPrice=1), # Dandelion Yellow
                    ShopItem(itemId=14186, price=5, goldPrice=1), # Honeycomb Yellow
                    ShopItem(itemId=14248, price=5, goldPrice=1), # Saffron Yellow
                    ShopItem(itemId=14011, price=5, goldPrice=1), # Marigold Yellow
                    ShopItem(itemId=14242, price=5, goldPrice=1), # Amber Yellow
                    ShopItem(itemId=14249, price=5, goldPrice=1), # Antique Yellow
                    ShopItem(itemId=14244, price=5, goldPrice=1), # Fairygold Yellow
                    ShopItem(itemId=14243, price=5, goldPrice=1), # Harvest Yellow
                    ShopItem(itemId=14254, price=5, goldPrice=1), # Sunflower Yellow
                    ShopItem(itemId=14179, price=5, goldPrice=1), # Iridessa Yellow
                    ShopItem(itemId=14168, price=5, goldPrice=1), # Never Gold
                    ShopItem(itemId=14226, price=5, goldPrice=1), # Goldenrod Yellow
                    ShopItem(itemId=14198, price=5, goldPrice=1), # Electric Yellow
                    ShopItem(itemId=14256, price=5, goldPrice=1), # Pear Yellow
                ],
            ),
            ShopCollection(
                collectionId=2008, # Blue & Green Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 85
                    ShopItem(itemId=14037, price=5, goldPrice=1), # Cloudy Blue
                    ShopItem(itemId=14062, price=5, goldPrice=1), # Bluebird Blue
                    ShopItem(itemId=14051, price=5, goldPrice=1), # Periwinkle Blue
                    ShopItem(itemId=14004, price=5, goldPrice=1), # Bluebell Blue
                    ShopItem(itemId=14022, price=5, goldPrice=1), # Blue Jay Blue
                    ShopItem(itemId=14042, price=5, goldPrice=1), # Blueberry Blue
                    ShopItem(itemId=14063, price=5, goldPrice=1), # Butterfly Blue
                    ShopItem(itemId=14006, price=5, goldPrice=1), # Havendish Blue
                    ShopItem(itemId=14024, price=5, goldPrice=1), # Sky Blue
                    ShopItem(itemId=14050, price=5, goldPrice=1), # Cornflower Blue
                    ShopItem(itemId=14118, price=5, goldPrice=1), # Sapphire Blue
                    ShopItem(itemId=14071, price=5, goldPrice=1), # Dewdrop Blue
                    ShopItem(itemId=14133, price=5, goldPrice=1), # Marina Blue
                    ShopItem(itemId=14124, price=5, goldPrice=1), # Forget-Me-Not Blue
                    ShopItem(itemId=14136, price=5, goldPrice=1), # Peacock Blue
                    ShopItem(itemId=14070, price=5, goldPrice=1), # Tinker blue
                    ShopItem(itemId=14219, price=5, goldPrice=1), # Crystal Blue
                    ShopItem(itemId=14267, price=5, goldPrice=1), # Celestial Blue
                    ShopItem(itemId=14195, price=5, goldPrice=1), # Electric Blue
                    ShopItem(itemId=14018, price=5, goldPrice=1), # Waterfall Blue
                    ShopItem(itemId=14158, price=5, goldPrice=1), # Icicle Blue
                    ShopItem(itemId=14068, price=5, goldPrice=1), # Huckleberry Blue
                    ShopItem(itemId=14049, price=5, goldPrice=1), # Robin Egg Blue
                    ShopItem(itemId=14265, price=5, goldPrice=1), # Bright Sky Blue
                    ShopItem(itemId=14040, price=5, goldPrice=1), # Candy Blue
                    ShopItem(itemId=14041, price=5, goldPrice=1), # Moonshadow Blue
                    ShopItem(itemId=14149, price=5, goldPrice=1), # Snowflake Blue
                    ShopItem(itemId=14153, price=5, goldPrice=1), # Frostbunny Blue
                    ShopItem(itemId=14155, price=5, goldPrice=1), # Frosty Blue
                    ShopItem(itemId=14176, price=5, goldPrice=1), # Silvermist Blue
                    ShopItem(itemId=14180, price=5, goldPrice=1), # Seashell Blue
                    ShopItem(itemId=14207, price=5, goldPrice=1), # Diamond Blue
                    ShopItem(itemId=14209, price=5, goldPrice=1), # Deep Sea Blue
                    ShopItem(itemId=14213, price=5, goldPrice=1), # Cobalt Blue
                    ShopItem(itemId=14223, price=5, goldPrice=1), # Teal Blue
                    ShopItem(itemId=14266, price=5, goldPrice=1), # Ocean Blue
                    ShopItem(itemId=14271, price=5, goldPrice=1), # True Blue
                    ShopItem(itemId=14270, price=5, goldPrice=1), # Horizon Blue
                    ShopItem(itemId=14036, price=5, goldPrice=1), # Hydrangea Blue
                    ShopItem(itemId=14182, price=5, goldPrice=1), # Twilight Blue
                    ShopItem(itemId=14268, price=5, goldPrice=1), # Navy Blue
                    ShopItem(itemId=14185, price=5, goldPrice=1), # Midnight Blue
                    ShopItem(itemId=14163, price=5, goldPrice=1), # Tundra Blue
                    ShopItem(itemId=14001, price=5, goldPrice=1), # Mint Green
                    ShopItem(itemId=14002, price=5, goldPrice=1), # Clover Green
                    ShopItem(itemId=14003, price=5, goldPrice=1), # Spruce Green
                    ShopItem(itemId=14017, price=5, goldPrice=1), # Tendershoot Green
                    ShopItem(itemId=14020, price=5, goldPrice=1), # Grassblade Green
                    ShopItem(itemId=14021, price=5, goldPrice=1), # Zucchini Green
                    ShopItem(itemId=14035, price=5, goldPrice=1), # Celery Green
                    ShopItem(itemId=14039, price=5, goldPrice=1), # Springtime Green
                    ShopItem(itemId=14048, price=5, goldPrice=1), # Sea Green
                    ShopItem(itemId=14064, price=5, goldPrice=1), # Emerald Green
                    ShopItem(itemId=14067, price=5, goldPrice=1), # Chartreuse Green
                    ShopItem(itemId=14115, price=5, goldPrice=1), # Asparagus Green
                    ShopItem(itemId=14120, price=5, goldPrice=1), # Fern Green
                    ShopItem(itemId=14122, price=5, goldPrice=1), # Lettuce Leaf Green
                    ShopItem(itemId=14127, price=5, goldPrice=1), # Grasshopper Green
                    ShopItem(itemId=14139, price=5, goldPrice=1), # Seedling Green
                    ShopItem(itemId=14038, price=5, goldPrice=1), # Apple Green
                    ShopItem(itemId=14258, price=5, goldPrice=1), # Spearmint Green
                    ShopItem(itemId=14143, price=5, goldPrice=1), # June Bug Green
                    ShopItem(itemId=14193, price=5, goldPrice=1), # Electric Green
                    ShopItem(itemId=14222, price=5, goldPrice=1), # Keylime Green
                    ShopItem(itemId=14263, price=5, goldPrice=1), # Aquamarine Green
                    ShopItem(itemId=14221, price=5, goldPrice=1), # Jade Green
                    ShopItem(itemId=14125, price=5, goldPrice=1), # Pine Green
                    ShopItem(itemId=14147, price=5, goldPrice=1), # Broccoli Stem Green
                    ShopItem(itemId=14150, price=5, goldPrice=1), # Dry Moss Green
                    ShopItem(itemId=14175, price=5, goldPrice=1), # Creek Green
                    ShopItem(itemId=14190, price=5, goldPrice=1), # Firefly Green
                    ShopItem(itemId=14202, price=5, goldPrice=1), # Honeydew Green
                    ShopItem(itemId=14203, price=5, goldPrice=1), # Shadow Green
                    ShopItem(itemId=14159, price=5, goldPrice=1), # Tea Green
                    ShopItem(itemId=14165, price=5, goldPrice=1), # Spring Breeze Green
                    ShopItem(itemId=14170, price=5, goldPrice=1), # Olive Green
                    ShopItem(itemId=14172, price=5, goldPrice=1), # Forest Green
                    ShopItem(itemId=14204, price=5, goldPrice=1), # Bamboo Green
                    ShopItem(itemId=14205, price=5, goldPrice=1), # Myrtle Green
                    ShopItem(itemId=14218, price=5, goldPrice=1), # Laurel Green
                    ShopItem(itemId=14257, price=5, goldPrice=1), # Lime Green
                    ShopItem(itemId=14260, price=5, goldPrice=1), # Peridot Green
                    ShopItem(itemId=14261, price=5, goldPrice=1), # Kelly Green
                    ShopItem(itemId=14264, price=5, goldPrice=1), # Jungle Green
                    ShopItem(itemId=14145, price=5, goldPrice=1), # Tinker Bell Green

                ],
            ),
            ShopCollection(
                collectionId=2009, # Brown & Neutral Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 47
                    ShopItem(itemId=14087, price=5, goldPrice=1), # Driftwood Brown
                    ShopItem(itemId=14083, price=5, goldPrice=1), # Cherry Brown
                    ShopItem(itemId=14079, price=5, goldPrice=1), # Sienna Brown
                    ShopItem(itemId=14075, price=5, goldPrice=1), # Umber Brown
                    ShopItem(itemId=14236, price=5, goldPrice=1), # Dusty Brown
                    ShopItem(itemId=14078, price=5, goldPrice=1), # Fawn Brown
                    ShopItem(itemId=14056, price=5, goldPrice=1), # Bole Brown
                    ShopItem(itemId=14076, price=5, goldPrice=1), # Chocolate Brown
                    ShopItem(itemId=14089, price=5, goldPrice=1), # Seashore Brown
                    ShopItem(itemId=14085, price=5, goldPrice=1), # Quail Brown
                    ShopItem(itemId=14246, price=5, goldPrice=1), # Bear Brown
                    ShopItem(itemId=14240, price=5, goldPrice=1), # Ironwood Brown
                    ShopItem(itemId=14161, price=5, goldPrice=1), # Buried Treasure Brown
                    ShopItem(itemId=14088, price=5, goldPrice=1), # Fruitwood Brown
                    ShopItem(itemId=14084, price=5, goldPrice=1), # Copper Brown
                    ShopItem(itemId=14074, price=5, goldPrice=1), # Soil Brown
                    ShopItem(itemId=14075, price=5, goldPrice=1), # Desert Brown
                    ShopItem(itemId=14154, price=5, goldPrice=1), # Beetle Brown
                    ShopItem(itemId=14046, price=5, goldPrice=1), # Bark Brown
                    ShopItem(itemId=14077, price=5, goldPrice=1), # Sepia Brown
                    ShopItem(itemId=14250, price=5, goldPrice=1), # Caramel Tan
                    ShopItem(itemId=14146, price=5, goldPrice=1), # Beech Brown
                    ShopItem(itemId=14245, price=5, goldPrice=1), # Earthy Tan
                    ShopItem(itemId=14251, price=5, goldPrice=1), # Polished Brown
                    ShopItem(itemId=14177, price=5, goldPrice=1), # Mud Brown
                    ShopItem(itemId=14166, price=5, goldPrice=1), # Snow White
                    ShopItem(itemId=14262, price=5, goldPrice=1), # Minty White
                    ShopItem(itemId=14269, price=5, goldPrice=1), # Crisp White
                    ShopItem(itemId=14282, price=5, goldPrice=1), # Magnolia White
                    ShopItem(itemId=14224, price=5, goldPrice=1), # Ivory White
                    ShopItem(itemId=14157, price=5, goldPrice=1), # Starry White
                    ShopItem(itemId=14116, price=5, goldPrice=1), # Mushroom White
                    ShopItem(itemId=14128, price=5, goldPrice=1), # Carnation White
                    ShopItem(itemId=14227, price=5, goldPrice=1), # Moonlight Gray
                    ShopItem(itemId=14169, price=5, goldPrice=1), # Squirrel Gray
                    ShopItem(itemId=14214, price=5, goldPrice=1), # Smokey Gray
                    ShopItem(itemId=14272, price=5, goldPrice=1), # Charcoal Gray
                    ShopItem(itemId=14239, price=5, goldPrice=1), # Coffee Black
                    ShopItem(itemId=14206, price=5, goldPrice=1), # Raven Black
                    ShopItem(itemId=14217, price=5, goldPrice=1), # Soft Gray
                    ShopItem(itemId=14215, price=5, goldPrice=1), # Pewter Gray
                    ShopItem(itemId=14141, price=5, goldPrice=1), # Thundercloud Gray
                    ShopItem(itemId=14273, price=5, goldPrice=1), # Panther Black
                    ShopItem(itemId=14167, price=5, goldPrice=1), # Never Silver
                    ShopItem(itemId=14216, price=5, goldPrice=1), # Slate Gray
                    ShopItem(itemId=14191, price=5, goldPrice=1), # Vidia Black
                    ShopItem(itemId=14055, price=5, goldPrice=1), # Pepper Black
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.PHOEBES_PARTY_FAVORS,
        shopId=3000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.PHOEBE,
            position=(352, 810),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_PHOEBE
        ),
        collections=[
            ShopCollection(
                collectionId=3000, # Party Decorations
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=17001, price=5, goldPrice=3), # Banner Party
                    ShopItem(itemId=17002, price=5, goldPrice=3), # Flower Party
                    ShopItem(itemId=17003, price=5, goldPrice=3), # Neverlight Party
                    ShopItem(itemId=17004, price=5, goldPrice=3), # Winter Party
                    ShopItem(itemId=17005, price=5, goldPrice=3), # Spring Party
                    ShopItem(itemId=17006, price=5, goldPrice=3), # Summer Party
                    ShopItem(itemId=17007, price=5, goldPrice=3), # Autumn Party
                ]
            ),
            ShopCollection(
                collectionId=3001, # Party Games
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=13012, price=10, goldPrice=5), # Pass The Popcorn
                    ShopItem(itemId=13013, price=10, goldPrice=5), # Simone Says
                    ShopItem(itemId=13016, price=10, goldPrice=5), # Rock, Paper, Scissors
                    ShopItem(itemId=13017, price=10, goldPrice=5), # Crazy Cakes
                    ShopItem(itemId=13018, price=10, goldPrice=5), # Two For Tea
                ]
            ),            
        ],
    ),

    NPCShop(
        zone=ZoneConstants.SCHELLYS_HAIR_SALON,
        shopId=4000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SCHELLY,
            position=(290, 470),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_SCHELLY
        ),
        collections=[
            ShopCollection(
                collectionId=4001, # Classic Hair Fronts (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5001, price=10, goldPrice=2), # Simple Style
                    ShopItem(itemId=5002, price=10, goldPrice=2), # Parted Bangs
                    ShopItem(itemId=5003, price=10, goldPrice=2), # Center Swoops
                    ShopItem(itemId=5004, price=10, goldPrice=2), # Sweepy Side Part
                    ShopItem(itemId=5005, price=10, goldPrice=2), # Wind-Swept Bangs
                    ShopItem(itemId=5006, price=10, goldPrice=2), # Sleek and Styled
                    ShopItem(itemId=5007, price=10, goldPrice=2), # Parted Pomp
                    ShopItem(itemId=5008, price=10, goldPrice=2), # Blunt Cut
                    ShopItem(itemId=5009, price=10, goldPrice=2), # Swoopy Side Part
                    ShopItem(itemId=5010, price=10, goldPrice=2), # Angled Bangs
                    ShopItem(itemId=5011, price=10, goldPrice=2), # Pulled Back -- Wavy
                    ShopItem(itemId=5012, price=10, goldPrice=2), # Pulled Back -- Glamorous
                    ShopItem(itemId=5013, price=10, goldPrice=2), # Pulled Back
                    ShopItem(itemId=5014, price=10, goldPrice=2), # Pulled Back -- Wispy
                    ShopItem(itemId=5015, price=10, goldPrice=2), # Sweeping Bangs
                    ShopItem(itemId=5016, price=10, goldPrice=2), # Shy Style
                    ShopItem(itemId=5017, price=10, goldPrice=2), # Tousled Layers
                    ShopItem(itemId=5018, price=10, goldPrice=2), # Tousled Top
                    ShopItem(itemId=5019, price=10, goldPrice=2), # Long Strand Front
                ],
            ),
            ShopCollection(
                collectionId=4003, # Classic Hair Backs (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                    ShopItem(itemId=5501, price=10, goldPrice=2), # Classic Back
                    ShopItem(itemId=5502, price=10, goldPrice=2), # Pixie Braids
                    ShopItem(itemId=5503, price=10, goldPrice=2), # Short Tresses
                    ShopItem(itemId=5504, price=10, goldPrice=2), # Fluffy Short
                    ShopItem(itemId=5505, price=10, goldPrice=2), # Styled Short
                    ShopItem(itemId=5506, price=10, goldPrice=2), # Super Long Braid
                    ShopItem(itemId=5507, price=10, goldPrice=2), # Berry Bouffant
                    ShopItem(itemId=5508, price=10, goldPrice=2), # Pixie Pom Pom
                    ShopItem(itemId=5509, price=10, goldPrice=2), # Big Hair
                    ShopItem(itemId=5510, price=10, goldPrice=2), # Long Tresses
                    ShopItem(itemId=5511, price=10, goldPrice=2), # Styled Long Strands
                    ShopItem(itemId=5512, price=10, goldPrice=2), # Fairy Braids
                    ShopItem(itemId=5513, price=10, goldPrice=2), # Long Tapered Tresses
                    ShopItem(itemId=5514, price=10, goldPrice=2), # Long Braids
                    ShopItem(itemId=5515, price=10, goldPrice=2), # Long and Straight
                    ShopItem(itemId=5516, price=10, goldPrice=2), # Short and Teased
                    ShopItem(itemId=5517, price=10, goldPrice=2), # Long Flowing Locks
                    ShopItem(itemId=5518, price=10, goldPrice=2), # Pixie Pin Curls
                    ShopItem(itemId=5519, price=10, goldPrice=2), # Wind-Swept Bun
                    ShopItem(itemId=5520, price=10, goldPrice=2), # Thick Ponytails
                    ShopItem(itemId=5522, price=10, goldPrice=2), # Puff Ball Back
                ],
            ),
            ShopCollection(
                collectionId=4004, # Stylish Hair Fronts (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5106, price=10, goldPrice=2),
                    ShopItem(itemId=5118, price=10, goldPrice=2), # Plaited Side Part Front
                    ShopItem(itemId=5119, price=10, goldPrice=2), # Sideswept Barrette Front
                    ShopItem(itemId=5121, price=10, goldPrice=2), # Curly Pompadour Front
                    ShopItem(itemId=5122, price=10, goldPrice=2), # Short Waves Front
                    ShopItem(itemId=5123, price=10, goldPrice=2), # Fashion Bob Front
                    ShopItem(itemId=5120, price=10, goldPrice=2), # Beautiful Bangs
                    ShopItem(itemId=5124, price=10, goldPrice=2), # Periwinkle's Hair Front
                    ShopItem(itemId=5125, price=10, goldPrice=2), # Spike's Hair Front
                    ShopItem(itemId=5126, price=10, goldPrice=2), # Long and Curly Front
                    ShopItem(itemId=5027, price=10, goldPrice=2), # Pixie Bangs
                    ShopItem(itemId=5113, price=10, goldPrice=2), # Original Pixie Bangs
                    ShopItem(itemId=5028, price=10, goldPrice=2), # Pixie Pigtails
                    ShopItem(itemId=5115, price=10, goldPrice=2), # Original Pixie Pigtails
                    ShopItem(itemId=5029, price=10, goldPrice=2), # Star Strands Front
                    ShopItem(itemId=5114, price=10, goldPrice=2), # Original Star Strands Front
                    ShopItem(itemId=5030, price=10, goldPrice=2), # Side Swept Bangs
                    ShopItem(itemId=5116, price=10, goldPrice=2), # Original Side Swept Bangs
                    ShopItem(itemId=5032, price=10, goldPrice=2), # Fairy Mary Hair
                    ShopItem(itemId=5075, price=10, goldPrice=2), # Cool Waves
                    ShopItem(itemId=5077, price=10, goldPrice=2), # Classic Pulled Back
                    ShopItem(itemId=5094, price=10, goldPrice=2), # Flowy Pigtails
                    ShopItem(itemId=5081, price=10, goldPrice=2), # Sweet and Stylish Bun
                    ShopItem(itemId=5080, price=10, goldPrice=2), # Puffy Bangs
                    ShopItem(itemId=5093, price=10, goldPrice=2), # Long and Flowing Tieback
                    ShopItem(itemId=5084, price=10, goldPrice=2), # Sleek Part
                    ShopItem(itemId=5107, price=10, goldPrice=2), # Royal Heart Braids
                    ShopItem(itemId=5102, price=10, goldPrice=2), # Lovely Layers
                    ShopItem(itemId=5076, price=10, goldPrice=2), # Fairy Fishtails
                    ShopItem(itemId=5108, price=10, goldPrice=2), # Will 'O Whisp Bangs
                    ShopItem(itemId=5101, price=10, goldPrice=2), # Long Swept Bangs
                    ShopItem(itemId=5089, price=10, goldPrice=2), # Braided Tieback
                    ShopItem(itemId=5109, price=10, goldPrice=2), # Short Twists
                    ShopItem(itemId=5092, price=10, goldPrice=2), # Long and Flitterific Locks
                    ShopItem(itemId=5082, price=10, goldPrice=2), # Stylish Ringlets
                    ShopItem(itemId=5033, price=10, goldPrice=2), # Side-Part Swirly Bob
                    ShopItem(itemId=5034, price=10, goldPrice=2), # Front Swept Bangs
                    ShopItem(itemId=5035, price=10, goldPrice=2), # Totally Tousled Bangs
                    ShopItem(itemId=5036, price=10, goldPrice=2), # Soft Tousled Bangs
                    ShopItem(itemId=5037, price=10, goldPrice=2), # Tight Wave Crop
                    ShopItem(itemId=5062, price=10, goldPrice=2), # Perfect Bob
                    ShopItem(itemId=5064, price=10, goldPrice=2), # Swift and Swooshy Locks
                    ShopItem(itemId=5063, price=10, goldPrice=2), # Long Angled Bangs
                    ShopItem(itemId=5066, price=10, goldPrice=2), # Braid Over Bangs
                    ShopItem(itemId=5078, price=10, goldPrice=2), # Mouse-Ear Buns
                    ShopItem(itemId=5099, price=10, goldPrice=2), # Pulled Back Twists
                    ShopItem(itemId=5090, price=10, goldPrice=2), # Inverted Bob
                    ShopItem(itemId=5087, price=10, goldPrice=2), # Rock and Roll Bangs
                    ShopItem(itemId=5086, price=10, goldPrice=2), # Double Roll Bangs
                    ShopItem(itemId=5100, price=10, goldPrice=2), # Triple Braid Bob
                    ShopItem(itemId=5079, price=10, goldPrice=2), # Topsy-Turvy Short
                    ShopItem(itemId=5105, price=10, goldPrice=2), # Twisty Locks
                    ShopItem(itemId=5088, price=10, goldPrice=2), # Bowtie Bob
                    ShopItem(itemId=5097, price=10, goldPrice=2), # Long and Curly Twisties

                    ShopItem(itemId=5096, price=10, goldPrice=2), # Short and Curly Twisties
                    ShopItem(itemId=5104, price=10, goldPrice=2), # Long Braided Front
                    ShopItem(itemId=5129, price=10, goldPrice=2), # Fishtail Braid Front
                    ShopItem(itemId=5130, price=10, goldPrice=2), # Poufy Pigtails
                    ShopItem(itemId=5131, price=10, goldPrice=2), # Swooped Bangs Front
                    ShopItem(itemId=5132, price=10, goldPrice=2), # Curly Ringlets Front
                    ShopItem(itemId=5133, price=10, goldPrice=2), # Flowery Waves Hair Front
                    
                ],
            ),
                 ShopCollection(
                collectionId=4010, # Classic Hair Fronts (Sparrowmen)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5044, price=10, goldPrice=2), # Side Swept Layers
                    ShopItem(itemId=5045, price=10, goldPrice=2), # Tousled Locks
                    ShopItem(itemId=5046, price=10, goldPrice=2), # Sparrow Man Spike
                    ShopItem(itemId=5047, price=10, goldPrice=2), # Casual Layers
                    ShopItem(itemId=5048, price=10, goldPrice=2), # Long Bang Sweep
                    ShopItem(itemId=5049, price=10, goldPrice=2), # Curl Cut
                    ShopItem(itemId=5050, price=10, goldPrice=2), # Square Tapered Sides
                    ShopItem(itemId=5051, price=10, goldPrice=2), # Layered Side Swipe
                    ShopItem(itemId=5052, price=10, goldPrice=2), # Stylish Center Part
                    ShopItem(itemId=5053, price=10, goldPrice=2), # Long Tapered Sides	
                    ShopItem(itemId=5054, price=10, goldPrice=2), # Short Knots
                    
                ],
            ),
                    
                ShopCollection(
                collectionId=4011, # Classic Hair Backs (Sparrowmen)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5560, price=10, goldPrice=2), # No Back
                    ShopItem(itemId=5547, price=10, goldPrice=2), # Clean-Cut Back
                    ShopItem(itemId=5548, price=10, goldPrice=2), # Square Trim Crop
                    ShopItem(itemId=5549, price=10, goldPrice=2), # Mid-Length Layers
                    ShopItem(itemId=5550, price=10, goldPrice=2), # Close Cropped Cap
                    ShopItem(itemId=5551, price=10, goldPrice=2), # Long-Stranded Back
                    ShopItem(itemId=5552, price=10, goldPrice=2), # Short Wave Trim
                    ShopItem(itemId=5553, price=10, goldPrice=2), # Wide Bob Back
                    ShopItem(itemId=5554, price=10, goldPrice=2), # Triple-V Back
                    ShopItem(itemId=5555, price=10, goldPrice=2), # Short Angled Back
                    ShopItem(itemId=5556, price=10, goldPrice=2), # Narrow Bob Back
                    ShopItem(itemId=5557, price=10, goldPrice=2), # Finger Fringe Trim

                ],
            ),


            ShopCollection(
                collectionId=4012, # Stylish Hair Fronts (Sparrowmen)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5061, price=10, goldPrice=2), # Fly Backwards
                    ShopItem(itemId=5060, price=10, goldPrice=2), # Hurricane Crop
                    ShopItem(itemId=5083, price=10, goldPrice=2), # Buzzed Do
                    ShopItem(itemId=5085, price=10, goldPrice=2), # Light Spikes
                    ShopItem(itemId=5095, price=10, goldPrice=2), # Shaggy Locks
                    ShopItem(itemId=5103, price=10, goldPrice=2), # Carefree Layers
                    ShopItem(itemId=5110, price=10, goldPrice=2), # Adventurer Pony
                    ShopItem(itemId=5098, price=10, goldPrice=2), # Short Twists
                ],
            ),
            ShopCollection(
                collectionId=4013, # Stylish Hair Backs (Sparrowmen)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5562, price=10, goldPrice=2), # Fly Backwards Back
                    ShopItem(itemId=5577, price=10, goldPrice=2), # Light Spikes Back 
                    ShopItem(itemId=5585, price=10, goldPrice=2), # Shaggy Locks Back
                    ShopItem(itemId=5592, price=10, goldPrice=2), # Carefree Layers Back
                    ShopItem(itemId=5595, price=10, goldPrice=2), # Adventurer Straight Back
                    ShopItem(itemId=5588, price=10, goldPrice=2), # Short Twists Back

                ],
            ),


            ShopCollection(
                collectionId=4005, # Stylish Hair Backs (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                    ShopItem(itemId=5602, price=10, goldPrice=2), # Sideswept Barrette Back
                    ShopItem(itemId=5603, price=10, goldPrice=2), # Plaited Side Part Back
                    ShopItem(itemId=5605, price=10, goldPrice=2), # Curly Pompadour Back
                    ShopItem(itemId=5606, price=10, goldPrice=2), # Pom Pom Pigtails
                    ShopItem(itemId=5604, price=10, goldPrice=2), # Beautiful Bangs Back
                    ShopItem(itemId=5607, price=10, goldPrice=2), # Periwinkle's Hair Back
                    ShopItem(itemId=5601, price=10, goldPrice=2), # Spike's Hair Back
                    ShopItem(itemId=5608, price=10, goldPrice=2), # Long and Curly Back
                    ShopItem(itemId=5532, price=10, goldPrice=2), # Sweet Bun
                    ShopItem(itemId=5533, price=10, goldPrice=2), # Girly Curlies
                    ShopItem(itemId=5534, price=10, goldPrice=2), # Pixie Ponytails Back
                    ShopItem(itemId=5535, price=10, goldPrice=2), # Star Strands Back
                    ShopItem(itemId=5599, price=10, goldPrice=2), # Original Star Strands Back
                    ShopItem(itemId=5536, price=10, goldPrice=2), # Pixie Bob Back
                    ShopItem(itemId=5537, price=10, goldPrice=2), # Long Pony
                    ShopItem(itemId=5598, price=10, goldPrice=2), # Original Long Pony
                    ShopItem(itemId=5569, price=10, goldPrice=2), # Cool Waves Back
                    ShopItem(itemId=5570, price=10, goldPrice=2), # Braided-Bun
                    ShopItem(itemId=5574, price=10, goldPrice=2), # Swept Up Hair Back
                    ShopItem(itemId=5573, price=10, goldPrice=2), # Puffy Pigtails
                    ShopItem(itemId=5576, price=10, goldPrice=2), # Twin Buns (Highlights)
                    ShopItem(itemId=5596, price=10, goldPrice=2), # Twin Buns (No Highlights)
                    ShopItem(itemId=5591, price=10, goldPrice=2), # Lovely Layers Back
                    ShopItem(itemId=5593, price=10, goldPrice=2), # Whale of a Fishtail
                    ShopItem(itemId=5582, price=10, goldPrice=2), # High Flowing Ponytail
                    ShopItem(itemId=5584, price=10, goldPrice=2), # Long and Flowing Hair
                    ShopItem(itemId=5590, price=10, goldPrice=2), # Swept Up
                    ShopItem(itemId=5581, price=10, goldPrice=2), # Bunny Tail Bun
                    ShopItem(itemId=5572, price=10, goldPrice=2), # Long Braided Back
                    ShopItem(itemId=5594, price=10, goldPrice=2), # Short Twists Back
                    ShopItem(itemId=5583, price=10, goldPrice=2), # Long and Flitterific Locks Back
                    ShopItem(itemId=5575, price=10, goldPrice=2), # Stylish Ringlets Back
                    ShopItem(itemId=5538, price=10, goldPrice=2), # Swirly Glamour Mane
                    ShopItem(itemId=5539, price=10, goldPrice=2), # Swept-Up Bun
                    ShopItem(itemId=5540, price=10, goldPrice=2), # Totally Rounded Bob
                    ShopItem(itemId=5541, price=10, goldPrice=2), # Soft Layered Locks
                    ShopItem(itemId=5563, price=10, goldPrice=2), # Perfect Bob Back
                    ShopItem(itemId=5565, price=10, goldPrice=2), # Swift and Swooshy Back
                    ShopItem(itemId=5564, price=10, goldPrice=2), # Angled Bang Back
                    ShopItem(itemId=5566, price=10, goldPrice=2), # Braid and Bun
                    ShopItem(itemId=5571, price=10, goldPrice=2), # Draping Locks
                    ShopItem(itemId=5580, price=10, goldPrice=2), # Super Long Ponytail
                    ShopItem(itemId=5589, price=10, goldPrice=2), # Pulled Back Twists Back
                    ShopItem(itemId=5579, price=10, goldPrice=2), # Wavy Silky Tresses
                    ShopItem(itemId=5578, price=10, goldPrice=2), # Rolled and Wavy Back
                    ShopItem(itemId=5587, price=10, goldPrice=2), # Long and Curly Twisties Back

                    ShopItem(itemId=5586, price=10, goldPrice=2), # Short and Curly Twisties Back
                    
                    ShopItem(itemId=5611, price=10, goldPrice=2), # Simple Ponytail
                    ShopItem(itemId=5612, price=10, goldPrice=2), # Curly Ringlets Back
                    ShopItem(itemId=5613, price=10, goldPrice=2), # Flowery Braid
                ],
            ),
            ShopCollection(
                collectionId=4014, # Hair Colors
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14055, price=10, goldPrice=1), # Pepper Black
                    ShopItem(itemId=14073, price=10, goldPrice=1), # Grape Purple
                    ShopItem(itemId=14141, price=10, goldPrice=1), # Thundercloud Gray
                    ShopItem(itemId=14075, price=10, goldPrice=1), # Umber Brown
                    ShopItem(itemId=14074, price=10, goldPrice=1), # Soil Brown
                    ShopItem(itemId=14191, price=10, goldPrice=1), # Vidia Black
                    ShopItem(itemId=14177, price=10, goldPrice=1), # Mud Brown
                    ShopItem(itemId=14076, price=10, goldPrice=1), # Chocolate Brown
                    ShopItem(itemId=14077, price=10, goldPrice=1), # Sepia Brown
                    ShopItem(itemId=14078, price=10, goldPrice=1), # Fawn Brown
                    ShopItem(itemId=14079, price=10, goldPrice=1), # Sienna Brown
                    ShopItem(itemId=14092, price=10, goldPrice=1), # Hawk Brown
                    ShopItem(itemId=14057, price=10, goldPrice=1), # Adobe Brown
                    ShopItem(itemId=14117, price=10, goldPrice=1), # Amethyst Purple
                    ShopItem(itemId=14043, price=10, goldPrice=1), # Violet Purple
                    ShopItem(itemId=14183, price=10, goldPrice=1), # Vidia Purple
                    ShopItem(itemId=14197, price=10, goldPrice=1), # Electric Purple
                    ShopItem(itemId=14080, price=10, goldPrice=1), # Pomegranate Purple
                    ShopItem(itemId=14081, price=10, goldPrice=1), # Crimson Red
                    ShopItem(itemId=14189, price=10, goldPrice=1), # Ladybug Red
                    ShopItem(itemId=14174, price=10, goldPrice=1), # Rosetta Red
                    ShopItem(itemId=14045, price=10, goldPrice=1), # Strawberry Red
                    ShopItem(itemId=14082, price=10, goldPrice=1), # Raspberry Red
                    ShopItem(itemId=14113, price=10, goldPrice=1), # Pale Rose Red
                    ShopItem(itemId=14083, price=10, goldPrice=1), # Cherry Brown
                    ShopItem(itemId=14114, price=10, goldPrice=1), # Foxtail Orange
                    ShopItem(itemId=14013, price=10, goldPrice=1), # Coral Pink
                    ShopItem(itemId=14181, price=10, goldPrice=1), # Cupcake Pink
                    ShopItem(itemId=14008, price=10, goldPrice=1), # Watermelon Pink
                    ShopItem(itemId=14121, price=10, goldPrice=1), # Daisy Pink
                    ShopItem(itemId=14084, price=10, goldPrice=1), # Copper Brown
                    ShopItem(itemId=14046, price=10, goldPrice=1), # Bark Brown
                    ShopItem(itemId=14095, price=10, goldPrice=1), # Sparrow Brown
                    ShopItem(itemId=14028, price=10, goldPrice=1), # Cinnamon Brown
                    ShopItem(itemId=14086, price=10, goldPrice=1), # Nutmeg Brown
                    ShopItem(itemId=14085, price=10, goldPrice=1), # Quail Brown
                    ShopItem(itemId=14087, price=10, goldPrice=1), # Driftwood Brown
                    ShopItem(itemId=14187, price=10, goldPrice=1), # Maple Orange
                    ShopItem(itemId=14171, price=10, goldPrice=1), # Sunrise Yellow
                    ShopItem(itemId=14067, price=10, goldPrice=1), # Chartreuse Green
                    ShopItem(itemId=14048, price=10, goldPrice=1), # Sea Green
                    ShopItem(itemId=14193, price=10, goldPrice=1), # Electric Green
                    ShopItem(itemId=14145, price=10, goldPrice=1), # Tinker Bell Green
                    ShopItem(itemId=14125, price=10, goldPrice=1), # Pine Green
                    ShopItem(itemId=14182, price=10, goldPrice=1), # Twilight Blue
                    ShopItem(itemId=14136, price=10, goldPrice=1), # Peacock Blue
                    ShopItem(itemId=14176, price=10, goldPrice=1), # Silvermist Blue
                    ShopItem(itemId=14180, price=10, goldPrice=1), # Seashell Blue
                    ShopItem(itemId=14195, price=10, goldPrice=1), # Electric Blue
                    ShopItem(itemId=14006, price=10, goldPrice=1), # Havendish Blue
                    ShopItem(itemId=14163, price=10, goldPrice=1), # Tundra Blue
                    ShopItem(itemId=14089, price=10, goldPrice=1), # Seashore Brown
                    ShopItem(itemId=14161, price=10, goldPrice=1), # Buried Treasure Brown
                    ShopItem(itemId=14088, price=10, goldPrice=1), # Fruitwood Brown
                    ShopItem(itemId=14196, price=10, goldPrice=1), # Electric Orange
                    ShopItem(itemId=14178, price=10, goldPrice=1), # Fawn Orange
                    ShopItem(itemId=14179, price=10, goldPrice=1), # Iridessa Yellow
                    ShopItem(itemId=14186, price=10, goldPrice=1), # Honeycomb Yellow
                    ShopItem(itemId=14027, price=10, goldPrice=1), # Corn Cob Yellow
                    ShopItem(itemId=14162, price=10, goldPrice=1), # Sunglow Yellow
                    ShopItem(itemId=14090, price=10, goldPrice=1), # Custard Yellow
                    ShopItem(itemId=14116, price=10, goldPrice=1), # Mushroom White
                    ShopItem(itemId=14109, price=10, goldPrice=1), # Soft Orange
                    ShopItem(itemId=14111, price=10, goldPrice=1), # Sparkling Yellow
                    ShopItem(itemId=14166, price=10, goldPrice=1), # Snow White
                ]
            ),
            ShopCollection(
                collectionId=4015, # Highlights 
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14055, price=10, goldPrice=1, specialType=2), # Pepper Black
                    ShopItem(itemId=14073, price=10, goldPrice=1, specialType=2), # Grape Purple
                    ShopItem(itemId=14141, price=10, goldPrice=1, specialType=2), # Thundercloud Gray
                    ShopItem(itemId=14075, price=10, goldPrice=1, specialType=2), # Umber Brown
                    ShopItem(itemId=14074, price=10, goldPrice=1, specialType=2), # Soil Brown
                    ShopItem(itemId=14191, price=10, goldPrice=1, specialType=2), # Vidia Black
                    ShopItem(itemId=14177, price=10, goldPrice=1, specialType=2), # Mud Brown
                    ShopItem(itemId=14076, price=10, goldPrice=1, specialType=2), # Chocolate Brown
                    ShopItem(itemId=14077, price=10, goldPrice=1, specialType=2), # Sepia Brown
                    ShopItem(itemId=14078, price=10, goldPrice=1, specialType=2), # Fawn Brown
                    ShopItem(itemId=14079, price=10, goldPrice=1, specialType=2), # Sienna Brown
                    ShopItem(itemId=14092, price=10, goldPrice=1, specialType=2), # Hawk Brown
                    ShopItem(itemId=14057, price=10, goldPrice=1, specialType=2), # Adobe Brown
                    ShopItem(itemId=14117, price=10, goldPrice=1, specialType=2), # Amethyst Purple
                    ShopItem(itemId=14043, price=10, goldPrice=1, specialType=2), # Violet Purple
                    ShopItem(itemId=14183, price=10, goldPrice=1, specialType=2), # Vidia Purple
                    ShopItem(itemId=14197, price=10, goldPrice=1, specialType=2), # Electric Purple
                    ShopItem(itemId=14080, price=10, goldPrice=1, specialType=2), # Pomegranate Purple
                    ShopItem(itemId=14081, price=10, goldPrice=1, specialType=2), # Crimson Red
                    ShopItem(itemId=14189, price=10, goldPrice=1, specialType=2), # Ladybug Red
                    ShopItem(itemId=14174, price=10, goldPrice=1, specialType=2), # Rosetta Red
                    ShopItem(itemId=14045, price=10, goldPrice=1, specialType=2), # Strawberry Red
                    ShopItem(itemId=14082, price=10, goldPrice=1, specialType=2), # Raspberry Red
                    ShopItem(itemId=14113, price=10, goldPrice=1, specialType=2), # Pale Rose Red
                    ShopItem(itemId=14083, price=10, goldPrice=1, specialType=2), # Cherry Brown
                    ShopItem(itemId=14114, price=10, goldPrice=1, specialType=2), # Foxtail Orange
                    ShopItem(itemId=14013, price=10, goldPrice=1, specialType=2), # Coral Pink
                    ShopItem(itemId=14181, price=10, goldPrice=1, specialType=2), # Cupcake Pink
                    ShopItem(itemId=14008, price=10, goldPrice=1, specialType=2), # Watermelon Pink
                    ShopItem(itemId=14121, price=10, goldPrice=1, specialType=2), # Daisy Pink
                    ShopItem(itemId=14084, price=10, goldPrice=1, specialType=2), # Copper Brown
                    ShopItem(itemId=14046, price=10, goldPrice=1, specialType=2), # Bark Brown
                    ShopItem(itemId=14095, price=10, goldPrice=1, specialType=2), # Sparrow Brown
                    ShopItem(itemId=14028, price=10, goldPrice=1, specialType=2), # Cinnamon Brown
                    ShopItem(itemId=14086, price=10, goldPrice=1, specialType=2), # Nutmeg Brown
                    ShopItem(itemId=14085, price=10, goldPrice=1, specialType=2), # Quail Brown
                    ShopItem(itemId=14087, price=10, goldPrice=1, specialType=2), # Driftwood Brown
                    ShopItem(itemId=14187, price=10, goldPrice=1, specialType=2), # Maple Orange
                    ShopItem(itemId=14171, price=10, goldPrice=1, specialType=2), # Sunrise Yellow
                    ShopItem(itemId=14067, price=10, goldPrice=1, specialType=2), # Chartreuse Green
                    ShopItem(itemId=14048, price=10, goldPrice=1, specialType=2), # Sea Green
                    ShopItem(itemId=14193, price=10, goldPrice=1, specialType=2), # Electric Green
                    ShopItem(itemId=14145, price=10, goldPrice=1, specialType=2), # Tinker Bell Green
                    ShopItem(itemId=14125, price=10, goldPrice=1, specialType=2), # Pine Green
                    ShopItem(itemId=14182, price=10, goldPrice=1, specialType=2), # Twilight Blue
                    ShopItem(itemId=14136, price=10, goldPrice=1, specialType=2), # Peacock Blue
                    ShopItem(itemId=14176, price=10, goldPrice=1, specialType=2), # Silvermist Blue
                    ShopItem(itemId=14180, price=10, goldPrice=1, specialType=2), # Seashell Blue
                    ShopItem(itemId=14195, price=10, goldPrice=1, specialType=2), # Electric Blue
                    ShopItem(itemId=14006, price=10, goldPrice=1, specialType=2), # Havendish Blue
                    ShopItem(itemId=14163, price=10, goldPrice=1, specialType=2), # Tundra Blue
                    ShopItem(itemId=14089, price=10, goldPrice=1, specialType=2), # Seashore Brown
                    ShopItem(itemId=14161, price=10, goldPrice=1, specialType=2), # Buried Treasure Brown
                    ShopItem(itemId=14088, price=10, goldPrice=1, specialType=2), # Fruitwood Brown
                    ShopItem(itemId=14196, price=10, goldPrice=1, specialType=2), # Electric Orange
                    ShopItem(itemId=14178, price=10, goldPrice=1, specialType=2), # Fawn Orange
                    ShopItem(itemId=14179, price=10, goldPrice=1, specialType=2), # Iridessa Yellow
                    ShopItem(itemId=14186, price=10, goldPrice=1, specialType=2), # Honeycomb Yellow
                    ShopItem(itemId=14027, price=10, goldPrice=1, specialType=2), # Corn Cob Yellow
                    ShopItem(itemId=14162, price=10, goldPrice=1, specialType=2), # Sunglow Yellow
                    ShopItem(itemId=14090, price=10, goldPrice=1, specialType=2), # Custard Yellow
                    ShopItem(itemId=14116, price=10, goldPrice=1, specialType=2), # Mushroom White
                    ShopItem(itemId=14109, price=10, goldPrice=1, specialType=2), # Soft Orange
                    ShopItem(itemId=14111, price=10, goldPrice=1, specialType=2), # Sparkling Yellow
                    ShopItem(itemId=14166, price=10, goldPrice=1, specialType=2), # Snow White
                ]
            )
        ],
    ),

    NPCShop(
        zone=ZoneConstants.BECKS_ANIMAL_NURSERY,
        shopId=5000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BECK,
            position=(387, 440),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BECK
        ),
        collections=[
            ShopCollection(
                collectionId=5001, # Fireflies
                currencyId=FairiesConstants.HONEYCOMBS,
                items=[
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=17, color2=60, itemType="Firefly"), # Tendershoot Green Firefly
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=11, color2=60, itemType="Firefly"), # Marigold Yellow Firefly	
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=64, color2=60, itemType="Firefly"), # Emerald Green Firefly
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=54, color2=130, itemType="Firefly"), # Peony Pink Firefly
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=32, color2=149, itemType="Firefly"), # Mulberry Purple Firefly	
                    ShopItem(itemId=73000, price=80, goldPrice=25, color1=142, color2=72, itemType="Firefly"), # Bumble Bee Yellow Firefly 
                ]
            ),
            ShopCollection(
                collectionId=5002, # Ladybugs
                currencyId=FairiesConstants.BUTTERCUP_PETALS,
                items=[
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=45, color2=55, itemType="Ladybug"), # Strawberry Red Ladybug	
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=142, color2=55, itemType="Ladybug"), # Bumble Bee Yellow Ladybug
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=124, color2=55, itemType="Ladybug"), # Forget-Me-Not Blue Ladybug
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=65, color2=118, itemType="Ladybug"), # Summer Green Ladybug
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=11, color2=125, itemType="Ladybug"), # Marigold Yellow Ladybug
                    ShopItem(itemId=73001, price=100, goldPrice=30, color1=8, color2=139, itemType="Ladybug"), # Watermelon Pink Ladybug

                ]
            ),   
            ShopCollection(
                collectionId=5003, # Baby Hummingbirds
                currencyId=FairiesConstants.BLUEBERRIES,
                items=[
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=82, color2=128, itemType="Hummingbird"), # Raspberry Red Hummingbird
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=64, color2=128, itemType="Hummingbird"), # Emerald Green Hummingbird
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=50, color2=128, itemType="Hummingbird"), # Cornflower Blue Hummingbird
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=50, color2=151, itemType="Hummingbird"), # Cornflower Blue Hummingbird with Yellow Trim
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=34, color2=111, itemType="Hummingbird"), # Primrose Pink Hummingbird
                    ShopItem(itemId=73002, price=110, goldPrice=35, color1=72, color2=153, itemType="Hummingbird"), # Mauve Purple Hummingbird
                ]
            ),
            ShopCollection(
                collectionId=5004, # Dragonflies
                currencyId=FairiesConstants.MEADOW_GRASS,
                items=[
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=81, color2=141, itemType="Dragonfly"), # Crimson Red Dragonfly
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=137, color2=141, itemType="Dragonfly"), # Lemon Yellow Dragonfly
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=145, color2=141, itemType="Dragonfly"), # Tinker Bell Green Dragonfly
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=144, color2=32, itemType="Dragonfly"), # Petal Pink Dragonfly
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=128, color2=41, itemType="Dragonfly"), # Carnation White Dragonfly	
                    ShopItem(itemId=73003, price=50, goldPrice=20, color1=133, color2=48, itemType="Dragonfly"), # Marina Blue Dragonfly

                ]
            ),
            ShopCollection(
                collectionId=5005, # Bees
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=142, color2=73, itemType="Bee"), # Bumble Bee Yellow Bee
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=10, color2=82, itemType="Bee"), # Cantaloupe Orange Bee
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=28, color2=56, itemType="Bee"), # Cinnamon Brown Bee
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=159, color2=40, itemType="Bee"), # Tea Green Bee
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=156, color2=73, itemType="Bee"), # Friendship Pink Bee
                    ShopItem(itemId=73004, price=55, goldPrice=23, color1=6, color2=118, itemType="Bee"), # Havendish Blue Bee


                ]
            ),
            ShopCollection(
                collectionId=5007, # Butterflies
                currencyId=FairiesConstants.LILY_PETALS,
                items=[
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=82, color2=189, itemType="Butterfly"), # Raspberry Red Butterfly
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=288, color2=200, itemType="Butterfly"), # Sparkle Pink Butterfly
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=11, color2=228, itemType="Butterfly"), # Marigold Yellow Butterfly	
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=143, color2=261, itemType="Butterfly"), # June Bug Green Butterfly
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=50, color2=185, itemType="Butterfly"), # Cornflower Blue Butterfly
                    ShopItem(itemId=73006, price=120, goldPrice=60, color1=278, color2=279, itemType="Butterfly"), # Aster Purple Butterfly
                ],
            ),
        ],
    ),
        

    NPCShop(
        zone=ZoneConstants.NEVILLES_NEW_HOMES,
        shopId=6000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.NEVILLE,
            position=(785, 458),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_NEVILLE,
            gender=2
        ),
        collections=[
            ShopCollection(
                collectionId=6000, # Small Homes
                currencyId=FairiesConstants.LILY_PETALS,
                items=[
                    ShopItem(itemId=29001, price=40, goldPrice=20), # Knothole Nest
                    ShopItem(itemId=29002, price=40, goldPrice=20), # Blossom Bungalow
                    ShopItem(itemId=29003, price=40, goldPrice=20), # Sunflower Studio
                    ShopItem(itemId=29004, price=40, goldPrice=20), # Lotus Loft
                    ShopItem(itemId=29005, price=40, goldPrice=20), # Mosswall Cottage
                ],
            ),
            ShopCollection(
                collectionId=6001, # Large Homes
                currencyId=FairiesConstants.LILY_PETALS,
                items=[
                    ShopItem(itemId=29026, price=160, goldPrice=80), # Snowflake Estate
                    ShopItem(itemId=29021, price=110, goldPrice=55), # Hollow Tree Heights
                    ShopItem(itemId=29022, price=110, goldPrice=55), # Petalstem Palace
                    ShopItem(itemId=29023, price=100, goldPrice=50), # Sunglow Spire
                    ShopItem(itemId=29024, price=130, goldPrice=80), # Streamside Suite
                    ShopItem(itemId=29025, price=100, goldPrice=50), # Greenleaf Tower
                ],
            ),
            ShopCollection(
                collectionId=6003, # Platforms
                currencyId=FairiesConstants.LILY_PETALS,
                items=[
                    ShopItem(itemId=6607, price=20, goldPrice=8, color1=77, color2=77), #  Sepia Brown Fallen Wood Flooring
                    ShopItem(itemId=6614, price=20, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Floor
                    ShopItem(itemId=6643, price=20, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Loft
                    ShopItem(itemId=6618, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Wall
                    ShopItem(itemId=6619, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Back


                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.GARDEN_SUPPLY,
        shopId=7000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BROOK,
            position=(418, 453),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BROOK
        ),
        collections=[
            ShopCollection(
                collectionId=119, # Basic Seeds
                items=[
                    ShopItem(itemId=89002, goldPrice=1), # Dulcie's Cookie Seeds
                    ShopItem(itemId=89017, goldPrice=1), # Dulcie's Truffle Seeds
                    ShopItem(itemId=89001, goldPrice=1), # Colorful Sweet Seeds
                    ShopItem(itemId=89023, goldPrice=1), # Rainbow Sweet Seeds
                    ShopItem(itemId=89018, goldPrice=1), # Sweet Trails Seeds
                    ShopItem(itemId=89031, goldPrice=1), # Summer Sweets Seeds
                ],
            ),
            ShopCollection(
                collectionId=118, # Special Edition Seeds
                items=[
                    ShopItem(itemId=89009, goldPrice=1), # Garden Premier Seeds
                    ShopItem(itemId=89022, goldPrice=1), # Autumn Breeze Seeds
                    ShopItem(itemId=89021, goldPrice=1), # Winter Wardrobe Seeds
                    ShopItem(itemId=89030, goldPrice=1), # Spring Style Seeds
                    ShopItem(itemId=89038, goldPrice=1), # Summer Chic Seeds
                ],
            ),
            ShopCollection(
                collectionId=132, # Summer 2012 Seeds
                items=[
                    ShopItem(itemId=89004, goldPrice=1), # Fancy Flower Seeds
                    ShopItem(itemId=89000, goldPrice=1), # Rainbow Dye Seeds
                    ShopItem(itemId=89006, goldPrice=1), # Teatime Seeds
                    ShopItem(itemId=89008, goldPrice=1), # Little Gardener Seeds
                    ShopItem(itemId=89005, goldPrice=1), # To-Fly-For Top Seeds
                    ShopItem(itemId=89007, goldPrice=1), # Skirt or Slacks Seeds
                    ShopItem(itemId=89003, goldPrice=1), # Stylish Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=131, # Fall 2012 Seeds
                items=[
                    ShopItem(itemId=89014, goldPrice=1), # Autumn Masquerade Dye Seeds
                    ShopItem(itemId=89019, goldPrice=1), # Autumn Harvest Seeds
                ],
            ),
            ShopCollection(
                collectionId=130, # Winter 2012 Seeds
                items=[
                    ShopItem(itemId=89012, goldPrice=1), # Chilly Plants Seeds
                    ShopItem(itemId=89013, goldPrice=1), # Winter Wonderland Dye Seeds
                    ShopItem(itemId=89016, goldPrice=1), # Tink's Decorating Seeds
                    ShopItem(itemId=89010, goldPrice=1), # Festive Ornament Seeds
                    ShopItem(itemId=89011, goldPrice=1), # Flitterific Tops Seeds
                    ShopItem(itemId=89015, goldPrice=1), # Flitterific Skirt or Slacks Seeds
                    ShopItem(itemId=89020, goldPrice=1), # Flitterific Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=129, # Spring 2013 Seeds
                items=[
                    ShopItem(itemId=89029, goldPrice=1), # Springtime Flower Seeds
                    ShopItem(itemId=89028, goldPrice=1), # Never Dove Egg Dye Seeds
                    ShopItem(itemId=89027, goldPrice=1), # Clover Comfort Seeds
                    ShopItem(itemId=89024, goldPrice=1), # Springtime Top Seeds
                    ShopItem(itemId=89025, goldPrice=1), # Springtime Skirt or Slacks Seeds
                    ShopItem(itemId=89026, goldPrice=1), # Springtime Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=120, # Summer 2013 Seeds
                items=[
                    ShopItem(itemId=89033, goldPrice=1), # Sprightly Sprouts Seeds
                    ShopItem(itemId=89032, goldPrice=1), # Midsummer Dye Seeds
                    ShopItem(itemId=89035, goldPrice=1), # Blooming Benches Seeds
                    ShopItem(itemId=89036, goldPrice=1), # Tropical Tops Seeds
                    ShopItem(itemId=89037, goldPrice=1), # Sunny Skirt or Slacks Seeds
                    ShopItem(itemId=89034, goldPrice=1), # Summertime Shoes Seeds
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.HARMONYS_SWEET_SHOP,
        shopId=8000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.HARMONY,
            position=(417, 455),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_HARMONY,
        ),
        collections=[
            ShopCollection(
                collectionId=146, # Scrumptious Cookies
                items=[
                    ShopItem(itemId=22502, goldPrice=1), # Sunflower Cookie
                    ShopItem(itemId=22503, goldPrice=1), # Honey Cookie
                    ShopItem(itemId=22504, goldPrice=1), # Raspberry Cookie
                    ShopItem(itemId=22505, goldPrice=1), # Blueberry Cookie
                    ShopItem(itemId=22506, goldPrice=1), # Honey Maple Cookie
                    ShopItem(itemId=22507, goldPrice=1), # Truffle Cookie
                    ShopItem(itemId=22508, goldPrice=1), # Honey Truffle Cookie
                    ShopItem(itemId=22509, goldPrice=1), # Raspberry Truffle Cookie
                    ShopItem(itemId=22510, goldPrice=1), # Blueberry Truffle Cookie
                    ShopItem(itemId=22532, goldPrice=1), # Sunflower Double Truffle Cookie
                    ShopItem(itemId=22533, goldPrice=1), # Honey Double Truffle Cookie
                    ShopItem(itemId=22534, goldPrice=1), # Raspberry Double Truffle Cookie
                    ShopItem(itemId=22535, goldPrice=1), # Blueberry Double Truffle Cookie
                    ShopItem(itemId=22542, goldPrice=1), # Honey Maple Double Truffle Cookie
                ],
            ),
            ShopCollection(
                collectionId=61, # Delectable Cupcakes
                items=[
                    ShopItem(itemId=22551, goldPrice=1), # Sunflower Cupcake
                    ShopItem(itemId=22552, goldPrice=1), # Honey Cupcake
                    ShopItem(itemId=22553, goldPrice=1), # Raspberry Cupcake
                ],
            ),
            ShopCollection(
                collectionId=147, # Color Changing Silly Sweets
                items=[
                    ShopItem(itemId=22520, goldPrice=1), # Red
                    ShopItem(itemId=22521, goldPrice=1), # Orange
                    ShopItem(itemId=22522, goldPrice=1), # Yellow
                    ShopItem(itemId=22518, goldPrice=1), # Green
                    ShopItem(itemId=22516, goldPrice=1), # Blue
                    ShopItem(itemId=22519, goldPrice=1), # Purple
                    ShopItem(itemId=22514, goldPrice=1), # Pink
                    ShopItem(itemId=22515, goldPrice=1), # White
                    ShopItem(itemId=22517, goldPrice=1), # Gray
                    ShopItem(itemId=22523, goldPrice=1), # Cool Rainbow
                    ShopItem(itemId=22524, goldPrice=1), # Bright Rainbow
                    ShopItem(itemId=22525, goldPrice=1), # Invisible
                ],
            ),
            ShopCollection(
                collectionId=38, # Aura Silly Sweets
                items=[
                    ShopItem(itemId=22527, goldPrice=1), # Rainbow Glow
                    ShopItem(itemId=22526, goldPrice=1), # Bubble
                    ShopItem(itemId=22543, goldPrice=1), # Bubble Trail
                    ShopItem(itemId=22530, goldPrice=1), # Tornado
                    ShopItem(itemId=22528, goldPrice=1), # Dizzy
                    ShopItem(itemId=22529, goldPrice=1), # Bright Idea
                    ShopItem(itemId=22539, goldPrice=1), # Puffy Cloud
                    ShopItem(itemId=22536, goldPrice=1), # Fairy Cupcake
                    ShopItem(itemId=22537, goldPrice=1), # Fireworks
                    ShopItem(itemId=22538, goldPrice=1), # Snowglobe
                    ShopItem(itemId=22540, goldPrice=1), # Ice Cube
                    ShopItem(itemId=22541, goldPrice=1), # Snowman
                    ShopItem(itemId=22544, goldPrice=1), # Flower Trail
                    ShopItem(itemId=22545, goldPrice=1), # Snowflake Trail
                    ShopItem(itemId=22546, goldPrice=1), # Raining Cloud
                    ShopItem(itemId=22547, goldPrice=1), # Snowing Cloud
                    ShopItem(itemId=22548, goldPrice=1), # Shrinking
                    ShopItem(itemId=22549, goldPrice=1), # Growing
                    ShopItem(itemId=22550, goldPrice=1), # Flip-Flop
                ],
            ),
            ShopCollection(
                collectionId=21, # Wing Changing Silly Sweets
                items=[
                    ShopItem(itemId=22571, goldPrice=1), # Sparkly Wings
                    ShopItem(itemId=22572, goldPrice=1), # Pepper Black Wings
                    ShopItem(itemId=22573, goldPrice=1), # Bluejay Blue Wings
                    ShopItem(itemId=22574, goldPrice=1), # Electric Blue Wings
                    ShopItem(itemId=22575, goldPrice=1), # Friendship Pink Wings
                    ShopItem(itemId=22576, goldPrice=1), # Electric Pink Wings
                    ShopItem(itemId=22577, goldPrice=1), # Electric Orange Wings
                    ShopItem(itemId=22578, goldPrice=1), # Electric Purple Wings
                    ShopItem(itemId=22579, goldPrice=1), # Lemon Yellow Wings
                    ShopItem(itemId=22580, goldPrice=1), # Rosetta Red Wings
                    ShopItem(itemId=22581, goldPrice=1), # Electric Green Wings
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.SPIKES_SWEETS,
        shopId=8001,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SPIKE,
            position=(417, 355),
            famousFairyId=45,
        ),
        collections=[
            ShopCollection(
                collectionId=4, # Holiday Treats
                items=[
                    ShopItem(itemId=22554, goldPrice=1), # Jack o' Lantern Cookie
                    ShopItem(itemId=22531, goldPrice=1), # Tea Scone
                    ShopItem(itemId=22513, goldPrice=1), # Clover Cookie
                    ShopItem(itemId=22512, goldPrice=1), # Pumpkin Cake
                    ShopItem(itemId=22511, goldPrice=1), # S'more
                    ShopItem(itemId=22587, goldPrice=1), # Magic Tea Cake
                    ShopItem(itemId=22588, goldPrice=1), # Magic Tea Drink

                ],
            ),
            ShopCollection(
                collectionId=57, # Baby Animal Sweets
                items=[
                    ShopItem(itemId=22582, goldPrice=1), # Baby Bunny Silly Sweet
                    ShopItem(itemId=22583, goldPrice=1), # Baby Chipmunk Silly Sweet
                    ShopItem(itemId=22584, goldPrice=1), # Baby Owl Silly Sweet
                    ShopItem(itemId=22585, goldPrice=1), # Baby Kitten Silly Sweet

                ],
            ),
            ShopCollection(
                collectionId=157, # Deluxe Silly Sweets
                items=[
                    ShopItem(itemId=22555, goldPrice=1), # Blackberry Silly Sweet
                    ShopItem(itemId=22556, goldPrice=1), # Deluxe Silly Sweet
                    ShopItem(itemId=22557, goldPrice=1), # Ice Cream Silly Sweet
                    ShopItem(itemId=22570, goldPrice=1), # Candy Corn Silly Sweet
                    ShopItem(itemId=22586, goldPrice=1), # Bunny Bubble Silly Sweet
                ],
            ),
        ],
    ),



    NPCShop(
        zone=ZoneConstants.PRISMS_PIXIE_SPA,
        shopId=9000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.PRISM,
            position=(290, 460),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_PRISM,
        ),
        collections=[
            ShopCollection(
                collectionId=4017, # Wings
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=6001, price=25, goldPrice=5),
                    ShopItem(itemId=6002, price=25, goldPrice=5),
                    ShopItem(itemId=6003, price=25, goldPrice=5),
                    ShopItem(itemId=6004, price=25, goldPrice=5),
                    ShopItem(itemId=6005, price=25, goldPrice=5),
                    ShopItem(itemId=6006, price=25, goldPrice=5),
                ],
            ),
            ShopCollection(
                collectionId=4018, # Expressions
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    # Fairies
                    ShopItem(itemId=4501, price=10, goldPrice=2),
                    ShopItem(itemId=4502, price=10, goldPrice=2),
                    ShopItem(itemId=4503, price=10, goldPrice=2),
                    ShopItem(itemId=4504, price=10, goldPrice=2),
                    ShopItem(itemId=4505, price=10, goldPrice=2),
                    ShopItem(itemId=4506, price=10, goldPrice=2),
                    ShopItem(itemId=4507, price=10, goldPrice=2),
                    ShopItem(itemId=4508, price=10, goldPrice=2),
                    ShopItem(itemId=4509, price=10, goldPrice=2),
                    ShopItem(itemId=4510, price=10, goldPrice=2),
                    ShopItem(itemId=4511, price=10, goldPrice=2),
                    ShopItem(itemId=4512, price=10, goldPrice=2),
                    ShopItem(itemId=4513, price=10, goldPrice=2),
                    ShopItem(itemId=4514, price=10, goldPrice=2),
                    ShopItem(itemId=4515, price=10, goldPrice=2),
                    ShopItem(itemId=4516, price=10, goldPrice=2),
                    ShopItem(itemId=4517, price=10, goldPrice=2),
                    ShopItem(itemId=4518, price=10, goldPrice=2),
                    ShopItem(itemId=4519, price=10, goldPrice=2),
                    ShopItem(itemId=4520, price=10, goldPrice=2),
                    ShopItem(itemId=4521, price=10, goldPrice=2),
                    ShopItem(itemId=4522, price=10, goldPrice=2),
                    ShopItem(itemId=4523, price=10, goldPrice=2),
                    
                ],
            ),
 ShopCollection(
                collectionId=4018, # Expressions
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    # Sparrowmen
                    ShopItem(itemId=4535, price=10, goldPrice=2), 
                    ShopItem(itemId=4536, price=10, goldPrice=2), 
                    ShopItem(itemId=4537, price=10, goldPrice=2),
                    ShopItem(itemId=4538, price=10, goldPrice=2),
                    ShopItem(itemId=4539, price=10, goldPrice=2),
                    ShopItem(itemId=4540, price=10, goldPrice=2),
                    ShopItem(itemId=4541, price=10, goldPrice=2),
                    ShopItem(itemId=4542, price=10, goldPrice=2),                   
                    ShopItem(itemId=4543, price=10, goldPrice=2),
                    ShopItem(itemId=4544, price=10, goldPrice=2),
                ],
            ),
            ShopCollection(
                collectionId=4019, # Skin Colors
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14091, price=5, goldPrice=1),
                    ShopItem(itemId=14092, price=5, goldPrice=1),
                    ShopItem(itemId=14093, price=5, goldPrice=1),
                    ShopItem(itemId=14094, price=5, goldPrice=1),
                    ShopItem(itemId=14095, price=5, goldPrice=1),
                    ShopItem(itemId=14096, price=5, goldPrice=1),
                    ShopItem(itemId=14097, price=5, goldPrice=1),
                    ShopItem(itemId=14098, price=5, goldPrice=1),
                    ShopItem(itemId=14099, price=5, goldPrice=1),
                    ShopItem(itemId=14100, price=5, goldPrice=1),
                    ShopItem(itemId=14101, price=5, goldPrice=1),
                    ShopItem(itemId=14102, price=5, goldPrice=1),
                    ShopItem(itemId=14103, price=5, goldPrice=1),
                    ShopItem(itemId=14104, price=5, goldPrice=1),
                    ShopItem(itemId=14105, price=5, goldPrice=1),
                    ShopItem(itemId=14106, price=5, goldPrice=1),
                    ShopItem(itemId=14107, price=5, goldPrice=1),
                    ShopItem(itemId=14108, price=5, goldPrice=1),
                    ShopItem(itemId=14028, price=5, goldPrice=1),
                    ShopItem(itemId=14057, price=5, goldPrice=1),
                    ShopItem(itemId=14160, price=5, goldPrice=1),
                    ShopItem(itemId=14007, price=5, goldPrice=1),
                ],
            ),
            ShopCollection(
                collectionId=4020, # Eye Colors
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14055, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14056, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14057, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14058, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14059, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14060, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14061, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14062, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14063, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14064, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14065, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14066, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14067, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14068, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14069, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14070, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14071, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14072, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14136, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14221, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14172, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14032, price=5, goldPrice=1, specialType=4),
                ],
            )
        ],
    ),

]

SHOPS_BY_ZONE = {shop.zone: shop for shop in SHOPS}

for shop in SHOPS:
    shop.collectionsById = {collection.collectionId: collection for collection in shop.collections}

def getShopByZone(zone: int) -> NPCShop | None:
    return SHOPS_BY_ZONE.get(zone)

def getShopItemByIndex(shop: NPCShop, collectionId: int, itemIndex: int) -> ShopItem | None:
    collection = shop.collectionsById.get(collectionId)

    if not collection:
        return None

    if 0 <= itemIndex < len(collection.items):
        return collection.items[itemIndex]

    return None

def getShopOutfitByOutfitId(shop: NPCShop, collectionId: int, outfitId: int) -> ShopOutfit | None:
    collection = shop.collectionsById.get(collectionId)

    if not collection:
        return None

    return next((outfit for outfit in collection.outfits if outfit.outfitId == outfitId), None)
