import random

from player_and_inventory_testing import leather_armor, buckler, leather_boots, canvas_cloak, ring_of_regeneration, \
    ring_of_protection, scroll_of_town_portal, short_sword, short_axe, quantum_sword, broad_sword, minor_healing_potion, \
    major_healing_potion, super_healing_potion

pack = {
    'Weapons': [],
    'Healing Potions': [],
    'Armor': [],
    'Shields': [],
    'Boots': [],
    'Cloaks': [],
    'Rings of Regeneration': [],
    'Rings of Protection': [],
    'Town Portal Implements': []
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
#value, key = random.choice(list(loot_dict.items()))
#rndm_item = random.choice(loot_dict[value])
#(pack[rndm_item.item_type]).append(rndm_item)
#(pack[rndm_item.item_type]).pop(rndm_item)
#print(key)

#print(rndm_item)
#print(rndm_item.item_type)
key = random.choice(list(loot_dict.keys()))  # get random key
rndm_item_index = random.randrange(len(loot_dict[key]))  # get random index depending on length of dict keys
rndm_item = loot_dict[key][rndm_item_index]  # item is grabbed from loot dict based on rndm key and rndm item index!
print(rndm_item)
pack[rndm_item.item_type].append(rndm_item)
print(pack)
del pack[key][rndm_item_index]
print(rndm_item)

#del loot_dict[key][rndm_item_index]
print(pack)
#print(value)
#print(key)
key = random.choice(list(loot_dict.keys()))
rndm_item_index = random.randrange(len(loot_dict[key]))
rndm_item = loot_dict[key][rndm_item_index]