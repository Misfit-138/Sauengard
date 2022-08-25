from player_module_testing import *
player_1 = Player('judd')
ability_dict = player_1.__dict__

# Define list of attributes you are allowed to change
attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

ability_dict_subset_too = {1: "strength", 2: "dexterity", 3: "constitution", 4: "intelligence", 5: "wisdom", 6: "charisma"}

improvement_ability = int(input(f"Enter number to increase"))

ability_to_improve = (ability_dict_subset_too[improvement_ability])

ability_dict[ability_to_improve] += 1
print(ability_to_improve)
#print(player_1.dexterity)

