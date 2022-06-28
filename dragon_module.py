''' Choose a challenge rating (CR) for your trap, object, effect, or creature
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

A monster’s Constitution modifier also affects the number of Hit Points it has.
Its Constitution modifier is multiplied by the number of Hit Dice it possesses,
and the result is added to its Hit Points.
For example, if a monster has a Constitution of 12 (+1 modifier) and 2d8 Hit Dice, it has 2d8 + 2 Hit Points (average 11).

Adult Red Dragon Stats per D&D
STR 27 (+8) DEX 10 (+0) CON 25 (+7) INT 16 (+3) WIS 13 (+1) CHA 21 (+5)
'''

from monster_class_module import *


class Dragon(Monster):

    def __init__(self, level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead, human_player_level):
        super().__init__(level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead, human_player_level)
        self.level = level
        self.experience_award = self.level * 1000
        self.gold = self.level * round(1000 * random.uniform(1, 2))
        self.weapon = weapon
        self.armor = armor_bonus
        self.shield = shield
        self.strength = random.randint(17, 27)
        self.dexterity = random.randint(10, 11)
        self.constitution = random.randint(14, 19)
        self.intelligence = random.randint(14, 17)
        self.wisdom = random.randint(12, 14)
        self.charisma = random.randint(18, 21)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        # For a dragon, hit points should be quite high. Level * random range 10-20 + con mod
        self.human_player_level = human_player_level
        self.hit_dice = 12  # 12 for huge monster
        # self.challenge_rating = 0
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((strength - 10) / 2)
        self.constitution_modifier = round((constitution - 10) / 2)
        self.hit_points = 1  # self.level * (random.randint(15, 20)) + self.constitution_modifier
        self.dexterity_modifier = round((dexterity - 10) / 2)
        self.armor_class = random.randint(17, 19)
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It strikes with its terrible claws!!"
        self.attack_2 = 6
        self.attack_2_phrase = "The dragon hisses and strikes with its gaping jaws!!"
        self.attack_3 = 6
        self.attack_3_phrase = "The dragon swings its tail!!"
        self.attack_4 = 7
        self.attack_4_phrase = "The dragon attacks with its wings!!"
        self.attack_5 = 10
        self.attack_5_phrase = "The dragon breathes fire!!"
    name = "Dragon"
