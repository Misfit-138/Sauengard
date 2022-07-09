import random
from dice_roll_module import *


class Monster:

    def __init__(self):
        self.level = level
        self.experience_award = experience_award
        self.gold = gold
        self.weapon = weapon
        self.armor = armor_bonus
        self.shield = shield
        self.armor_class = armor_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_points = hit_points


class Ghoul(Monster):

    def __init__(self, level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                 constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead,
                 human_player_level, difficulty_class, proficiency, damage, challenge_rating):
        super().__init__(level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                         constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead,
                         human_player_level, difficulty_class, proficiency, damage, challenge_rating)
        self.level = level
        self.experience_award = self.level * 600
        self.gold = self.level * 103 * round(random.uniform(1, 2))  # ghouls shouldn't have much gold
        self.weapon = weapon
        self.armor = armor_bonus
        self.shield = shield
        self.strength = random.randint(7, 12)
        self.dexterity = random.randint(6, 11)
        self.constitution = random.randint(6, 12)
        self.intelligence = random.randint(1, 10)
        self.wisdom = random.randint(7, 15)
        self.charisma = random.randint(1, 5)