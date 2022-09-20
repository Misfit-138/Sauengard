from random import random

from player_module_testing import Player

player_1 = Player("foo")


def sell_chemist_items_beta(self):
    belt_dict = self.__dict__
    # Define list of attributes you are allowed to change
    belt_items = ["potions_of_healing", "town_portals", "potions_of_strength", "elixirs", "antidotes"]
    # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
    belt_dict_subset = {key: value for key, value in belt_dict.items() if key in belt_items}
    # Choose random attribute name
    non_zero_items = (list(belt_dict_subset.values()))
    print(non_zero_items)

    belt_items2 = [player_1.potions_of_healing, player_1.town_portals, player_1.potions_of_strength, player_1.elixirs,
                  player_1.antidotes]
    non_zero_items = []
    print(belt_items2)
    for each_item in belt_items2:
        if each_item > 0:
            non_zero_items.append(each_item)
    working_dict = dict(enumerate(non_zero_items, start=1))
    print(non_zero_items)
    # working_dict = {key_lst[i]: value_list[i] for i in range(len(key_lst))}
    for key, value in working_dict.items():
        print(f"{key}: {value}")


sell_chemist_items_beta(player_1)
