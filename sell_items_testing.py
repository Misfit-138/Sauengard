from player_class_module_reliable import minor_healing_potion
from player_module_testing import leather_armor, buckler, leather_boots, canvas_cloak, ring_of_regeneration, \
    ring_of_protection, scroll_of_town_portal, short_sword, short_axe, quantum_sword, broad_sword, healing_potion

pack = {
    'Weapons': [short_sword, short_axe, quantum_sword, broad_sword],
    'Healing Potions': [healing_potion, healing_potion, healing_potion, healing_potion],

    'Armor': [],  # [leather_armor],
    'Shields': [],  # [buckler],
    'Boots': [],  ##[leather_boots],
    'Cloaks': [canvas_cloak],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal]

}


non_empty_item_type_lst = []
# make a list of non-empty inventory item keys from player's inventory
for key in pack:
    if len(pack[key]) > 0:
        non_empty_item_type_lst.append(key)

# make a dictionary from the non_empty item type list, index and print
item_type_dict = {}
for item_type in pack:
    if len(pack[item_type]):
        item_type_dict[item_type] = non_empty_item_type_lst.index(item_type)
for key, value in item_type_dict.items():
    print(value + 1, ':', key)
item_type_index_to_sell = int(input(f"Enter type of item to sell:"))
item_type_to_sell = non_empty_item_type_lst[item_type_index_to_sell - 1]


#print(pack[item_type]) this prints the list
#(pack[item_type]).sort(key=lambda x: x.name)  # do we need to sort it?

print(f"{item_type_to_sell} you can sell")
mgmt_dict = {}
for item in (pack[item_type_to_sell]):
    mgmt_dict[item] = (pack[item_type_to_sell]).index(item)
for key, value in mgmt_dict.items():
    print(value + 1, ':', key)
item_index_to_sell = int(input(f"Enter item to sell:"))
#item = new_item_type_lst[item_type_index_to_sell - 1]
(pack[item_type_to_sell]).pop(item_index_to_sell - 1)
print(f"{pack[item_type_to_sell]}")



# print it again







#new_item_type_lst = []
#for key in pack:
#    if len(pack[key]) > 0:
#        new_item_type_lst.append(key)
#print(new_item_type_lst)
