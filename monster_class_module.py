'''Choose a challenge rating (CR) for your trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)
• Multi-Target Damage = 3 x CR (or 1d6 per CR)
A monster usually dies or is destroyed when it drops to 0 Hit Points.
A monster’s Hit Points are presented both as a die expression and as an average number.
For example, a monster with 2d8 Hit Points has 9 Hit Points on average (2 × 4½).

A monster’s size determines the die used to calculate its Hit Points, as shown in the Hit Dice by Size table.

Table: Size Categories
Size	Space	Examples
Tiny	2½ by 2½ ft.	Imp, Sprite
Small	5 by 5 ft.	    Giant Rat, Goblin
Medium	5 by 5 ft.	    Orc, Werewolf
Large	10 by 10 ft.	Hippogriff, Ogre
Huge	15 by 15 ft.	Fire Giant, Treant
Gargantuan 20 by 20 ft. or more Kraken, Purple Worm



Table: Hit Dice by Size
Monster Size	Hit Die	Average HP
                         per Die
Tiny	        d4	       2½
Small	        d6	       3½
Medium	        d8	       4½
Large	        d10	       5½
Huge	        d12	       6½
Gargantuan	    d20	       10½
A monster’s Constitution modifier also affects the number of Hit Points it has.
Its Constitution modifier is multiplied by the number of Hit Dice it possesses,
and the result is added to its Hit Points.
For example, if a monster has a Constitution of 12 (+1 modifier) and 2d8 Hit Dice, it has 2d8 + 2 Hit Points (average 11).
'''

import random
from dice_roll_module import dice_roll


# # monsters have Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma
class Monster:

    def __init__(self, level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                 constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead,
                 human_player_level):
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
        self.can_paralyze = can_paralyze
        self.can_drain = can_drain
        self.undead = undead
        self.hit_dice = 0  # tiny d4, small d6, medium d8, large d10, huge d12, gargantuan d20
        self.human_player_level = human_player_level
        self.proficiency_bonus = 0  # 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.dexterity_modifier = 0  # round((dexterity - 10) / 2)
        self.strength_modifier = 0  # round((strength - 10) / 2)
        self.constitution_modifier = 0  # round((constitution - 10) / 2)
        self.attack_1 = 0
        self.attack_1_phrase = ""
        self.attack_2 = 0
        self.attack_2_phrase = ""
        self.attack_3 = 0
        self.attack_3_phrase = ""
        self.attack_4 = 0
        self.attack_4_phrase = ""
        self.attack_5 = 0
        self.attack_5_phrase = ""

    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def swing(self, name, level, dexterity, strength, weapon, player_level, player_hp, player_dexterity,
              player_armor_class):
        attack_bonus = random.randint(1, 5)
        if attack_bonus == 1:
            attack_bonus = self.attack_1
            attack_phrase = self.attack_1_phrase
        if attack_bonus == 2:
            attack_bonus = self.attack_2
            attack_phrase = self.attack_2_phrase
        if attack_bonus == 3:
            attack_bonus = self.attack_3
            attack_phrase = self.attack_3_phrase
        if attack_bonus == 4:
            attack_bonus = self.attack_4
            attack_phrase = self.attack_4_phrase
        if attack_bonus == 5:
            attack_bonus = self.attack_5
            attack_phrase = self.attack_5_phrase
        roll20 = dice_roll(1, 20)
        print(f"{name} rolls 20 sided die---> {roll20}")
        if roll20 == 1:
            print(f"{name} rolled a 1..failure!")
            return 0
        print(f"Dexterity modifier {self.dexterity_modifier}")
        print(f"Your armor class ---> {player_armor_class}")
        if roll20 + self.dexterity_modifier >= player_armor_class:
            damage_roll = dice_roll(self.level, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus)
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                print(f"{name} rolls {self.hit_dice} sided dice---> {damage_roll}")
                print(f"Strength modifier---> {self.strength_modifier}\nAttack bonus---> {attack_bonus}")
                print(f"It does {damage_to_opponent} points of damage!")
                return damage_to_opponent
            else:
                print(f"The {name} strikes, but you block the attack!")  # zero damage to player result
                return 0  # 0 points damage to player
        else:
            print(f"It missed..")
        return 0

    def paralyze(self, name, level, dexterity, strength, weapon, human_player_level, human_player_hit_points,
                 human_player_dexterity, human_player_armor_class, human_player_wisdom, human_player_wisdom_modifier):
        paralyze = dice_roll(1, 20)
        if paralyze == 20 and self.wisdom > (human_player_wisdom + human_player_wisdom_modifier):
            print("You're paralyzed!!")
            damage_to_player = self.swing(name, self.level, self.dexterity, self.strength,
                                          self.weapon,
                                          human_player_level, human_player_hit_points, human_player_dexterity,
                                          human_player_armor_class)
            return True
        else:
            return False

    def drain(self, human_player_level, human_player_wisdom, human_player_wisdom_modifier):
        drain_level = dice_roll(1, 20)
        if drain_level == 20 and self.wisdom > (human_player_wisdom + human_player_wisdom_modifier):
            # print("It drains a level!")
            level_drain = True
            return level_drain
        else:
            level_drain = False
            return level_drain


'''
    def monster_turn(self,):
        if not monster.check_dead():  # if monster is not dead
            damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity, monster.strength,
                                             monster.weapon,
                                             player_1.level, player_1.hit_points, player_1.dexterity,
                                             player_1.armor_class)
            player_1.reduce_health(damage_to_player)
            if not player_1.check_dead():  # if player not dead
                print(f"You are alive")
                if monster.undead and monster.can_paralyze:
                    player_1.is_paralyzed = monster.paralyze(monster.name, monster.level, monster.dexterity,
                                                             monster.strength,
                                                             monster.weapon,
                                                             player_1.level, player_1.hit_points, player_1.dexterity,
                                                             player_1.armor_class, player_1.wisdom,
                                                             player_1.wisdom_modifier)
                    player_1.reduce_health(damage_to_player)
                    if not player_1.check_dead():  # if player not dead
                        print(f"You are alive")

                if monster.undead and monster.can_drain:
                    level_drain = monster.drain(monster.wisdom, player_1.level, player_1.wisdom,
                                                player_1.wisdom_modifier)
                    if level_drain:  # if level_drain True
                        print("It drains a level!\nYou go down a level!!")
                        player_1.level -= 1
                        if player_1.level <= 0:
                            print(f"You have died from drainage!!!!!")
                            break

                    else:
                        print(
                            f"You have {player_1.hit_points} hitpoints, and {player_1.experience} experience. You are level {player_1.level}")
                        continue
            else:
                print(f"You have died.")
                break
            print(
                f"You have {player_1.hit_points} hitpoints, and {player_1.experience} experience. You are level {player_1.level}")
        else:
            break'''


class Dragon(Monster):

    def __init__(self, level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                 constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead,
                 human_player_level):
        super().__init__(level, experience_award, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                         constitution, intelligence, wisdom, charisma, hit_points, can_paralyze, can_drain, undead,
                         human_player_level)
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
        self.hit_dice = 12  # 12 for huge monster, 20 for gargantuan
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
