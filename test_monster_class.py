import random


class Monster:

    def __init__(self, name, level):
        self.name = name
        self.level = level


class Dragon(Monster):

    def breathe_fire(self):
        print("The Dragon breathes fire!")


class Skeleton(Monster):

    def strikes(self):
        print("The Skeleton strikes with its sword!")


MONSTERS = ["Skeleton", "Dragon"]
monster_type = random.choice(MONSTERS)
# monster_type = "Dragon"
monster_level = 1
monster_stats = [monster_type, monster_level]
print(monster_stats)
monster = random.choice(MONSTERS(*monster_stats))  # send stats to class and create 'monster' as object
