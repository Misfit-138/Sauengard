"""

Choose a challenge rating (CR) for your trap, object, effect, or creature
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

Difficulty Class (DC) is something that’s used a lot. Whether that’s Saving Throws or Ability Checks.
Even Armor Class is a kind of DC. To put it simply, a DC determines how hard something is to do.
Whether that’s climbing a rope, evading a breath weapon, or swinging an ax, different actions have different DCs.

To determine whether you beat a DC, you need to roll equal to or higher than said DC.
But choosing how hard one is, is easier said than done. For example, walking across a treacherous rope bridge without
falling might take a DC 15 Dexterity (Acrobatics) check, but resisting a Wolf knocking you prone takes
a DC 11 Strength Saving Throw.

Many spells require Saving Throws and ability checks to negate but don’t even tell you what the DC is.
That’s because the DC equals 8 + Your Spellcasting Modifier + Your Proficiency Bonus.
And most other classes or features that require Saving Throws typically tell you how to calculate the DC or even
tell you what the DC is outright!

But what if it’s something you make that requires a DC to be set, like an ability check? For that,
you can use the following values as a guide (DMG p. 238):

TASK	            DC
Very easy	        5
Easy	            10
Moderate	        15
Hard	            20
Very Hard	        25
Nearly Impossible	30

A few things to know; however, a natural 20 doesn’t mean you automatically succeed.
You still have to add your bonuses, but it usually results in the most favorable outcome,
even though you can’t crit on ability checks. Likewise,
a natural 1 doesn’t mean automatic failure or a critical failure.
You could still pass the check if your bonuses are high enough. And on the note of failing a Check, the DM could still
have it succeed, but just at a cost (e.g., you leap across the chasm, but you break your leg on the ledge as you didn’t
land properly).

As you can see, it’s not that bad when you think about it. A DC is just a minimum result needed to perform a particular
task and succeed with minimal loss. And so with that, I hope you roll high and low in the best of moments!
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
For example, if a monster has a Constitution of 12 (+1 modifier)
and 2d8 Hit Dice, it has 2d8 + 2 Hit Points (average 11).

Adult Red Dragon
Huge dragon, chaotic evil
Armor Class 19 (Natural Armor)
Hit Points 256 (19d12+133)
Speed 40 ft., climb 40 ft., fly 80 ft.
STR 27 (+8)
DEX 10 (+0)
CON 25 (+7)
INT 16 (+3)
WIS 13 (+1)
CHA 21 (+5)
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st
# MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]
average treasure per encounter per level:
1-75.15
2-107.15
3-151.9
4-209.6
5-280
6-376
7-536
8-760
9-1048
10-1400
11-1880
12-2680
13-3800
14-5240
15-7000
16-9400
17-13400
18-19000
19-26200
20-35000
21-47000
22-67000
23-95000
24-131000
25-175000
26-235000
27-285000
28-325000
29-355000
30-437500

"""
import math
import os
import random
import time

# from player_module_testing import *  # sikira, torbron, magnus, vozzbozz

# from dice_roll_module import dice_roll

'''Choose a challenge rating (CR) for your custom trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)'''


def dice_roll(no_of_dice, no_of_sides):
    dice_rolls = []  # create list for multiple die rolls
    for dice in range(no_of_dice):  # (1 hit die per level according to DnD 5E rules)
        dice_rolls.append(random.randint(1, no_of_sides))
    your_roll_sum = sum(dice_rolls)
    return your_roll_sum


# # monsters have Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma
def pause():
    if os.name == 'nt':
        # print("You're on Windows. Program should work")
        os.system('pause')
    else:
        input("Strike [ENTER] to continue. . .")


def convert_list_to_string_with_commas_only(list1):
    return str(list1).replace('[', '').replace(']', '').replace("'", "")


def reduce_npc_health(npc, damage):
    npc.hit_points -= damage


