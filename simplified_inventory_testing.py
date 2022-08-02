import random

from player_and_inventory_testing import leather_armor, buckler, leather_boots, canvas_cloak, ring_of_regeneration, \
    ring_of_protection, scroll_of_town_portal, short_sword, short_axe, quantum_sword, broad_sword, minor_healing_potion, \
    major_healing_potion, super_healing_potion

pack = {
    'Weapons': [short_sword, short_axe, quantum_sword, broad_sword],
    'Healing Potions': [minor_healing_potion, major_healing_potion, super_healing_potion],
    'Armor': [leather_armor],
    'Shields': [buckler],
    'Boots': [leather_boots],
    'Cloaks': [canvas_cloak],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal]
}
loot_dict = {
    'Weapons': [short_sword, short_axe, quantum_sword, broad_sword],
    'Healing Potions': [minor_healing_potion, major_healing_potion, super_healing_potion],
    'Armor': [leather_armor],
    'Shields': [buckler],
    'Boots': [leather_boots],
    'Cloaks': [canvas_cloak],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal]
}
# value, key = random.choice(list(loot_dict.items()))
# rndm_item = random.choice(loot_dict[value])
# (pack[rndm_item.item_type]).append(rndm_item)
# (pack[rndm_item.item_type]).pop(rndm_item)
# print(key)

# print(rndm_item)
# print(rndm_item.item_type)

# key = random.choice(list(loot_dict.keys()))  # get random key
# key = random.randrange(len(loot_dict.keys()))
# rndm_item_index = random.randrange(len(loot_dict[key]))  # get random index depending on length of dict keys
# rndm_item = loot_dict[key][rndm_item_index]  # item is grabbed from loot dict based on rndm key and rndm item index!
# print(rndm_item)
# pack[rndm_item.item_type].append(rndm_item)
# print(pack)
# del pack[key][rndm_item_index]
# print(rndm_item)

# del loot_dict[key][rndm_item_index]
print(pack)
# print(value)
# print(key)
# key = random.choice(list(loot_dict.keys()))
# rndm_item_index = random.randrange(len(loot_dict[key]))
# rndm_item = loot_dict[key][rndm_item_index]

# Get types of items which player have
# Get types of items which player have
available = []
for i in pack.keys():
    if len(pack[i]) > 0:
        available.append(i)
t = random.choice(available)  # Get an item type you want to "steal" (i.e. Weapon, Armor, etc.)
print(t)
if len(available) > 0:
    if len(pack[t]) > 0:  # If the player has an item of type "t",
        # print(t, i)
        pack[t].pop(random.randint(0, len(pack[t]) - 1))  # remove it
else:
    print()
print(pack)
# code for explicitly removing item from list within dictionary!!!!!!!!!!!!!!!!
sub_item_type = short_axe.item_type
sub_item = short_axe
(pack[sub_item_type]).remove(sub_item)
# code to index weapons into dictionary
(pack[sub_item_type]).sort(key=lambda x: x.damage_bonus)

stuff = {}
for item in (pack[sub_item_type]):
    # if getattr(item, item.item_type) == "weapon":
    stuff[item] = (pack[sub_item_type]).index(item)
for key, value in stuff.items():
    print(value + 1, ':', key)

print(pack)