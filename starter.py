from player_class_module import *
import random
player_name = "Legolas"
player_stats = [player_name, 1, 0, 0, 0, 0, *random.sample(range(3, 19), 5), 0]
# print(player_stats)
con = round(player_stats[6] * 1.2)
player_stats[11] = con
player_1 = Player(*player_stats)  # sending stats to Player Class
print(f"Name: {player_1.name}")
print(f"Hitpoints: {player_1.hit_points}")
player_1.swing(player_name, player_1.dexterity, player_1.strength, player_1.sword)
print(f'You have {player_1.hit_points} hitpoints...Program continues...')
