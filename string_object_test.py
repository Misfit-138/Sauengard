from monster_class_module import *
from dragon_module import *
monster_type = "Dragon"
monster_level = 1
monster_stats = [monster_type, monster_level]
monster = Dragon(*monster_stats)  # send stats to Dragon class and create 'monster' as object
print(monster_stats)
monster.breathe_fire(monster.strength)
