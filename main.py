from player_class_module import Player
import random
#player_stats = [18,17,16,15,14]
player_stats = random.sample(range(6, 18), 5)
#print(player_stats)
player_1 = Player(*player_stats)
print(player_1)