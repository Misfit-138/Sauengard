# Sauengard © Copyright 2022 by Jules Pitsker
# GPLV3 LICENSE https://www.gnu.org/licenses/gpl-3.0.en.html

# Dark Sorrowful Cello "Soul's Departure" Royalty Free Music by Darren Curtis
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Blacksmith theme: 'Viking Intro loop' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Dungeon theme: 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Chemist Theme: 'Might and Magic' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Town theme: 'Tavern Loop 1' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Boss battle theme: 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# Tavern Theme: 'The Medieval Banquet' by Silverman Sound is under a Creative Commons license (CC BY 3.0)
# Music promoted by BreakingCopyright: http://bit.ly/Silvermansound_Medieval

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
    for dice in range(no_of_dice):  # (1 hit die per level according to DnD 5E rules)
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
        self.name = ""
        self.proper_name = ""
        self.he_she_it = ""
        self.his_her_its = ""
        self.him_her_it = ""
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
        self.is_discovered = False

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
        print(f"The {self.name} attacks you! (It rolls {roll_d20})")
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
        print(f"{self.name} Attack bonus: {attack_bonus}")
        print(f"{self.name} Dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # test out pro bonus
        print(f"{self.name} Total: {monster_total}")
        print(f"Your armor class: {player_1.armor_class}")

        if monster_total >= player_1.armor_class:
            damage_roll = dice_roll((self.number_of_hd * critical_bonus), self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)

            if roll_d20 == 20 and damage_to_opponent < 1:
                damage_to_opponent = 1  # a natural 20 must always hit - 5e rules

            if damage_to_opponent > 0:  # # at this point the player is the opponent!
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
            sleep(2)
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
        player_1.hud()
        print(self.paralyze_phrase)
        sleep(1.25)
        paralyze_chance = dice_roll(1, 20)
        human_player_roll_d20 = dice_roll(1, 20)
        player_total = (human_player_roll_d20 + player_1.ring_of_prot.protect + player_1.temp_protection_effect)
        print(f"Paralyze roll: {paralyze_chance} + monster wisdom modifier: {self.wisdom_modifier}")  # rm after testing
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
            # print("As you stand, frozen and defenseless, it savagely gores you!")
            sleep(1)

            for i in range(self.paralyze_turns):  # this seems too brutal if paralyze turns is anything but 1!!!
                paralyze_damage = (dice_roll(self.number_of_hd, self.hit_dice) -
                                   (player_1.ring_of_prot.protect + player_1.temp_protection_effect))
                if paralyze_damage < 1:
                    paralyze_damage = self.level
                player_1.reduce_health(paralyze_damage)
                print(f"{self.he_she_it.capitalize()} strikes at you for {paralyze_damage} points of damage!!")
                pause()
                player_1.hud()
            return True

        else:
            print(f"You ignore {self.his_her_its} wiles and break free from {self.his_her_its} grip!")
            return False

    def poison_attack(self, player_1):
        player_saving_throw = dice_roll(1, 20)
        difficulty_class = (player_saving_throw + player_1.constitution_modifier)
        # (player_1.constitution + player_1.constitution_modifier)
        roll_d20 = dice_roll(1, 20)  # attack roll
        # print(f"The {self.name} hisses in evil glee..")
        print(self.poison_phrase)
        print(f"Attack roll: {roll_d20}")
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

            if roll_d20 == 20 or roll_d20 >= difficulty_class:  # self.constitution + self.constitution_modifier:
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
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {self.name} attempts to harness its innate understanding of quantum necrosis..")
        print(f"Attack roll---> {roll_d20}")
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

            if roll_d20 == 20 or roll_d20 >= difficulty_class:
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
        print(f"{self.name} Attack bonus: {attack_bonus}")
        print(f"{self.name} Dexterity modifier {self.dexterity_modifier}")  # MONSTER DEX MODIFIER
        print(f"{self.name} Proficiency Bonus: {self.proficiency_bonus}")  # test out pro bonus
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
            sleep(2)
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
        self.is_discovered = False

    # name = "Quasit"


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
        self.is_discovered = False

    # name = "Kobold"


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
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "With unexpected speed, he strikes with its dagger.."
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
        self.is_discovered = False

    # name = "Cultist"


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
        self.is_discovered = False

    # name = "Goblin"


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
        self.is_discovered = False

    # "Winged Kobold"


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
        self.is_discovered = False

    # name = "Shadow"


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
                            f"in hand, it fearlessly hammers its shield with sword, taunting an attack. " \
                            f"A full-toothed\n" \
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
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.lesser_multi_attack = False
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "He strikes at you with unnerving strength and speed..."
        self.attack_2 = 1
        self.attack_2_phrase = "He strikes at you with arms flailing..."
        self.attack_3 = 2
        self.attack_3_phrase = "He darts forward with reckless abandon.."
        self.attack_4 = 2
        self.attack_4_phrase = "He thrusts forward with its heavy, iron sceptre!"
        self.attack_5 = 3
        self.attack_5_phrase = "He strikes wildly with its iron sceptre!!"
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
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.attack_5_phrase = f"Reaching over its back, it produces a battle axe and strikes wildly!!"
        self.introduction = f"The ancient king rises in skeletal form. The once gleaming armor and weaponry now\n" \
                            f"clings wearily to his bony form as he raises sword and shield, taunting you to " \
                            f"attack!\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False


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
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.is_discovered = False


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
        self.is_discovered = False


class Troglodyte(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Troglodyte"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.is_discovered = False

    # "Troglodyte"


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.name = "Orc"
        self.proper_name = "None"
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.is_discovered = False

    # name = "Orc"


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
        self.he_she_it = "it"
        self.his_her_its = "its"
        self.him_her_it = "it"
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
        self.is_discovered = False


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
        self.is_discovered = False


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
        self.he_she_it = "he"
        self.his_her_its = "his"
        self.him_her_it = "him"
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
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
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
        self.lesser_multi_attack = False
        self.attack_1 = 1  # attack bonus
        self.attack_1_phrase = "He thrusts mightily forward with its javelin!.."
        self.attack_2 = 2
        self.attack_2_phrase = "He swings its greatsword with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "He swings its greatsword with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "He roars and swings its greatsword with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "He raises its greatsword overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Hobgoblin Captain. Fierce, intelligent and disciplined, " \
                            f"his heavy armor and\nweaponry are polished and well-maintained. His yellow " \
                            f"teeth stretch into a surly grin behind its great helm.\nNarrowing his eyes, " \
                            f"he approaches and stands before you unaffected and unafraid; ready for battle."
        self.is_discovered = False


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
        self.lesser_multi_attack = False
        self.attack_1 = 2  # attack bonus
        self.attack_1_phrase = "It thrusts forward with gaping jaws.."
        self.attack_2 = 3
        self.attack_2_phrase = "With a languid growl, it strikes with its jaws.. "
        self.attack_3 = 4
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
        self.is_discovered = False


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
        self.lesser_multi_attack = False
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


class WickedQueenJannbrielle(Monster):

    def __init__(self):
        super().__init__()
        self.level = 20
        self.name = "Wicked Queen"
        self.proper_name = "Queen Jannbrielle"
        self.he_she_it = "she"
        self.his_her_its = "her"
        self.him_her_it = "her"
        self.experience_award = 64000
        self.gold = random.randint(150, 2500)
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = 30
        self.dexterity = 10
        self.constitution = 29
        self.intelligence = 18
        self.wisdom = 18
        self.charisma = 25
        self.can_paralyze = True
        self.paralyze_turns = 1
        self.can_poison = True
        self.necrotic = True
        self.dot_multiplier = 5
        self.dot_turns = 5
        self.undead = True
        self.immunities = ["Turn Undead"]
        self.vulnerabilities = ["Immolation", "Fireball", "Fire Storm"]
        self.resistances = []
        self.quantum_energy = True
        self.difficulty_class = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 20
        self.hit_dice = 10
        self.number_of_hd = 2
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.hit_points = 1200  # dice_roll(35, 20) + 30
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.armor_class = 20
        self.multi_attack = True
        self.lesser_multi_attack = False
        self.attack_1 = 7  # attack bonus
        self.attack_1_phrase = "The queen attacks with her skull-scepter!"
        self.attack_2 = 10
        self.attack_2_phrase = "With a gleeful laugh, she attacks with her whip!"
        self.attack_3 = 12
        self.attack_3_phrase = "With catlike agility, she strikes with her beautiful, horrible claws!"
        self.attack_4 = 14
        self.attack_4_phrase = "Producing a long, black blade, she strikes with a frenzied rage!"
        self.attack_5 = 18
        self.attack_5_phrase = "The queen leaps into the air and releases a crippling scream of fell hatred and malice!"
        self.quantum_attack_1 = 10
        self.quantum_attack_1_phrase = "The queen smiles, licks her lips with a forked tongue and attacks with a\n" \
                                       "wall of quantum energy!"
        self.quantum_attack_2 = 12
        self.quantum_attack_2_phrase = "The queen unleashes a storm of dark, dancing liquid quantum energy\n" \
                                       "from both of her outstretched hands!"
        self.quantum_attack_3 = 14
        self.quantum_attack_3_phrase = "Placing both hands together, she releases a black torrent of\n" \
                                       "quantum energy!"
        self.quantum_attack_4 = 16
        self.quantum_attack_4_phrase = "From beautiful claw-like hands, she attacks with evil Quantum Forces\n" \
                                       "that form a dark mist of terror!"
        self.quantum_attack_5 = 20
        self.quantum_attack_5_phrase = "The queen releases Quantum Forces which wildly entangle\n" \
                                       "you in a maelstrom of malice!"
        self.introduction = f"\'I shall enjoy watching you die.\', says the undead queen, plainly."
        self.is_discovered = False
        self.poison_phrase = f"The queen attacks with venomous fangs!"
        self.paralyze_phrase = f"The irresistible beauty of the undead queen begins to weaken you.."


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

"""    def initiative(self):
        if self.level > 6:  # testing
            monster_initiative = dice_roll(1, 20) + self.dexterity_modifier + self.proficiency_bonus
        else:
            monster_initiative = dice_roll(1, 20) + self.dexterity_modifier
        return monster_initiative"""