'''Choose a challenge rating (CR) for your trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)
• Multi-Target Damage = 3 x CR (or 1d6 per CR)

Difficulty Class:
Task Difficulty   DC
Very easy         5
Easy              10
Medium            15
Hard              20
Very hard         25
Nearly impossible 30

'''

from monster_class_module import *


class Dragon(Monster):

    def __init__(self, level, experience_award, gold, sword, armor, shield, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, human_player_level):
        super().__init__(level, experience_award, gold, sword, armor, shield, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, human_player_level)
        self.level = level
        self.experience_award = self.level * 1000
        self.gold = gold
        self.sword = sword
        self.armor = armor
        self.shield = shield
        self.armor_class = 10
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_points = hit_points
        self.human_player_level = human_player_level
        self.hit_dice = 12
        #self.challenge_rating = pass
        self.dexterity_modifier = round((dexterity - 10) / 2)
    name = "Dragon"

    def breathe_fire(self, strength):
        print("The Dragon breathes fire!")
        fire_damage_to_player = strength + dice_roll(1, 20)
        print(f"It does {fire_damage_to_player} points of damage!")
        return fire_damage_to_player
