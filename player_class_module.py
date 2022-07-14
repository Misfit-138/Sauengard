# import random
import time
import os
import winsound
from dice_roll_module import *

# from main import monster
# from monster_class_module import *
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

# name0, level1, experience2, gold3, weapon4, armor5, shield6, constitution7,
# intelligence8, wisdom9, strength10, dexterity11, charisma12, hit_points13, maximum_hit_points14,
# 15is_paralyzed

# **** TRY DEFINING DEXTERITY AND STRENGTH MODIFIERS HERE ****
'''Hit Dice: 1d10 per Fighter level
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st
In most cases, your AC will be equal to 10 + your DEX modifier + bonus from armor + bonus from magic items/effects.'''


class Player:

    def __init__(self, name, level, experience, gold, weapon, armor_bonus, shield, armor_class, strength, dexterity,
                 constitution, intelligence, wisdom, charisma, hit_points, maximum_hit_points, is_paralyzed, boots,
                 cloak, weapon_name):
        self.name = name
        self.level = level
        self.experience = experience
        self.gold = gold
        self.weapon = weapon
        self.armor_bonus = armor_bonus
        self.shield = shield
        self.strength = strength
        self.dexterity = dexterity
        self.dexterity_modifier = round((dexterity - 10) / 2)
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.maximum_hit_points = maximum_hit_points
        self.hit_points = hit_points  # Hit Points at 1st Level: 10 + your Constitution modifier
        self.hit_dice = 10  # Hit Dice: 1d10 per Fighter level

        self.strength_modifier = round((strength - 10) / 2)
        self.constitution_modifier = round((constitution - 10) / 2)
        self.intelligence_modifier = round((intelligence - 10) / 2)
        self.wisdom_modifier = round((wisdom - 10) / 2)
        self.charisma_modifier = round((charisma - 10) / 2)
        self.proficiency_bonus = 2  # 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.is_paralyzed = is_paralyzed
        self.boots = boots
        self.cloak = cloak
        self.two_handed = False
        self.extra_attack = 0
        self.armor_class = 10 + self.dexterity_modifier + self.armor_bonus + self.shield + self.boots
        self.weapon_name = weapon_name

    def hud(self):
        os.system('cls')
        print(f"                                                                     Name: {self.name}")
        print(f"                                                                     Level: {self.level}")
        print(f"                                                                     Experience: {self.experience}")
        print(f"                                                                     Gold: {self.gold}")
        print(f"                                                                     Weapon + {self.weapon}")
        print(
            f"                                                                     Armor Class {self.armor_class}")
        print(f"                                                                     Shield + {self.shield}")
        print(
            f"                                                                     Constitution {self.constitution}")
        print(
            f"                                                                     Intelligence: {self.intelligence}")
        print(f"                                                                     Wisdom: {self.wisdom}")
        print(f"                                                                     Strength: {self.strength}")
        print(f"                                                                     Dexterity: {self.dexterity}")
        print(f"                                                                     Charisma: {self.charisma}")
        print(f"                                                                     Hit points: {self.hit_points}/"
              f"{self.maximum_hit_points}")
        if self.boots == 0:
            print(f"                                                                     Boots: Leather")
        else:
            print(
                f"                                                                     Boots: Elven Boots + {self.boots}")
        if self.cloak == 0:
            print(f"                                                                     Cloak: none")
        else:
            print(
                f"                                                                     Cloak: Elven Cloak + {self.boots}")

    def calculate_proficiency_bonus(self):
        if self.level <= 4:
            self.proficiency_bonus = 2
        if self.level > 4 < 9:
            self.proficiency_bonus = 3
        if self.level > 8 < 13:
            self.proficiency_bonus = 4
        if self.level > 12 < 17:
            self.proficiency_bonus = 5
        if self.level > 16:
            self.proficiency_bonus = 6

    def calculate_current_level(self):
        if self.experience < 300:
            self.level = 1
        if self.experience >= 300 < 900:
            self.level = 2
        if self.experience >= 900 < 2700:
            self.level = 3
        if self.experience >= 2700 < 6500:
            self.level = 4
        if self.experience >= 6500 < 14000:
            self.level = 5
        if self.experience >= 14000 < 23000:
            self.level = 6
        if self.experience >= 23000 < 34000:
            self.level = 7
        if self.experience >= 34000 < 48000:
            self.level = 8
        if self.experience >= 48000 < 64000:
            self.level = 9
        if self.experience >= 64000 < 85000:
            self.level = 10
        if self.experience >= 85000 < 100000:
            self.level = 11
        if self.experience >= 100000 < 120000:
            self.level = 12
        if self.experience >= 120000 < 140000:
            self.level = 13
        if self.experience >= 140000 < 165000:
            self.level = 14
        if self.experience >= 165000 < 195000:
            self.level = 15
        if self.experience >= 195000 < 225000:
            self.level = 16
        if self.experience >= 225000 < 265000:
            self.level = 17
        if self.experience >= 265000 < 305000:
            self.level = 18
        if self.experience >= 305000 < 355000:
            self.level = 19
        if self.experience >= 355000:
            self.level = 20
        return

    def increase_experience(self, exp_award):
        self.experience += exp_award
        return

    def level_up(self, exp_award, monster_gold):
        self.gold += monster_gold
        before_level = self.level
        before_proficiency_bonus = self.proficiency_bonus
        self.increase_experience(exp_award)  # EXPERIENCE UP!!
        self.calculate_current_level()
        self.calculate_proficiency_bonus()
        after_proficiency_bonus = self.proficiency_bonus
        after_level = self.level
        if after_level > before_level:
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\sound.wav', winsound.SND_ASYNC)
            print(f"You went up a level!!")
            time.sleep(2)
            print(f"You are now level {self.level}.")
            time.sleep(2)
            self.calculate_proficiency_bonus()  # according to DnD 5e
            gain_hit_points = dice_roll(1, self.hit_dice) + self.constitution_modifier
            if gain_hit_points < 1:
                gain_hit_points = 1
            self.hit_points += gain_hit_points  # (previous HP + Hit Die roll + CON modifier)
            self.maximum_hit_points += gain_hit_points
            print(f"You gain {gain_hit_points} hit points")
            time.sleep(2)
            if self.level == 5:
                print("You gain the Extra Attack skill!!")
                time.sleep(2)
            if after_proficiency_bonus > before_proficiency_bonus:
                print(f"Your proficiency bonus increases from {before_proficiency_bonus} to {after_proficiency_bonus}!")
                time.sleep(2)
            print(f"You snarf {monster_gold} gold pieces and gain {exp_award} experience points.")
            time.sleep(2)
            self.hud()
        else:
            print(f"You snarf {monster_gold} gold pieces and gain {exp_award} experience points")
            time.sleep(2)
            self.hud()

    def monster_likes_you(self, name, monster_intel):
        if dice_roll(1, 20) == 20 and monster_intel > 8 and self.charisma > 15:
            print(f"The {name} likes you!")
            gift_item = dice_roll(1, 5)
            if gift_item == 1:
                self.armor_bonus += 1
                print(f"He gives you quantum armor + {self.armor_bonus}!")
                return True
            if gift_item == 2:
                self.shield += 1
                print(f"He gives you a quantum shield + {self.shield}!")
                return True
            if gift_item == 3:
                self.weapon += 1
                print(f"He gives you a quantum sword + {self.weapon}!")
                return True
            if gift_item == 4:
                self.boots += 1
                print(f"He gives you Elven boots + {self.boots}!")
                return True
            if gift_item == 5:
                self.cloak += 1
                print(f"He gives you an Elven cloak + {self.cloak}!")
                return True
        else:
            return False

    def reduce_health(self, damage):
        self.hit_points -= damage
        return  # damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def swing(self, name, level, dexterity, strength, weapon, monster_level, monster_name, monster_dexterity,
              monster_armor_class):
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"You strike at the {monster_name}..")
        # print(f"{name} rolls 20 sided die---> {roll_d20}")
        time.sleep(1)
        if roll_d20 == 1:
            print("You missed.")
            # print(f"You rolled a 1. 1 means failure..")
            time.sleep(1)
            return 0
        # print(f"Dexterity modifier {self.dexterity_modifier}\nProficiency bonus {self.proficiency_bonus}")
        # print(f"Monster armor class {monster_armor_class}")
        if roll_d20 == 20 or roll_d20 + self.proficiency_bonus + self.dexterity_modifier >= monster_armor_class:
            damage_roll = dice_roll(self.level, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + weapon)
            if damage_to_opponent > 0:
                print(f"You hit!")
                time.sleep(1)
                '''print(f"{name} rolls {self.hit_dice} sided hit dice---> {damage_roll} + weapon bonus {weapon} "
                      f"+ {self.strength_modifier} "
                      f"Strength modifier = {damage_to_opponent} ")'''
                print(f"You do {damage_to_opponent} points of damage!")
                time.sleep(2)
                self.hud()
                return damage_to_opponent
            else:
                print(f"It blocks!")  # zero damage result
                time.sleep(1)
                return 0
        elif self.level > 4:
            print("You missed..")
            time.sleep(2)
            print("Extra Attack Skill chance to hit!")
            time.sleep(2)
            damage_roll = dice_roll(self.level, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + weapon) + 1
            print(f"You manage an off-balance attack for {damage_to_opponent} points of damage!")
            time.sleep(2)
            self.hud()
            return damage_to_opponent
        else:
            print(f"You missed...")
            return 0

    def evade(self, monster_name, monster_dexterity):
        evade_success = dice_roll(1, 20)
        if evade_success + self.dexterity_modifier >= monster_dexterity or evade_success == 20:
            print(f"You successfully evade the {monster_name}.")
            return True