class Monster:

    def __init__(self):
        self.monster = "Super class"
        self.name = ""
        self.proper_name = ""
        self.level = 0
        self.experience_award = 0
        self.gold = 0
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.armor_class = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.hit_points = 0
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 0  # tiny d4, small d6, medium d8, large d10, huge d12, gargantuan d20
        self.number_of_hd = self.level
        self.human_player_level = 0
        self.difficulty_class = 0
        self.proficiency_bonus = 0  # 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 0
        self.dexterity_modifier = 0
        self.strength_modifier = 0
        self.constitution_modifier = 0
        self.wisdom_modifier = 0
        self.multi_attack = False
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
        self.quantum_attack_1 = 0
        self.quantum_attack_1_phrase = ""
        self.quantum_attack_2 = 0
        self.quantum_attack_2_phrase = ""
        self.quantum_attack_3 = 0
        self.quantum_attack_3_phrase = ""
        self.quantum_attack_4 = 0
        self.quantum_attack_4_phrase = ""
        self.quantum_attack_5 = 0
        self.quantum_attack_5_phrase = ""
        self.introduction = ""
        self.paralyze_phrase = ""
        self.paralyze_free_attack_phrase = ""
        self.poison_phrase = ""
        self.is_discovered = False

    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def initiative(self):
        # if self.level > 6:
        #    monster_initiative = dice_roll(1, 20) + self.dexterity_modifier + self.proficiency_bonus
        # else:
        monster_initiative = dice_roll(1, 20) + self.dexterity_modifier
        return monster_initiative

    def monster_data(self):
        if self.proper_name == "None":
            mon_data = f"{self.name}  Challenge Lvl: {self.level}  AC: {self.armor_class}  HP: {self.hit_points}  ({self.number_of_hd}d{self.hit_dice})"
        else:
            mon_data = f"{self.proper_name}  AC: {self.armor_class}  HP: {self.hit_points}  ({self.number_of_hd}d{self.hit_dice})"
        if self.undead:
            print(f"{mon_data} (UNDEAD)")
        else:
            print(f"{mon_data}")
        if len(self.immunities):
            # immunities = str(self.immunities).replace('[', '').replace(']', '').replace("'", "")
            immunities = convert_list_to_string_with_commas_only(self.immunities)
            print("Immunities:", immunities)
        if len(self.resistances):
            # immunities = str(self.immunities).replace('[', '').replace(']', '').replace("'", "")
            resistances = convert_list_to_string_with_commas_only(self.resistances)
            print("Resistances:", resistances)
        if len(self.vulnerabilities):
            # vulnerabilities = str(self.vulnerabilities).replace('[', '').replace(']', '').replace("'", "")
            vulnerabilities = convert_list_to_string_with_commas_only(self.vulnerabilities)
            print("Vulnerabilities:", vulnerabilities)

    def melee(self, player_1):
        attack_bonus = 0
        attack_bonus_roll = random.randint(1, 100)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing
        attack_phrase = ""
        if attack_bonus_roll <= 50:
            attack_bonus = self.attack_1
            attack_phrase = self.attack_1_phrase
        if attack_bonus_roll > 50 <= 75:
            attack_bonus = self.attack_2
            attack_phrase = self.attack_2_phrase
        if attack_bonus_roll > 75 <= 85:
            attack_bonus = self.attack_3
            attack_phrase = self.attack_3_phrase
        if attack_bonus_roll > 85 <= 95:
            attack_bonus = self.attack_4
            attack_phrase = self.attack_4_phrase
        if attack_bonus_roll > 95:
            attack_bonus = self.attack_5
            attack_phrase = self.attack_5_phrase

        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks you! (It rolls {roll_d20})")
        if roll_d20 == 1:
            print(f"..it awkwardly strikes and you easily block.")
            # time.sleep(2)
            # os.system('pause')
            pause()
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = ""
        monster_total = roll_d20 + self.dexterity_modifier + self.proficiency_bonus  # test out pro bonus
        print(f"Monster attack bonus: {attack_bonus}")
        print(f"{self.name} dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # test out pro bonus
        print(f"Monster Total: {monster_total}")
        print(f"Your armor class: {player_1.armor_class}")
        if monster_total >= player_1.armor_class:
            damage_roll = dice_roll((self.number_of_hd * critical_bonus), self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)
            if roll_d20 == 20 and damage_to_opponent < 1:
                damage_to_opponent = 1  # a natural 20 must always hit - 5e rules
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice}: {damage_roll}")  # hit dice
                time.sleep(1.5)
                print(f"Strength modifier: {self.strength_modifier}\nAttack bonus: {attack_bonus}\n"
                      f"Weapon bonus: {self.weapon_bonus}")
                time.sleep(1.5)
                print(f"You suffer {damage_to_opponent} points of damage!")
                pause()
                # time.sleep(5)
                return damage_to_opponent
            else:
                # zero damage to player result
                print(f"The {self.name} strikes..")
                time.sleep(1)
                print(f"Its awkward attack manages 1 point of damage..")
                damage_to_opponent = 1
                pause()
                return damage_to_opponent  # 0 points damage to player
        else:
            print(f"It missed..")
            pause()
            return 0

    def quantum_energy_attack(self, player_1):
        attack_bonus = 0
        attack_phrase = ""
        attack_bonus_roll = random.randint(1, 100)
        if attack_bonus_roll <= 50:
            attack_bonus = self.quantum_attack_1
            attack_phrase = self.quantum_attack_1_phrase
        if attack_bonus_roll > 50 <= 75:
            attack_bonus = self.quantum_attack_2
            attack_phrase = self.quantum_attack_2_phrase
        if attack_bonus_roll > 75 <= 85:
            attack_bonus = self.quantum_attack_3
            attack_phrase = self.quantum_attack_3_phrase
        if attack_bonus_roll > 85 <= 95:
            attack_bonus = self.quantum_attack_4
            attack_phrase = self.quantum_attack_4_phrase
        if attack_bonus_roll > 95:
            attack_bonus = self.quantum_attack_5
            attack_phrase = self.quantum_attack_5_phrase
        human_player_roll_d20 = dice_roll(1, 20)
        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks you with Quantum Energy!\n"
              f"(It rolls {roll_d20})\n"
              f"Proficiency Bonus: {self.proficiency_bonus}\n"
              f"Wisdom modifier: {self.wisdom_modifier}\n"
              f"Total: {roll_d20 + self.wisdom_modifier + self.proficiency_bonus}")
        if roll_d20 == 1:
            print(f"..its attempts to procure the universal forces fail miserably.")
            time.sleep(2)
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = ""
        # print(f"{self.name} Wisdom modifier {self.wisdom_modifier}")  # MONSTER WISDOM MODIFIER
        print(f"Your Saving Throw: {human_player_roll_d20} + wisdom modifier: ({player_1.wisdom_modifier})")
        if player_1.ring_of_prot.protect > 0:
            print(f"Your Ring of Protection Modifier: {player_1.ring_of_prot.protect}")
        if player_1.temp_protection_effect:
            print(f"+ Quantum Protection effect: {player_1.temp_protection_effect} ")
        print(
            f"Total = {human_player_roll_d20 + player_1.wisdom_modifier + player_1.ring_of_prot.protect + player_1.temp_protection_effect}")
        monster_total = roll_d20 + self.wisdom_modifier + self.proficiency_bonus  # test out pro bonus
        if monster_total >= (human_player_roll_d20 + player_1.wisdom_modifier +
                             player_1.ring_of_prot.protect + player_1.temp_protection_effect):

            damage_roll = dice_roll(self.number_of_hd * critical_bonus, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.wisdom_modifier + attack_bonus)
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice} hit dice: {damage_roll}")
                print(f"Wisdom modifier: {self.wisdom_modifier}\nAttack bonus: {attack_bonus}")
                print(f"You suffer {damage_to_opponent} points of damage!")
                pause()
                # time.sleep(5)
                return damage_to_opponent
            else:
                print(
                    f"The {self.name} strikes with Quantum Powers, but you dodge the attack!")  # zero damage to player result
                time.sleep(2)
                return 0  # 0 points damage to player
        else:
            print(f"It fails to harness the mysterious powers..")
            pause()
            return 0

    def paralyze(self, player_1):
        print(self.paralyze_phrase)
        time.sleep(1.25)
        paralyze_chance = dice_roll(1, 20)
        human_player_roll_d20 = dice_roll(1, 20)
        player_total = (human_player_roll_d20 + player_1.ring_of_prot.protect + player_1.temp_protection_effect)
        print(
            f"Paralyze roll: {paralyze_chance} + monster wisdom modifier: {self.wisdom_modifier}")  # remove after testing
        paralyze_total = paralyze_chance + self.wisdom_modifier
        print(f"Monster Total: {paralyze_total}")
        print(
            f"Your Saving Throw: {human_player_roll_d20} ")  # remove after testing
        if player_1.ring_of_prot.protect > 0:
            print(f"Your Ring of Protection Modifier: {player_1.ring_of_prot.protect}")
        if player_1.protection_effect:
            print(f"Protection from Evil Effect: {player_1.temp_protection_effect}")
        print(f"Total: {player_total}")
        if (paralyze_chance + self.wisdom_modifier) >= player_total:
            print("You are paralyzed!!")
            time.sleep(1)
            print(self.paralyze_free_attack_phrase)
            # print("As you stand, frozen and defenseless, it savagely gores you!")
            time.sleep(1)
            for i in range(self.paralyze_turns):  # this seems too brutal if paralyze turns is anything but 1!!!
                paralyze_damage = (dice_roll(self.number_of_hd, self.hit_dice) -
                                   (player_1.ring_of_prot.protect + player_1.temp_protection_effect))
                if paralyze_damage < 1:
                    paralyze_damage = self.level
                player_1.reduce_health(paralyze_damage)
                print(f"It strikes at you for {paralyze_damage} points of damage!!")
                time.sleep(1.5)
                player_1.hud()
            # time.sleep(1)
            return True
        else:
            print("You ignore its wiles and break free from its grip!")
            return False

    def poison_attack(self, player_1):
        player_saving_throw = dice_roll(1, 20)
        difficulty_class = (player_saving_throw + player_1.constitution_modifier)
        # (player_1.constitution + player_1.constitution_modifier)
        roll_d20 = dice_roll(1, 20)  # attack roll
        # print(f"The {self.name} hisses in evil glee..")
        print(self.poison_phrase)
        print(f"Attack roll: {roll_d20}")
        time.sleep(1)
        if roll_d20 == 1:
            print("You easily dodge the poison attack!")
            time.sleep(1)
            # print(f"And you perceive it was attempting to poison you!")
            pause()
            player_1.hud()
            return False
        else:
            print(f"Your Saving Throw: {player_saving_throw}\n"
                  f"Your Constitution Modifier: {player_1.constitution_modifier}\n")

            print(f"Total: {difficulty_class}")
            if roll_d20 == 20 or roll_d20 >= difficulty_class:  # self.constitution + self.constitution_modifier:
                # return True
                # self.hud()
                player_1.dot_multiplier = self.dot_multiplier
                player_1.dot_turns = self.dot_turns
                rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                         "An unnerving frailty spreads throughout your body...",
                                         "Pain and tenderness courses through your body.."
                                         ]
                poisoned_phrase = random.choice(rndm_poisoned_phrases)
                print(f"{poisoned_phrase}")
                time.sleep(1.5)
                print(f"You have been poisoned!")
                player_1.poisoned = True
                player_1.poisoned_turns = 0
                # self.calculate_poison()
                pause()
                # self.dungeon_description()
                # self.hud()
                return player_1.poisoned
            else:
                print(f"You swiftly dodge its poison attack!")
                time.sleep(1)
                pause()
                player_1.hud()
                return False

    def necrotic_attack(self, player_1):
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {self.name} attempts to harness its innate understanding of quantum necrosis..")
        print(f"Attack roll---> {roll_d20}")
        time.sleep(1)
        if roll_d20 == 1:
            print("You dodge the deadly necrotic attack!")
            time.sleep(1)
            pause()
            player_1.hud()
            return False
        else:
            player_saving_throw = (dice_roll(1, 20))
            difficulty_class = (player_saving_throw + player_1.constitution_modifier)
            print(f"Your Saving Throw: {player_saving_throw}\n"
                  f"Your Constitution Modifier: {player_1.constitution_modifier}\n")
            print(f"Total: {difficulty_class}")
            if roll_d20 == 20 or roll_d20 >= difficulty_class:
                player_1.dot_multiplier = self.dot_multiplier
                player_1.dot_turns = self.dot_turns
                rndm_necrotic_phrases = ["You feel morbid dread and withering overcoming you..",
                                         "An unnerving pain, planted like a seed, germinates within you...",
                                         "Agony creeps into your very veins..."
                                         ]
                necrotic_phrase = random.choice(rndm_necrotic_phrases)
                print(f"{necrotic_phrase}")
                time.sleep(1.5)
                print(f"Necrotic forces ravage through your body!")
                player_1.necrotic = True
                player_1.necrotic_turns = 0
                pause()
                player_1.hud()
                return player_1.necrotic
            else:
                print(f"You swiftly dodge its death-dealing necrotic attack!")
                time.sleep(1)
                pause()
                player_1.hud()
                return False

    def meta_monster_vs_npc_function(self, npc):
        # print(npc.retreating)
        if not npc.retreating:
            melee_or_quantum = dice_roll(1, 20)
            # if monster has quantum energy
            if self.quantum_energy and melee_or_quantum > 10:
                # quantum attack
                damage_to_player = self.quantum_energy_attack_vs_npc(npc)
                reduce_npc_health(npc, damage_to_player)
            else:
                # if it has no quantum, then melee attack
                damage_to_player = self.melee_vs_npc(npc)
                reduce_npc_health(npc, damage_to_player)
            return
        else:
            # print(f"{npc.name} is in retreat...")
            # time.sleep(1)
            return

    def meta_monster_function(self, player_1):
        melee_or_quantum = dice_roll(1, 20)
        # if monster has quantum energy and player is not poisoned or necrotic
        if self.quantum_energy and melee_or_quantum > 10 and not player_1.poisoned \
                and not player_1.necrotic:
            if not self.can_poison and not self.necrotic:  # quantum attack if no necrotic or poison abilities
                damage_to_player = self.quantum_energy_attack(player_1)
                player_1.reduce_health(damage_to_player)
                player_1.end_of_turn_calculation()
            elif self.can_poison and self.necrotic:  # if monster has both poison
                poison_or_necrotic = dice_roll(1, 20)  # and necrotic damage,
                if poison_or_necrotic > 10:  # greater than 10 for poison
                    self.poison_attack(player_1)  # player_1.poison_attack(self.name, self.dot_multiplier)
                else:
                    self.necrotic_attack(player_1)  # player_1.necrotic_attack(self)
            elif self.can_poison:  # otherwise, if it can only poison, then attempt poison
                self.poison_attack(player_1)  # player_1.poison_attack(self.name, self.dot_multiplier)
                player_1.end_of_turn_calculation()
            elif self.necrotic:  # otherwise if it only has necrotic, then attempt necrotic
                self.necrotic_attack(player_1)
                player_1.end_of_turn_calculation()
        else:
            # if it has neither, then melee attack
            damage_to_player = self.melee(player_1)
            player_1.reduce_health(damage_to_player)
            player_1.end_of_turn_calculation()
        return

    def melee_vs_npc(self, npc):
        attack_bonus = 0
        attack_bonus_roll = random.randint(1, 100)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing
        attack_phrase = f"The {self.name} hits!"
        if attack_bonus_roll <= 50:
            attack_bonus = self.attack_1
        if attack_bonus_roll > 50 <= 75:
            attack_bonus = self.attack_2
        if attack_bonus_roll > 75 <= 85:
            attack_bonus = self.attack_3
        if attack_bonus_roll > 85 <= 95:
            attack_bonus = self.attack_4
        if attack_bonus_roll > 95:
            attack_bonus = self.attack_5
        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks {npc.name}! (It rolls {roll_d20})")
        if roll_d20 == 1:
            print(f"..it awkwardly strikes and {npc.name} easily blocks.")
            # time.sleep(2)
            # os.system('pause')
            pause()

            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = ""
        monster_total = roll_d20 + self.dexterity_modifier + self.proficiency_bonus  # test out pro bonus
        print(f"Monster attack bonus: {attack_bonus}")
        print(f"{self.name} dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # test out pro bonus
        print(f"Monster Total: {monster_total}")
        print(f"{npc.name}'s armor class: {npc.armor_class}")
        if monster_total >= npc.armor_class:
            damage_roll = dice_roll((self.number_of_hd * critical_bonus), self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)
            if roll_d20 == 20 and damage_to_opponent < 1:
                damage_to_opponent = 1  # a natural 20 always hits
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice}: {damage_roll}")  # hd
                time.sleep(1.5)
                print(f"Strength modifier: {self.strength_modifier}\nAttack bonus: {attack_bonus}\n"
                      f"Weapon bonus: {self.weapon_bonus}")
                time.sleep(1.5)
                print(f"{npc.name} suffers {damage_to_opponent} points of damage!")
                pause()

                return damage_to_opponent
            else:
                # zero damage to player result
                print(f"The {self.name} strikes..")
                time.sleep(1)
                print(f"Its awkward attack manages 1 point of damage to {npc.name}..")
                damage_to_opponent = 1
                pause()
                return damage_to_opponent  # 0 points damage to player
        else:
            print(f"It missed..")
            pause()
            return 0

    def quantum_energy_attack_vs_npc(self, npc):
        attack_bonus = 0
        attack_phrase = f"With great concentration, it procures the weird universal forces.."
        attack_bonus_roll = random.randint(1, 100)
        if attack_bonus_roll <= 50:
            attack_bonus = self.quantum_attack_1

        if attack_bonus_roll > 50 <= 75:
            attack_bonus = self.quantum_attack_2

        if attack_bonus_roll > 75 <= 85:
            attack_bonus = self.quantum_attack_3

        if attack_bonus_roll > 85 <= 95:
            attack_bonus = self.quantum_attack_4

        if attack_bonus_roll > 95:
            attack_bonus = self.quantum_attack_5

        human_player_roll_d20 = dice_roll(1, 20)
        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks {npc.name} with Quantum Energy!\n"
              f"(It rolls {roll_d20})\n"
              f"Proficiency Bonus: {self.proficiency_bonus}\n"
              f"Wisdom modifier: {self.wisdom_modifier}\n"
              f"Total: {roll_d20 + self.wisdom_modifier + self.proficiency_bonus}")
        if roll_d20 == 1:
            print(f"..its attempts to procure the universal forces fail miserably.")
            time.sleep(2)
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = f"The weird energies are unleashed upon {npc.name}.."
        # print(f"{self.name} Wisdom modifier {self.wisdom_modifier}")  # MONSTER WISDOM MODIFIER
        print(f"{npc.name} Saving Throw: {human_player_roll_d20} + wisdom modifier: ({npc.wisdom_modifier})")
        if npc.protect > 0:
            print(f"Protection Modifier: {npc.protect}")

        print(
            f"Total = {human_player_roll_d20 + npc.wisdom_modifier + npc.protect}")
        monster_total = roll_d20 + self.wisdom_modifier + self.proficiency_bonus  # test out pro bonus
        if monster_total >= (human_player_roll_d20 + npc.wisdom_modifier +
                             npc.protect):

            damage_roll = dice_roll(self.number_of_hd * critical_bonus, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.wisdom_modifier + attack_bonus)
            if damage_to_opponent > 0:  # # at this point the npc is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice} hit dice: {damage_roll}")
                print(f"Wisdom modifier: {self.wisdom_modifier}\nAttack bonus: {attack_bonus}")
                print(f"{npc.name} suffers {damage_to_opponent} points of damage!")
                pause()
                # time.sleep(5)
                return damage_to_opponent
            else:
                print(
                    f"The {self.name} strikes with Quantum Powers, but {npc.name} dodges the attack!")  # 0 damage
                time.sleep(2)
                return 0  # 0 points damage to player
        else:
            print(f"It fails to harness the mysterious powers..")
            pause()
            return 0


