import random
from player_class_module import *


# import player_class_module

#def swing(name, dexterity, strength, sword):
def swing(name, dexterity, strength, sword):
    roll20 = random.randint(1, 20)
    dexterity_modifier = round((dexterity - 10) / 2)
    opponent_roll20 = random.randint(1, 20)
    roll12 = random.randint(1, 12)
    strength_modifier = round((strength - 10) / 2)

    print(f"{name} rolls 20 sided die---> {roll20}")
    print(f"Dexterity modifier {dexterity_modifier}")
    print(f"Monster rolls 20 sided die ---> {opponent_roll20}")
    if roll20 + dexterity_modifier > opponent_roll20:
        damage_to_opponent = round(roll12 + strength_modifier + sword)
        if damage_to_opponent > 0:
            print(f"{name} hits!")
            print(f"{name} rolls 12 sided die---> {roll12}")
            print(f'Strength modifier---> {strength_modifier}')
            print(f"{name} does {damage_to_opponent} points of damage!")
            return damage_to_opponent
            #Player.reduce_health(damage_to_opponent)
            #print(Player.hitpoints)

        else:
            print("0 or less than zero....Miss")
            return
    else:
        print(f"{name} misses..")
        return
