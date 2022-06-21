import randoomtest


# check_dead returns a string value, it does not output it to stdout.
# If you want to see the output from check_dead, try print(player.check_dead())

class Player:
    def __init__(self, weapon, health):
        self.weapon = weapon
        self.health = health

    def reduce_health(self, amount):
        self.health -= amount

    def check_dead(self):
        if self.health > 0:
            return "Player not dead"
        else:
            return "Player dead"

    def calculate_damage(self, weapon):
        damage_inflicted = random.randint(3, 15) + weapon
        return damage_inflicted

    def fight(self):
        self.reduce_health(self.calculate_damage(self.weapon))
        print(self.health)
        #print(self.check_dead())


player = Player(1, 15)

player.fight()
print(player.check_dead())
