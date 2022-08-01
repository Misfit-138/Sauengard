# name, level, gold, sword, armor, shield, constitution, intelligence, wisdom, strength, dexterity, hitpoints
from player_class_module_old import *
# from player_class_module import
import random
import os

player_name = input("Enter Player name: ")
player_stats = [player_name,1,0,0,0,0,*random.sample(range(3, 19), 5), 0]
constitution = round(player_stats[6] * 1.2)
player_stats[11] = constitution

print(player_stats)
player_1 = Player(*player_stats)  # sending stats to Player Class

print(f"Name: {player_1.name}")
print(f"Level: {player_1.level}")
print(f"Gold: {player_1.gold}")
print(f"Sword + {player_1.sword}")
print(f"Armor + {player_1.armor}")
print(f"Shield + {player_1.shield_bonus}")
print(f"Constitution {player_1.constitution}")
print(f"Intelligence: {player_1.intelligence}")
print(f"Wisdom: {player_1.wisdom}")
print(f"Strength: {player_1.strength}")
print(f"Dexterity: {player_1.dexterity}")
print(f"Hitpoints: {player_1.hit_points}")

player_1.reduce_health(5)
print(player_1.hit_points)

#player_1.swing("name", 12, 12, 12)
#damage = swing()
#print(damage)