class Quasit(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Quasit"
        self.proper_name = "None"
        self.experience_award = 25
        self.gold = random.randint(0, 1)  # self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(4, 6)
        self.dexterity = random.randint(16, 17)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(9, 10)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # tiny
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It polymorphs into toad form.."
        self.attack_2 = 0
        self.attack_2_phrase = "It polymorphs into centipede form and rears up.."
        self.attack_3 = 1
        self.attack_3_phrase = "It polymorphs into bat form and darts at you with gaping jaws!."
        self.attack_4 = 3
        self.attack_4_phrase = "Croaking in disturbing malice, it swings its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "With blinding speed, it kicks with its hind claws.."
        self.introduction = f"You have encountered a {self.name}.\n" \
                            f"Its large, lidless eyes stare blankly at you as it quickly readjusts its pointed ears\n" \
                            f"with a continual twitching. Its long, serpentine tail wags with its sinews and scales\n" \
                            f"as it lets out a high pitched, fiendish and wretched cry. The air around it becomes hazy.."
        self.is_discovered = False

    # name = "Quasit"


class Kobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Kobold"
        self.proper_name = "None"
        self.experience_award = 25
        self.gold = random.randint(1, 3)  # self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(6, 8)
        self.dexterity = random.randint(14, 15)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(7, 8)
        self.wisdom = random.randint(7, 8)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # small
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It quickly strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It thrusts forward and bites with its foaming jaws!"
        self.attack_3 = 2
        self.attack_3_phrase = "It raises its sling to bludgeon you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, it kicks with its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "It whips its tail!"
        self.introduction = f"You have encountered a {self.name}. A short, reptilian creature with orange eyes\n" \
                            f"and skin. Its ragged tunic looks more like a robe on its tiny frame; you have no doubt\n" \
                            f"it was stolen from an unwary adventurer. Its tail stands up as it retrieves a dagger\n" \
                            f"from a brass scabbard, twirling it deftly between scaled, sinewy fingers. It looks\n" \
                            f"you over for items to rid you of!"
        self.is_discovered = False

    # name = "Kobold"


class Cultist(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Cultist"
        self.proper_name = "None"
        self.experience_award = 50
        self.gold = random.randint(2, 8)  # self.level * 373 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(10, 12)
        self.dexterity = random.randint(11, 13)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  #
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(8, 10) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "With unexpected speed, it strikes with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "He swings his gleaming scimitar!"
        self.attack_3 = 2
        self.attack_3_phrase = "It throws an acrid powder at you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, he swings his scimitar.."
        self.attack_5 = 3
        self.attack_5_phrase = "Crying out with insane hatred, he raises his scimitar with both hands in a mighty blow!"
        self.introduction = f"You have encountered a Cultist. Adorned with a foul robe speckled with disgusting\n" \
                            f"symbols, and face hidden in the deep shadow of his cowl, you see his insane eyes\n" \
                            f"smoulder in the darkness. His loyalties long since revealed, he cries out in sworn\n" \
                            f"allegiance to some dark Quantum Manipulator..."
        self.is_discovered = False

    # name = "Cultist"


class Goblin(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Goblin"
        self.proper_name = "None"
        self.experience_award = self.level * 50
        self.gold = random.randint(2, 10)  # self.level * 200 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(7, 9)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(7, 9)
        self.charisma = random.randint(7, 9)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  # mm
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its scimitar.."
        self.attack_2 = 1
        self.attack_2_phrase = "It feints to the side and swings!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its scimitar wildly!"
        self.attack_4 = 2
        self.attack_4_phrase = "It raises its scimitar overhead with both hands for a mighty blow.."
        self.attack_5 = 3
        self.attack_5_phrase = "Its scimitar flashes with impossible speed!"
        self.introduction = f"You have encountered a {self.name}. Hideously foul and ugly, its grimacing flat face\n" \
                            f"wrinkles up as it sniffs the air around you. Its pointed ears twitch and then draw \n" \
                            f"straight up. Smiling wickedly with blackened teeth, it unsheathes a rusty, crooked\n" \
                            f"scimitar and faces you with ill-intent."
        self.is_discovered = False

    # name = "Goblin"


class WingedKobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Winged Kobold"
        self.proper_name = "None"
        self.experience_award = 50
        self.gold = random.randint(1, 5)  # self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(6, 8)
        self.dexterity = random.randint(15, 17)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(8, 10)
        self.wisdom = random.randint(6, 8)
        self.charisma = random.randint(6, 8)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # mm
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "Deadly quick, it strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It thrusts forward and bites with its prognathous jaws!"
        self.attack_3 = 3
        self.attack_3_phrase = "It raises its spear and thrusts forward with a shriek.."
        self.attack_4 = 3
        self.attack_4_phrase = "Feinting with its weapon hand, it kicks at you with its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "It readies its spear and lunges with a growling grunt.."
        self.introduction = f"You have encountered a {self.name}. Standing three feet tall, with short ivory horns\n" \
                            f"and a frail body covered with mottled brick red scales, it grabs its dagger and\n" \
                            f"spreads its leathery, batlike wings."
        self.is_discovered = False

    # "Winged Kobold"


class Shadow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Shadow"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(0, 1)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(5, 6)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(9, 11)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 1
        self.dot_turns = dice_roll(1, 8)
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 2
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(15, 17)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its elongated claws..."
        self.attack_2 = 0
        self.attack_2_phrase = "It raises its arms, lost in blackness, and swings silently..wickedly.."
        self.attack_3 = 1
        self.attack_3_phrase = "It darts forward, rushing with speed, and yet without any sound.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!"
        self.attack_5 = 3
        self.attack_5_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!!"
        self.quantum_attack_1 = 1
        self.quantum_attack_1_phrase = "Its form slithers and strikes at you with terrible outstretched claws\n" \
                                       "in perfect silence. The quantum necrotic aura of its form sends\n" \
                                       "a shockwave through you! "
        self.quantum_attack_2 = 1
        self.quantum_attack_2_phrase = "It thrusts forward, its maw gaping with impossible blackness\n" \
                                       "as the air crackles.."
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "Its amorphous form strikes at you, unleashing terrible necrotic malice.\n" \
                                       "You feel the hairs of your body quivering.."
        self.quantum_attack_4 = 2
        self.quantum_attack_4_phrase = "With a silent scream, it releases a torrent of\n" \
                                       "quantum necrotic energy that rushes toward you!!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "Its looming form towers over you..\n" \
                                       "it clutches you with necrotic malice!"
        self.introduction = f"You have encountered a {self.name}..an unnatural abomination with form,\n" \
                            f"but also, without form.. Its body rises up, absorbing all ambient light into an\n" \
                            f"endless darkness. You intuitively catch glimpses of its actual appearance\n" \
                            f"beneath- impossibly long, bony, outstretched arms extending from wispy black rags,\n" \
                            f"and the hints of a humanoid, skullish face, forever grimacing in confusion over its\n" \
                            f"own existence..\nYou feel the air crackle with quantum energy.."
        self.paralyze_phrase = "Rising menacingly and with both clawed, shadowy hands, it reaches out, and you\n" \
                               "feel your motor skills quivering.."
        self.paralyze_free_attack_phrase = "As you stand frozen and defenseless, the Shadow silently places\n" \
                                           "its hands upon you..a sickening visceral emptiness fills you!"
        self.is_discovered = False

    # name = "Shadow"


class ShadowKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Shadow King"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(5, 10)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(7, 8)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(12, 13)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 8)
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 10  # mm
        self.number_of_hd = 2
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(15, 17)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its elongated claws..."
        self.attack_2 = 0
        self.attack_2_phrase = "It raises its arms, lost in blackness, and swings silently..wickedly.."
        self.attack_3 = 1
        self.attack_3_phrase = "It darts forward, rushing with speed, and yet without any sound.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!"
        self.attack_5 = 3
        self.attack_5_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!!"
        self.quantum_attack_1 = 1
        self.quantum_attack_1_phrase = "Its form slithers and strikes at you with terrible outstretched claws\n" \
                                       "in perfect silence. The quantum necrotic aura of its form sends\n" \
                                       "a shockwave through you! "
        self.quantum_attack_2 = 1
        self.quantum_attack_2_phrase = "It thrusts forward, its maw gaping with impossible blackness\n" \
                                       "as the air crackles.."
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "Its amorphous form strikes at you, unleashing terrible necrotic malice.\n" \
                                       "You feel the hairs of your body quivering.."
        self.quantum_attack_4 = 2
        self.quantum_attack_4_phrase = "With a silent scream, it releases a torrent of\n" \
                                       "quantum necrotic energy that rushes toward you!!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "Its looming form towers over you..\n" \
                                       "it clutches you with necrotic malice!"
        self.introduction = f"From the nothingness you see the {self.name} approach with ancient malice.\n" \
                            f"Its body rises up, absorbing all ambient light into a silhouette of\n" \
                            f"endless darkness. And yet, somehow, you randomly catch glimpses of its actual form\n" \
                            f"beneath- impossibly long, bony, outstretched arms extending from its once\n" \
                            f"royal raiment..a humanoid, skullish face forever grimacing in confusion over its\n" \
                            f"own existence..and lamenting the long lost grandeur of a kingdom now forgotten\n" \
                            f"and erased from the annals of time.\n" \
                            f"You feel the air crackle with quantum energy.."
        self.paralyze_phrase = "Rising menacingly and with both clawed, shadowy hands, it reaches out, and you\n" \
                               "feel your motor skills quivering.."
        self.paralyze_free_attack_phrase = "You feel your life force weakening as it drains you mercilessly!"
        self.is_discovered = False


class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1  # I think level 1 is more appropriate.
        self.name = "Skeleton"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(0, 5)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(9, 11)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(7, 9)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 1  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(11, 13) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its shortsword..."
        self.attack_2 = 1
        self.attack_2_phrase = "It raises its shortsword and swings mightily.."
        self.attack_3 = 2
        self.attack_3_phrase = "It darts forward with unnerving speed, sword in bony hand.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward with its heavy, iron spear!"
        self.attack_5 = 3
        self.attack_5_phrase = "Reaching over its back, it produces a battle axe and strikes wildly!!"
        self.introduction = f"From the ground rises a skeleton warrior. Its battle-scarred and weary weaponry still\n" \
                            f"in hand, it fearlessly hammers its shield with sword, taunting an attack. A full-toothed\n" \
                            f"grin forever emblazoned on its bony countenance, it shouts an absent, yet echoing\n" \
                            f"battle-cry at you from behind its slack, gaping jaw!\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False

    # name = "Skeleton"


class ZombieProphet(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Zombie Prophet"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(6, 15)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(12, 15)
        self.dexterity = random.randint(11, 15)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(12, 13)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(15, 19) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with unnerving strength and speed..."
        self.attack_2 = 1
        self.attack_2_phrase = "It strikes at you with arms flailing..."
        self.attack_3 = 2
        self.attack_3_phrase = "It darts forward with reckless abandon.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward with its heavy, iron sceptre!"
        self.attack_5 = 3
        self.attack_5_phrase = "It strikes wildly with its iron sceptre!!"
        self.introduction = f"The ancient prophet rises from the ground. The once beautiful and exquisite\n" \
                            f"garb now hangs off his rotten, worm-infested flesh in tatters and rags.\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False


class SkeletonKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Skeleton King"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(6, 22)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 2
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 13)
        self.dexterity = random.randint(11, 15)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(11, 13)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(17, 22) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = f"He strikes at you with his longsword..."
        self.attack_2 = 1
        self.attack_2_phrase = f"He raises his longsword and swings mightily.."
        self.attack_3 = 2
        self.attack_3_phrase = f"He darts forward with unnerving speed, longsword in bony hand.."
        self.attack_4 = 2
        self.attack_4_phrase = f"He thrusts forward with his heavy, iron spear!"
        self.attack_5 = 3
        self.attack_5_phrase = f"Reaching over its back, it produces a battle axe and strikes wildly!!"
        self.introduction = f"The ancient king rises in skeletal form. The once gleaming armor and weaponry now\n" \
                            f"clings wearily to his bony form as he raises sword and shield, taunting you to attack!\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False


class SkeletalProphet(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Skeletal Prophet"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(6, 22)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 2
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 13)
        self.dexterity = random.randint(11, 15)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(11, 13)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(17, 22) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = f"He strikes at you with his sceptre..."
        self.attack_2 = 1
        self.attack_2_phrase = f"He raises his sceptre and swings with abandon.."
        self.attack_3 = 2
        self.attack_3_phrase = f"He darts forward in a mad frenzy.."
        self.attack_4 = 2
        self.attack_4_phrase = f"Raising the sceptre overhead, he swings with both bony hands..!"
        self.attack_5 = 3
        self.attack_5_phrase = f"Taunting and glaring through its rottenness, he strikes wildly!!"
        self.introduction = f"The ancient prophet rises in skeletal form. The once spectacular raiment now\n" \
                            f"clings wearily to his bony form as he raises his sceptre, taunting you to attack!\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False


class Drow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Drow"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(5, 12)  # self.level * 300 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(9, 11)
        self.dexterity = random.randint(13, 14)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(10, 12)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(12, 13)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = True
        self.necrotic = True
        self.dot_multiplier = 1
        self.dot_turns = dice_roll(1, 6)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 1  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(12, 14) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "Grabbing its nasty dagger, it darts forward with smooth quickness.."
        self.attack_2 = 1
        self.attack_2_phrase = "Clutching its shortsword, it swings wildly.."
        self.attack_3 = 2
        self.attack_3_phrase = "It raises its sadistic-looking flail.."
        self.attack_4 = 2
        self.attack_4_phrase = "Clutching its shortsword with both black claws, it swings mightily!"
        self.attack_5 = 3
        self.attack_5_phrase = "With blinding speed and unexpected might, it swings its shortsword!!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "It releases weird quantum flames from its outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Weird electrical energies dance over its form as it unleashes a volley\n" \
                                       "of flames and lightning from both of its outstretched hands!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "It cries out in its own foul tongue, harnessing the quantum energies and\n" \
                                       "hurling a wall of crackling lightning toward you!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "Placing its hands together and fidgeting wildly, it releases a growing\n" \
                                       "orb of energy which rushes straight at you!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "Crying out wildly, and thrusting its arms forward, it shoots \n" \
                                       "the weirdness of entangled quantum flames and energies at you!"
        self.introduction = f"You have encountered a {self.name}; A race that, in many ways, resembles other\n" \
                            f"elves, yet, dark, twisted and evil. Its chiseled, attractive face, and wiry,\n" \
                            f"athletic frame belie its true nature."
        self.poison_phrase = "It slashes at you with its poison dagger!!"
        self.is_discovered = False


class Zombie(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Zombie"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(1, 5)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(12, 14)
        self.dexterity = random.randint(6, 8)
        self.constitution = random.randint(15, 17)
        self.intelligence = random.randint(3, 4)
        self.wisdom = random.randint(6, 7)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 1  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(22, 25) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(8, 9)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its gaping hands..."
        self.attack_2 = 1
        self.attack_2_phrase = "It raises its club and swings awkwardly.."
        self.attack_3 = 2
        self.attack_3_phrase = "It staggers forward with its club.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward with surprising speed.."
        self.attack_5 = 3
        self.attack_5_phrase = "It gropes for you, jaws chomping, it anticipation of flesh!"
        self.introduction = f"From the ground rises a languishing zombie. Lurching with jerking, uneven gait\n" \
                            f"and befouled with the stench of putrefaction, it mindlessly approaches, deaf, mute\n" \
                            f"and blind- and yet somehow, consumed with murderous intent."
        self.is_discovered = False


class Troglodyte(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Troglodyte"
        self.proper_name = "None"
        self.experience_award = 50
        self.gold = random.randint(2, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 2
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(13, 15)
        self.dexterity = random.randint(9, 11)
        self.constitution = random.randint(13, 15)
        self.intelligence = random.randint(6, 7)
        self.wisdom = random.randint(9, 11)
        self.charisma = random.randint(5, 7)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # mm
        self.number_of_hd = 2  # mm says 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(12, 14)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its greataxe.."
        self.attack_2 = 1
        self.attack_2_phrase = "It swings its greataxe with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its mace!"
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts mightily forward with its spear!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its greataxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Troglodyte; a horrid reptilian humanoid. Short, with spindly\n" \
                            f"but muscular arms and squat legs and a long, slender tail which raises at the site\n" \
                            f"you, its eyes light up in malicious glee."
        self.is_discovered = False

    # "Troglodyte"


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Orc"
        self.proper_name = "None"
        self.experience_award = 100
        self.gold = random.randint(5, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = random.randint(11, 14)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 12  # MM says should be 1d12
        self.number_of_hd = 1  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(11, 13)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.attack_1 = 1  # attack bonus
        self.attack_1_phrase = "It thrusts mightily forward with its spear!.."
        self.attack_2 = 2
        self.attack_2_phrase = "It swings its greataxe with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its greataxe with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "It roars and swings its greataxe with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its greataxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a savage Orc. Stooping forward with its piggish face " \
                            f"and prominent teeth,\nit prepares to satisfy its bloodlust by slaying any " \
                            f"humanoids that stand against it.."
        self.is_discovered = False

    # name = "Orc"


class CultFanatic(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Cult Fanatic"
        self.proper_name = "None"
        self.experience_award = 450
        self.gold = random.randint(2, 8)  # self.level * 373 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(10, 12)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(11, 13)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(12, 13)
        self.charisma = 14
        self.can_paralyze = True
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Charm", "Banish", "Fear"]
        self.quantum_energy = True
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  #
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(25, 32) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 14)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "With unexpected speed, he strikes with his dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "He swings his gleaming scimitar!"
        self.attack_3 = 2
        self.attack_3_phrase = "He throws an acrid powder at you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, he swings his scimitar.."
        self.attack_5 = 3
        self.attack_5_phrase = "Crying out with insane hatred, he swings his scimitar!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "He releases weird smouldering energies from his outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Dark weaponry is released from his palms in the form of weird Quantum " \
                                       "flames!!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "He raises both hands, harnessing the quantum energies and\n" \
                                       "firing a cone of dark smouldering flames!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "He steps forward, thrusting his hands toward you, as disturbing\n" \
                                       "images and fearsome nightmarish creatures materialize in your mind!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "With a horrible cry, he releases a green mist from his hands\n" \
                                       "that envelopes you!"
        self.introduction = f"You have encountered a Cult Fanatic. Decked in a grand robe of black and gold\n" \
                            f"symbology and face hidden in shadow, he cries aloud in dark allegiance\n" \
                            f"to his fell religious creed. His hands glow dimly with Quantum Weirdness..."
        self.paralyze_phrase = "He points at you with one hand and slowly raises the other. Suddenly, he  clenches " \
                               "the raised hand into a fist..."
        self.paralyze_free_attack_phrase = "Patiently and sadistically, he slices at you with his crooked dagger " \
                                           "as you helplessly watch!"
        self.is_discovered = False


class Ghoul(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Ghoul"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(0, 5)  # self.level * 103 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 12)
        self.dexterity = random.randint(14, 16)
        self.constitution = random.randint(12, 13)
        self.intelligence = random.randint(5, 10)
        self.wisdom = random.randint(7, 9)
        self.charisma = random.randint(1, 5)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = dice_roll(1, 6)
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.human_player_level = 0
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 2  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(20, 24) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes swiftly with one terrible claw.."
        self.attack_2 = 1
        self.attack_2_phrase = "It lunges forward and attacks with its hideous, rancid teeth!"
        self.attack_3 = 2
        self.attack_3_phrase = "It strikes wildly with both of its terrible claws!"
        self.attack_4 = 2
        self.attack_4_phrase = "It rushes straight at you, arms wildly flailing!"
        self.attack_5 = 3
        self.attack_5_phrase = "It leaps upon your shoulders, savagely swiping at you!!"
        self.introduction = "You have encountered a Ghoul, crouching and licking a skull. Noticing your approach,\n" \
                            "it drops the skull and rises to its feet, hissing through razor-sharp teeth and\n" \
                            "working its jagged claws. Driven by an insatiable hunger for humanoid flesh,\n " \
                            "its bulbous black eyes grow impossibly wide as it draws in its serpentine tongue. "
        self.is_discovered = False
        self.paralyze_phrase = "It lurches forward, grabbing your arm in its cold, sinewy and awful claws!"
        self.paralyze_free_attack_phrase = "As you stand helplessly frozen, it savagely gores you!"
    # name = "Ghoul"


class Bugbear(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Bugbear"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(5, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = random.randint(13, 14)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(8, 9)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(8, 10)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 8
        self.number_of_hd = 2
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(25, 28)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(14, 16)
        self.multi_attack = False
        self.attack_1 = 1  # attack bonus
        self.attack_1_phrase = "It thrusts mightily forward with its spear!.."
        self.attack_2 = 2
        self.attack_2_phrase = "It swings its morningstar with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its morningstar with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "It roars and swings its morningstar with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its morningstar overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Bugbear; a hairy goblinoid born for battle and mayhem. " \
                            f"Equally deadly at hunting,\nraiding and melee, it stands before you, fearlessly " \
                            f"brandishing its weapons with a deep, slow snarl..."
        self.is_discovered = False


class HalfOgre(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Half-Ogre"
        self.proper_name = "None"
        self.experience_award = 200
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(16, 18)
        self.dexterity = random.randint(9, 11)
        self.constitution = random.randint(13, 15)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(8, 10)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 10
        self.number_of_hd = 2
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(28, 32)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 13)
        self.multi_attack = True
        self.attack_1 = 2  # attack bonus
        self.attack_1_phrase = "It thrusts brutally toward you with its javelin!.."
        self.attack_2 = 2
        self.attack_2_phrase = "It swings its battleaxe with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its battleaxe with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "It roars and swings its battleaxe with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its battleaxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Half-Ogre; a brutal, muscled monstrosity of primal rage." \
                            f"Neither human nor ogre,\nand equally shunned in both worlds, it lumbers " \
                            f"toward you, towering above and shaking the ground with great power.."
        self.is_discovered = False


class Specter(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Specter"
        self.proper_name = "None"
        self.experience_award = 250
        self.gold = random.randint(0, 1)  # self.level * 103 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 12)
        self.dexterity = random.randint(12, 16)
        self.constitution = random.randint(10, 12)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(9, 11)
        self.charisma = random.randint(10, 12)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 8)
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.human_player_level = 0
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 3  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(20, 24) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 13)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It places a cold, yet immaterial hand upon you for just a moment.."
        self.attack_2 = 1
        self.attack_2_phrase = "It extends a hand, which elongates into a horrible mist that thrusts toward you.. "
        self.attack_3 = 2
        self.attack_3_phrase = f"A cold, dreadful feeling overcomes you as the {self.name} looms over you, reaching\n" \
                               f"out to embrace you within its deadly touch!"
        self.attack_4 = 2
        self.attack_4_phrase = "It rushes straight at you and phase-shifts. It re-appears behind you, ready to strike!!"
        self.attack_5 = 3
        self.attack_5_phrase = "It silently raises its hands, releasing dreadfully wicked energies!!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "It releases weird draining energies from its outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Dreadful black droplets dance over its form as it unleashes\n" \
                                       "impossibly cold, white flames from both of its outstretched hands!!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "Its empty eyes widen, as it rises up, harnessing the quantum energies and\n" \
                                       "hurling a wall of black energy toward you!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "Swirling around you in a confusing arc, it releases a mist\n" \
                                       "of dark energy which envelopes you!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "With muted malice, its arms elongate unnaturally, wildly entangling you in \n" \
                                       "a storm of wicked forces!"
        self.introduction = f"From out of nothingness, materializes a Specter....A vile, undead form created\n" \
                            f"through a combination of wickedness, quantum manipulations, and a violent death.\n" \
                            f"Its ghostly form resembles what it was in life, but its now dispossessed\n" \
                            f"identity has been completely erased and replaced with a simple motive and \n" \
                            f"purpose; A revulsion for the living and a hunger for their life-energy.."
        self.is_discovered = False
        self.is_discovered = False
        self.paralyze_phrase = "It places a cold, yet immaterial hand upon you!!"
        self.paralyze_free_attack_phrase = "Completely helpless, you feel your strength failing as it unnaturally " \
                                           "drains you!!"


class SpecterKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Specter King"
        self.proper_name = "None"
        self.experience_award = 500
        self.gold = random.randint(6, 16)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(13, 16)
        self.dexterity = random.randint(12, 16)
        self.constitution = random.randint(11, 13)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(12, 13)
        self.charisma = random.randint(10, 12)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 10)
        self.undead = True
        self.immunities = ["Sleep", "Charm"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.human_player_level = 0
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 8  #
        self.number_of_hd = 3  #
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = random.randint(25, 34) + self.constitution_modifier
        # self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier) + 1
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It places a cold, yet immaterial hand upon you for just a moment.."
        self.attack_2 = 1
        self.attack_2_phrase = "It extends a hand, which elongates into a horrible mist that thrusts toward you.. "
        self.attack_3 = 2
        self.attack_3_phrase = f"A cold, dreadful feeling overcomes you as the {self.name} looms over you, reaching\n" \
                               f"out to embrace you within its deadly touch!"
        self.attack_4 = 2
        self.attack_4_phrase = "It rushes straight at you and phase-shifts. It re-appears behind you, ready to strike!!"
        self.attack_5 = 3
        self.attack_5_phrase = "It silently raises its hands, releasing dreadfully wicked energies!!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "It releases weird draining energies from its outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Dreadful black droplets dance over its form as it unleashes\n" \
                                       "impossibly cold, white flames from both of its outstretched hands!!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "Its empty eyes widen, as it rises up, harnessing the quantum energies and\n" \
                                       "hurling a wall of black energy toward you!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "Swirling around you in a confusing arc, it releases a mist\n" \
                                       "of dark energy which envelopes you!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "With muted malice, its arms elongate unnaturally, wildly entangling\n" \
                                       "you in a storm of wicked forces!"
        self.introduction = f"From out of nothingness, the Specter King materializes..A vile, undead form\n" \
                            f"of fear-inspiring and unnatural horrors. Its ghostly form resembles its former\n" \
                            f"royal greatness, but now its entire existence is a mere quantum-driven and\n" \
                            f"endless nightmare of madness, devoid of any humanity. Upon seeing you, it silently\n" \
                            f"approaches, its countenance twisted in insane thirst for your life-energy.."
        self.is_discovered = False
        self.paralyze_phrase = "With unnatural speed and silent swiftness, it places a cold, immaterial hand upon you.."
        self.paralyze_free_attack_phrase = "You feel agony crawling deep within you as you stand helpless and still!!"


class HobgoblinCaptain(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Hobgoblin Captain"
        self.proper_name = "None"
        self.experience_award = 700
        self.gold = random.randint(7, 15)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 2
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(15, 15)
        self.dexterity = 14
        self.constitution = 14
        self.intelligence = 12
        self.wisdom = 10
        self.charisma = 13
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  # MM
        self.number_of_hd = 2  # mm
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(36, 49)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(17, 17)
        self.multi_attack = True
        self.attack_1 = 1  # attack bonus
        self.attack_1_phrase = "It thrusts mightily forward with its javelin!.."
        self.attack_2 = 2
        self.attack_2_phrase = "It swings its greatsword with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its greatsword with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "It roars and swings its greatsword with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its greatsword overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Hobgoblin Captain. Fierce, intelligent and disciplined, " \
                            f"its heavy armor and\nweaponry are polished and well-maintained. Its yellow " \
                            f"teeth stretch into a surly grin behind its great helm.\nNarrowing its eyes, " \
                            f"it approaches and stands before you unaffected and unafraid; ready for battle."
        self.is_discovered = False


class GreenDragonWyrmling(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Green Dragon Wyrmling"
        self.proper_name = "None"
        self.experience_award = 450
        self.gold = random.randint(15, 25)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = 12
        self.constitution = random.randint(13, 15)
        self.intelligence = 14
        self.wisdom = 11
        self.charisma = 13
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(1, 6)
        self.dot_turns = dice_roll(1, 6)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Fear", "Charm"]
        self.quantum_energy = False
        self.difficulty_class = 4
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 10
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(30, 32)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.attack_1 = 2  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 3
        self.attack_2_phrase = "With a languid growl, it strikes with its jaws.. "
        self.attack_3 = 4
        self.attack_3_phrase = "Proud and poised, it prepares to strike with its murderous jaws.."
        self.attack_4 = 14
        self.attack_4_phrase = "\'I am sorry. This will hurt you, my little friend.\', it says dryly, as it draws back " \
                               "and bites with venomous guile!"
        self.attack_5 = 18
        self.attack_5_phrase = "The beast leaps upon you, attacking fiercely!"
        self.introduction = f"You have encountered a Green Dragon Wyrmling; a young, cunning and evil beast. " \
                            f"As it approaches, it chuckles\nand addresses you in the common tongue! " \
                            f"\"Greetings, little one! It is most fortuitous to meet you..\"\n" \
                            f"You have very little time to ponder its greeting..."
        self.poison_phrase = "Wide-eyed and evil, it exhales a blast of putrid poison from its deepest evil innards!!"
        self.is_discovered = False


class WhiteDragonWyrmling(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "White Dragon Wyrmling"
        self.proper_name = "None"
        self.experience_award = 450
        self.gold = random.randint(15, 25)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(13, 15)
        self.dexterity = random.randint(9, 11)
        self.constitution = random.randint(13, 15)
        self.intelligence = random.randint(5, 6)
        self.wisdom = random.randint(10, 11)
        self.charisma = random.randint(10, 11)
        self.can_paralyze = False
        self.paralyze_turns = 0
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = ["Ice Storm"]
        self.vulnerabilities = ["Immolation", "Fireball", "Fire Storm"]
        self.resistances = []
        self.quantum_energy = False
        self.difficulty_class = 4
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 10
        self.number_of_hd = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = (random.randint(30, 32)) + self.constitution_modifier
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.attack_1 = 2  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 3
        self.attack_2_phrase = "With a serpentine swaying, it strikes with its jaws.. "
        self.attack_3 = 4
        self.attack_3_phrase = "Perfectly focused, it prepares to strike.."
        self.attack_4 = 14
        self.attack_4_phrase = "Rearing up with elegant, murderous intent, it exhales an icy blast of hail!"
        self.attack_5 = 18
        self.attack_5_phrase = "Rearing up with elegant, murderous intent, it exhales a terrible, icy blast of hail!"
        self.introduction = f"You have encountered a White Dragon Wyrmling; a slow witted, evil, efficient hunter. " \
                            f"Confidently stepping forth,\nit roars viciously, undoubtedly preparing to have you " \
                            f"as a meal!"
        self.is_discovered = False


# monster dictionaries. keys correspond to difficulty

# regular monsters:
monster_dict = {
    1: [Quasit, Kobold, Cultist, Goblin, Skeleton, WingedKobold],
    2: [Shadow, Drow, Troglodyte, Orc, Zombie, Ghoul],
    3: [Specter, Bugbear, CultFanatic, HalfOgre],
    4: [WhiteDragonWyrmling, GreenDragonWyrmling, HobgoblinCaptain]
}
# undead monsters:
undead_monster_dict = {
    1: [Skeleton],
    2: [Shadow, Zombie, Ghoul],
    3: [Specter]
}
# boss lists
undead_prophet_list = [ZombieProphet(), SkeletalProphet()]
king_boss_list = [SkeletonKing(), ShadowKing(), SpecterKing()]

# For monster hit points..take hit dice and add (constitution modifier x number of hit dice).
# For example, if a monster has a Constitution of 12 (+1 modifier) and 2d8 Hit Dice, it has 2d8 + 2 Hit Points
# self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier)
'''def drain(self, monster_wisdom, monster_wisdom_modifier, human_player_level, human_player_wisdom,
              human_player_wisdom_modifier):
        drain_level = dice_roll(1, 20)  # need player_1 experience logic for proper drain??
        if drain_level > 17 and (monster_wisdom + monster_wisdom_modifier) > (
                human_player_wisdom + human_player_wisdom_modifier):
            # print("It drains a level!")
            level_drain = True
            return level_drain
        else:
            level_drain = False
            return level_drain'''
