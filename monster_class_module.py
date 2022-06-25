'''Choose a challenge rating (CR) for your trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)
• Multi-Target Damage = 3 x CR (or 1d6 per CR)'''

import random
from dice_roll_module import dice_roll


class Monster:

    def __init__(self, level, experience_award, gold, sword, armor_class, shield, constitution, strength, dexterity,
                 hit_points, human_player_level):
        # self.name = name
        self.level = level
        self.experience_award = experience_award
        self.gold = gold
        self.sword = sword
        self.armor_class = armor_class
        self.shield = shield
        self.constitution = constitution
        self.strength = strength
        self.dexterity = dexterity
        self.hit_points = hit_points
        self.hit_dice = 10
        self.human_player_level = human_player_level
    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def roll_12(self, level):
        dice_rolls = []  # create list for multiple dice rolls
        for dice in range(level):  # (1 hit die per level according to DnD 5E rules)
            dice_rolls.append(random.randint(1, 12))
        roll12_sum = sum(dice_rolls)
        return roll12_sum

    def swing(self, name, level, dexterity, strength, sword, player_level, player_hp, player_dexterity):
        dexterity_modifier = round((dexterity - 10) / 2)
        opponent_roll20 = dice_roll(1, 20) + round((player_dexterity - 10) / 2)  # at this point player is opponent!
        strength_modifier = round((strength - 10) / 2)
        roll20 = dice_roll(1, 20)
        print(f"{name} rolls 20 sided die---> {roll20}")
        print(f"Dexterity modifier {dexterity_modifier}")
        print(f"You roll 20 sided die ---> {opponent_roll20}")  # at this point the player is the opponent!
        if roll20 + dexterity_modifier > opponent_roll20:
            roll12 = dice_roll(self.level, 12)
            damage_to_opponent = round(roll12 + strength_modifier + sword)
            if damage_to_opponent > 0:
                print(f"The {name} hits you!")
                print(f"{name} rolls 12 sided dice---> {roll12}")
                print(f'Strength modifier---> {strength_modifier}')
                print(f"It does {damage_to_opponent} points of damage!")
                return damage_to_opponent
            else:
                print(f"The {name} strikes, but you block the attack!")  # zero damage to player result
                return 0  # 0 points damage to player
        else:
            print(f"It missed..")
        return 0
