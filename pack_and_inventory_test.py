from player_class_module import *

item_type = 'weapon'
pack = {
                        'weapon': [short_sword, short_axe, quantum_sword, broad_sword],
                        'potion': [healing_potion]
                    }

print(*pack[item_type])  # print list without any brackets or commas. 'pack' is the dictionary, 'weapon' is the key for the list of weapons
(pack[item_type]).sort(key=lambda x: x.damage_bonus)  # sort the weapon list by damage_bonus, ascending
stuff_dict = Counter(item.name for item in pack[item_type])  # create a dictionary of the sorted list, which is within the pack dictionary
for key, value in stuff_dict.items():  # loop through each key and value
    print(key, 's', ':    ', value, sep='')  # print each key and value. add an 's' and a colon, without any spaces


number_of_items = len(pack[item_type])
print(f"You have {number_of_items} items in your pack.")
found_item = short_sword
print(f"You have found a {found_item.name}")
(pack[found_item.item_type]).append(found_item)
(pack[item_type]).sort(key=lambda x: x.damage_bonus)
stuff_dict = Counter(item.name for item in pack[item_type])
for key, value in stuff_dict.items():
    print(key, 's', ':    ', value, sep='')
print(f"You now have {number_of_items} items in your pack.")