# Sauengard © Copyright 2022 by Jules Pitsker
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.

"""

Copyright 2022, JULES PITSKER  (pitsker@proton.me)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. All advertising materials mentioning features or use of this software must
   display the following acknowledgement:
     This product includes software developed by Jules Pitsker.

4. Neither the name of the copyright holder nor the names of his
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Thanks to the following STACK OVERFLOW members:
The Spider, Anentropic, The Thonnu and Optimal: for helping me get my footing during my first days of learning python
Yarik0urWorld: for help with python list syntax
Angus Nicolson: for self.__dict__ code snippet and explanation
Liju and snakecharmerb: for explanation of hashable objects
Pawel Pietraszko: for assistance with initializing new object instances every time player gets new item
triplee: for assistance with Path syntax

Thanks to @LearntoCodeGCSE for the 2D array video.

SOUND/MUSIC:
Main theme: "Soul's Departure" Royalty Free Music by Darren Curtis
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Blacksmith Theme: 'Viking Intro loop' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Dungeon Themes: 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Chemist Theme: 'Might and Magic' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Fieldenberg Theme: 'Tavern Loop 1' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Boss battle theme: 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Tavern Theme: 'The Medieval Banquet' by Silverman Sound is under a Creative Commons license (CC BY 3.0)
Music promoted by BreakingCopyright: http://bit.ly/Silvermansound_Medieval

Pit theme: 'Epic 39' by Jules Pitsker
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Hall of the Mountain King by Kevin MacLeod http://incompetech.com
Creative Commons Attribution License 4.0 International (CC BY 4.0)
Free Download / Stream: https://bit.ly/hall-of-the-mountain-king
Music promoted by Audio Library https://youtu.be/2RDX5sVEfs4
PC Boot up sounds: Eirikr / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Floppy Disk Insert Sound: Joseph Sardin (BigSoundBank.com)
Creative Commons CC0 1.0 Universal (CC0 1.0)

Floppy Disk Drive R/W Sounds: Dennis Johansson (MrAuralization / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)

Gong: juskiddink / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Clacky Keyboard: Denis McDonald (denismcdonald / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)"""

# Telengard monsters:
# "Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon

import math
import os
import random
import time


def sleep(seconds):
    time.sleep(seconds)
    return


def dice_roll(no_of_dice, no_of_sides):
    dice_rolls = []  # create list for multiple die rolls
    for dice in range(no_of_dice):
        dice_rolls.append(random.randint(1, no_of_sides))
    your_roll_sum = sum(dice_rolls)
    return your_roll_sum


def pause():
    if os.name == 'nt':
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
        self.name = "Generic Monster"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.a_an = "a"
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
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 0
        self.number_of_hd = 0
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.multi_attack = False
        self.lesser_multi_attack = False
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
        self.necrotic_phrase = ""

    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def monster_data(self):
        if self.proper_name == "None":
            mon_data = f"{self.name}  Challenge Lvl: {self.level}  AC: {self.armor_class}  " \
                       f"HP: {self.hit_points}  ({self.number_of_hd}d{self.hit_dice})"
        else:
            mon_data = f"{self.proper_name}  AC: {self.armor_class}  " \
                       f"HP: {self.hit_points}  ({self.number_of_hd}d{self.hit_dice})"
        if self.undead:
            print(f"{mon_data} (UNDEAD)")
        else:
            print(f"{mon_data}")
        if len(self.immunities):
            immunities = convert_list_to_string_with_commas_only(self.immunities)
            print("Immunities:", immunities)
        if len(self.resistances):
            resistances = convert_list_to_string_with_commas_only(self.resistances)
            print("Resistances:", resistances)
        if len(self.vulnerabilities):
            vulnerabilities = convert_list_to_string_with_commas_only(self.vulnerabilities)
            print("Vulnerabilities:", vulnerabilities)

    def melee(self, player_1):
        attack_bonus = 0
        attack_bonus_roll = random.randint(1, 20)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing
        attack_phrase = ""

        if attack_bonus_roll <= 10:
            attack_bonus = self.attack_1
            attack_phrase = self.attack_1_phrase
        if attack_bonus_roll > 10 <= 15:
            attack_bonus = self.attack_2
            attack_phrase = self.attack_2_phrase
        if attack_bonus_roll > 15 <= 17:
            attack_bonus = self.attack_3
            attack_phrase = self.attack_3_phrase
        if attack_bonus_roll > 17 <= 19:
            attack_bonus = self.attack_4
            attack_phrase = self.attack_4_phrase
        if attack_bonus_roll > 19:
            attack_bonus = self.attack_5
            attack_phrase = self.attack_5_phrase

        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks you! ({self.he_she_it.capitalize()} rolls {roll_d20})")

        if roll_d20 == 1:
            print(f"..{self.he_she_it} awkwardly strikes and you easily block.")
            pause()
            return 0

        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = ""

        monster_total = roll_d20 + self.dexterity_modifier + self.proficiency_bonus  # test out pro bonus
        # print(f"{self.name} Attack bonus: {attack_bonus}")
        print(f"{self.name} Dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # testing out pro bonus
        print(f"{self.name} Total: {monster_total}")
        print(f"Your armor class: {player_1.armor_class}")

        if monster_total >= player_1.armor_class:
            damage_roll = dice_roll((self.number_of_hd * critical_bonus), self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)

            if roll_d20 == 20 and damage_to_opponent < 1:
                damage_to_opponent = 1  # 20 always hits

            if damage_to_opponent > 0:  # # at this point the human player is the opponent!
                print(f"{attack_phrase}")
                sleep(1.5)
                print(hit_statement)
                print(f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice}: {damage_roll}")  # hd
                sleep(1.5)
                print(f"Strength modifier: {self.strength_modifier}\nAttack bonus: {attack_bonus}\n"
                      f"Weapon bonus: {self.weapon_bonus}")
                sleep(1.5)
                print(f"You suffer {damage_to_opponent} points of damage!")
                pause()
                return damage_to_opponent

            else:
                # zero damage to player result
                print(f"The {self.name} strikes..")
                sleep(1)
                print(f"Your armor absorbs the blow!")
                sleep(1)
                print(f"It does no damage..")
                sleep(.25)
                damage_to_opponent = 0
                pause()
                return damage_to_opponent  # 0 points damage to player
        else:
            print(f"{self.he_she_it.capitalize()} missed..")
            pause()
            return 0

    def quantum_energy_attack(self, player_1):
        attack_bonus = 0
        attack_phrase = ""
        attack_bonus_roll = random.randint(1, 20)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing

        if attack_bonus_roll <= 10:
            attack_bonus = self.quantum_attack_1
            attack_phrase = self.quantum_attack_1_phrase
        if attack_bonus_roll > 10 <= 15:
            attack_bonus = self.quantum_attack_2
            attack_phrase = self.quantum_attack_2_phrase
        if attack_bonus_roll > 15 <= 17:
            attack_bonus = self.quantum_attack_3
            attack_phrase = self.quantum_attack_3_phrase
        if attack_bonus_roll > 17 <= 19:
            attack_bonus = self.quantum_attack_4
            attack_phrase = self.quantum_attack_4_phrase
        if attack_bonus_roll > 19:
            attack_bonus = self.quantum_attack_5
            attack_phrase = self.quantum_attack_5_phrase

        human_player_roll_d20 = dice_roll(1, 20)
        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks you with Quantum Energy!\n"
              f"({self.he_she_it.capitalize()} rolls {roll_d20})\n"
              f"Proficiency Bonus: {self.proficiency_bonus}\n"
              f"Wisdom modifier: {self.wisdom_modifier}\n"
              f"{self.name} Total: {roll_d20 + self.wisdom_modifier + self.proficiency_bonus}")

        if roll_d20 == 1:
            print(f"..{self.his_her_its} attempts to procure the universal forces fail miserably.")
            pause()
            return 0

        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"

        else:
            critical_bonus = 1
            hit_statement = ""
        print(f"Your Saving Throw: {human_player_roll_d20} + wisdom modifier: ({player_1.wisdom_modifier})")

        if player_1.ring_of_prot.protect > 0:
            print(f"Your Ring of Protection Modifier: {player_1.ring_of_prot.protect}")

        if player_1.temp_protection_effect:
            print(f"+ Quantum Protection effect: {player_1.temp_protection_effect} ")
        human_total = human_player_roll_d20 + player_1.wisdom_modifier + player_1.ring_of_prot.protect \
            + player_1.temp_protection_effect
        print(f"Your Total: {human_total}")
        monster_total = roll_d20 + self.wisdom_modifier + self.proficiency_bonus  # test out pro bonus

        if monster_total >= human_total:
            damage_roll = dice_roll(self.number_of_hd * critical_bonus, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.wisdom_modifier + attack_bonus)

            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice} hit dice: {damage_roll}")
                print(f"Wisdom modifier: {self.wisdom_modifier}\nAttack bonus: {attack_bonus}")
                print(f"You suffer {damage_to_opponent} points of damage!")
                pause()
                # sleep(5)
                return damage_to_opponent

            else:
                print(f"The {self.name} strikes with Quantum Powers, but you dodge {self.his_her_its} attack!")  # 0 dmg
                sleep(2)
                return 0  # 0 points damage to player

        else:
            print(f"{self.he_she_it.capitalize()} fails to harness the mysterious powers..")
            pause()
            return 0

    def paralyze(self, player_1):
        if dice_roll(1, 20) > 10:  # 50% chance
            player_1.hud()
            print(self.paralyze_phrase)
            sleep(1.25)
            paralyze_chance = dice_roll(1, 20)
            human_player_roll_d20 = dice_roll(1, 20)
            player_total = (human_player_roll_d20 + player_1.ring_of_prot.protect + player_1.temp_protection_effect)
            print(f"Paralyze roll: {paralyze_chance} + monster wisdom modifier: {self.wisdom_modifier}")  # testing
            paralyze_total = paralyze_chance + self.wisdom_modifier
            print(f"Monster Total: {paralyze_total}")
            print(f"Your Saving Throw: {human_player_roll_d20} ")  # remove after testing

            if player_1.ring_of_prot.protect > 0:
                print(f"Your Ring of Protection Modifier: {player_1.ring_of_prot.protect}")

            if player_1.protection_effect:
                print(f"Protection from Evil Effect: {player_1.temp_protection_effect}")
            print(f"Your Total: {player_total}")

            if (paralyze_chance + self.wisdom_modifier) >= player_total:
                print("You are paralyzed!!")
                sleep(1)
                print(self.paralyze_free_attack_phrase)
                sleep(1)
                turns = 0
                for i in range(self.paralyze_turns):  # this seems too brutal if paralyze_turns is anything but 1!!!
                    paralyze_damage = (dice_roll((self.number_of_hd * 2), self.hit_dice) -
                                       (player_1.ring_of_prot.protect + player_1.temp_protection_effect))
                    turns += 1
                    if paralyze_damage < 1:
                        paralyze_damage = self.level
                    player_1.reduce_health(paralyze_damage)
                    if turns == 1:
                        print(f"You suffer {paralyze_damage} points of damage!!")
                    else:
                        print(f"{self.he_she_it.capitalize()} strikes again for {paralyze_damage} points of damage!!")
                    pause()
                    player_1.hud()
                return True

            else:
                # print(f"You ignore {self.his_her_its} wiles and break free from {self.his_her_its} grip!")
                print(f"You break free from {self.his_her_its} grip!")
                pause()
                player_1.hud()
                return False
        else:
            return False

    def poison_attack(self, player_1):
        # added intelligence modifier to monster roll
        player_saving_throw = dice_roll(1, 20)
        difficulty_class = (player_saving_throw + player_1.constitution_modifier)
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(self.poison_phrase)
        print(f"{self.name} Attack roll: {roll_d20}")
        print(f"{self.name} Intelligence Modifier: {math.floor((self.intelligence - 10) / 2)}")
        monster_poison_total = roll_d20 + math.floor((self.intelligence - 10) / 2)
        print(f"Total: {monster_poison_total}")
        sleep(1)

        if roll_d20 == 1:
            print(f"You easily dodge {self.his_her_its} poison attack!")
            sleep(1)
            pause()
            player_1.hud()
            return False
        else:
            print(f"Your Saving Throw: {player_saving_throw}\n"
                  f"Your Constitution Modifier: {player_1.constitution_modifier}\n")
            print(f"Your Total: {difficulty_class}")

            if roll_d20 == 20 or monster_poison_total >= difficulty_class:
                player_1.dot_multiplier = self.dot_multiplier
                player_1.dot_turns = self.dot_turns
                rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                         "An unnerving frailty spreads throughout your body...",
                                         "Pain and tenderness courses through your body.."
                                         ]
                poisoned_phrase = random.choice(rndm_poisoned_phrases)
                print(f"{poisoned_phrase}")
                sleep(1.5)
                print(f"You have been poisoned!")
                player_1.poisoned = True
                player_1.poisoned_turns = 0
                pause()
                return player_1.poisoned

            else:
                print(f"You swiftly dodge {self.his_her_its} poison attack!")
                sleep(1)
                pause()
                player_1.hud()
                return False

    def necrotic_attack(self, player_1):
        # added wisdom modifier to monster roll
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"{self.necrotic_phrase}")
        print(f"{self.name} Attack roll: {roll_d20}")
        print(f"{self.name} Wisdom Modifier: {self.wisdom_modifier}")
        print(f"Total: {roll_d20 + self.wisdom_modifier}")
        sleep(1)

        if roll_d20 == 1:
            print(f"You dodge {self.his_her_its} deadly necrotic attack!")
            sleep(1)
            pause()
            player_1.hud()
            return False

        else:
            player_saving_throw = (dice_roll(1, 20))
            difficulty_class = (player_saving_throw + player_1.constitution_modifier)
            print(f"Your Saving Throw: {player_saving_throw}\n"
                  f"Your Constitution Modifier: {player_1.constitution_modifier}\n")
            print(f"Your Total: {difficulty_class}")

            if roll_d20 == 20 or (roll_d20 + self.wisdom_modifier) >= difficulty_class:
                player_1.dot_multiplier = self.dot_multiplier
                player_1.dot_turns = self.dot_turns
                rndm_necrotic_phrases = ["You feel morbid dread and withering overcoming you..",
                                         "An unnerving pain, planted like a seed, germinates within you...",
                                         "Agony creeps into your very veins..."
                                         ]
                necrotic_phrase = random.choice(rndm_necrotic_phrases)
                print(f"{necrotic_phrase}")
                sleep(1.5)
                print(f"Necrotic forces ravage through your body!")
                player_1.necrotic = True
                player_1.necrotic_turns = 0
                pause()
                player_1.hud()
                return player_1.necrotic

            else:
                print(f"You swiftly dodge {self.his_her_its} death-dealing necrotic attack!")
                sleep(1)
                pause()
                player_1.hud()
                return False

    def meta_monster_vs_npc_function(self, npc):
        if not npc.retreating:
            melee_or_quantum = dice_roll(1, 20)

            # if monster has quantum energy:
            if self.quantum_energy and melee_or_quantum > 10:
                # quantum attack
                damage_to_player = self.quantum_energy_attack_vs_npc(npc)
                reduce_npc_health(npc, damage_to_player)

            else:
                # if it has no quantum, then melee attack:
                damage_to_player = self.melee_vs_npc(npc)
                reduce_npc_health(npc, damage_to_player)
            return

        else:
            # npc is in retreat. move on.
            return

    def meta_monster_function(self, player_1):
        melee_or_quantum = dice_roll(1, 20)

        # if monster has quantum energy,
        # and rolls more than 10,
        # and human player is not poisoned or necrotic:
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

        else:  # then melee attack:
            damage_to_player = self.melee(player_1)
            player_1.reduce_health(damage_to_player)
            player_1.end_of_turn_calculation()
        return

    def melee_vs_npc(self, npc):
        attack_bonus = 0
        attack_bonus_roll = random.randint(1, 20)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing
        attack_phrase = f"The {self.name} hits!"

        if attack_bonus_roll <= 10:
            attack_bonus = self.attack_1
        if attack_bonus_roll > 10 <= 15:
            attack_bonus = self.attack_2
        if attack_bonus_roll > 15 <= 17:
            attack_bonus = self.attack_3
        if attack_bonus_roll > 17 <= 19:
            attack_bonus = self.attack_4
        if attack_bonus_roll > 19:
            attack_bonus = self.attack_5

        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks {npc.name}! ({self.he_she_it.capitalize()} rolls {roll_d20})")

        if roll_d20 == 1:
            print(f"..{self.he_she_it} awkwardly strikes and {npc.name} easily blocks.")
            pause()
            return 0

        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = ""

        monster_total = roll_d20 + self.dexterity_modifier + self.proficiency_bonus  # test out pro bonus
        # print(f"{self.name} Attack bonus: {attack_bonus}")
        print(f"{self.name} Dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # testing out pro bonus
        print(f"{self.name} Total: {monster_total}")
        print(f"{npc.name}'s armor class: {npc.armor_class}")

        if monster_total >= npc.armor_class:
            damage_roll = dice_roll((self.number_of_hd * critical_bonus), self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)

            if roll_d20 == 20 and damage_to_opponent < 1:
                damage_to_opponent = 1  # a natural 20 always hits

            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice}: {damage_roll}")  # hd
                sleep(1.5)
                print(f"Strength modifier: {self.strength_modifier}\nAttack bonus: {attack_bonus}\n"
                      f"Weapon bonus: {self.weapon_bonus}")
                sleep(1.5)
                print(f"{npc.name} suffers {damage_to_opponent} points of damage!")
                pause()
                return damage_to_opponent

            else:
                # zero damage to player result
                print(f"The {self.name} strikes..")
                sleep(1)
                print(f"{npc.name}'s armor absorbs the blow!")
                damage_to_opponent = 0
                sleep(1)
                print(f"No damage is sustained.")
                sleep(.25)
                pause()
                return damage_to_opponent  # 0 points damage to player

        else:
            print(f"{self.he_she_it.capitalize()} missed..")
            pause()
            return 0

    def quantum_energy_attack_vs_npc(self, npc):
        attack_bonus = 0
        attack_phrase = f"With great concentration, {self.he_she_it} procures the weird universal forces.."
        attack_bonus_roll = random.randint(1, 20)
        # print(f"Monster attack bonus roll: {attack_bonus_roll}")  # remove after testing

        if attack_bonus_roll <= 10:
            attack_bonus = self.quantum_attack_1

        if attack_bonus_roll > 10 <= 15:
            attack_bonus = self.quantum_attack_2

        if attack_bonus_roll > 15 <= 17:
            attack_bonus = self.quantum_attack_3

        if attack_bonus_roll > 17 <= 19:
            attack_bonus = self.quantum_attack_4

        if attack_bonus_roll > 19:
            attack_bonus = self.quantum_attack_5

        npc_roll_d20 = dice_roll(1, 20)
        roll_d20 = dice_roll(1, 20)
        print(f"The {self.name} attacks {npc.name} with Quantum Energy!\n"
              f"({self.he_she_it.capitalize()} rolls {roll_d20})\n"
              f"Proficiency Bonus: {self.proficiency_bonus}\n"
              f"Wisdom modifier: {self.wisdom_modifier}\n"
              f"{self.name} Total: {roll_d20 + self.wisdom_modifier + self.proficiency_bonus}")

        if roll_d20 == 1:
            print(f"..{self.his_her_its} attempts to procure the universal forces fail miserably.")
            pause()
            return 0

        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = f"The weird energies are unleashed upon {npc.name}.."
        print(f"{npc.name} Saving Throw: {npc_roll_d20} + wisdom modifier: ({npc.wisdom_modifier})")

        if npc.protect > 0:
            print(f"Protection Modifier: {npc.protect}")
        print(f"{npc.name} Total: {npc_roll_d20 + npc.wisdom_modifier + npc.protect}")
        monster_total = roll_d20 + self.wisdom_modifier + self.proficiency_bonus  # pro bonus

        if monster_total >= (npc_roll_d20 + npc.wisdom_modifier + npc.protect):
            damage_roll = dice_roll(self.number_of_hd * critical_bonus, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.wisdom_modifier + attack_bonus)

            if damage_to_opponent > 0:  # at this point the npc is the opponent!
                print(f"{attack_phrase}")
                sleep(1.5)
                print(hit_statement)
                print(
                    f"{self.name} rolls {self.number_of_hd * critical_bonus}d{self.hit_dice} hit dice: {damage_roll}")
                print(f"Wisdom modifier: {self.wisdom_modifier}\nAttack bonus: {attack_bonus}")
                print(f"{npc.name} suffers {damage_to_opponent} points of damage!")
                pause()
                # sleep(5)
                return damage_to_opponent

            else:
                print(
                    f"The {self.name} strikes with Quantum Powers, but {npc.name} dodges the attack!")  # 0 damage
                sleep(2)
                return 0  # 0 points damage to npc

        else:
            print(f"{self.he_she_it.capitalize()} fails to harness the mysterious powers..")
            pause()
            return 0


