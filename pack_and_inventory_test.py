import random

# from main import player_1, monster_dict
from player_class_test import Weapon, Player, short_sword, short_axe, quantum_sword, broad_sword, minor_healing_potion, \
    Counter, time, buckler, leather_armor, leather_boots, canvas_cloak, scroll_of_town_portal, ring_of_regeneration, \
    ring_of_protection, major_healing_potion, super_healing_potion, sleep
player_1 = Player()
# ****************************************************************************************************************************

pack = {
    'Weapons': [],
    # 'Weapons': [short_sword, short_axe, quantum_sword, broad_sword],
    #'Healing Potions': [minor_healing_potion, major_healing_potion, super_healing_potion],
    'Healing Potions': [],
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


# get rid of defaults like short sword, leather armor, boots and canvas cloak as custom class instances...
# just have them exist as default descriptors... create custom armor, boots and cloaks like splint, plate, and elven

def item_type_inventory(item_type):
    # print(*pack[item_type])  # print list without any brackets or commas. 'pack' is the dictionary, 'weapon' is the key for the list of weapons
    (pack[item_type]).sort(key=lambda x: x.name)  # sort the weapon list by damage_bonus, ascending
    stuff_dict = Counter(item.name for item in
                         pack[item_type])  # create a dictionary of the sorted list, which is within the pack dictionary
    total_number_of_items = len(pack[item_type])
    if total_number_of_items:
        print(f"{item_type}")
        # print(f"You currently have {total_number_of_items} items in your {item_type} inventory:")
        for key, value in stuff_dict.items():  # loop through the key and values
            print(key, ':    ', value, sep='')
            return True
            # print(key, 's', ':    ', value, sep='')  # print each key and value. add an 's' and a colon, without any spaces
    # total_number_of_items = len(pack[item_type])
    # print(f"You have {total_number_of_items} items in your {item_type} pack.")
    else:
        print(f"You currently have no {item_type} in your inventory.")
        return False


# list_of_values = list(pack.values())

# FIND RANDOM LOOT LOGIC:
item_type_key_lst = ['Weapons', 'Healing Potions', 'Armor', 'Shields', 'Boots', 'Cloaks', 'Rings of Regeneration',
                     'Rings of Protection', 'Town Portal Implements']
found_item = random.choice(loot_dict[random.choice(item_type_key_lst)])

print(f"You have found a {found_item.name}")

if found_item.item_type != 'Healing Potions' and found_item not in pack[found_item.item_type]:
    (pack[found_item.item_type]).append(found_item)
    (pack[found_item.item_type]).sort(key=lambda x: x.name)
    stuff_dict = Counter(item.name for item in pack[found_item.item_type])
    for key, value in stuff_dict.items():
        print(key, 's', ':    ', value, sep='')
    number_of_items = len(pack[found_item.item_type])
    print(f"You now have {number_of_items} items in your {found_item.item_type} inventory.")
elif found_item.item_type == 'Healing Potions':
    (pack[found_item.item_type]).append(found_item)
    (pack[found_item.item_type]).sort(key=lambda x: x.name)
    stuff_dict = Counter(item.name for item in pack[found_item.item_type])
    for key, value in stuff_dict.items():
        print(key, 's', ':    ', value, sep='')
    number_of_items = len(pack[found_item.item_type])
    print(f"You now have {number_of_items} items in your {found_item.item_type} inventory.")
else:
    print(f"You already have a {found_item.name}")

# Get all values of a dictionary as list
list_of_values = list(pack.values())
# stuff_dict = Counter(item.name for item in list(pack.values()))
# Print the list containing all values of dictionary
print(*list_of_values)
# print()


# list_of_values.sort()
# stuff_dict = Counter(item.name for item in list_of_values)
# for key, value in stuff_dict.items():
#    print(key, 's', ':    ', value, sep='')
'''def print_whole_inventory():
    print_item_type_inventory('weapon')
    print_item_type_inventory('healing potion')
    print_item_type_inventory('armor')
    print_item_type_inventory('shield')
    print_item_type_inventory('boot')
    print_item_type_inventory('cloak')
    print_item_type_inventory('ring of regeneration')
    print_item_type_inventory('ring of protection')
    print_item_type_inventory('town portal scroll')


print_whole_inventory()'''


# (pack['Weapons'].append(broad_sword))

# PRINT ENTIRE INVENTORY USING 'print_item_type_inventory' FUNCTION: ************************************************
def whole_inventory():
    item_type_lst = ['Weapons', 'Healing Potions', 'Armor', 'Shields', 'Boots', 'Cloaks', 'Rings of Regeneration',
                     'Rings of Protection', 'Town Portal Implements']
    current_items = []
    for each_item in item_type_lst:
        is_item_on_list = item_type_inventory(each_item)
        print(is_item_on_list)
        if is_item_on_list:
            current_items.append(each_item)
    print(current_items)

whole_inventory()
#dic.values()[index]
print(pack.values())
def inventory(self):
    while True:
        item_type_lst = ['Weapons', 'Healing Potions', 'Armor', 'Shields', 'Boots', 'Cloaks', 'Rings of Regeneration',
                         'Rings of Protection', 'Town Portal Implements']
        current_items = []
        for each_item in item_type_lst:
            is_item_on_list = item_type_inventory(each_item)
            print(is_item_on_list)
            if is_item_on_list:
                current_items.append(each_item)
        print(f"Your current wielded weapon: "
              f"{self.wielded_weapon}\n"
              f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
              f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
        if not len(current_items):
            return
        inventory_choice = input(f"(S)ubstitute wielded weapon or (E)xit: ").lower()
        if inventory_choice not in ('s', 'e'):
            continue
        if inventory_choice == 'e':
            return
        if inventory_choice == 's':
            self.hud()
            # stuff = Counter(item.name for item in self.pack)
            # items = [item for item in self.pack if item.item_type == "weapon"]
            # self.pack.sort(key=lambda x: x.damage_bonus)
            (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus)
            # stuff = Counter(item.name for item in items)
            stuff = {}
            for item in self.pack['Weapons']:
                stuff[item] = (self.pack['Weapons']).index(item)
            for key, value in stuff.items():
                print(value, ':', key)
            old_weapon = self.wielded_weapon
            print(f"Your current wielded weapon: "
                  f"{self.wielded_weapon}\n"
                  f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                  f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
            try:
                new_weapon = int(input(f"Enter the number of the weapon from your pack you wish to wield: "))
                #dic.values()[index]
                # (pack[found_item.item_type]).append(found_item)
                self.wielded_weapon = (self.pack['Weapons'])[new_weapon]
            except (IndexError, ValueError):
                print("Invalid entry..")
                sleep(1)
                break
            print(f"You remove the {self.pack[new_weapon]} from your pack and are now wielding it.\n"
                  f"You place the {old_weapon} in your pack.")
            self.pack.pop(new_weapon)
            self.pack.append(old_weapon)
            self.pack.sort(key=lambda x: x.damage_bonus)
            sleep(1)
            if not len(self.pack):
                print("Your pack is now empty.")
                sleep(1)
                return
        else:
            print("Your pack is empty..see if this statement is ever seen")
            return
