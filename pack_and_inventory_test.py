from player_class_test import Weapon, Player, short_sword, short_axe, quantum_sword, broad_sword, minor_healing_potion, \
    Counter, time, buckler, leather_armor, leather_boots, canvas_cloak, scroll_of_town_portal, ring_of_regeneration, \
    ring_of_protection, major_healing_potion


def inventory(self):
    while True:
        if len(self.pack):
            self.hud()
            print("Your pack contains:")
            print("Item                       Quantity")
            print()

            self.pack.sort(key=lambda x: x.damage_bonus)
            stuff_dict = Counter(item.name for item in self.pack)

            for key, value in stuff_dict.items():
                print(key, 's', ':    ', value, sep='')
                # print(value, ':', key)
            print()
        else:
            print("Your pack is empty")
        print(f"Your current wielded weapon: "
              f"{self.wielded_weapon}\n"
              f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
              f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
        if not len(self.pack):
            return
        inventory_choice = input(f"Manage (W)eapons or (E)xit: ").lower()
        if inventory_choice not in ('w', 'e'):
            continue
        if inventory_choice == 'e':
            return
        if inventory_choice == 'w':
            self.hud()
            # stuff = Counter(item.name for item in self.pack)
            # items = [item for item in self.pack if item.item_type == "weapon"]
            # self.pack.sort(key=lambda x: x.damage_bonus)
            # stuff = Counter(item.name for item in items)
            stuff = {}
            for item in self.pack:
                # if getattr(item, item.item_type) == "weapon":
                monster_key = random.randint(1, (player_1.level + 1))
                monster_cls = random.battle_choice(monster_dict[monster_key])
                stuff[item] = self.pack.index(item)
            for key, value in stuff.items():
                print(value, ':', key)
            old_weapon = self.wielded_weapon
            print(f"Your current wielded weapon: "
                  f"{self.wielded_weapon}\n"
                  f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                  f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
            try:
                new_weapon = int(input(f"Enter the number of the weapon from your pack you wish to wield: "))
                # try:
                self.wielded_weapon = self.pack[new_weapon]
            except (IndexError, ValueError):
                print("Invalid entry..")
                time.sleep(1)
                continue
            print(f"You remove the {self.pack[new_weapon]} from your pack and are now wielding it.\n"
                  f"You place the {old_weapon} in your pack.")
            self.pack.pop(new_weapon)
            self.pack.append(old_weapon)
            self.pack.sort(key=lambda x: x.damage_bonus)
            time.sleep(1)
            if not len(self.pack):
                print("Your pack is now empty.")
                time.sleep(1)
                return
        else:
            print("Your pack is empty..see if this statement is ever seen")
            return


item_type = 'weapon'
pack = {
    'weapon': [short_axe, quantum_sword, broad_sword],
    'healing potion': [minor_healing_potion, major_healing_potion],
    'armor': [leather_armor],
    'shield': [buckler, buckler],
    'boot': [leather_boots],
    'cloak': [canvas_cloak],
    'ring of regeneration': [ring_of_regeneration],
    'ring of protection': [ring_of_protection],
    'town portal scroll': [scroll_of_town_portal]

}
loot_dict = {

}


def print_item_type_inventory(item_type):
    # print(*pack[item_type])  # print list without any brackets or commas. 'pack' is the dictionary, 'weapon' is the key for the list of weapons
    (pack[item_type]).sort(key=lambda x: x.name)  # sort the weapon list by damage_bonus, ascending
    stuff_dict = Counter(item.name for item in
                         pack[item_type])  # create a dictionary of the sorted list, which is within the pack dictionary
    total_number_of_items = len(pack[item_type])
    if total_number_of_items:
        print(f"You currently have {total_number_of_items} items in your {item_type} inventory:")
        for key, value in stuff_dict.items():  # loop through each key and value
            print(key, ':    ', value, sep='')
            #print(key, 's', ':    ', value, sep='')  # print each key and value. add an 's' and a colon, without any spaces
    # total_number_of_items = len(pack[item_type])
    # print(f"You have {total_number_of_items} items in your {item_type} pack.")
    else:
        return

found_item = short_sword

print(f"You have found a {found_item.name}")
if found_item not in pack[item_type]:
    (pack[found_item.item_type]).append(found_item)
    (pack[item_type]).sort(key=lambda x: x.damage_bonus)
    stuff_dict = Counter(item.name for item in pack[item_type])
    for key, value in stuff_dict.items():
        print(key, 's', ':    ', value, sep='')
    number_of_items = len(pack[item_type])
    print(f"You now have {number_of_items} items in your {found_item.item_type} inventory.")
else:
    print(f"You already have a {found_item.name}")

# Get all values of a dictionary as list
list_of_values = list(pack.values())
# stuff_dict = Counter(item.name for item in list(pack.values()))
# Print the list containing all values of dictionary
print(*list_of_values)
print()


# list_of_values.sort()
# stuff_dict = Counter(item.name for item in list_of_values)
# for key, value in stuff_dict.items():
#    print(key, 's', ':    ', value, sep='')
def print_whole_inventory():
    print_item_type_inventory('weapon')
    print_item_type_inventory('healing potion')
    print_item_type_inventory('armor')
    print_item_type_inventory('shield')
    print_item_type_inventory('boot')
    print_item_type_inventory('cloak')
    print_item_type_inventory('ring of regeneration')
    print_item_type_inventory('ring of protection')
    print_item_type_inventory('town portal scroll')
print_whole_inventory()
