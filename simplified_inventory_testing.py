import random

from player_module_old import leather_armor, buckler, leather_boots, canvas_cloak, ring_of_regeneration, \
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
        #stolen_item = random.randint(0, len(pack[t]) - 1)
        #print(stolen_item)
        #pack[t].pop(stolen_item)
        stolen_item = (pack[t].pop(random.randint(0, len(pack[t]) - 1)))  # remove it
        print(stolen_item)
else:
    print()
print(pack)

#This randomly chooses a type and then randomly chooses an item of that type -
#which means that the canvas cloak is more likely to be stolen than the broad sword. –
#Martin Bonner supports Monica
# 23 hours ago
#Better to add an (item_type, item_index) tuple to available and then delete *that item*.
#(The OP might want to add some items multiple times if they are particularly easy/attractive to steal.)
# code for explicitly removing item from list within dictionary!!!!!!!!!!!!!!!!
#sub_item_type = short_axe.item_type
#sub_item = short_axe
#(pack[sub_item_type]).remove(sub_item)
# syntax for indexing list within dictionary !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#a = (pack['Weapons'])[2]

#print(a)

'''
# code to index weapons into dictionary
    (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus)
    stuff = {}
    for item in (self.pack['Weapons']):
        stuff[item] = (pack['Weapons']).index(item)
    for key, value in stuff.items():
        print(value + 1, ':', key)
# *******************************************************************      
    old_weapon = self.wielded_weapon
    print(f"Your current wielded weapon: "
          f"{self.wielded_weapon}\n"
          f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
          f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
    try:
        new_weapon = int(input(f"Enter the number of the weapon from your pack you wish to wield: "))
        new_weapon = new_weapon - 1

        #a = (pack['Weapons'])[2]
        self.wielded_weapon = (self.pack['Weapons'])[new_weapon]
        # self.wielded_weapon = self.pack['Weapons']new_weapon  # find syntax
    except (IndexError, ValueError):
        print("Invalid entry..")
        sleep(1)
        break
    print(f"You remove the {(self.pack['Weapons'])[new_weapon]} from your pack and are now wielding it.\n"
          f"You place the {old_weapon} in your pack.")

    (self.pack['Weapons']).remove(new_weapon)
    #self.pack.pop(new_weapon)
    (self.pack['Weapons']).append(old_weapon)
    (self.pack[sub_item_type]).sort(key=lambda x: x.damage_bonus)
    #self.pack.append(old_weapon)
    #self.pack.sort(key=lambda x: x.damage_bonus)
    sleep(1)
    if not len(self.pack['Weapons']):
        print("Your weapons inventory is now empty.")
        sleep(1)
        return
'''


print(pack)