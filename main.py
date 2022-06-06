from player_class_module import Player
import random
# player_stats = [18,17,16,15,14]
player_name = input("Enter Player name: ")
# player_stats = (player_name,18,18,18,18,18)
# the asterisk * before the random function passes the parameters without
# the brackets
player_stats = (player_name, *random.sample(range(6, 18), 5))
print(player_stats)

player_1 = Player(*player_stats)  # sending stats to Player Class
print(f"Name: {player_1.name}")
print(f"Constitution {player_1.constitution}")
print(player_1.intelligence)
print(player_1.wisdom)
print(player_1.strength)
print(player_1.dexterity)
if player_1.dexterity > 12:
    print("Great dexterity!!")

