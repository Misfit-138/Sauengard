import random


# name0, level1, experience2, gold3, sword4, armor5, shield6, constitution7,
# intelligence8, wisdom9, strength10, dexterity11, hitpoints12

class Player:

    def __init__(self, name, level, experience, gold, sword, armor, shield, constitution, intelligence, wisdom, strength,
                 dexterity, hitpoints):
        self.name = name
        self.level = level
        self.experience = experience
        self.gold = gold
        self.sword = sword
        self.armor = armor
        self.shield = shield
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity
        self.hitpoints = hitpoints

    def increase_experience(self, experience_points):
        self.experience = + experience_points

    def current_level(self):
        if self.experience < 2000:
            self.level = 1
        if self.experience >= 2000 < 4000:
            self.level = 2
        if self.experience >= 4000 < 8000:
            self.level = 3
        if self.experience >= 8000 < 16000:
            self.level = 4
        if self.experience >= 16000 < 32000:
            self.level = 5
        if self.experience >= 32000 < 64000:
            self.level = 6
        if self.experience >= 64000 < 128000:
            self.level = 7
        if self.experience >= 128000 < 256000:
            self.level = 8
        if self.experience >= 256000 < 512000:
            self.level = 9
        if self.experience >= 512000 < 1024000:
            self.level = 10
        if self.experience > 1024000:
            self.level = 11

    def reduce_health(self, damage):
        self.hitpoints -= damage
        return damage

    def check_dead(self):
        if self.hitpoints > 0:
            return f"You are alive"
        else:
            return f"You are dead"

    def roll_20(self):
        roll20 = random.randint(1, 20)
        return roll20

    def roll_12(self, level):
        dice_rolls = []  # create list for multiple dice rolls
        for i in range(level):  # (1 hit die per level according to DnD 5E rules)
            dice_rolls.append(random.randint(1, 12))
        roll12_sum = sum(dice_rolls)
        return roll12_sum

    def swing(self, name, level, dexterity, strength, sword, monster_level, monster_type):
        dexterity_modifier = round((dexterity - 10) / 2)
        opponent_roll20 = random.randint(1, 20)
        strength_modifier = round((strength - 10) / 2)
        roll20 = self.roll_20()
        print(f"{name} rolls 20 sided die---> {roll20}")
        print(f"Dexterity modifier {dexterity_modifier}")
        print(f"The {monster_type} rolls 20 sided die ---> {opponent_roll20}")
        if roll20 + dexterity_modifier > opponent_roll20:
            roll12 = self.roll_12(self.level)
            damage_to_opponent = round(roll12 + strength_modifier + sword)
            if damage_to_opponent > 0:
                print(f"You hit the {monster_type}!")
                print(f"{name} rolls 12 sided die---> {roll12}")
                print(f'Strength modifier---> {strength_modifier}')
                print(f"You do {damage_to_opponent} points of damage!")
                exp = 64000
                before_level = self.level
                self.increase_experience(exp)
                self.current_level()
                after_level = self.level
                if after_level > before_level:
                    print(f"You went up a level!")
                print(f"You gain {exp} experience points for a total of {self.experience}")
            else:
                print(f"You strike the {monster_type}, but it blocks!")  # zero damage result
                return
        else:
            print(f"{name} misses..and gets hit!")
            print(f"You suffer {self.reduce_health(self.roll_12(monster_level))} points damage!! ")
            print(self.check_dead())
        return

