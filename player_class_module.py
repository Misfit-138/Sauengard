# import random
from dice_roll_module import *

# name0, level1, experience2, gold3, sword4, armor5, shield6, constitution7,
# intelligence8, wisdom9, strength10, dexterity11, charisma12, hit_points13

# **** TRY DEFINING DEXTERITY AND STRENGTH MODIFIERS HERE ****

class Player:

    def __init__(self, name, level, experience, gold, sword, armor, shield, constitution, intelligence, wisdom,
                 strength,
                 dexterity, charisma, hit_points):
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
        self.charisma = charisma
        self.hit_points = hit_points
        self.hit_dice = 12

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
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

#    def dice_roll(self, no_of_dice, no_of_sides):
#        dice_rolls = []  # create list for multiple die rolls
#        for dice in range(no_of_dice):  # (1 hit die per level according to DnD 5E rules)
#            dice_rolls.append(random.randint(1, no_of_sides))
#        your_roll_sum = sum(dice_rolls)
#        return your_roll_sum

    def swing(self, name, level, dexterity, strength, sword, monster_level, monster_type, monster_dexterity):
        player_dexterity_modifier = round((dexterity - 10) / 2)
        opponent_roll20 = dice_roll(1, 20) + ((monster_dexterity - 10) / 2)  # determine mon dex modifier
        player_strength_modifier = round((strength - 10) / 2)
        roll_d20 = dice_roll(1, 20)
        print(f"{name} rolls 20 sided die---> {roll_d20}")
        print(f"Dexterity modifier {player_dexterity_modifier}")
        print(f"The {monster_type} rolls 20 sided die ---> {opponent_roll20}")
        if roll_d20 + player_dexterity_modifier > opponent_roll20:
            roll_d12 = dice_roll(self.level, 12)  # Barbarians have d12..fighters have d10; may want to change this
            damage_to_opponent = round(roll_d12 + player_strength_modifier + sword)
            if damage_to_opponent > 0:
                print(f"You hit the {monster_type}!")
                print(
                    f"{name} rolls 12 sided die---> {roll_d12} + {player_strength_modifier} Strength modifier = {damage_to_opponent} ")
                # print(f'Strength modifier---> {strength_modifier}')
                print(f"You do {damage_to_opponent} points of damage!")
                return damage_to_opponent
            else:
                print(f"You strike the {monster_type}, but it blocks!")  # zero damage result
                return 0
        else:
            print(f"You missed...")
            return 0


"""leveling up logic
                exp = 64000
                before_level = self.level
                self.increase_experience(exp)
                self.current_level()
                after_level = self.level
                if after_level > before_level:
                    print(f"You went up a level!")
                print(f"You gain {exp} experience points for a total of {self.experience}")"""
