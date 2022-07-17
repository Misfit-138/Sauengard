'''from monster_class_module import *
from dragon_module import *
monster_type = "Dragon"
monster_level = 1
monster_stats = [monster_type, monster_level]
monster = Dragon(*monster_stats)  # send stats to Dragon class and create 'monster' as object
print(monster_stats)
monster.breathe_fire(monster.strength)'''

# MONSTER_ATTACKS = ["swing"]
# print(*MONSTER_ATTACKS)
# attack = MONSTER_ATTACKS[0]
# print(attack)
import random
from collections import Counter

class QuantumSword:

    def __init__(self):
        self.name = "Rudimentary Quantum Sword"
        self.damage_bonus = 1

    def __repr__(self):
        # return "Rudimentary Quantum Sword"
        return self.name


class Axe:

    damage_bonus: int

    def __init__(self):
        self.name = "Battle Axe"
        self.a_name = "A Battle Axe"
        self.damage_bonus = 2

    def __repr__(self):
        return self.name


quantum_sword = QuantumSword()
quantum_sword_2 = QuantumSword()
axe = Axe()


class Adventurer:
    def __init__(self):
        self.name = 'foo'
        self.pack = [quantum_sword]
        self.wielded_weapon_1 = axe
        self.weapon_bonus = self.wielded_weapon_1.damage_bonus


player_1 = Adventurer()
player_1.pack.append(axe)
player_1.pack.append(axe)
# player_1.pack.remove(quantum_sword)

player_1.pack.append(axe)
player_1.pack.append(axe)
player_1.pack.append(axe)

# print(f"Your pack contains {(repr(player_2.pack))}")
print("Your pack contains:")
print(repr(player_1.pack).strip("[]"))

# print(repr(player_2.pack).strip("[]"))
#player_2.pack.clear()  # someone steals your entire inventory!!!

print(f"The hobbit makes a quick move.")
if len(player_1.pack):
    stolen_item = random.choice(player_1.pack)
    print(f"He steals your {stolen_item}")
else:
    print("You have nothing in your pack!")
    exit()
player_1.pack.remove(stolen_item)
print("Your pack contains:")
print(repr(player_1.pack).strip("[]"))
print(f"You are currently wielding a {player_1.wielded_weapon_1}")
found_weapon_lst = [axe, quantum_sword]
found_weapon = random.choice(found_weapon_lst)
print(f"You find a {found_weapon}")
if found_weapon not in player_1.pack:
    player_1.pack.append(found_weapon)
    print(f"You snarf the {found_weapon}")
    print("Your pack contains:")
    print(repr(player_1.pack).strip("[]"))

else:
    print(f"You already have one.")
    print("Your pack contains:")
    print(repr(player_1.pack).strip("[]"))
print(f"You swing your {player_1.wielded_weapon_1} and get a bonus of {player_1.weapon_bonus}")


# MyList = ["a", "b", "a", "c", "c", "a", "c"]
res = Counter(player_1.pack)

print(res)
res = {}

for i in player_1.pack:
    res[i] = player_1.pack.count(i)

print(res)

import pprint
pretty = pprint.PrettyPrinter(width=16)
pretty.pprint(res)
