import random


def calculate_damage():
    damage_inflicted = random.randint(3, 5)
    return damage_inflicted


class Player:
    def __init__(self, name, weapon, health):
        self.name = name
        self.weapon = weapon
        self.health = health

    def reduce_health(self, amount):
        self.health -= amount

    def check_dead(self):
        if self.health > 0:
            return False


def calculate_damage():
    damage_inflicted = random.randint(3, 5)
    return damage_inflicted


class Monster:
    def __init__(self, name, weapon, health):
        self.name = name
        self.weapon = weapon
        self.health = health

    def reduce_health(self, amount):
        self.health -= amount

    def check_dead(self):
        print(self.health)
        if self.health > 0:
            return "Monster not dead"

player = Player("Trett", "Sword", 20)
monster = Monster("Skeleton", "sword", 20)


'''You can add additional methods like calculate_damage()
to the Player class that take into account the type of weapon the player has.
If you also create a monster class , your fight sequence could look something like


def fight():
    monster.reduce_health(player.calculate_damage())
    monster.check_dead()
    player.reduce_health(monster.calculate_damage())
    player.check_dead()
    '''


def fight():
    monster.reduce_health(calculate_damage())
    print(monster.health)
    monster.check_dead()
    player.reduce_health(calculate_damage())
    print(player.health)
    player.check_dead()


fight()