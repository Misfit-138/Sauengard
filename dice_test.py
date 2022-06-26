import random


def roll_12(level):
    dice_rolls = []
    for dice in range(level):
        dice_rolls.append(random.randint(1, 12))
    total_of_rolls = sum(dice_rolls)
    return dice_rolls, total_of_rolls
    # print(f"Randomised list is: {dice_list}. Sum of all numbers is {sum(dice_list)}")


#roll_12(2)
dice_list, total_roll = roll_12(2)  # assign returned tuple. this is somewhat counterintuitive.
# remember that the return statement is determining what is actually being sent back, this assignment is merely
# naming the results- giving them variables that we can print, or use
print(dice_list)
print(total_roll)

# if you call a function and expect to use a return value, like, by printing it, you must first assign a variable in
# the call itself!!!
# 1 + (total level/4)Rounded up
level = 7
var = round(1 + (level / 4))
var2 = 1 + round(level / 4)
print(var, var2)
roll_2 = random.randint(1, 3)
print(f"Roll 3 sided die:{roll_2}")

ability_score = int(input("Input ability score"))
ability_modifier = round((ability_score - 10) / 2)
print(ability_modifier)
