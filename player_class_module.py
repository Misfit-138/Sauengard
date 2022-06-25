# import random
from dice_roll_module import *
'''Target
Identify your target to the table. 
Attack
Roll a d20. During an Attack roll, 1 always fails, and 20 always succeeds. 
Modify
Add your modifiers.  
Armor Class 
If the modified result is ≥ target’s Armor Class (AC) , the attack hits the target. 
Damage Roll Damage Dice and add modifiers. The target’s HP are reduced, factoring resistances and vulnerabilities. 
Spell Attack Many spells count as attacks. 
The caster rolls d20 + Spellcasting Ability Modifier + Proficiency Bonus to hit vs AC. PHB 205'''



# name0, level1, experience2, gold3, sword4, armor5, shield6, constitution7,
# intelligence8, wisdom9, strength10, dexterity11, charisma12, hit_points13

# **** TRY DEFINING DEXTERITY AND STRENGTH MODIFIERS HERE ****

class Player:

    def __init__(self, name, level, experience, gold, sword, armor_class, shield, constitution, intelligence, wisdom,
                 strength,
                 dexterity, charisma, hit_points):
        self.name = name
        self.level = level
        self.experience = experience
        self.gold = gold
        self.sword = sword
        self.armor_class = armor_class
        self.shield = shield
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity
        self.charisma = charisma
        self.hit_points = hit_points
        self.hit_dice = 12
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.dexterity_modifier = round((dexterity - 10) / 2)
        self.strength_modifier = round((strength - 10) / 2)

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

    def swing(self, name, level, dexterity, strength, sword, monster_level, monster_type, monster_dexterity, monster_armor_class):
        opponent_roll20 = dice_roll(1, 20) + round((monster_dexterity - 10) / 2)  # determine mon dex modifier
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"Attack roll..")
        print(f"{name} rolls 20 sided die---> {roll_d20}")
        print(f"Dexterity modifier {self.dexterity_modifier}")
        print(f"Monster armor class {monster_armor_class}")
        if roll_d20 + self.proficiency_bonus + self.dexterity_modifier > monster_armor_class:
            damage_roll = dice_roll(self.level, 12)  # Barbarians have d12..fighters have d10 or d8?; may want to change this
            damage_to_opponent = round(damage_roll + self.strength_modifier + sword)
            if damage_to_opponent > 0:
                print(f"You hit the {monster_type}!")
                print(f"{name} rolls 12 sided die---> {damage_roll} + {self.strength_modifier} Strength modifier = {damage_to_opponent} ")
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