class Quasit(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Quasit"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 4  # tiny
        self.number_of_hd = 1
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.lesser_multi_attack = False
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
                            f"as it lets out a high pitched, fiendish and wretched cry. The air around it " \
                            f"becomes hazy.."


class Kobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Kobold"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 4  # small
        self.number_of_hd = 1
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.lesser_multi_attack = False
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
                            f"and skin. Its ragged tunic looks more like a robe on its tiny frame; you have no " \
                            f"doubt\n" \
                            f"it was stolen from an unwary adventurer. Its tail stands up as it retrieves a dagger\n" \
                            f"from a brass scabbard, twirling it deftly between scaled, sinewy fingers. It looks\n" \
                            f"you over for items to rid you of!"


class Cultist(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Cultist"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6  #
        self.number_of_hd = 1
        self.hit_points = random.randint(8, 10) + self.constitution_modifier
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "With unexpected speed, he strikes with his dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "He swings his gleaming scimitar!"
        self.attack_3 = 2
        self.attack_3_phrase = "He throws an acrid powder at you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, he swings his scimitar.."
        self.attack_5 = 3
        self.attack_5_phrase = "Crying out with insane hatred, he raises his scimitar with both hands in a mighty blow!"
        self.introduction = f"You have encountered a Cultist. Adorned with a foul robe speckled with disgusting\n" \
                            f"symbols, and face hidden in the deep shadow of his cowl, you see his insane eyes\n" \
                            f"smoulder in the darkness. His loyalties long since revealed, he cries out in sworn\n" \
                            f"allegiance to some dark Quantum Manipulator..."


class Goblin(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Goblin"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6
        self.number_of_hd = 1
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
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
                            f"scimitar and faces you."


class WingedKobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.name = "Winged Kobold"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 4
        self.number_of_hd = 1
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = False
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
                            f"and a frail body covered with mottled, brick-red scales, it grabs its dagger and\n" \
                            f"spreads its leathery, bat-like wings."


class Gnoll(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Gnoll"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 100
        self.gold = random.randint(1, 7)  # self.level * 200 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 14
        self.dexterity = 12
        self.constitution = random.randint(9, 11)
        self.intelligence = 6
        self.wisdom = 10
        self.charisma = 7
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 1
        self.hit_points = (random.randint(18, 21)) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = False
        self.lesser_multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It thrusts forward, jaws gaping.."
        self.attack_2 = 2
        self.attack_2_phrase = "It pounces, ready to bite!"
        self.attack_3 = 2
        self.attack_3_phrase = "It strikes with gnarled and hairy claws.."
        self.attack_4 = 3
        self.attack_4_phrase = "It grabs a jagged dagger from its belt and strikes.."
        self.attack_5 = 3
        self.attack_5_phrase = "It strikes forward with its bloodied spear!"
        self.introduction = f"You have encountered a {self.name}. A wild, unthinking unnatural humanoid driven\n" \
                            f"by basic instincts of necessity. Like its Kobold cousins, it lurks about, in search\n" \
                            f"of food and supplies which can be procured by any means.."


class Shadow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Shadow"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 100
        self.gold = random.randint(0, 1)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(5, 6)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(5, 7)
        self.wisdom = 10
        self.charisma = random.randint(7, 8)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
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
        self.hit_dice = 6
        self.number_of_hd = 2
        self.hit_points = random.randint(15, 17)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = True
        self.lesser_multi_attack = False
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
        self.necrotic_phrase = "The Shadow reaches out toward you with groping hands, from which extends a black " \
                               "cloud of dark Quantum energy.."


class ShadowKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Shadow King"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 100
        self.gold = random.randint(5, 10)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(7, 8)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(5, 7)
        self.wisdom = 14
        self.charisma = random.randint(7, 8)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 8)
        self.undead = True
        self.immunities = ["Turn Undead", "Web", "Hold Monster", "Banish"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.hit_dice = 10
        self.number_of_hd = 2
        self.hit_points = random.randint(15, 17)
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
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
                            f"His body rises up, absorbing all ambient light into a silhouette of\n" \
                            f"endless darkness. And yet, somehow, you randomly catch glimpses of his actual form\n" \
                            f"beneath- impossibly long, bony, outstretched arms extending from his once\n" \
                            f"royal raiment..a humanoid, skullish face forever grimacing in confusion over his\n" \
                            f"own existence..and lamenting the long lost grandeur of a kingdom now forgotten\n" \
                            f"and erased from the annals of time.\n" \
                            f"You feel the air crackle with quantum energy.."
        self.paralyze_phrase = "Rising menacingly and with both clawed, shadowy hands, he reaches out, and you\n" \
                               "feel your motor skills quivering.."
        self.paralyze_free_attack_phrase = "You feel your life force weakening as he drains you mercilessly!"
        self.necrotic_phrase = "The King reaches out toward you with groping hands, from which extends a black " \
                               "cloud of dark Quantum energy.."


class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2  # I think level 1 might be more appropriate.
        self.name = "Skeleton"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6
        self.number_of_hd = 1
        self.hit_points = random.randint(11, 13) + self.constitution_modifier
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
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
                            f"in hand, it fearlessly hammers its sword hilt against its shield, taunting an attack." \
                            f"\nA full-toothed grin forever emblazoned on its bony countenance, it shouts an\n" \
                            f"absent, yet echoing battle-cry at you from behind its slack, gaping jaw!\n" \
                            f"The air bristles with Quantum Energy.."


class ZombieProphet(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Zombie Prophet"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 200
        self.gold = random.randint(6, 15)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 4
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 16
        self.constitution = 16
        self.intelligence = 12
        self.wisdom = 13
        self.charisma = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Turn Undead", "Web", "Hold Monster", "Banish"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.hit_points = random.randint(15, 19) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "He strikes at you with unnerving strength and speed..."
        self.attack_2 = 1
        self.attack_2_phrase = "He strikes at you with arms flailing..."
        self.attack_3 = 2
        self.attack_3_phrase = "He darts forward with reckless abandon.."
        self.attack_4 = 2
        self.attack_4_phrase = "He thrusts forward with his heavy, iron sceptre!"
        self.attack_5 = 3
        self.attack_5_phrase = "He strikes wildly with his iron sceptre!!"
        self.introduction = f"The ancient prophet rises from the ground. The once beautiful and exquisite\n" \
                            f"garb now hangs off his rotten, worm-infested flesh in tatters and rags.\n" \
                            f"The air bristles with Quantum Energy.."


class SkeletonKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Skeleton King"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 200
        self.gold = random.randint(6, 22)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 16
        self.constitution = 16
        self.intelligence = 13
        self.wisdom = 12
        self.charisma = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Turn Undead", "Web", "Hold Monster", "Banish"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.hit_points = random.randint(17, 22) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = f"He strikes at you with his longsword..."
        self.attack_2 = 1
        self.attack_2_phrase = f"He raises his longsword and swings mightily.."
        self.attack_3 = 2
        self.attack_3_phrase = f"He darts forward with unnerving speed, longsword in bony hand.."
        self.attack_4 = 2
        self.attack_4_phrase = f"He thrusts forward with his heavy, iron spear!"
        self.attack_5 = 3
        self.attack_5_phrase = f"Reaching over his back, he produces a battle axe and strikes wildly!!"
        self.introduction = f"The ancient king rises in skeletal form. The once gleaming armor and weaponry now\n" \
                            f"clings wearily to his bony form as he raises sword and shield, taunting you to " \
                            f"attack!\n" \
                            f"The air bristles with Quantum Energy.."


class SkeletalProphet(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Skeletal Prophet"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 200
        self.gold = random.randint(6, 22)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 16
        self.constitution = 16
        self.intelligence = 13
        self.wisdom = 13
        self.charisma = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = ["Turn Undead", "Web", "Hold Monster", "Banish"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10  #
        self.number_of_hd = 1  #
        self.hit_points = random.randint(17, 22) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = f"He strikes at you with his sceptre..."
        self.attack_2 = 1
        self.attack_2_phrase = f"He raises his sceptre and swings with abandon.."
        self.attack_3 = 2
        self.attack_3_phrase = f"He darts forward in a mad frenzy.."
        self.attack_4 = 2
        self.attack_4_phrase = f"Raising the sceptre overhead, he swings with both bony hands..!"
        self.attack_5 = 3
        self.attack_5_phrase = f"Taunting and glaring through his rottenness, he strikes wildly!!"
        self.introduction = f"The ancient prophet rises in skeletal form. His once spectacular raiment now\n" \
                            f"clings wearily to his bony form as he raises his sceptre and laughs wildly!\n" \
                            f"The air bristles with Quantum Energy.."


class Drow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Drow"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 100
        self.gold = random.randint(5, 12)  # self.level * 300 * round(random.uniform(1, 2))
        self.weapon_bonus = 1
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(9, 11)
        self.dexterity = random.randint(13, 14)
        self.constitution = random.randint(9, 11)
        self.intelligence = 11
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(12, 13)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = dice_roll(1, 6)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.hit_dice = 6
        self.number_of_hd = 1
        self.hit_points = random.randint(12, 14) + self.constitution_modifier
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
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
        self.poison_phrase = "It slashes at you with its poisonous blade!!"


class Zombie(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Zombie"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6
        self.number_of_hd = 1
        self.hit_points = random.randint(22, 25) + self.constitution_modifier
        self.armor_class = random.randint(8, 9)
        self.multi_attack = False
        self.lesser_multi_attack = True
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


class Troglodyte(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Troglodyte"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 200
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 4
        self.number_of_hd = 2
        self.hit_points = random.randint(12, 14)
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
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


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Orc"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.a_an = "an"
        self.experience_award = 100
        self.gold = random.randint(5, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 1
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = random.randint(11, 14)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(9, 11)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 1
        self.hit_points = (random.randint(11, 13)) + self.constitution_modifier
        self.armor_class = random.randint(12, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
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


class CultFanatic(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Cult Fanatic"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Charm", "Banish", "Fear"]
        self.quantum_energy = True
        self.hit_dice = 8  #
        self.number_of_hd = 1
        self.hit_points = random.randint(25, 32) + self.constitution_modifier
        self.armor_class = random.randint(12, 14)
        self.multi_attack = True
        self.lesser_multi_attack = False
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
                            f"symbology and with face hidden in shadow, he cries aloud in dark allegiance\n" \
                            f"to his fell religious creed. His hands glow dimly with Quantum Weirdness..."
        self.paralyze_phrase = "He points at you with one hand and slowly raises the other. Suddenly, he clenches " \
                               "the raised hand into a fist..."
        self.paralyze_free_attack_phrase = "Patiently and sadistically, he slices at you with his crooked dagger " \
                                           "as you helplessly watch!"


class Gargoyle(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Gargoyle"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 450
        self.gold = random.randint(1, 5)  # self.level * 373 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 15
        self.dexterity = 11
        self.constitution = 16
        self.intelligence = 6
        self.wisdom = 11
        self.charisma = 7
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6  #
        self.number_of_hd = 2
        self.hit_points = 52
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 3  # attack bonus
        self.attack_1_phrase = "It strikes with its ravenous jaws.."
        self.attack_2 = 3
        self.attack_2_phrase = "It strikes with a horrible claw.."
        self.attack_3 = 3
        self.attack_3_phrase = "It swings its spiked tail with surprising, fluid speed."
        self.attack_4 = 5
        self.attack_4_phrase = "With blinding speed, it strikes with both terrible claws.."
        self.attack_5 = 6
        self.attack_5_phrase = "In a flurry of movement, it strikes with teeth and claws in deadly combination! "
        self.introduction = f"You see a grotesque, fiendish-looking statue in the form of a winged beast. " \
                            f"Suddenly, it begins to move!\n" \
                            f"You have encountered a Gargoyle! It breaks from its suspended pose and approaches you."
        self.paralyze_phrase = ""
        self.paralyze_free_attack_phrase = ""


class Ghoul(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Ghoul"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = dice_roll(1, 6)
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6
        self.number_of_hd = 2
        self.hit_points = random.randint(20, 24) + self.constitution_modifier
        self.armor_class = random.randint(11, 12)
        self.multi_attack = False
        self.lesser_multi_attack = True
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes swiftly, with one terrible claw.."
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
                            "working its jagged claws. Driven by an insatiable hunger for humanoid flesh,\n" \
                            "its bulbous black eyes grow impossibly wide as it draws in its serpentine tongue. "
        self.paralyze_phrase = "It lurches forward, grabbing your arm in its cold, sinewy and awful claws!"
        self.paralyze_free_attack_phrase = "As you stand helplessly frozen, it savagely gores you!"


class Bugbear(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Bugbear"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 200
        self.gold = random.randint(5, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 3
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = random.randint(13, 14)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(8, 9)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(8, 10)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 2
        self.hit_points = (random.randint(25, 28)) + self.constitution_modifier
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.lesser_multi_attack = False
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


class HalfOgre(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Half-Ogre"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 200
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 3
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(16, 18)
        self.dexterity = random.randint(9, 11)
        self.constitution = random.randint(13, 15)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(8, 10)
        self.charisma = random.randint(9, 11)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 2
        self.hit_points = (random.randint(28, 32)) + self.constitution_modifier
        self.armor_class = 13
        self.multi_attack = True
        self.lesser_multi_attack = False
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


class Doppelganger(Monster):

    def __init__(self):
        super().__init__()
        forms = ["a silvery-haired, white-bearded fiend with spectacles wearing a slick, green coat and heavy boots",
                 "a black-bearded, silvery-haired, spectacled and slovenly fiend in a filthy undergarment",
                 "an exact replica of you",
                 "a tall, spectacled, smelly and lanky man with a lizard hanging from his nose by its teeth",
                 "a mirror-image of you",
                 "a silvery-haired, white-bearded fiend with spectacles wearing a dress coat",
                 "an extremely short man with a gray wig, hat, and wearing a comically long coat with sleeves hanging "
                 "far beyond his hands"]
        self.level = 3
        self.name = "Doppelganger"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 700
        self.gold = random.randint(1, 5)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 11
        self.dexterity = 18
        self.constitution = 14
        self.intelligence = 11
        self.wisdom = 12
        self.charisma = 14
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = ["Charm", "Sleep", "Web", "Phantasm"]
        self.vulnerabilities = ["Scorch", "Fireball", "Firestorm", "Immolation"]
        self.resistances = ["Hold Monster", "Banish"]
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 2
        self.hit_points = 52
        self.armor_class = 14
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = f"It polymorphs into the form of {random.choice(forms)}!!"
        self.attack_2 = 4
        self.attack_2_phrase = f"It shape-shifts into the form of {random.choice(forms)}!!"
        self.attack_3 = 4
        self.attack_3_phrase = f"It becomes {random.choice(forms)}!!"
        self.attack_4 = 4
        self.attack_4_phrase = f"It changes into {random.choice(forms)}!!"
        self.attack_5 = 4
        self.attack_5_phrase = f"It morphs into {random.choice(forms)}!!"
        self.introduction = f"You have encountered a Doppelganger! Your eyes see it as it truly is for just an " \
                            f"instant,\nbefore its dark humanoid silhouette begins to " \
                            f"churn like a tempestuous body of black water;\nTall, horrific, foul, and with inhuman " \
                            f"eyes that smoulder with greedy hunger.\nIts flesh is covered in disease and its mouth " \
                            f"is full of razor-sharp teeth.\nIt begins to smile in hideous delight."
        self.paralyze_phrase = "It thrusts forward, clutching your arm within its iron grip!!"
        self.paralyze_free_attack_phrase = "Completely petrified, you stand helpless as it slices at you with a " \
                                           "horrid claw\nand spits shards of broken glass into your frozen face!!"


class Specter(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Specter"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 250
        self.gold = random.randint(0, 1)  # self.level * 103 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 12)
        self.dexterity = random.randint(12, 16)
        self.constitution = random.randint(10, 12)
        self.intelligence = random.randint(9, 11)
        self.wisdom = 12
        self.charisma = random.randint(10, 12)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 8)
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.hit_dice = 6
        self.number_of_hd = 3
        self.hit_points = random.randint(20, 24) + self.constitution_modifier
        self.armor_class = random.randint(11, 13)
        self.multi_attack = True
        self.lesser_multi_attack = False
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
                            f"through a combination of wickedness, quantum manipulations, and its own death.\n" \
                            f"Its ghastly form resembles what it was in life, but its now dispossessed\n" \
                            f"identity has been completely erased and replaced with a simple motive and \n" \
                            f"purpose; A revulsion for the living and a hunger for their life-energy.."
        self.paralyze_phrase = "It places a cold, yet immaterial hand upon you!!"
        self.paralyze_free_attack_phrase = "Completely helpless, you feel your strength failing as it unnaturally " \
                                           "drains you!!"
        self.necrotic_phrase = "With pulsing energy, it reaches out to you, as a dark mist is released from its " \
                               "extended hand.."


class SpecterKing(Monster):

    def __init__(self):
        super().__init__()
        self.level = 3
        self.name = "Specter King"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 500
        self.gold = random.randint(6, 16)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = random.randint(15, 16)
        self.constitution = random.randint(15, 16)
        self.intelligence = random.randint(12, 13)
        self.wisdom = 14
        self.charisma = random.randint(10, 12)
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = 2
        self.dot_turns = dice_roll(1, 10)
        self.undead = True
        self.immunities = ["Turn Undead", "Web", "Hold Monster", "Banish"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.hit_dice = 8  #
        self.number_of_hd = 3  #
        self.hit_points = random.randint(25, 34) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "He places a cold, yet immaterial hand upon you for just a moment.."
        self.attack_2 = 1
        self.attack_2_phrase = "He extends a hand, which elongates into a horrible mist that thrusts toward you.. "
        self.attack_3 = 2
        self.attack_3_phrase = f"A cold, dreadful feeling overcomes you as the {self.name} looms over you, reaching\n" \
                               f"out to embrace you within his deadly touch!"
        self.attack_4 = 2
        self.attack_4_phrase = "He rushes straight at you and phase-shifts. He re-appears behind you, ready to strike!!"
        self.attack_5 = 3
        self.attack_5_phrase = "He silently raises his hands, releasing dreadfully wicked energies!!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "He releases weird draining energies from its outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Dreadful black droplets dance over his form as he unleashes\n" \
                                       "impossibly cold, white flames from both of its outstretched hands!!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "His empty eyes widen, as he rises up, harnessing the quantum energies and\n" \
                                       "hurling a wall of black energy toward you!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "Swirling around you in a confusing arc, he releases a mist\n" \
                                       "of dark energy which envelopes you!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "With muted malice, its arms elongate unnaturally, wildly entangling\n" \
                                       "you in a storm of wicked forces!"
        self.introduction = f"From out of nothingness, the Specter King materializes..A vile, undead form\n" \
                            f"of fear-inspiring and unnatural horrors. His ghostly form resembles his former\n" \
                            f"royal greatness, but now his entire existence is a mere quantum-driven and\n" \
                            f"endless nightmare of madness, devoid of any humanity. Upon seeing you, he silently\n" \
                            f"approaches, his countenance twisted in insane thirst for your life-energy.."
        self.paralyze_phrase = "With unnatural speed and silent swiftness, it places a cold, immaterial hand upon you.."
        self.paralyze_free_attack_phrase = "You feel agony crawling deep within you as you stand helpless and still!!"
        self.necrotic_phrase = "With pulsing energy, he reaches out to you, as a dark mist is released from his " \
                               "extended hand.."


class HobgoblinCaptain(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Hobgoblin Captain"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 2
        self.hit_points = (random.randint(36, 49)) + self.constitution_modifier
        self.armor_class = random.randint(17, 17)
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 3  # attack bonus
        self.attack_1_phrase = "He thrusts mightily forward with its javelin!.."
        self.attack_2 = 3
        self.attack_2_phrase = "He swings his greatsword with blinding speed!"
        self.attack_3 = 3
        self.attack_3_phrase = "He swings his greatsword with blinding speed!"
        self.attack_4 = 5
        self.attack_4_phrase = "He roars and swings his greatsword with murderous rage!"
        self.attack_5 = 5
        self.attack_5_phrase = "He raises his greatsword overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Hobgoblin Captain. Fierce, intelligent and disciplined, " \
                            f"and wearing heavy armor.\nWith weaponry polished and well-maintained, his yellow " \
                            f"teeth stretch into a surly grin behind his iron helm.\nNarrowing his eyes, " \
                            f"he approaches and stands before you unaffected and unafraid; ready for battle."


class Harpy(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Harpy"
        self.proper_name = "None"
        self.he_she_it = "she"
        self.his_her_its = "her"
        self.him_her_it = "her"
        self.experience_award = 450
        self.gold = random.randint(1, 5)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 13)
        self.dexterity = 13
        self.constitution = random.randint(11, 13)
        self.intelligence = 7
        self.wisdom = 10
        self.charisma = 13
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(1, 6)
        self.dot_turns = dice_roll(1, 6)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Fear", "Charm"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 1
        self.hit_points = (random.randint(36, 40)) + self.constitution_modifier
        self.armor_class = random.randint(11, 13)
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "She strikes with her blood-soaked club.."
        self.attack_2 = 5
        self.attack_2_phrase = "With a guttural growl, she strikes with her foul claws.. "
        self.attack_3 = 6
        self.attack_3_phrase = "She raises her heavy club overhead.."
        self.attack_4 = 8
        self.attack_4_phrase = "With terrible speed, she swings her horrid claws!"
        self.attack_5 = 10
        self.attack_5_phrase = "She leaps upon you, goring and striking fiercely!"
        self.introduction = f"You have encountered a Harpy. With the upper body of a humanoid female and unnatural, " \
                            f"horrific bestial appendages,\nshe stands, sniffing the air in your direction. " \
                            f"Her grotesque face contorts behind a nest of matted hair which hangs in clumps\n" \
                            f"as she lets out an awful shriek..."
        self.poison_phrase = ""
        self.paralyze_phrase = "She begins to sing a most beautiful, harmonic melody that is hypnotically alluring.."
        self.paralyze_free_attack_phrase = "You stand frozen in place as she ferociously attacks!!"


class GreenDragonWyrmling(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Green Dragon Wyrmling"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(1, 6)
        self.dot_turns = dice_roll(1, 6)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Fear", "Charm"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 1
        self.hit_points = (random.randint(36, 40)) + self.constitution_modifier
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 5
        self.attack_2_phrase = "With a languid growl, it strikes with its jaws.. "
        self.attack_3 = 5
        self.attack_3_phrase = "Proud and poised, it prepares to strike with its murderous jaws.."
        self.attack_4 = 14
        self.attack_4_phrase = "\'I am sorry. This will hurt you, my little friend.\', it says dryly, as it " \
                               "draws back and bites with venomous guile!"
        self.attack_5 = 18
        self.attack_5_phrase = "The beast leaps upon you, attacking fiercely!"
        self.introduction = f"You have encountered a Green Dragon Wyrmling; a young, cunning and evil beast. " \
                            f"As it approaches, it chuckles\nand addresses you in the common tongue! " \
                            f"\"Greetings, little one! It is most fortuitous to meet you..\"\n" \
                            f"You have very little time to ponder its greeting..."
        self.poison_phrase = "Wide-eyed and evil, it exhales a blast of putrid poison from its deepest evil innards!!"


class WhiteDragonWyrmling(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "White Dragon Wyrmling"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = ["Ice Storm"]
        self.vulnerabilities = ["Immolation", "Fireball", "Fire Storm"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 1
        self.hit_points = (random.randint(30, 32)) + self.constitution_modifier
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 5
        self.attack_2_phrase = "With a serpentine swaying, it strikes with its jaws.. "
        self.attack_3 = 5
        self.attack_3_phrase = "Perfectly focused, it prepares to strike.."
        self.attack_4 = 14
        self.attack_4_phrase = "Rearing up with elegant, murderous intent, it exhales an icy blast of hail!"
        self.attack_5 = 18
        self.attack_5_phrase = "Rearing up with elegant, murderous intent, it exhales a terrible, icy blast of hail!"
        self.introduction = f"You have encountered a White Dragon Wyrmling; a slow witted, evil, efficient hunter. " \
                            f"Confidently stepping forth,\nit roars viciously, undoubtedly preparing to have you " \
                            f"as a meal!"


class BugbearCaptain(Monster):

    def __init__(self):
        super().__init__()
        self.level = 4
        self.name = "Bugbear Captain"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 700
        self.gold = random.randint(3, 12)  # 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 3
        self.armor = 0
        self.shield = 0
        self.strength = 17
        self.dexterity = 14
        self.constitution = 14
        self.intelligence = 11
        self.wisdom = 12
        self.charisma = 11
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = 65 + self.constitution_modifier
        self.armor_class = 17
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 2  # attack bonus
        self.attack_1_phrase = "It thrusts mightily forward with its javelin!.."
        self.attack_2 = 4
        self.attack_2_phrase = "It swings its morningstar with blinding speed!"
        self.attack_3 = 4
        self.attack_3_phrase = "It swings its morningstar with blinding speed!"
        self.attack_4 = 5
        self.attack_4_phrase = "It roars and swings its morningstar with murderous rage!"
        self.attack_5 = 6
        self.attack_5_phrase = "It raises its morningstar overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Bugbear Captain; A battle-proven and fierce " \
                            f"enemy, driven by its\nhatred for humankind.  It stands, with weapons at the ready, " \
                            f"releasing a deep, slow snarl..."


class Ogre(Monster):

    def __init__(self):
        super().__init__()
        self.level = 5
        self.name = "Ogre"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.a_an = "an"
        self.experience_award = 650
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 4
        self.armor = 0
        self.shield = 0
        self.strength = 19
        self.dexterity = 8
        self.constitution = 16
        self.intelligence = 5
        self.wisdom = 7
        self.charisma = 7
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(58, 62)) + self.constitution_modifier
        self.armor_class = 11
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "It thrusts brutally toward you with its javelin!.."
        self.attack_2 = 4
        self.attack_2_phrase = "It swings its greatclub with blinding speed!"
        self.attack_3 = 4
        self.attack_3_phrase = "It swings its greatclub with blinding speed!"
        self.attack_4 = 4
        self.attack_4_phrase = "It roars and swings its greatclub with murderous rage!"
        self.attack_5 = 6
        self.attack_5_phrase = "It raises its greatclub overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered an Ogre; a dim-witted, ugly, giant brute of solid muscle. " \
                            f"Its dull disinterest quickly\nchanges to alertness as soon as it spots you. " \
                            f"It approaches, standing some 10 feet tall and shaking the ground beneath you.."


class Minotaur(Monster):

    def __init__(self):
        super().__init__()
        self.level = 5
        self.name = "Minotaur"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.a_an = "an"
        self.experience_award = 750
        self.gold = random.randint(3, 11)
        self.weapon_bonus = 4
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 11
        self.constitution = 16
        self.intelligence = 6
        self.wisdom = 16
        self.charisma = 9
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(70, 75)) + self.constitution_modifier
        self.armor_class = 14
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "It swings its greataxe with terrible power."
        self.attack_2 = 4
        self.attack_2_phrase = "It swings a heavy warhammer with awesome speed."
        self.attack_3 = 4
        self.attack_3_phrase = "It swings its greataxe."
        self.attack_4 = 4
        self.attack_4_phrase = "With a snort from its ringed nose, it raises its axe overhead for a mighty blow."
        self.attack_5 = 6
        self.attack_5_phrase = "It roars and swings its greataxe with murderous rage!"
        self.introduction = f"You have encountered a Minotaur; a massive, improbable humanoid of incredible strength " \
                            f"and stature.\nWith the head of a bull atop a towering frame, it roars with fearsome " \
                            f"evil and stands to face you!"


class DarkDwarf(Monster):

    def __init__(self):
        super().__init__()
        self.level = 5
        self.name = "Dark Dwarf"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 750
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 4
        self.armor = 0
        self.shield = 0
        self.strength = 14
        self.dexterity = 11
        self.constitution = 15
        self.intelligence = 11
        self.wisdom = 11
        self.charisma = 9
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Charm", "Sleep"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = 70
        self.armor_class = 16
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "He raises his warpick.."
        self.attack_2 = 4
        self.attack_2_phrase = "He swings his warhammer with blinding speed!"
        self.attack_3 = 4
        self.attack_3_phrase = "He readies his javelin for a stout thrust."
        self.attack_4 = 4
        self.attack_4_phrase = "He bellows with malice and rage as he swings his greataxe!"
        self.attack_5 = 6
        self.attack_5_phrase = "He raises his greataxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Dark Dwarf; A race of Dwarves who were cast out and forced " \
                            f"to delve more deeply\ninto the subterranean realms, eventually embracing the darkness " \
                            f"and shunning all outsiders.\nTheir shame turned to evil and their isolation to " \
                            f"rage. They call themselves the Duergar, \nand though they still resemble their" \
                            f" Dwarven cousins in stature, all else about them appears gray, evil and without light."


class Mummy(Monster):

    def __init__(self):
        super().__init__()
        self.level = 5
        self.name = "Mummy"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 700
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 8
        self.constitution = 15
        self.intelligence = 6
        self.wisdom = 12
        self.charisma = 12
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = dice_roll(2, 3)
        self.dot_turns = 5
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Web", "Banish"]
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 3
        self.hit_points = 70
        self.armor_class = 11
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "It gropes you in unnatural evil."
        self.attack_2 = 4
        self.attack_2_phrase = "It swings its dry limbs with unexpected speed."
        self.attack_3 = 4
        self.attack_3_phrase = "It thrusts a rotting fist toward you with great speed."
        self.attack_4 = 4
        self.attack_4_phrase = "It raises both rotting arms overhead to strike."
        self.attack_5 = 6
        self.attack_5_phrase = "It strikes with both dry, bony fists."
        self.introduction = f"Deadly and yet undead; You have encountered a Mummy. Still wrapped in bandages and " \
                            f"lurching slowly but unwaveringly\ntowards you, it stands before you in a field of " \
                            f"crackling Quantum energy."
        self.paralyze_phrase = "It latches onto your arm with an iron grip!"
        self.paralyze_free_attack_phrase = "You stare in complete helplessness as it gores you mercilessly!"
        self.necrotic_phrase = self.paralyze_phrase


class ZombieOgre(Monster):

    def __init__(self):
        super().__init__()
        self.level = 5
        self.name = "Zombie Ogre"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 750
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 4
        self.armor = 0
        self.shield = 0
        self.strength = 19
        self.dexterity = 6
        self.constitution = 18
        self.intelligence = 3
        self.wisdom = 6
        self.charisma = 5
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 3
        self.hit_points = (random.randint(80, 84)) + self.constitution_modifier
        self.armor_class = 10
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 4  # attack bonus
        self.attack_1_phrase = "With jerking thrusts, it lumbers toward you with its morningstar.."
        self.attack_2 = 4
        self.attack_2_phrase = "With a gasping and a growl, it swings its morningstar with blinding speed!"
        self.attack_3 = 4
        self.attack_3_phrase = "It swings its morningstar with both rotting hands!"
        self.attack_4 = 4
        self.attack_4_phrase = "It swings its morningstar with murderous rage!"
        self.attack_5 = 6
        self.attack_5_phrase = "It raises its morningstar overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Zombie Ogre; an abomination of nature which should not be. " \
                            f"Devoid of life energy,\nand, through some evil Quantum Manipulation, its giant hulking " \
                            f"mass now exists in an indefinite,\nmindless quest of seeking out the living and " \
                            f"devouring them entirely!\nIts towering, undead form bristles with quantum weirdness.."


class Troll(Monster):

    def __init__(self):
        super().__init__()
        self.level = 6
        self.name = "Troll"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2000
        self.gold = random.randint(5, 10)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 13
        self.constitution = 20
        self.intelligence = 7
        self.wisdom = 9
        self.charisma = 7
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 0
        self.dot_turns = 0
        self.undead = False
        self.immunities = []
        self.vulnerabilities = ["Immolation", "Fireball", "Fire Storm"]
        self.resistances = ["All"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(80, 85)) + self.constitution_modifier
        self.armor_class = random.randint(15, 16)
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 6
        self.attack_2_phrase = "It strikes with one terrible claw.. "
        self.attack_3 = 7
        self.attack_3_phrase = "With unexpected speed, it thrusts forward with jaws open wide.."
        self.attack_4 = 8
        self.attack_4_phrase = "It strikes with both terrible claws!"
        self.attack_5 = 10
        self.attack_5_phrase = "It assaults you with both its claws and horrid teeth!"
        self.introduction = f"You have encountered a Troll; A giant lizard-like humanoid of immense stature. " \
                            f"An insatiable, vile and stout creature,\nit slurps, snorts and approaches you fearlessly."


class HillGiant(Monster):

    def __init__(self):
        super().__init__()
        self.level = 6
        self.name = "Hill Giant"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2000
        self.gold = random.randint(2, 12)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 21
        self.dexterity = 8
        self.constitution = 19
        self.intelligence = 5
        self.wisdom = 9
        self.charisma = 6
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 0
        self.dot_turns = 0
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(100, 105)) + self.constitution_modifier
        self.armor_class = 13
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It thrusts forward with club in hand, swinging wildly."
        self.attack_2 = 6
        self.attack_2_phrase = "It strikes at you with great speed and strength. "
        self.attack_3 = 7
        self.attack_3_phrase = "It raises its fists overhead to strike.."
        self.attack_4 = 8
        self.attack_4_phrase = "It swings the club with dizzying power!"
        self.attack_5 = 10
        self.attack_5_phrase = "It reaches for you with its massive, crushing hands!"
        self.introduction = f"You have encountered a Hill Giant; A monstrous humanoid of immense size and miniscule " \
                            f"intellect. Holding a twisted tree in its hand\nwhich serves as a club, it shakes the " \
                            f"ground beneath your feet in its approach."


class Cyclops(Monster):

    def __init__(self):
        super().__init__()
        self.level = 6
        self.name = "Cyclops"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2300
        self.gold = random.randint(2, 12)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 22
        self.dexterity = 11
        self.constitution = 20
        self.intelligence = 8
        self.wisdom = 6
        self.charisma = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 0
        self.dot_turns = 0
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(100, 105)) + self.constitution_modifier
        self.armor_class = 13
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "The Cyclops lifts a rock to hurl at you."
        self.attack_2 = 6
        self.attack_2_phrase = "It grabs for you, attemping to crush your tiny frame! "
        self.attack_3 = 7
        self.attack_3_phrase = "It clenches a fist and swings its gargantuan left arm.."
        self.attack_4 = 8
        self.attack_4_phrase = "It raises its greatclub overheard to strike you."
        self.attack_5 = 10
        self.attack_5_phrase = "It reaches for you with its massive, crushing hands!"
        self.introduction = f"You have encountered a Cyclops; A one-eyed giant of fear-inspiring size and strength " \
                            f"who languidly wanders the underground realms.\nIt approaches you with ground-shaking " \
                            f"power and mass."


class WrathfulAvenger(Monster):

    def __init__(self):
        super().__init__()
        self.level = 6
        self.name = "Wrathful Avenger"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2300
        self.gold = random.randint(1, 10)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 14
        self.constitution = 18
        self.intelligence = 13
        self.wisdom = 16
        self.charisma = 18
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(4, 6)
        self.dot_turns = dice_roll(4, 6)
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Turn Undead"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(120, 135)) + self.constitution_modifier
        self.armor_class = 13
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It lunges at you with its dagger."
        self.attack_2 = 6
        self.attack_2_phrase = "With a wide swing, it slices at you with its dagger."
        self.attack_3 = 7
        self.attack_3_phrase = "Swiftly, it stabs you with its nasty dagger."
        self.attack_4 = 8
        self.attack_4_phrase = "It feints to the side, then, switching hands, it swings its dagger with deadly speed."
        self.attack_5 = 10
        self.attack_5_phrase = "With incredible speed, it juts forward, stabbing mercilessly."
        self.introduction = f"You have encountered a Wrathful Avenger; The unnatural, undead, quantum-infused " \
                            f"remains " \
                            f"of a human victim of an egregious injustice-\nforever searching for its killer... " \
                            f"It seems to have found you first!"
        self.paralyze_phrase = "Its white, lifeless eyes begin to burn with bright fury! You feel your motor skills " \
                               "retreat as it gazes upon you.."
        self.paralyze_free_attack_phrase = "Patiently and without remorse, it slices at you with misguided purpose " \
                                           "and hate."


class HobgoblinWarlord(Monster):

    def __init__(self):
        super().__init__()
        self.level = 6
        self.name = "Hobgoblin Warlord"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2300
        self.gold = random.randint(1, 10)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 14
        self.constitution = 16
        self.intelligence = 14
        self.wisdom = 11
        self.charisma = 15
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = 0
        self.dot_turns = 0
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(90, 105)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It swings its longsword with great power."
        self.attack_2 = 6
        self.attack_2_phrase = "It raises its longsword overhead for a chopping blow."
        self.attack_3 = 7
        self.attack_3_phrase = "It jumps to the side, turns, and thrusts its heavy javelin with fluid speed."
        self.attack_4 = 8
        self.attack_4_phrase = "It bashes you with its massive shield!"
        self.attack_5 = 11
        self.attack_5_phrase = "It swings its sword mightily, and then bashes with its heavy shield for a lethal " \
                               "combination attack!"
        self.introduction = f"You have encountered a Hobgoblin Warlord; A calculating, seasoned veteran, forged by " \
                            f"countless wars and battles.\nIts thick, heavy armor covers every inch of vulnerable " \
                            f"flesh. Only its eyes, smouldering in the shadows of a great helm, can be seen."


class Wyvern(Monster):

    def __init__(self):
        super().__init__()
        self.level = 7
        self.name = "Wyvern"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 2800
        self.gold = random.randint(1, 5)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 19
        self.dexterity = 10
        self.constitution = 16
        self.intelligence = 10
        self.wisdom = 12
        self.charisma = 6
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(7, 6)
        self.dot_turns = dice_roll(1, 2)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = (random.randint(105, 115)) + self.constitution_modifier
        self.armor_class = 13
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 5  # attack bonus
        self.attack_1_phrase = "It swings its deadly claws great power."
        self.attack_2 = 7
        self.attack_2_phrase = "It thrusts forward with ravenous jaws!"
        self.attack_3 = 8
        self.attack_3_phrase = "Flapping its great wings, it rears up and prepares to pounce!"
        self.attack_4 = 9
        self.attack_4_phrase = "It swings its claws in a swift combination."
        self.attack_5 = 13
        self.attack_5_phrase = "It bites, and then claws you in a horrible combination!"
        self.introduction = f"You have encountered a Wyvern; A dragon-like beast with wide, fleshy wings and skin " \
                            f"covered in jagged spikes.\nIt holds a long, deadly, twitching tail high in the air. " \
                            f"You spot the lethal, poisonous barb at the tip, and steel yourself for\n" \
                            f"the confrontation."
        self.poison_phrase = f"The Wyvern attacks with its poisonous tail stinger!"


class DrowManipulator(Monster):

    def __init__(self):
        super().__init__()
        self.level = 7
        self.name = "Drow Manipulator"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 3000
        self.gold = random.randint(1, 15)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 9
        self.dexterity = 14
        self.constitution = 10
        self.intelligence = 17
        self.wisdom = 13
        self.charisma = 17
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(2, 6)
        self.dot_turns = dice_roll(1, 3)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["All"]
        self.quantum_energy = True
        self.hit_dice = 10
        self.number_of_hd = 5
        self.hit_points = 45
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "He raises a fist, and disappears in a puff of darkness, reappearing behind you and " \
                               "striking with a nasty knife!"
        self.attack_2 = 8
        self.attack_2_phrase = "He phase-shifts into nothingness, appearing beside you and stabbing with deadly " \
                               "quickness!"
        self.attack_3 = 8
        self.attack_3_phrase = "Time seems to slow, and you along with it, as he swings his dagger with impossible, " \
                               "world-bending speed!"
        self.attack_4 = 8
        self.attack_4_phrase = "The room spins, disorienting you, as he stabs at you mercilessly!"
        self.attack_5 = 12
        self.attack_5_phrase = "He splits into 12 replicas of himself, all stabbing at you from every conceivable " \
                               "angle!"
        self.quantum_attack_1 = 12
        self.quantum_attack_1_phrase = "Deadly tentacles of dark energies thrust toward you from his outstretched " \
                                       "hand!"
        self.quantum_attack_2 = 12
        self.quantum_attack_2_phrase = "Dark weaponry is released from his palms in the form of weird Quantum " \
                                       "flames!"
        self.quantum_attack_3 = 12
        self.quantum_attack_3_phrase = "He raises both hands, harnessing the quantum energies and\n" \
                                       "releases bolts of searing lightning!"
        self.quantum_attack_4 = 13
        self.quantum_attack_4_phrase = "He steps forward, thrusting his hands toward you, as disturbing\n" \
                                       "images and fearsome nightmarish creatures materialize in your mind!"
        self.quantum_attack_5 = 13
        self.quantum_attack_5_phrase = "He releases a frigid ice storm from his hands that envelopes you!"
        self.introduction = f"You see a fuzzy silhouette of a humanoid approaching, as the air bristles with " \
                            f"Quantum Weirdness.\n" \
                            f"You have encountered a Drow Manipulator! It phases into form and approaches you."
        self.paralyze_phrase = "The manipulator holds out a hand, and you fight the gripping Quantum Forces holding " \
                               "you fast!"
        self.paralyze_free_attack_phrase = "With perfect and pragmatic poise, he slices at you with his nasty knife!"
        self.poison_phrase = f"He attacks with a poisonous dagger!"


class MindFlayer(Monster):

    def __init__(self):
        super().__init__()
        self.level = 7
        self.name = "Mind FLayer"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 3000
        self.gold = random.randint(1, 15)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 11
        self.dexterity = 12
        self.constitution = 12
        self.intelligence = 19
        self.wisdom = 17
        self.charisma = 17
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(2, 6)
        self.dot_turns = dice_roll(1, 4)
        self.undead = False
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["All"]
        self.quantum_energy = True
        self.hit_dice = 10
        self.number_of_hd = 5
        self.hit_points = 71
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "Its tentacles stretch out toward you with impossible speed!"
        self.attack_2 = 11
        self.attack_2_phrase = "Its tentacles shoot forth, wrapping around your leg!"
        self.attack_3 = 12
        self.attack_3_phrase = "Its tentacles stretch out and wrap around your arm!"
        self.attack_4 = 13
        self.attack_4_phrase = "Its tentacles dart toward you, wrapping around you and squeezing with terrible malice!!"
        self.attack_5 = 14
        self.attack_5_phrase = "Its tentacles shoot out and wrap around your neck! You gasp for air!"
        self.quantum_attack_1 = 15
        self.quantum_attack_1_phrase = "A blast of Quantum Energies hit you, creating mental anguish beyond any pain" \
                                       "you have ever known!"
        self.quantum_attack_2 = 15
        self.quantum_attack_2_phrase = "Terrible, nightmarish visions plague your mind as it wickedly reaches out " \
                                       "toward you with clawed fingers.."
        self.quantum_attack_3 = 15
        self.quantum_attack_3_phrase = "It rises up, levitating on a Quantum platform and releases a wall of " \
                                       "Quantum Energy!"
        self.quantum_attack_4 = 16
        self.quantum_attack_4_phrase = "It reaches a claw-like hand over its head. Suddenly, you feel yourself being " \
                                       "lifted off the ground....and dropped!\nThe ground rushes toward you!"
        self.quantum_attack_5 = 18
        self.quantum_attack_5_phrase = "It points a bony finger at your arm. You lose control of it! " \
                                       "You stand, helplessly striking at yourself!"
        self.introduction = f"You have encountered a Mind Flayer; A hideous, tyrannical humanoid with a head " \
                            f"resembling an octopus.\nEndowed with evil Quantum insights and innate understanding, " \
                            f"Mind Flayers tunnel through realities in search of slaves\nfor their twisted purposes." \
                            f"Any who resist them are reduced to helpless, mindless servants through " \
                            f"wicked manipulations.."
        self.paralyze_phrase = "Its tentacles shoot out and wrap around your head! You feel your motor skills diminish!"
        self.paralyze_free_attack_phrase = "It tears at your flesh with pure evil and precision!"
        self.poison_phrase = f"Its tentacles wrap around you, as a protruding, poisonous stinger approaches " \
                             f"your face!"


class MorbidDefender(Monster):

    def __init__(self):
        super().__init__()
        self.level = 7
        self.name = "Morbid Defender"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 3000
        self.gold = random.randint(2, 14)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 16
        self.constitution = 18
        self.intelligence = 13
        self.wisdom = 16
        self.charisma = 18
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = True
        self.immunities = []
        self.vulnerabilities = []
        self.resistances = ["Turn Undead"]
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 4
        self.hit_points = (random.randint(125, 135)) + self.constitution_modifier
        self.armor_class = 16
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "It swings its greatsword with haste and hate."
        self.attack_2 = 8
        self.attack_2_phrase = "With a skillful feint, it strikes with its greatsword."
        self.attack_3 = 8
        self.attack_3_phrase = "Moving forward in a flurry of Quantum energy, it strikes with fiery power!"
        self.attack_4 = 10
        self.attack_4_phrase = "Thrusting toward you, it swings its great blade, crackling with white-hot lightning!"
        self.attack_5 = 16
        self.attack_5_phrase = "With great strength, it bashes with its shield and follows up with a deadly " \
                               "sword strike!"
        self.introduction = f"You have encountered a Morbid Defender; An undead soldier who swore, ages ago, " \
                            f"an oath to preserve and protect\nthe peace and prosperity of Sauengard. Now infused " \
                            f"with Quantum Energy by some evil Manipulator, the Defender roams the dungeons,\n" \
                            f"forever bound to a pointless mission: Attack the living."
        self.paralyze_phrase = "It slams its shield on the ground at your feet, sending shockwaves through you! You" \
                               "feel your body weakening..."
        self.paralyze_free_attack_phrase = "In your petrified state, it hacks at you mercilessly with evil malice!"


class BoltThrower(Monster):

    def __init__(self):
        super().__init__()
        self.level = 7
        self.name = "Bolt Thrower"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 3000
        self.gold = random.randint(5, 25)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 16
        self.constitution = 18
        self.intelligence = 12
        self.wisdom = 11
        self.charisma = 11
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Lightning"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 4
        self.hit_points = (random.randint(135, 145)) + self.constitution_modifier
        self.armor_class = 16
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "It swings an arcing greataxe with great power and precision."
        self.attack_2 = 8
        self.attack_2_phrase = "It strikes at you with its heavy, electrified warhammer."
        self.attack_3 = 12
        self.attack_3_phrase = "It strikes in combination; an electrified greataxe in its left hand, followed by " \
                               "its warhammer!"
        self.attack_4 = 16
        self.attack_4_phrase = "It cracks its Quantum whip, and the powerful arcflash surges through your very bones!"
        self.attack_5 = 20
        self.attack_5_phrase = "It circles its Quantum whip menacingly as it suddenly shoots forth, with " \
                               "great speed and precision. You feel the heat and power of its arcflash!"
        self.introduction = f"You have encountered a Bolt Thrower; A powerful race of warriors possessing both " \
                            f"impressive physical\nstrength as well as expansive Quantum abilities. " \
                            f"With thick, armored skin and standing some 8 feet tall,\na flattened cranium," \
                            f"immense, muscled appendages, and armed with a deadly arsenal\nof weapons including a " \
                            f"whip endowed with electrified Quantum weirdness,\nit fearlessly approaches you."
        self.paralyze_phrase = "It encircles you with its whip!"
        self.paralyze_free_attack_phrase = "In your helplessness, it hammers you mercilessly!"


class FrostGiant(Monster):

    def __init__(self):
        super().__init__()
        self.level = 8
        self.name = "Frost Giant"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 4000
        self.gold = random.randint(10, 35)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 23
        self.dexterity = 9
        self.constitution = 21
        self.intelligence = 9
        self.wisdom = 10
        self.charisma = 12
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Ice Storm"]
        self.vulnerabilities = ["Firestorm", "Fireball"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 5
        self.hit_points = (random.randint(135, 145)) + self.constitution_modifier
        self.armor_class = 15
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its greataxe with might and skill.."
        self.attack_2 = 12
        self.attack_2_phrase = "It strikes at you with a heavy fist, followed by a an axe swing!"
        self.attack_3 = 14
        self.attack_3_phrase = "It swings its axe with both hands for a mighty blow."
        self.attack_4 = 18
        self.attack_4_phrase = "It stomps the ground with a foot, stumbling you, and comes down with a mighty axe blow!"
        self.attack_5 = 22
        self.attack_5_phrase = "It grabs you with a crushing fist, and attacks with a mighty axe blow!"
        self.introduction = f"You have encountered a Frost Giant; A huge humanoid out of myths, now brought to this " \
                            f"reality by Quantum improbability.\nBuilt of hard, frozen flesh for battle, " \
                            f"wielding an enormous greataxe, and towering above you at some 12 feet in height,\n" \
                            f"its footsteps shake you to the core as it approaches."


class YoungBlackDragon(Monster):

    def __init__(self):
        super().__init__()
        self.level = 8
        self.name = "Young Black Dragon"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 4000
        self.gold = random.randint(10, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 20
        self.dexterity = 14
        self.constitution = 17
        self.intelligence = 12
        self.wisdom = 11
        self.charisma = 15
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = ["Ice Storm"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 6
        self.hit_points = (random.randint(135, 145)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its jagged tail.."
        self.attack_2 = 12
        self.attack_2_phrase = "It bites and claws at you with frightening power!"
        self.attack_3 = 14
        self.attack_3_phrase = "It hisses with evil, swings its jagged tail, then spins to follow up with a terrible" \
                               " bite!"
        self.attack_4 = 18
        self.attack_4_phrase = "Roaring with hate, it bites and claws at you, followed by a swing of its jagged tail!"
        self.attack_5 = 22
        self.attack_5_phrase = "It rears up and blasts you with acid from its foul innards!"
        self.introduction = f"You have encountered a Young Black Dragon; a purely evil, 4-legged, winged beast " \
                            f"with thick, armored scales,\nand a golden underbelly. Its massive claws and teeth " \
                            f"glisten like raven's claws as it snorts and approaches you on all 4 legs."


class YoungGreenDragon(Monster):

    def __init__(self):
        super().__init__()
        self.level = 8
        self.name = "Young Green Dragon"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 4000
        self.gold = random.randint(10, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 20
        self.dexterity = 12
        self.constitution = 17
        self.intelligence = 16
        self.wisdom = 13
        self.charisma = 15
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 6
        self.hit_points = (random.randint(135, 145)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its scaly tail.."
        self.attack_2 = 12
        self.attack_2_phrase = "It bites and claws at you with terrible speed and power!"
        self.attack_3 = 14
        self.attack_3_phrase = "It roars hatefully, swings its jagged tail, then bites with its razor-sharp teeth!"
        self.attack_4 = 18
        self.attack_4_phrase = "With a bellowing roar, it bites and strikes at you with its front claws!"
        self.attack_5 = 22
        self.attack_5_phrase = "Roaring with hate, it bites and claws at you, followed by a swing of its jagged tail!"
        self.introduction = f"You have encountered a Young Black Dragon; a purely evil, 4-legged, winged beast " \
                            f"with thick, armored scales,\nand a golden underbelly. Its massive claws and teeth " \
                            f"glisten like raven's claws as it snorts and approaches you on all 4 legs."
        self.poison_phrase = "Wide-eyed and evil, it exhales a blast of putrid poison from its deepest evil innards!!"


class MorbidKnight(Monster):

    def __init__(self):
        super().__init__()
        self.level = 8
        self.name = "Morbid Knight"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 4000
        self.gold = random.randint(10, 35)
        self.weapon_bonus = 7
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 14
        self.constitution = 15
        self.intelligence = 14
        self.wisdom = 14
        self.charisma = 15
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = True
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = ["Turn Undead"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 6
        self.hit_points = (random.randint(90, 100)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its greatsword with blazing speed.."
        self.attack_2 = 12
        self.attack_2_phrase = "It strikes and stabs with its glaring greatsword!"
        self.attack_3 = 15
        self.attack_3_phrase = "It hacks at you repeatedly."
        self.attack_4 = 19
        self.attack_4_phrase = "It slams you with its shield, followed by a quick sword strike!"
        self.attack_5 = 24
        self.attack_5_phrase = "It stuns you momentarily with its tower shield, and hacks at you repeatedly with " \
                               "deadly sword strikes!"
        self.introduction = f"You have encountered a Morbid Knight; Undead due to Quantum probabilities, it forever " \
                            f"holds to its sworn duty\nto protect and defend the royal realm of Sauengard. Heavily " \
                            f"armored and wielding a shimmering greatsword,\nit stands ready for any confrontation."


class Assassin(Monster):

    def __init__(self):
        super().__init__()
        self.level = 8
        self.name = "Assassin"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.a_an = "an"
        self.experience_award = 4000
        self.gold = random.randint(25, 35)
        self.weapon_bonus = 6
        self.armor = 0
        self.shield = 0
        self.strength = 11
        self.dexterity = 16
        self.constitution = 14
        self.intelligence = 13
        self.wisdom = 11
        self.charisma = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 3
        self.hit_points = (random.randint(60, 75)) + self.constitution_modifier
        self.armor_class = 20  # super high armor, hard to hit, low damage, low hitpoints
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "He swings a dark blade from the shadows.."
        self.attack_2 = 12
        self.attack_2_phrase = "With quiet precision, he swings from the darkness.."
        self.attack_3 = 14
        self.attack_3_phrase = "Disappearing from view for an instant, he cuts you with his dagger.."
        self.attack_4 = 18
        self.attack_4_phrase = "He swings, cuts, and retreats into the shadows.."
        self.attack_5 = 25
        self.attack_5_phrase = "With a whispering swing, his blade finds your soft flesh and cuts deep.."
        self.introduction = f"You have encountered an Assassin; An amoral killer for hire, schooled in all manner of " \
                            f"poisons and stealth.\nFrom his boots to his hood, his garb is so dark, light seems to " \
                            f"simply fall into it. His movements are fluid,\nsmooth, and deadly quiet. His " \
                            f"silhouette " \
                            f"is so difficult to track, you conclude he must be manipulating reflections\nwith " \
                            f"Quantum weirdness!"
        self.poison_phrase = "Suddenly appearing behind you, he stabs at you with a poison blade!!"


class FireGiant(Monster):

    def __init__(self):
        super().__init__()
        self.level = 9
        self.name = "Fire Giant"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 5000
        self.gold = random.randint(20, 35)
        self.weapon_bonus = 6
        self.armor = 0
        self.shield = 0
        self.strength = 25
        self.dexterity = 9
        self.constitution = 23
        self.intelligence = 10
        self.wisdom = 14
        self.charisma = 13
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Firestorm", "Fireball", "Scorch", "Immolation"]
        self.vulnerabilities = ["Ice Storm"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 6
        self.hit_points = (random.randint(155, 165)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its greatsword with might and skill.."
        self.attack_2 = 12
        self.attack_2_phrase = "It strikes at you with a heavy, armored fist, followed by a greatsword swing!"
        self.attack_3 = 14
        self.attack_3_phrase = "It swings its sword with both hands for a mighty blow."
        self.attack_4 = 18
        self.attack_4_phrase = "It punches you square in the face, and follows with a mighty " \
                               "sword blow!"
        self.attack_5 = 24
        self.attack_5_phrase = "It grabs you with a crushing, armored fist, and attacks with a mighty sword swing!"
        self.introduction = f"You have encountered a Fire Giant; A prodigious humanoid from out of legend, " \
                            f"now tunneled to this " \
                            f"reality by Quantum improbability.\nFire Giants are battle-hardened " \
                            f"mercenaries and raiders, known for merciless destruction and fighting skills.\n" \
                            f"With flaming hair and eyes, it thunders toward you as its black, heavy plate mail " \
                            f"creaks with ominous dread."


class Widow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 9
        self.name = "Widow"
        self.proper_name = "None"
        self.he_she_it = "she"
        self.his_her_its = "her"
        self.him_her_it = "her"
        self.experience_award = 5000
        self.gold = random.randint(5, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 16
        self.constitution = 14
        self.intelligence = 16
        self.wisdom = 11
        self.charisma = 16
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 6
        self.hit_points = (random.randint(135, 155)) + self.constitution_modifier
        self.armor_class = 17
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "She swings her Drow blade with incredible speed.."
        self.attack_2 = 12
        self.attack_2_phrase = "Knocking you down with a leg, she stabs sadistically with her blade.."
        self.attack_3 = 14
        self.attack_3_phrase = "Towering above you, she pounces with all her might and then cuts with her Drow blade!"
        self.attack_4 = 18
        self.attack_4_phrase = "She holds you fast with 2 spidery legs as she hacks with her blade!"
        self.attack_5 = 25
        self.attack_5_phrase = "Calling out with a screeching howl, myriads of spiders are called forth and attack!"
        self.introduction = f"You have encountered a Widow; An improbable life form from the cruel imagination of " \
                            f"a Master Manipulator.\nWith the upper body of a beautiful human fused to that of a " \
                            f"spider, her own tortured existence\nhas twisted her toward wild evil. Her movements " \
                            f"are quick as lightning, and her light-footed crawling\nbelies her massive body. " \
                            f"Her glistening fangs drip with poison as she approaches!"
        self.poison_phrase = "Grabbing you in her lean, lovely arms, she attacks with poison fangs!!"


class YoungBlueDragon(Monster):

    def __init__(self):
        super().__init__()
        self.level = 9
        self.name = "Young Blue Dragon"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 5000
        self.gold = random.randint(20, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 21
        self.dexterity = 10
        self.constitution = 19
        self.intelligence = 14
        self.wisdom = 13
        self.charisma = 17
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Lightning"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 6
        self.hit_points = (random.randint(145, 155)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 12  # attack bonus
        self.attack_1_phrase = "It swings its spiked and scaly tail.."
        self.attack_2 = 14
        self.attack_2_phrase = "It bites and claws at you with terrible speed and power!"
        self.attack_3 = 16
        self.attack_3_phrase = "It roars hatefully, swings its jagged tail, then bites with its razor-sharp teeth!"
        self.attack_4 = 18
        self.attack_4_phrase = "With a bellowing roar, it bites and strikes at you with its front claws!"
        self.attack_5 = 35
        self.attack_5_phrase = "Drawing a deep breath, it releases a storm of electrical energy from deep within!"
        self.introduction = f"You have encountered a Young Blue Dragon; An electrified beast crackling with " \
                            f"Quantum energy.\nArcing blue currents dance upon its scales as it snorts dismissively " \
                            f"and approaches."


class Wraith(Monster):

    def __init__(self):
        super().__init__()
        self.level = 9
        self.name = "Wraith"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 5000
        self.gold = random.randint(1, 4)
        self.weapon_bonus = 7
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 14
        self.constitution = 15
        self.intelligence = 19
        self.wisdom = 17
        self.charisma = 17
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = dice_roll(7, 9)
        self.dot_turns = dice_roll(5, 7)
        self.undead = True
        self.immunities = ["Turn Undead", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = ["Web", "Banish"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 6
        self.hit_points = (random.randint(125, 145)) + self.constitution_modifier
        self.armor_class = 17
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings its greatsword with deadly malice."
        self.attack_2 = 12
        self.attack_2_phrase = "It swings its greatsword with unexpected speed."
        self.attack_3 = 14
        self.attack_3_phrase = "It hacks at you repeatedly with its greatsword."
        self.attack_4 = 16
        self.attack_4_phrase = "It strikes at you with blinding speed in a skillful combination."
        self.attack_5 = 20
        self.attack_5_phrase = "It raises its greatsword overhead, strikes with great strength, and continues " \
                               "hacking with merciless malice!"
        self.introduction = f"A black mist coalesces in front of you; You have encountered a Wraith. Floating " \
                            f"before you in a field of Quantum weirdness, \nand hidden from your mind's full " \
                            f"comprehension, your eyes strain to see its true form; A crowned, skull-ish head, " \
                            f"gaping bony arms,\n" \
                            f"grand, kingly armor, and a long, deadly sword gripped within fleshless fingers. You " \
                            f"feel the air around you surge with energy."
        self.paralyze_phrase = "It clutches your arm with an ironclad grip!"
        self.paralyze_free_attack_phrase = "You look on, completely helpless as it gores you mercilessly!"
        self.necrotic_phrase = "With slow, methodical mania, it stabs at you with a necrotic blade.."


class Necrophagist(Monster):

    def __init__(self):
        super().__init__()
        self.level = 9
        self.name = "Necrophagist"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 5000
        self.gold = random.randint(5, 12)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 16
        self.dexterity = 14
        self.constitution = 15
        self.intelligence = 11
        self.wisdom = 12
        self.charisma = 12
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 2
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(7, 9)
        self.dot_turns = dice_roll(5, 7)
        self.undead = True
        self.immunities = ["Turn Undead", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = ["Web"]
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 6
        self.hit_points = 135
        self.armor_class = 16
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "It swings its claw-like and bony hands wildly."
        self.attack_2 = 10
        self.attack_2_phrase = "It swings its claw-like and bony hands with unexpected speed."
        self.attack_3 = 11
        self.attack_3_phrase = "It strikes at you repeatedly and mercilessly."
        self.attack_4 = 16
        self.attack_4_phrase = "It swings a combination of wild, tumultuous blows!"
        self.attack_5 = 35
        self.attack_5_phrase = "It spins around...\nThe casket roped to its back bursts open! An explosion of\n" \
                               "filth, bones and jagged fragmentation rush at you!"
        self.introduction = f"You come upon a foul, putrefying humanoid wretch with a rotting coffin strapped upon " \
                            f"its back.\nWith pale gray flesh covered in malignancy, and with stark, staring eyes," \
                            f" it senses you and approaches.\n" \
                            f"You have encountered a Necrophagist;\nA Quantum-undead human" \
                            f"forever cursed to roam among the graves, in search of carrion."
        self.paralyze_phrase = "It looks upon you with a terrifying, morbid gaze! You feel your resolve weakening!"
        self.paralyze_free_attack_phrase = "Stiff and motionless, you dig for the courage to endure its savage attack!"


class YoungRedDragon(Monster):

    def __init__(self):
        super().__init__()
        self.level = 10
        self.name = "Young Red Dragon"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 6000
        self.gold = random.randint(25, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 23
        self.dexterity = 10
        self.constitution = 21
        self.intelligence = 14
        self.wisdom = 11
        self.charisma = 19
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Firestorm", "Fireball", "Scorch", "Immolation"]
        self.vulnerabilities = ["Ice Storm"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 6
        self.hit_points = (random.randint(165, 175)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 12  # attack bonus
        self.attack_1_phrase = "It whips its heavy, spiked tail.."
        self.attack_2 = 14
        self.attack_2_phrase = "It bites and claws at you with terrible speed and power!"
        self.attack_3 = 16
        self.attack_3_phrase = "It roars hatefully, swings its huge tail, then bites with its razor-sharp teeth!"
        self.attack_4 = 18
        self.attack_4_phrase = "With a bellowing roar, it bites and strikes at you with both of its front claws!"
        self.attack_5 = 45
        self.attack_5_phrase = "Drawing a deep breath, it releases a column of hot flames from deep within!!"
        self.introduction = f"You have encountered a Young Red Dragon; A dangerous, deadly and proud beast from " \
                            f"out of Quantum improbability.\nHot smoke leaks from its nostrils, and the ground " \
                            f"shakes as it approaches."


class MorbidBehemoth(Monster):

    def __init__(self):
        super().__init__()
        self.level = 10
        self.name = "Morbid Behemoth"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 6000
        self.gold = random.randint(1, 5)
        self.weapon_bonus = 5
        self.armor = 0
        self.shield = 0
        self.strength = 19
        self.dexterity = 18
        self.constitution = 16
        self.intelligence = 16
        self.wisdom = 16
        self.charisma = 13
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 2
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = True
        self.immunities = ["Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 8
        self.number_of_hd = 6
        self.hit_points = (random.randint(115, 125)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "It slams you with a heavy fist.."
        self.attack_2 = 10
        self.attack_2_phrase = "It strikes in a flurry of heavy hands.."
        self.attack_3 = 11
        self.attack_3_phrase = "It slams the ground at your feet, knocking you off balance, and pounds you with a\n" \
                               "heavy fist!"
        self.attack_4 = 12
        self.attack_4_phrase = "It raises its intertwined hands overhead and slams you with great speed and power!"
        self.attack_5 = 35
        self.attack_5_phrase = "Grabbing you in its unyielding grip, it pummels you relentlessly with a hammering " \
                               "fist!!"
        self.introduction = f"You have encountered a Morbid Behemoth; An immense, hateful creature of Quantum origin " \
                            f"in life, and now,\nundead and mindless by the will of a Master Manipulator. Covered " \
                            f"with sludge, silt and swamp-ish slime, its trunk dangles and swings as it approaches.\n" \
                            f"From behind muddy, hanging seaweed, two green and glowing eyes focus upon you!"
        self.paralyze_phrase = f"It grabs you within its thick, heavy, root-wrapped arms!"
        self.paralyze_free_attack_phrase = "From deep within, you burn with agony as it squeezes you with " \
                                           "unrelenting, wild power!!"
        self.necrotic_phrase = "With burning energy and groping limbs, it pulls you into its crushing grip.."


class ChaosMonster(Monster):

    def __init__(self):
        super().__init__()
        self.level = 10
        self.name = "Chaos Monster"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 6000
        self.gold = random.randint(25, 35)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 18
        self.dexterity = 16
        self.constitution = 18
        self.intelligence = 18
        self.wisdom = 18
        self.charisma = 16
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster"]
        self.vulnerabilities = ["Fear"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 6
        self.hit_points = (random.randint(135, 155)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 11  # attack bonus
        self.attack_1_phrase = "It whips at you with materialized weaponry from outstretched arms.."
        self.attack_2 = 12
        self.attack_2_phrase = "A volly of sharp stone, sand and ice shoot at you from its now blackened, empty form!"
        self.attack_3 = 14
        self.attack_3_phrase = "Dozens of appendages form spontaneously and strike at you from every conceivable " \
                               "angle!!"
        self.attack_4 = 18
        self.attack_4_phrase = "Chains, spikes and living steel burst forth from 12 fingered hands and shoot toward " \
                               "you with serpentine weirdness!"
        self.attack_5 = 25
        self.attack_5_phrase = "Stretching into a twisted and elongated trail of negative energy, it encircles you " \
                               "with searing heat and light\nthat crush and burn you from within!!"
        self.introduction = f"You see a vaguely humanoid silhouette of ever-changing dark, random patterns and " \
                            f"colors.\nYou have encountered a Chaos Monster. Its large stature and limbs churn " \
                            f"continually with shape-shifting confusion\nwhich covers every inch of its form. " \
                            f"Its arms grow long, and then shorten, a tail appears and becomes nonexistent.\n" \
                            f"An impossibly large and completely disproportional, gaping mouth of jagged, chromatic " \
                            f"teeth chomp menacingly, and then morph\ninto nothingness. It approaches in haphazard, " \
                            f"unpredictable zig-zags and leaps. The air is alight\nwith Quantum weirdness.."
        self.paralyze_phrase = f"Dark, twisted energy wraps around you in a rapid, boiling froth!!"
        self.paralyze_free_attack_phrase = "Terrible tentacles and trails of Quantum weaponry penetrate your flesh " \
                                           "as you stare, helplessly mesmerized and moribund!"


class Leviathan(Monster):

    def __init__(self):
        super().__init__()
        self.level = 10
        self.name = "Leviathan"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 6000
        self.gold = random.randint(1, 5)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 19
        self.dexterity = 18
        self.constitution = 16
        self.intelligence = 16
        self.wisdom = 19
        self.charisma = 18
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(6, 9)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Vortex", "Charm"]
        self.vulnerabilities = ["Scorch", "Fireball", "Firestorm", "Immolation"]
        self.resistances = ["Banish"]
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 8
        self.hit_points = (random.randint(135, 155)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 11  # attack bonus
        self.attack_1_phrase = "It whips at you with a chattering tail.."
        self.attack_2 = 12
        self.attack_2_phrase = "It bites with clamping jaws and dripping fangs!"
        self.attack_3 = 13
        self.attack_3_phrase = "Whipping at you with its deadly tail, it turns and bites at you with a hideous hiss.."
        self.attack_4 = 18
        self.attack_4_phrase = "It bites, whips and finally, gores you with its gleaming horns in a " \
                               "flurry of fierce attacks!"
        self.attack_5 = 25
        self.attack_5_phrase = "Twisting around you in a swirl of scales and spikes, it collapses inward upon you. " \
                               "You hear your armor creak and groan\nas it squeezes and constricts " \
                               "from every direction!"
        self.introduction = f"You have encountered a Leviathan; A large, serpentine and destructive creature " \
                            f"of ruination.\nCovered in armor-like scales and spikes, it coils up and " \
                            f"slithers toward you. Glowing yellow eyes, dripping\nfangs and stupendous horns endow " \
                            f"its crowned head as it looks down at your tiny, insignificant form.."
        self.poison_phrase = "It hisses, rises up and spits a vile venom!!"


class Gojira(Monster):

    def __init__(self):
        super().__init__()
        self.level = 10
        self.name = "Gojira"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 6000
        self.gold = random.randint(1, 3)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 21
        self.dexterity = 9
        self.constitution = 15
        self.intelligence = 16
        self.wisdom = 14
        self.charisma = 13
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 2
        self.can_poison = True
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 7)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Charm", "Vortex"]
        self.vulnerabilities = ["Scorch", "Fireball", "Firestorm", "Immolation"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 8
        self.hit_points = (random.randint(125, 135)) + self.constitution_modifier
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "It whips at you with a slithering tentacle.."
        self.attack_2 = 9
        self.attack_2_phrase = "It whips at you you with 2 tentacles.."
        self.attack_3 = 10
        self.attack_3_phrase = "It thrusts forward and bites with seemingly endless rows of ravenous teeth!"
        self.attack_4 = 14
        self.attack_4_phrase = "It strikes with whipping tentacles and bites with its horrendous teeth!"
        self.attack_5 = 25
        self.attack_5_phrase = "It whips at you with innumerable tentacles and holds you immobile as it bites " \
                               "ferociously!"
        self.introduction = f"You have encountered a Gojira; A looming, amphibious and hideous beast that roams " \
                            f"both land and sea.\nWith 8 lifeless and black eyes, and nerve sensor-pods covering its " \
                            f"slimy skin, it slithers toward you\nupon many tentacles, sensing every inch of you and " \
                            f"your movements before ever you saw it.\nYou hear and see its many rows of teeth " \
                            f"chomping in anticipation of its next meal.."
        self.poison_phrase = "It strikes with venomous tentacles!!"


class CorpseGrinder(Monster):

    def __init__(self):
        super().__init__()
        self.level = 11
        self.name = "Corpsegrinder"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
        self.experience_award = 7200
        self.gold = random.randint(15, 25)
        self.weapon_bonus = 7
        self.armor = 0
        self.shield = 0
        self.strength = 22
        self.dexterity = 18
        self.constitution = 21
        self.intelligence = 12
        self.wisdom = 12
        self.charisma = 13
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Charm"]
        self.vulnerabilities = []
        self.resistances = ["Firestorm", "Fireball", "Scorch", "Immolation", "Lightning"]
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 7
        self.hit_points = (random.randint(165, 175)) + self.constitution_modifier
        self.armor_class = 19
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 10  # attack bonus
        self.attack_1_phrase = "It swings an arcing Quantum Axe with great power and precision."
        self.attack_2 = 11
        self.attack_2_phrase = "It thrusts toward you with a heavy, trident spear."
        self.attack_3 = 12
        self.attack_3_phrase = "It strikes in combination; an electrified Quantum Axe in its right hand, followed by " \
                               "its Warhammer in the left!"
        self.attack_4 = 16
        self.attack_4_phrase = "It whips its Quantum chain, and the powerful arcflash rocks your internals with " \
                               "deadly concussive force!"
        self.attack_5 = 30
        self.attack_5_phrase = "It circles its Quantum chain menacingly as it suddenly shoots forth, with " \
                               "great speed and precision. You feel the heat and power of its arcflash!"
        self.introduction = f"You have encountered a Corpsegrinder; An other-dimensional, barbaric race of immense " \
                            f"size, strength and skill,\nsimilar to their cousins, the Bolt Throwers." \
                            f"Named for their pure savagery, and unlike Bolt Throwers,\n Corpsegrinders have very " \
                            f"little regard for any sort of hierarchical or social structure or code.\n" \
                            f"Mayhem, chaos and victory are their only pursuits.\n" \
                            f"With a thick, naturally camouflaged exoskeleton and standing some 8 feet tall,\n" \
                            f"an other-worldly helm, and a deadly arsenal of weapons including a sadistic, spiked " \
                            f"chain endowed\n" \
                            f"with electrified Quantum weirdness, it rushes toward you in an unpredictable, " \
                            f"serpentine pattern."
        self.paralyze_phrase = "It encircles you with its Quantum-electrified chain!"
        self.paralyze_free_attack_phrase = "In your helplessness, it slams, gores and cuts you with reckless " \
                                           "abandon. Drunk on violence,\nit jumps in the air, landing with a thud. " \
                                           "Steadying itself with hands on bent knees, it thrashes its head wildly!"


class BoltThrowerCaptain(Monster):

    def __init__(self):
        super().__init__()
        self.level = 11
        self.name = "Bolt Thrower Captain"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 7200
        self.gold = random.randint(15, 25)
        self.weapon_bonus = 7
        self.armor = 0
        self.shield = 0
        self.strength = 20
        self.dexterity = 17
        self.constitution = 19
        self.intelligence = 16
        self.wisdom = 16
        self.charisma = 16
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = False
        self.dot_multiplier = dice_roll(5, 8)
        self.dot_turns = dice_roll(3, 5)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Charm"]
        self.vulnerabilities = []
        self.resistances = ["Firestorm", "Fireball", "Scorch", "Immolation", "Lightning"]
        self.quantum_energy = False
        self.hit_dice = 12
        self.number_of_hd = 7
        self.hit_points = (random.randint(165, 175)) + self.constitution_modifier
        self.armor_class = 20
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "He swings an arcing Quantum Axe with great power and precision."
        self.attack_2 = 8
        self.attack_2_phrase = "He strikes at you with his heavy, electrified Warhammer."
        self.attack_3 = 10
        self.attack_3_phrase = "He strikes in combination; an electrified Quantum Axe in his left hand, followed by " \
                               "his Warhammer!"
        self.attack_4 = 16
        self.attack_4_phrase = "He cracks his Quantum Whip, and the powerful arcflash surges through your very " \
                               "bones, knocking you off your feet!"
        self.attack_5 = 33
        self.attack_5_phrase = "He circles his Quantum Whip menacingly as it suddenly shoots forth, with " \
                               "great speed and precision. You feel the heat and power of the arcflash\n" \
                               "deep within!"
        self.introduction = f"You have encountered a Bolt Thrower Captain; An intelligent, competent and disciplined " \
                            f"warrior race holding to a strict code of rank, strength and skill.\nHis stoic, " \
                            f"unaffected eyes stare at your from within a glorious helm of remarkable craftsmanship. "
        self.paralyze_phrase = "He encircles you with his whip!"
        self.paralyze_free_attack_phrase = "In your helplessness, he strikes skillfully with his arcing weaponry!"


class Apocryphage(Monster):

    def __init__(self):
        super().__init__()
        self.level = 11
        self.name = "Apocryphage"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.a_an = "an"
        self.experience_award = 7000
        self.gold = random.randint(10, 30)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 8
        self.dexterity = 20
        self.constitution = 8
        self.intelligence = 15
        self.wisdom = 20
        self.charisma = 20
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = False
        self.necrotic = True
        self.dot_multiplier = dice_roll(18, 22)
        self.dot_turns = dice_roll(5, 7)
        self.undead = False
        self.immunities = ["Sleep", "Web", "Hold Monster", "Charm"]
        self.vulnerabilities = ["Fear"]
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 10
        self.number_of_hd = 4
        self.hit_points = 81
        self.armor_class = 18
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 8  # attack bonus
        self.attack_1_phrase = "He swings his nasty dagger wildly.."
        self.attack_2 = 10
        self.attack_2_phrase = "He swings his nasty dagger with unexpected speed.."
        self.attack_3 = 10
        self.attack_3_phrase = "Jumping forward, he cuts you with his nasty knife.."
        self.attack_4 = 12
        self.attack_4_phrase = "With lightning speed, he lurches forward and cuts at you with a howl!"
        self.attack_5 = 14
        self.attack_5_phrase = "He leaps forward, unleashing a scream and a flurry of blows from his blade!!"
        self.introduction = f"You have encountered an Apocryphage; A human student of foul arts and forbidden " \
                            f"scrolls.\nTall, awkward, sallow, and with ill-fitting black clothes and a rumpled " \
                            f"hat, he grasps a Fallen Blade\ntightly and rolls up his sleeves. His emaciated flesh " \
                            f"tells of a sedentary existence of study, to the\nexclusion of all else."
        self.necrotic_phrase = f"Grabbing his deadly Fallen Blade from his belt and chuckling softly, he swiftly" \
                               f" stabs at you with a long, skinny arm.."


class MorbidAssassin(Monster):

    def __init__(self):
        super().__init__()
        self.level = 11
        self.name = "Morbid Assassin"
        self.proper_name = "None"
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
        self.experience_award = 7000
        self.gold = random.randint(35, 45)
        self.weapon_bonus = 6
        self.armor = 0
        self.shield = 0
        self.strength = 14
        self.dexterity = 18
        self.constitution = 16
        self.intelligence = 14
        self.wisdom = 18
        self.charisma = 8
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = False
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = True
        self.dot_multiplier = dice_roll(16, 20)
        self.dot_turns = dice_roll(3, 5)
        self.undead = True
        self.immunities = ["Web", "Hold Monster"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = False
        self.hit_dice = 6
        self.number_of_hd = 8
        self.hit_points = (random.randint(85, 95)) + self.constitution_modifier
        self.armor_class = 21  # super high armor, hard to hit, low damage, low hitpoints
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 14  # attack bonus
        self.attack_1_phrase = "His dark, shadowy form swings with a blade from the shadows.."
        self.attack_2 = 14
        self.attack_2_phrase = "With perfect, quiet precision, he swings from the darkness.."
        self.attack_3 = 15
        self.attack_3_phrase = "Blinking out of existence for an instant, he appears in your blind spot, " \
                               "and cuts deeply with his long, nasty dagger.."
        self.attack_4 = 18
        self.attack_4_phrase = "He cuts you with his gleaming blade and retreats into the shadows.."
        self.attack_5 = 30
        self.attack_5_phrase = "With a whispering swing, his blade finds your soft flesh and cuts deep.."
        self.introduction = f"You have encountered a Morbid Assassin; An amoral killer for hire in life, and now " \
                            f"undead through the weirdness\nof a Master Manipulator's evil will. The light simply " \
                            f"falls into him. His movements resemble nothing more than black, humanoid smoke.\n" \
                            f"He approaches you in pure silence and stands still long enough for you to see his true " \
                            f"form- dark garb,\ncriss-crossed leather belts full of knives and vials, black boots, " \
                            f"skegg beard, and an aristocratic smugness that has followed him beyond natural life."
        self.poison_phrase = "Suddenly appearing behind you, he stabs at you with a poison blade!!"
        self.necrotic_phrase = f"He retrieves a black, shimmering blade with a green, glowing edge from his belt and " \
                               f"attacks.."


class WickedQueenJannbrielle(Monster):

    def __init__(self):
        super().__init__()
        self.level = 20
        self.name = "Wicked Queen"
        self.proper_name = "Queen Jannbrielle the Wicked"
        self.he_she_it = "she"
        self.his_her_its = "her"
        self.him_her_it = "her"
        self.experience_award = 64000
        self.gold = random.randint(150, 2500)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 30
        self.dexterity = 17
        self.constitution = 29
        self.intelligence = 20
        self.wisdom = 20
        self.charisma = 30
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # Rounded up
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.can_paralyze = True
        self.paralyze_turns = 2
        self.can_poison = True
        self.necrotic = True
        self.dot_multiplier = dice_roll(6, 8)
        self.dot_turns = 5
        self.undead = True
        self.immunities = ["All"]
        self.vulnerabilities = []
        self.resistances = []
        self.quantum_energy = True
        self.hit_dice = 10
        self.number_of_hd = 3
        self.hit_points = 1750  # dice_roll(35, 20) + 30
        self.armor_class = 22
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 12  # attack bonus
        self.attack_1_phrase = "She strikes with her foul skull-scepter!"
        self.attack_2 = 15
        self.attack_2_phrase = "With a gleeful laugh, she attacks with her whip!"
        self.attack_3 = 16
        self.attack_3_phrase = "With catlike elegance and agility, she strikes with a nasty dagger!"
        self.attack_4 = 18
        self.attack_4_phrase = "Producing a long, black blade, she strikes with a frenzied rage!"
        self.attack_5 = 20
        self.attack_5_phrase = "The queen leaps into the air and releases a crippling scream of fell hatred and malice!"
        self.quantum_attack_1 = 25
        self.quantum_attack_1_phrase = "The queen smiles, licks her lips with a forked tongue and attacks with a\n" \
                                       "wall of quantum energy that forms an army of attacking Necrophagists!"
        self.quantum_attack_2 = 25
        self.quantum_attack_2_phrase = "The queen unleashes a storm of dark, dancing liquid quantum energy\n" \
                                       "from both of her outstretched hands that morphs into an attacking\n" \
                                       "Morbid Behemoth!"
        self.quantum_attack_3 = 25
        self.quantum_attack_3_phrase = "Placing both hands together, she releases a black torrent of\n" \
                                       "Quantum energy that splits open the ground, from which crawls out\n" \
                                       "an ethereal army of attacking Morbid Knights!"
        self.quantum_attack_4 = 25
        self.quantum_attack_4_phrase = "From beautiful hands that elongate into claws, she attacks with evil " \
                                       "Quantum Forces\n" \
                                       "that form a dark mist of terror that invades your mind!"
        self.quantum_attack_5 = 45
        self.quantum_attack_5_phrase = "The queen releases Quantum Forces which wildly entangle\n" \
                                       "you in a maelstrom of malice which crushes with impossible gravity!"
        self.introduction = f"\'I am your doom. Your life beckons to be taken!\', says the undead queen, with a hiss!"
        self.poison_phrase = f"The queen attacks with her venomous fangs!"
        self.paralyze_phrase = f"The irresistible beauty of the undead queen begins to weaken you.."
        self.paralyze_free_attack_phrase = "Up close and personal, the wicked queen looks deeply into your eyes " \
                                           "as she slowly and sadistically gores you with her terrible claws!"
        self.necrotic_phrase = "She places her forefingers to her head briefly, and then, with closed eyes, " \
                               "exhales a cool,\nwhite mist that begins to encircle you\n..you feel a shivering cold " \
                               "overcoming you.."


# monster dictionaries. keys correspond to difficulty/challenge level
# regular monsters:
monster_dict = {
    1: [Quasit, Kobold, Cultist, Goblin, WingedKobold],
    2: [Skeleton, Gnoll, Shadow, Drow, Troglodyte, Orc, Zombie, Ghoul],
    3: [Specter, Bugbear, CultFanatic, HalfOgre, Gargoyle, Doppelganger],
    4: [WhiteDragonWyrmling, GreenDragonWyrmling, HobgoblinCaptain, Harpy, BugbearCaptain],
    5: [Ogre, ZombieOgre, DarkDwarf, Minotaur, Mummy],
    6: [Troll, HillGiant, Cyclops, WrathfulAvenger, HobgoblinWarlord],
    7: [Wyvern, DrowManipulator, MorbidDefender, MindFlayer, BoltThrower],
    8: [FrostGiant, YoungBlackDragon, YoungGreenDragon, MorbidKnight, Assassin],
    9: [FireGiant, Widow, YoungBlueDragon, Wraith, Necrophagist],
    10: [YoungRedDragon, MorbidBehemoth, ChaosMonster, Leviathan, Gojira],
    11: [CorpseGrinder, BoltThrowerCaptain, Apocryphage, MorbidAssassin]
}

# undead monsters:
undead_monster_dict = {
    1: [Skeleton],
    2: [Shadow, Zombie, Ghoul],
    3: [Specter],
    5: [ZombieOgre]
}
# boss lists
undead_prophet_list = [ZombieProphet(), SkeletalProphet()]
king_boss_list = [SkeletonKing(), ShadowKing(), SpecterKing()]
