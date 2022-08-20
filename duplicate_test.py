from player_module_testing import *

# from main_testing import player_1

player_1 = Player("fart")


def item_is_in_inventory(item_type, possible_duplicate):
    item_name_lst = []
    # player_1.pack[item_type].sort(key=lambda x: x.name)
    inv_dict = Counter(item for item in player_1.pack[item_type])
    print(inv_dict)
    for key, value in inv_dict.items():
        print(key, ':    ', value, sep='')
        # if value > 0:
        item_name_lst.append(key.name)
    print(item_name_lst)
    if possible_duplicate.name in item_name_lst or \
            possible_duplicate.name == player_1.wielded_weapon.name or \
            possible_duplicate.name == player_1.armor.name or \
            possible_duplicate.name == player_1.shield.name or \
            possible_duplicate.name == player_1.boots.name:
        return True
        # print(value, ' ', key, 's', sep='')
        # print(key, 's', ':    ', value, sep='')
    else:
        return False


# print(item_is_in_inventory('Weapons', short_axe))
def sell_everything(player):
    sell_all = []
    print(f"Sell everything but potions, scrolls:")
    item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
    #        if len(player.pack[item_type]) and item_type != 'Rings of Protection' and item_type != 'Rings of Regeneration':
    mgmt_dict = {}
    for each_item_type in item_type_lst:
        if len(player.pack[each_item_type]):
            for item in (player.pack[each_item_type]):
                mgmt_dict[item] = (player.pack[each_item_type]).index(item)
    for key, value in mgmt_dict.items():
        print(key.name, '- Sell price:', key.sell_price, 'GP')
        sell_all.append(key.sell_price)
        #(player.pack[each_item_type]).clear()
        #print(player.pack[each_item_type])
    #print(player.pack)
    total = sum(sell_all)
    print(f"Total: {total}")
    for each_item_type in item_type_lst:
        (player.pack[each_item_type]).clear()
    total = sum(sell_all)
    print(player.pack)
    #print(total)

''' print((player.pack[each_item_type]))
(player.pack[each_item_type]).clear()
print((player.pack[each_item_type]))
print(sum(sell_all))
'''
sell_everything(player_1)