'''
In most cases, your AC will be equal to 10 + your DEX modifier + bonus from armor + bonus from magic items/effects.

Fighter
As a Fighter, you gain the following Class Features.

Hit Points
Hit Dice: 1d10 per Fighter level
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st

Starting Proficiencies
You are proficient with the following items, in addition to any Proficiencies provided by your race or Background.

Armor: Light Armor, Medium Armor, Heavy Armor, Shields
Weapons: simple Weapons, martial Weapons
Tools: none
Saving Throws: Strength, Constitution
Skills: Choose two Skills from Acrobatics, Animal Handling, Athletics, History, 
Insight, Intimidation, Perception, and Survival

Starting Equipment
You start with the following items, plus anything provided by your Background.

• (a) Chain Mail or (b) Leather Armor, Longbow, and 20 Arrows
• (a) a martial weapon and a Shield or (b) two martial Weapons
• (a) a Light Crossbow and 20 bolts or (b) two handaxes
• (a) a Dungeoneer's Pack or (b) an Explorer's Pack

Table: The Fighter
Level	Proficiency Bonus	Bonus Features
1st	+2	Fighting Style, Second Wind
2nd	+2	Action Surge (one use)
3rd	+2	Martial Archetype
4th	+2	Ability Score Improvement
5th	+3	Extra Attack
6th	+3	Ability Score Improvement
7th	+3	Martial Archetype feature
8th	+3	Ability Score Improvement
9th	+4	Indomitable (one use)
10th	+4	Martial Archetype feature
11th	+4	Extra Attack (2)
12th	+4	Ability Score Improvement
13th	+5	Indomitable (two uses)
14th	+5	Ability Score Improvement
15th	+5	Martial Archetype feature
16th	+5	Ability Score Improvement
17th	+6	Action Surge (two uses), Indomitable (three uses)
18th	+6	Martial Archetype feature
19th	+6	Ability Score Improvement
20th	+6	Extra Attack (3)
Fighting Style
You adopt a particular style of Fighting as your specialty. Choose a Fighting style from the list of optional features.
 You can't take the same Fighting Style option more than once, even if you get to choose again.
Archery
You gain a +2 bonus to Attack rolls you make with ranged Weapons.

Defense
While you are wearing armor, you gain a +1 bonus to AC.

Dueling
When you are wielding a melee weapon in one hand and no other Weapons, 
you gain a +2 bonus to Damage Rolls with that weapon.

Great Weapon Fighting
When you roll a 1 or 2 on a damage die for an Attack you make with a melee weapon that you are wielding with two hands,
 you can Reroll the die and must use the new roll, even if the new roll is a 1 or a 2. 
 The weapon must have the Two-Handed or Versatile property for you to gain this benefit.

Protection
When a creature you can see attacks a target other than you that is within 5 feet of you,

you can use your Reaction to impose disadvantage on the Attack roll. You must be wielding a Shield.

Two-Weapon Fighting
When you engage in two-weapon Fighting, you can add your ability modifier to the damage of the second Attack.

Second Wind
You have a limited well of stamina that you can draw on to protect yourself from harm. On Your Turn, 
you can use a bonus Action to regain Hit Points equal to 1d10 + your Fighter level.

Once you use this feature, you must finish a short or Long Rest before you can use it again.

Action Surge
Starting at 2nd Level, you can push yourself beyond your normal limits for a moment. On Your Turn, 
you can take one additional Action on top of your regular Action and a possible bonus Action.

Once you use this feature, you must finish a short or Long Rest before you can use it again. Starting at 17th level, 
you can use it twice before a rest, but only once on the same turn.

Martial Archetype
At 3rd Level, you choose an archetype that you strive to emulate in your Combat styles and Techniques, 
such as Champion. The archetype you choose grants you features at 3rd Level 
and again at 7th, 10th, 15th, and 18th level.

Ability Score Improvement
When you reach 4th Level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, 
you can increase one ability score of your choice by 2, or you can increase two Ability Scores of your choice by 1. 
As normal, you can’t increase an ability score above 20 using this feature.

Extra Attack
Beginning at 5th Level, you can Attack twice, instead of once, whenever you take the Attack Action on Your Turn.

The number of attacks increases to three when you reach 11th level in this class 
and to four when you reach 20th level in this class.

Indomitable
Beginning at 9th level, you can Reroll a saving throw that you fail.
 If you do so, you must use the new roll, and you can't use this feature again until you finish a Long Rest.

You can use this feature twice between long rests starting at 13th level 
and three times between long rests starting at 17th level.

Martial Archetypes
Different fighters choose different approaches to perfecting their Fighting Prowess. 
The Martial Archetype you choose to emulate reflects your approach.

Champion
The archetypal Champion focuses on the Development of raw physical power honed to deadly perfection.
 Those who model themselves on this archetype combine rigorous Training with physical excellence 
 to deal devastating blows.

Improved Critical
Beginning when you choose this archetype at 3rd Level, your weapon attacks score a critical hit on a roll of 19 or 20.

Remarkable Athlete
Starting at 7th level, you can add half your Proficiency bonus (round up) to any Strength, 
Dexterity, or Constitution check you make that doesn’t already use your Proficiency bonus.

In addition, when you make a running Long Jump, the distance you can cover increases 
by a number of feet equal to your Strength modifier.

Additional Fighting Style
At 10th level, you can choose a second option from the Fighting Style class feature.

Superior Critical
Starting at 15th level, your weapon attacks score a critical hit on a roll of 18–20.

Survivor
At 18th level, you attain the pinnacle of resilience in battle. 
At the start of each of your turns, you regain Hit Points equal to 5 + your Constitution modifier,
 if you have no more than half of your Hit Points left.

You don’t gain this benefit if you have 0 Hit Points.
Attributes
Hit Die
d10
Starting Gold
5d4 x 10
Subclass Name
Martial Archetype
Suggested Abilities
Strength or Dexterity, Constitution or Intelligence
Experience Points	Level	Proficiency Bonus
0	                1	    +2
300	                2	    +2
900	                3	    +2
2,700	            4	    +2
6,500	            5	    +3
14,000	            6	    +3
23,000	            7	    +3
34,000	            8	    +3
48,000	            9	    +4
64,000	            10	    +4
85,000	            11	    +4
100,000	            12	    +4
120,000	            13	    +5
140,000	            14	    +5
165,000	            15	    +5
195,000	            16	    +5
225,000	            17	    +6
265,000	            18	    +6
305,000	            19	    +6
355,000	            20	    +6
'''
