# Sauengard © Copyright 2022 by Jules Pitsker
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.

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

# Pit theme 'Epic 39' by Jules Pitsker
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

import collections
import math
import pickle
import random
import time
import os
import sys
from collections import Counter
from dungeons import dungeon_dict
from monster_module import monster_dict, king_boss_list, undead_prophet_list, WickedQueenJannbrielle
from pathlib import Path
import keyboard
if os.name == 'nt':
    import winsound

# if you call a function and expect to use a return value, like, by printing it, you must first assign a variable in
# the call itself!!!
# when passing a list as an argument, remember to use the * unpacking operator
# seq = [1, 2, 3]
# foo(*seq)

'''DIFFICULTY CLASSES (HIPSTER’S REMIX)
Task Difficulty	DC
Very Easy	5
Easy	8
Medium	10
Tricky	12
Hard	15
Very hard	20
Incredibly hard	25
Why bother?	30'''


def check_for_escape():
    if keyboard.is_pressed('Esc'):
        quit_game()


def quit_game():
    cls()
    typewriter("Quit game..")

    if are_you_sure():
        sys.exit()

    else:
        return


def are_you_sure():
    while True:
        confirm = input("Are you sure? (y/n) ").lower()

        if confirm == 'y':
            return True
        else:
            return False


def typewriter(message):
    # based this snippet on a snippet from 101computing.net:
    print()
    for each_char in message:
        sleep(0.0065)  # 0.01 seems very good
        sys.stdout.write(each_char)
        sys.stdout.flush()

        # I am proud of this little snippet I figured out :)
        if keyboard.is_pressed('Esc'):
            # print("\n\n*SKIP*")
            # if are_you_sure():
            cls()
            print()
            print(message)
            return

    sleep(.1)
    return


def print_txt_file(txt_file_name):
    cls()
    try:
        p = Path(__file__).with_name(txt_file_name)
        with p.open('r') as txt:
            if txt.readable():
                print(txt.read())

    except FileNotFoundError:
        print(f"Missing {txt_file_name} or bad file path.")


def typewriter_txt_file(txt_file_name):
    cls()
    try:
        p = Path(__file__).with_name(txt_file_name)
        with p.open('r') as message:
            if message.readable():
                typewriter(message.read())

    except FileNotFoundError:
        print(f"Missing {txt_file_name} or bad file path.")


def game_splash():
    while True:
        cls()
        print_txt_file('splash_art.txt')
        print("                               "
              "W  E  L  C  O  M  E    T  O    S  A  U  E  N  G  A  R  D.\n")
        print(f"                                         "
              f"© Copyright 2022 by Jules Pitsker")
        choice = input(f"                     "
                       f"(I)ntroduction  (A)bout  (T)ips  (C)redits and Acknowledgement  (L)icense  (B)egin ").lower()

        if choice == 'i':
            typewriter_txt_file('introduction.txt')
            pause()

        elif choice == 'a':
            typewriter_txt_file('about.txt')
            pause()

        elif choice == 't':
            typewriter_txt_file('tips.txt')
            pause()

        elif choice == 'c':
            print_txt_file('credits.txt')
            pause()

        elif choice == 'l':
            print_txt_file('LICENSE.txt')
            pause()

        elif choice == 'b':
            return


rndm_aroma_lst = ['agarwood', 'angelica root', 'anise', 'basil', 'bergamot', 'calamodin', 'calamus', 'camphor',
                  'cardamom', 'cedar', 'camomile', 'cinnamon', 'citron', 'clary sage', 'clove', 'davana', 'eucalyptus',
                  'frankincense', 'galbanum', 'hemlock', 'jasmine', 'lavender', 'lemongrass', 'mugwort oil',
                  'pennyroyal', 'peppermint', 'sage', 'sandalwood', 'sassafras', 'garden mint', 'spikenard',
                  'spruce oil', 'star anise oil', 'tea tree oil', 'tarragon oil', 'tsuga oil', 'valerian',
                  'vanilla sweet grass', 'warionia', 'vetiver', 'wintergreen', 'yarrow oil']


def convert_list_to_string(list1):
    # no brackets, no quotes, no commas
    return str(list1).replace('[', '').replace(']', '').replace("'", "").replace(",", "")


def convert_list_to_string_with_commas_only(list1):
    # no brackets, no quotes. WITH commas
    return str(list1).replace('[', '').replace(']', '').replace("'", "")


def convert_list_to_string_with_and(list1):
    # no brackets, no quotes. WITH commas. add "and" before last element to be more naturally readable
    list1.insert(-1, 'and')
    readable_list = str(', '.join(list1[:-2]) + ' ' + ' '.join(list1[-2:]))
    return readable_list


def compare():
    lambda x, y: collections.Counter(x) == collections.Counter(y)


def pause():
    if os.name == 'nt':
        os.system('pause')
    else:
        input("Press [ENTER] to continue . . . ")
    return


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return


def sleep(seconds):
    time.sleep(seconds)
    return


def dice_roll(no_of_dice, no_of_sides):
    dice_rolls = []  # create list for multiple die rolls
    for dice in range(no_of_dice):
        dice_rolls.append(random.randint(1, no_of_sides))
    your_roll_sum = sum(dice_rolls)
    return your_roll_sum


def dungeon_command_choices():
    command = input("(L)ook at surroundings, use (MAP), (C)larifying elixir,\n"
                    "(Quit), Town (P)ortal, (H)ealing potion, (M)anage inventory,\n"
                    "(G)iant strength potion, (V)ial of Antidote, (I)nventory,\n"
                    "(Q)uantum effects, or W-A-S-D to navigate. --> ").lower()
    return command


def character_generator():
    cls()
    explanation_dict = {"Strength": "Strength is a measure of a character's physical power. A character high\n"
                                    "in Strength can lift heavier loads, break objects with brute force, and\n"
                                    "do more damage with melee weapons.",
                        "Dexterity": "Dexterity is a measure of a character’s nimbleness, agility, muscular "
                                     "coordination, and balance.\nIt is also an essential component of your Armor "
                                     "Class; Your Dexterity Modifier is added directly to your AC.",
                        "Constitution": "Constitution encompasses the character's physique, toughness, health and\n"
                                        "resistance to poison and necrosis. The higher a character's constitution,\n"
                                        "the more hit points the character will have.",
                        "Intelligence": "Intelligence determines how well your character learns and reasons. It is\n"
                                        "important for certain quantum effects, your ability to recall lore, \n"
                                        "languages, and runes, as well as your ability to investigate your \n"
                                        "surroundings.",
                        "Wisdom": "Wisdom enables sound judgment and action based on intelligence and understanding; "
                                  "the ability\n"
                                  "to practically apply one's knowledge successfully, to solve problems, avoid or "
                                  "avert\n"
                                  "dangers, attain certain goals, or counsel others in doing so. It is the opposite\n"
                                  "of foolishness, stupidity, and madness. Wisdom is absolutely critical for "
                                  "harnessing\n"
                                  "many Quantum effects, as well as avoiding many Quantum attacks.",
                        "Charisma": "Charisma measures one's ability to interact effectively with others. It includes\n"
                                    "such factors as confidence, persuasion and eloquence, and it can represent a\n"
                                    "charming or commanding personality. *Players with high charisma will also have a\n"
                                    "better chance of favorable outcomes when encountering certain monsters.*"}
    standard_array = f"Ability Score    	Ability Modifier\n" \
                     f"15	                            +3\n14	                            " \
                     f"+2\n13	                            +1\n12	                            +1\n10" \
                     f"	                            +0\n8	                            -1\n"

    stats = {
        "strength": 15,
        "dexterity": 14,
        "constitution": 13,
        "intelligence": 10,
        "wisdom": 12,
        "charisma": 8,
    }

    while True:
        cls()
        player_name = input(f"Please enter character name: ")
        if len(player_name) < 3:
            print(f"Minimum 3 characters!")
            sleep(.25)
            continue
        confirm_player_name = input(f"Player name is {player_name}. Is this ok? (y/n) ").lower()
        if confirm_player_name == 'y':
            break
        else:
            continue

    cls()
    # print(f"{player_name}:")
    print(f"Standard ability scores (Recommended if unsure)")
    for key, value in stats.items():
        print(key.capitalize(), ":", value)
    default_choice = input(f"[ENTER] to use the above default ability scores or (C)ustomize? ([ENTER]/C): ").lower()
    if default_choice != 'c':
        player_1 = Player(name=player_name, **stats)
        # pause()
        return player_1
    cls()
    print(f"Customization involves assigning scores from The Standard Array.\n"
          f"The Standard Array is a set pool of six numbers: 15, 14, 13, 12, 10, 8\n"
          f"Each number will be matched with one of the six character abilities.\n"
          f"Note that each ability score has a corresponding ability modifier, which\n"
          f"acts as a bonus, (or, as a penalty, in the case of a negative modifier),\n"
          f"and will become more important as you progress.\n"
          f"Abilities and ability modifiers increase as you level up.\n")
    print(standard_array)
    pause()
    score_list = [15, 14, 13, 12, 10, 8]
    while len(score_list):
        for key in stats:
            cls()
            print(standard_array)
            human_key = key.capitalize()
            print(f"{human_key}:")
            print(explanation_dict[human_key])
            scores = convert_list_to_string_with_commas_only(score_list)
            print(f"Available scores: {scores}")
            try:
                score = int(input(f"Enter score to assign to {human_key} (or hit [ENTER] to start over): "))
                if score in score_list:
                    print(f"{key} = {score}")
                    sleep(.5)
                    stats[key] = score
                    score_list.remove(score)

                else:
                    score_list = [15, 14, 13, 12, 10, 8]  # re-set list
                    print(f"Valid scores are listed above.")
                    sleep(0.5)
                    print(f"Starting over.")
                    sleep(0.5)
                    break
            except ValueError:
                print(f"Invalid entry..")
                score_list = [15, 14, 13, 12, 10, 8]  # re-set list
                sleep(0.5)
                print(f"Starting over.")
                sleep(0.5)
                break
    # for key, value in stats.items():
    # print(key, ":", value)
    player_1 = Player(name=player_name, **stats)  # **stats sends the 'stats' dictionary as parameters
    # pause()
    return player_1


def asi_intro():
    cls()
    print(f"                                  *Ability Score Improvement*")
    print()
    print(
        f"You may choose to improve a single ability score, such as strength, and increase it by 2 points.\n"
        f"\n"
        f"                           *OR*\n"
        f"\n"
        f"You may choose to improve two ability scores, such as charisma and constitution, by 1 point each.\n"
        f"\n"
        f"NOTES: \n"
        f"* Ability *modifiers* improve with each ascending even-numbered score, therefore, if unsure,\n"
        f"  it is generally recommended to apply 1 point to odd-numbered ability scores and apply \n"
        f"2 points to even-numbered scores.\n"
        f"* When your Constitution modifier increases by 1, your hit point maximum increases by 1 for each\n"
        f"  level you have attained.\n"
        f"                         *The maximum score for any ability is 20*"
        f"\n")
    pause()


def sound_player(sound_file):
    # a sound player function which simply plays sound_file asynchronously
    if os.name == 'nt':
        try:
            p = Path(__file__).with_name(sound_file)
            with p.open('rb') as sound:
                if sound.readable():
                    winsound.PlaySound(str(p), winsound.SND_FILENAME | winsound.SND_ASYNC)
        except FileNotFoundError:
            print(f"{sound_file} not found in directory path.")
            pause()
            # pass


def sound_player_loop(sound_file):
    # a sound player function which plays sound_file asynchronously on a continuous loop
    if os.name == 'nt':
        try:
            p = Path(__file__).with_name(sound_file)
            with p.open('rb') as sound:
                if sound.readable():
                    winsound.PlaySound(str(p), winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        except FileNotFoundError:
            print(f"{sound_file} not found in directory path.")
            pause()
            # pass


def gong():
    # notice the gong is not looped
    sound_player('gong.wav')


def sad_cello_theme():
    sound_player_loop('sad_cello_darren_curtis.wav')


def blacksmith_theme():
    sound_player_loop('blacksmith_theme_2.wav')


def chemist_theme():
    sound_player_loop('chemist_theme.wav')


def mountain_king_theme():
    sound_player_loop('mountain_king.wav')


def pit_theme():
    sound_player_loop('creepy_dungeon_theme_loop.wav')


def boss_battle_theme():
    sound_player_loop('boss_battle_2.wav')


def town_theme():
    sound_player_loop('town_(tavern)_loop_by_alexander_nakarada.wav')


def tavern_theme():
    sound_player_loop('silvermansound_the medieval_banquet.wav')


class Weapon:

    def __init__(self):
        self.name = ""
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f"{self.name} - Damage Bonus: {self.damage_bonus}  To-hit bonus: {self.to_hit_bonus}  " \
               f"Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP"


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 10
        self.minimum_level = 1
        self.a_an = "a"


short_sword = ShortSword()


class BroadSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Broad Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = 1
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 1
        self.a_an = "a"


broad_sword = BroadSword()


class GreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Great Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 3
        self.to_hit_bonus = 1
        self.sell_price = 15
        self.buy_price = 500
        self.minimum_level = 4
        self.a_an = "a"


great_sword = GreatSword()


class ElvishGreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Elvish Great Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 10
        self.to_hit_bonus = 3
        self.sell_price = 2500
        self.buy_price = 5000
        self.minimum_level = 8
        self.a_an = "an"


elvish_great_sword = ElvishGreatSword()


class QuantumSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 12  # 5
        self.to_hit_bonus = 4
        self.sell_price = 5000
        self.buy_price = 8000
        self.minimum_level = 10  # 3
        self.a_an = "a"


quantum_sword = QuantumSword()


class QuantumAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 15  # 5
        self.to_hit_bonus = 4
        self.sell_price = 5000
        self.buy_price = 8000
        self.minimum_level = 10  # 3
        self.a_an = "a"


quantum_axe = QuantumAxe()


class ShortAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = -1
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1
        self.a_an = "a"


short_axe = ShortAxe()


class BattleAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Battle Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 3
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 2
        self.a_an = "a"


battle_axe = BattleAxe()


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Great Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 4
        self.to_hit_bonus = 0
        self.sell_price = 15
        self.buy_price = 500
        self.minimum_level = 4
        self.a_an = "a"


great_axe = GreatAxe()


class ElvishGreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Elvish Great Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 12
        self.to_hit_bonus = 2
        self.sell_price = 2750
        self.buy_price = 6000
        self.minimum_level = 8
        self.a_an = "an"


elvish_great_axe = ElvishGreatAxe()


class Armor:

    def __init__(self):
        self.name = ""
        self.item_type = "Armor"
        self.armor_bonus = 0
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a set of"

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - AC: {self.ac}  Armor bonus: {self.armor_bonus}  ' \
               f'Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class PaddedArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Padded Armor"
        self.item_type = "Armor"
        self.ac = 10
        self.armor_bonus = 0
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1
        self.a_an = "a set of"


padded_armor = PaddedArmor()


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Leather Armor"
        self.item_type = "Armor"
        self.ac = 11
        self.armor_bonus = 0
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 1
        self.a_an = "a set of"


leather_armor = LeatherArmor()


class StuddedLeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Studded Leather Armor"
        self.item_type = "Armor"
        self.ac = 12
        self.armor_bonus = 0
        self.sell_price = 30
        self.buy_price = 45
        self.minimum_level = 2
        self.a_an = "a set of"


studded_leather_armor = StuddedLeatherArmor()


class ScaleMail(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Scale Mail"
        self.item_type = "Armor"
        self.ac = 14
        self.armor_bonus = 0
        self.sell_price = 300
        self.buy_price = 500
        self.minimum_level = 7
        self.a_an = "a set of"


scale_mail = ScaleMail()


class HalfPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Half Plate Armor"
        self.item_type = "Armor"
        self.ac = 16
        self.armor_bonus = 0
        self.sell_price = 550
        self.buy_price = 750
        self.minimum_level = 8
        self.a_an = "a set of"


half_plate = HalfPlate()


class FullPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Full Plate Armor"
        self.item_type = "Armor"
        self.ac = 18
        self.armor_bonus = 0
        self.sell_price = 1000
        self.buy_price = 1500
        self.minimum_level = 10
        self.a_an = "a set of"


full_plate = FullPlate()


class Shield:

    def __init__(self):
        self.name = ""
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = ""

    def __repr__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class NoShield(Shield):  # default
    def __init__(self):
        super().__init__()
        self.name = "No Shield"
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = ""


no_shield = NoShield()


class Buckler(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Buckler"
        self.item_type = "Shields"
        self.ac = 1
        self.sell_price = 5
        self.buy_price = 50
        self.minimum_level = 1  # 2
        self.a_an = "a"


buckler = Buckler()


class KiteShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Kite Shield"
        self.item_type = "Shields"
        self.ac = 2
        self.sell_price = 50
        self.buy_price = 100
        self.minimum_level = 5
        self.a_an = "a"


kite_shield = KiteShield()


class QuantumTowerShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Tower Shield"
        self.item_type = "Shields"
        self.ac = 3
        self.sell_price = 375
        self.buy_price = 700
        self.minimum_level = 7
        self.a_an = "a"


quantum_tower_shield = QuantumTowerShield()


class Boots:

    def __init__(self):
        self.name = ""
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a pair of"

    def __repr__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class LeatherBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Leather Boots"
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 1
        self.buy_price = 1
        self.minimum_level = 1
        self.a_an = "a pair of"


leather_boots = LeatherBoots()


class ElvenBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Elven Boots"
        self.item_type = "Boots"
        self.ac = 1
        self.sell_price = 30
        self.buy_price = 50
        self.minimum_level = 1
        self.a_an = "a pair of"


elven_boots = ElvenBoots()


class AncestralFootsteps(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Ancestral Footsteps"
        self.item_type = "Boots"
        self.ac = 2
        self.sell_price = 300
        self.buy_price = 500
        self.minimum_level = 5
        self.a_an = "a pair of"


ancestral_footsteps = AncestralFootsteps()


class Cloak:

    def __init__(self):
        self.name = ""
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Stealth: {self.stealth}  Minimum level: {self.minimum_level}  ' \
               f'Purchase Price: {self.buy_price} GP'


class CanvasCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Canvas Cloak"
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 1
        self.buy_price = 0
        self.minimum_level = 1
        self.a_an = "a"


canvas_cloak = CanvasCloak()


class ElvenCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Elven Cloak"
        self.item_type = "Cloaks"
        self.stealth = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1
        self.a_an = "an"


elven_cloak = ElvenCloak()


class Healing:
    def __init__(self):
        self.name = ""
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 0
        self.sell_price = 0
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class Elixir:
    def __init__(self):
        self.name = "Clarifying Elixir"
        self.item_type = "Elixirs"
        self.uses = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


elixir = Elixir()


class Antidote:
    def __init__(self):
        self.name = "Vial of Antidote"
        self.item_type = "Antidotes"
        self.uses = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


antidote = Antidote()


class HealingPotion(Healing):
    def __init__(self):
        super().__init__()
        self.name = "Potion of Healing"
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


healing_potion = HealingPotion()


class StrengthPotion:
    def __init__(self):
        self.name = "Potion of Strength"
        self.item_type = "Potions of Strength"
        self.duration = 5
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


strength_potion = StrengthPotion()


class Regeneration:

    def __init__(self):
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return self.name


class DefaultRingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "Lead Ring"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = ""


default_ring_of_regeneration = DefaultRingOfRegeneration()


class RingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


ring_of_regeneration = RingOfRegeneration()


class Protection:

    def __init__(self):
        self.name = ""
        self.item_type = "Rings"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"

    def __repr__(self):
        return self.name


class DefaultRingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "Tin Ring"
        self.item_type = "Rings of Protection"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


default_ring_of_protection = DefaultRingOfProtection()


class RingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "Ring Of Protection"
        self.item_type = "Rings of Protection"
        self.protect = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1
        self.a_an = "a"


ring_of_protection = RingOfProtection()


class TownPortalImplements:

    def __init__(self):
        self.name = "Scroll of Town Portal"
        self.item_type = "Town Portal Implements"
        self.protect = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1
        self.uses = 1
        self.a_an = "a"

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


scroll_of_town_portal = TownPortalImplements()


top_level_loot_dict = {
            'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
            'Shields': [buckler, kite_shield, quantum_tower_shield],
            'Boots': [elven_boots, ancestral_footsteps],
            'Cloaks': [elven_cloak],
            'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                        quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
            'Elixirs': [elixir],
            'Healing': [healing_potion],
            'Rings of Regeneration': [ring_of_regeneration],
            'Rings of Protection': [ring_of_protection],
            'Town Portal Implements': [scroll_of_town_portal],
            'Potions of Strength': [strength_potion],
            'Antidotes': [antidote]
        }

new_top_level_loot_dict = {
            'Armor': [LeatherArmor, StuddedLeatherArmor, ScaleMail, HalfPlate, FullPlate],
            'Shields': [Buckler, KiteShield, QuantumTowerShield],
            'Boots': [ElvenBoots, AncestralFootsteps],
            'Cloaks': [ElvenCloak],
            'Weapons': [ShortAxe, BroadSword, GreatSword, ElvishGreatSword, QuantumSword,
                        BattleAxe, GreatAxe, QuantumAxe],
            'Elixirs': [Elixir],
            'Healing': [HealingPotion],
            'Rings of Regeneration': [RingOfRegeneration],
            'Rings of Protection': [RingOfProtection],
            'Town Portal Implements': [TownPortalImplements],
            'Potions of Strength': [StrengthPotion],
            'Antidotes': [Antidote]}


def undead_prophet_returns():
    return "Undead Prophet"


def king_returns():
    return "King Boss"


def nothing_happens():
    print(f"Nothing happens....")
    pause()
    return


def npc_retreat_counter_logic(npc):
    # called from self.monster_attacks_npc_meta(), for each npc, if retreating
    npc.retreat_counter += 1
    if npc.retreat_counter >= npc.retreat_counter_threshold:
        return npc_end_of_turn_calculation(npc)


def npc_end_of_turn_calculation(npc):
    # called from npc_calculation()
    # when monster defeated, turned, or no longer in proximity, npc allies no longer in retreat
    # they also fully heal
    # also called from npc_retreat_counter_logic() when npc.retreat_counter >= npc.retreat_counter_threshold
    if npc.retreating:
        npc.retreating = False
        npc.retreat_counter = 0
        print(f"{npc.name} is no longer retreating")
        sleep(1)
    if npc.hit_points < npc.maximum_hit_points:
        print(f"{npc.name} heals to full strength.")
        npc.hit_points = npc.maximum_hit_points
        sleep(1)

# NPC allies


class VozzBozz:

    def __init__(self):
        self.name = "Vozzbozz"
        self.level = 13
        self.quantum_level = 6
        self.maximum_quantum_units = 6000
        self.quantum_units = 6000
        self.experience = 0
        self.base_dc = 10
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = quantum_sword
        self.armor = half_plate
        self.shield = no_shield
        self.boots = elven_boots
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 13
        self.strength_bonus = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 16
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 14
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 20
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 20
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 18
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 8
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 199 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus + self.shield.ac +
                            self.boots.ac + self.dexterity_modifier)
        self.protect = 6
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


vozzbozz = VozzBozz()


class SiKira:

    def __init__(self):
        self.name = "Si'Kira"
        self.level = 10
        self.quantum_level = 2
        self.maximum_quantum_units = 2
        self.quantum_units = 6
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = elvish_great_sword
        self.armor = scale_mail
        self.shield = kite_shield
        self.boots = elven_boots
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 13
        self.strength_bonus = 1
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 17
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 14
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 16
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 16
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 18
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 8
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 70 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.protect = 3
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 2  # 2 full rounds of retreat, not including initial round


sikira = SiKira()


class TorBron:

    def __init__(self):
        self.name = "Tor'Bron"
        self.level = 10
        self.quantum_level = 2
        self.maximum_quantum_units = 2
        self.quantum_units = 6
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = quantum_sword
        self.armor = half_plate
        self.shield = kite_shield
        self.boots = ancestral_footsteps
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 17
        self.strength_bonus = 1.5
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 15
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 18
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 14
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 10
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 10
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 12
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 100 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.protect = 4
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


torbron = TorBron()


class Magnus:

    def __init__(self):
        self.name = "Magnus"
        self.level = 10
        self.quantum_level = 5
        self.maximum_quantum_units = 15
        self.quantum_units = 15
        self.experience = 0
        self.base_dc = 8
        self.gold = random.randint(2500, 4000)
        self.wielded_weapon = quantum_axe
        self.armor = half_plate
        self.shield = kite_shield
        self.boots = ancestral_footsteps
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 16
        self.strength_bonus = 1.33
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 15
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 16
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 14
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 10
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 10
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 10
        self.proficiency_bonus = 1 + math.ceil(self.level / 4)
        self.maximum_hit_points = 100 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.protect = 4
        self.retreating = False
        self.retreat_counter = 0
        self.retreat_counter_threshold = 1  # 1 full round of retreat, not including initial round


magnus = Magnus()

# Human Player:


class Player:

    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.level = 1
        self.quantum_level = 1
        self.maximum_quantum_units = 2
        self.quantum_units = self.maximum_quantum_units
        self.encounter = 0
        self.experience = 0
        self.base_dc = 8
        self.gold = 0
        self.wielded_weapon = short_sword
        self.armor = padded_armor
        self.shield = no_shield
        self.boots = leather_boots
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = strength
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = dexterity
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = constitution
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = intelligence
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = wisdom
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = charisma
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 10
        self.proficiency_bonus = 2
        self.maximum_hit_points = 10 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points  # Hit Points at 1st Level: 10 + your Constitution modifier
        self.in_proximity_to_monster = False
        self.is_paralyzed = False
        self.cloak = canvas_cloak
        self.ring_of_prot = default_ring_of_protection
        self.ring_of_reg = default_ring_of_regeneration
        self.two_handed = False
        self.extra_attack = 0
        self.armor_class = (self.armor.ac + self.armor.armor_bonus +
                            self.shield.ac + self.boots.ac + self.dexterity_modifier)
        self.stealth = self.cloak.stealth
        self.town_portals = 1
        self.elixirs = 1
        self.potions_of_healing = 1
        self.antidotes = 1
        self.potions_of_strength = 1
        self.potion_of_strength_effect = False
        self.potion_of_strength_uses = 0
        self.max_quantum_strength_uses = self.quantum_level + self.strength_modifier
        self.quantum_strength_uses = 0
        self.quantum_strength_effect = False
        self.protection_effect = False
        self.protection_effect_uses = 0
        self.max_protection_effect_uses = self.quantum_level + self.constitution_modifier
        self.temp_protection_effect = 0
        self.poisoned = False
        self.poisoned_turns = 0
        self.max_poisoned_turns = 0
        self.necrotic = False
        self.necrotic_turns = 0
        self.dot_multiplier = 1
        self.dot_turns = 1
        self.current_dungeon_level = 1
        self.dungeon_key = 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        self.discovered_interactives = []
        self.discovered_monsters = []
        self.position = 0
        self.x = 0
        self.y = 0
        self.coordinates = (self.x, self.y)
        self.previous_x = 0
        self.previous_y = 0
        self.in_a_pit = False
        self.vanquished_foes = []
        self.sikira_ally = False
        self.torbron_ally = False
        self.magnus_ally = False
        self.vozzbozz_ally = False
        self.boss_hint_1 = True
        self.boss_hint_1_event = False
        self.boss_hint_2 = False
        self.boss_hint_2_event = False
        self.boss_hint_3 = False
        self.boss_hint_3_event = False
        self.boss_hint_4 = False
        self.boss_hint_4_event = False
        # self.boss_hint_5 = False
        # self.boss_hint_5_event = False
        # self.boss_hint_6 = False
        # self.boss_hint_6_event = False
        self.loaded_game = False
        self.forest_explored = False
        self.town_portal_exists = False
        self.in_town = False
        self.in_dungeon = False
        self.pack = {
            'Armor': [],
            'Shields': [],
            'Boots': [],
            'Weapons': [],
            'Cloaks': [],
            # 'Rings of Regeneration': [],  # beta
            # 'Rings of Protection': []    # beta
            # 'Town Portal Implements': []  # [scroll_of_town_portal]

        }

    # COMMENTED OUT RINGS FROM PACK 10/11/2022

    def dungeon_theme(self):
        if os.name == 'nt':
            if not self.in_a_pit:
                sound_player_loop('dungeon_theme_2.wav')
            else:
                pit_theme()

    def regenerate(self):
        if self.hit_points < self.maximum_hit_points and self.ring_of_reg.regenerate > 0:
            regeneration = self.ring_of_reg.regenerate
            self.hit_points = self.hit_points + regeneration
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points
            print(f"You regenerate + {regeneration}")  # remove after testing
            sleep(1)
        return

    def hud(self):
        cls()
        print(f"Name: {self.name}")
        print(f"Level: {self.level} ({self.level}d{self.hit_dice})")
        print(f"Experience: {self.experience}")
        print(f"Gold: {self.gold}")
        print(f"Weapon: {self.wielded_weapon.name} (Damage Bonus: {self.wielded_weapon.damage_bonus}) "
              f"(To hit bonus: {self.wielded_weapon.to_hit_bonus})")
        print(f"Armor: {self.armor.name} (AC: {self.armor.ac})")
        print(f"Shield: {self.shield.name} (AC: {self.shield.ac})")
        print(f"Boots: {self.boots.name} (AC: {self.boots.ac})")
        print(f"Your Armor Class: {self.armor_class}")
        print(f"Strength: {self.strength} (Modifier: {self.strength_modifier})")
        print(f"Dexterity: {self.dexterity} (Modifier: {self.dexterity_modifier})")
        print(f"Constitution: {self.constitution} (Modifier: {self.constitution_modifier})")
        print(f"Intelligence: {self.intelligence} (Modifier: {self.intelligence_modifier})")
        print(f"Wisdom: {self.wisdom} (Modifier: {self.wisdom_modifier})")
        print(f"Charisma: {self.charisma} (Modifier: {self.charisma_modifier})")
        print(f"Hit points: {self.hit_points}/{self.maximum_hit_points}")
        print(f"Quantum units: {self.quantum_units}/{self.maximum_quantum_units}")
        print(f"Cloak: {self.cloak.name} (Stealth: {self.stealth})")
        if self.potions_of_strength > 0:
            number_of_potions_of_strength = self.potions_of_strength
            print(f"Strength Potions: {number_of_potions_of_strength}")
        if self.potion_of_strength_effect and self.potion_of_strength_uses > -1:
            print(f"(STRENGTH POTION EFFECT)  ({self.potion_of_strength_uses}/{self.max_quantum_strength_uses})")
        if self.quantum_strength_effect and self.quantum_strength_uses > -1:
            print(f"QUANTUM STRENGTH EFFECT)  ({self.quantum_strength_uses}/{self.max_quantum_strength_uses})")
        if self.protection_effect and self.protection_effect_uses > -1:
            print(f"(PROT/EVIL: {self.temp_protection_effect}) "
                  f"({self.protection_effect_uses}/{self.max_protection_effect_uses})")
        if self.poisoned:
            print(f"(POISONED)  Poison clarifying: ({self.poisoned_turns}/{self.dot_turns})")
        if self.necrotic:
            print(f"(NECROTIC)  Necrotic clarifying: ({self.necrotic_turns}/{self.dot_turns})")
        if self.potions_of_healing > 0:
            number_of_potions_of_healing = self.potions_of_healing
            print(f"Healing Potions: {number_of_potions_of_healing}")
        if self.antidotes > 0:
            number_of_antidotes = self.antidotes
            print(f"Vials of Antidote: {number_of_antidotes}")
        if self.elixirs > 0:
            number_of_elixirs = self.elixirs
            print(f"Elixirs: {number_of_elixirs}")
        if self.town_portals > 0:
            number_of_portal_scrolls = self.town_portals
            print(f"Town Portal Scrolls: {number_of_portal_scrolls}")
        if self.ring_of_reg.name != default_ring_of_regeneration.name:
            print(f"Ring of Regeneration: +{self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != default_ring_of_protection.name:
            print(f"Ring of Protection: +{self.ring_of_prot.protect}")
        print()
        return

    # CALCULATION
    def monster_attacks_npc_meta(self, monster):
        # called from main loop, after monster attacks human player. (also called after paralyze attacks.)
        # if monster has multi_attack ability, monster attacks all npc allies
        self.hud()
        # multi_attack ability allows monster to attack ALL npc allies
        if monster.multi_attack:
            if self.sikira_ally:
                if not sikira.retreating:
                    monster.meta_monster_vs_npc_function(sikira)
                    self.npc_retreat_logic(sikira)
                    self.hud()
                else:
                    npc_retreat_counter_logic(sikira)
            if self.torbron_ally:
                if not torbron.retreating:
                    monster.meta_monster_vs_npc_function(torbron)
                    self.npc_retreat_logic(torbron)
                    self.hud()
                else:
                    npc_retreat_counter_logic(torbron)
            if self.magnus_ally:
                if not magnus.retreating:
                    monster.meta_monster_vs_npc_function(magnus)
                    self.npc_retreat_logic(magnus)
                    self.hud()
                else:
                    npc_retreat_counter_logic(magnus)
            if self.vozzbozz_ally:
                if not vozzbozz.retreating:
                    monster.meta_monster_vs_npc_function(vozzbozz)
                    self.npc_retreat_logic(vozzbozz)
                    self.hud()
                else:
                    npc_retreat_counter_logic(vozzbozz)
            return

        elif monster.lesser_multi_attack:

            # lesser_multi_attack creates a list of non-retreating allies, if any:
            allies = []

            if self.sikira_ally:
                if not sikira.retreating:
                    allies.append(sikira)
                else:
                    npc_retreat_counter_logic(sikira)

            if self.torbron_ally:
                if not torbron.retreating:
                    allies.append(torbron)
                else:
                    npc_retreat_counter_logic(torbron)

            if self.magnus_ally:
                if not magnus.retreating:
                    allies.append(magnus)
                else:
                    npc_retreat_counter_logic(magnus)

            if self.vozzbozz_ally:
                if not vozzbozz.retreating:
                    allies.append(vozzbozz)
                else:
                    npc_retreat_counter_logic(vozzbozz)

            # one ally is then randomly chosen and attacked by monster:
            if len(allies):
                ally = random.choice(allies)
                monster.meta_monster_vs_npc_function(ally)
                self.npc_retreat_logic(ally)

    def npc_retreat_logic(self, npc):
        # called from self.monster_attacks_npc_meta(), after monster attack turn
        if npc.hit_points < 1:
            npc.retreating = True
            self.hud()
            print(f"{npc.name} is retreating!")
            pause()

    def npc_calculation(self):
        # called from main loop, after player end_of_turn_calculation()
        # when monster defeated, turned, or no longer in proximity, npc allies no longer in retreat
        # they also fully heal
        if self.sikira_ally:
            npc_end_of_turn_calculation(sikira)
        if self.torbron_ally:
            npc_end_of_turn_calculation(torbron)
        if self.magnus_ally:
            npc_end_of_turn_calculation(magnus)
        if self.vozzbozz_ally:
            npc_end_of_turn_calculation(vozzbozz)

    def end_of_turn_calculation(self):
        # called from main loop at end of player navigation, or battle turn
        self.regenerate()
        self.calculate_potion_of_strength()  # potions of strength have max uses = self.max_quantum_strength_uses
        self.calculate_quantum_strength()  # self.max_quantum_strength_uses= self.quantum_level + self.strength_modifier
        self.calculate_protection_effect()  # max_protection_effect_uses= self.quantum_level+ self.constitution_modifier
        self.calculate_poison()  # poison wears off after self.dot_turns which = monster.dot_turns during battle
        self.calculate_necrotic_dot()  # necrosis wears off after self.dot_turns which = monster.dot_turns during battle

    def calculate_stealth(self):
        # called from found_cloak_substitution() as well as item_management()
        self.stealth = self.cloak.stealth
        return

    def calculate_armor_class(self):
        # called from monster_likes_you(), item_management(), found_shield_substitution, found_armor_substitution()
        self.armor_class = self.armor.ac + self.armor.armor_bonus + \
                           self.shield.ac + self.boots.ac + self.dexterity_modifier
        return

    def calculate_poison(self):
        # called from end_of_turn_calculation() meta function
        if self.poisoned:

            if self.poisoned_turns >= self.dot_turns:
                self.poisoned = False
                self.poisoned_turns = 0
                print(f"The poison leaves your body..")
                sleep(1.5)

            else:
                self.poisoned = True
                self.poisoned_turns += 1
                poison_damage = (1 * self.dot_multiplier)
                self.hit_points -= poison_damage
                print(f"*POISON DAMAGE: {poison_damage}*")
                sleep(1.5)

        return self.poisoned

    def calculate_necrotic_dot(self):
        # called from end_of_turn_calculation() meta function
        if self.necrotic:

            if self.necrotic_turns >= self.dot_turns:
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The necrotic plague leaves your body..")
                sleep(1.5)

            else:
                self.necrotic = True
                self.necrotic_turns += 1
                necrotic_damage = (1 * self.dot_multiplier)
                self.hit_points -= necrotic_damage
                print(f"*NECROTIC DAMAGE: {necrotic_damage}*")
                sleep(1.5)

        return self.necrotic

    def calculate_quantum_strength(self):
        # called from end_of_turn_calculation() meta function
        if self.quantum_strength_effect:

            if self.quantum_strength_uses >= self.max_quantum_strength_uses:  # self.quantum_lvl+self.strength_modifier
                self.quantum_strength_effect = False
                self.quantum_strength_uses = 0
                print(f"The Quantum Effects wear off....the giant strength leaves your body..")
                pause()

            else:
                self.quantum_strength_effect = True
                self.quantum_strength_uses += 1

        return self.quantum_strength_effect

    def calculate_potion_of_strength(self):
        # called from end_of_turn_calculation() meta function
        if self.potion_of_strength_effect:

            if self.potion_of_strength_uses >= self.max_quantum_strength_uses:  # self.strength_modifier + 2:
                self.potion_of_strength_effect = False
                self.potion_of_strength_uses = 0
                print(f"The potion's effect wears off....the giant strength leaves your body..")
                pause()

            else:
                self.potion_of_strength_effect = True
                self.potion_of_strength_uses += 1

        return self.potion_of_strength_effect

    def calculate_protection_effect(self):
        # called from end_of_turn_calculation() meta function
        if self.protection_effect:

            if self.protection_effect_uses >= self.max_protection_effect_uses:
                self.protection_effect = False
                self.protection_effect_uses = 0
                self.temp_protection_effect = 0
                print(f"The Quantum Protection effect wears off...")
                pause()

            else:
                self.protection_effect = True
                self.protection_effect_uses += 1
                # self.temp_protection_effect = (2 + self.level)
                if self.temp_protection_effect > 10:
                    self.temp_protection_effect = 10

        return self.protection_effect

    def calculate_modifiers(self):
        # called from ability score improvement asi(), increase_random_ability(), decrease_random_ability(),
        # level_up(), increase_lowest_ability() and decrease_lowest_ability()
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        # When your Constitution modifier increases by 1,
        # your hit point maximum increases by 1 for each level you have attained.
        before_con_mod = self.constitution_modifier
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        after_con_mod = self.constitution_modifier
        if after_con_mod > before_con_mod:
            print(f"Weird powers are stirred up within you...")
            sleep(1)
            self.maximum_hit_points += self.level
            self.hit_points = self.maximum_hit_points
            print(f"Your Constitution Modifier has increased from {before_con_mod} to {after_con_mod}!")
            sleep(1)
            print(f"You gain {self.level} maximum hit points!")
            sleep(1)
            print(f"You feel your vitality surge.")
            sleep(1)
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.max_protection_effect_uses = self.quantum_level + self.constitution_modifier
        self.max_quantum_strength_uses = self.quantum_level + self.strength_modifier
        return

    def calculate_proficiency_bonus(self):
        # called from level_up()
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

        return

    # Quantum LEVEL   EXPERIENCE LEVEL
    #                    NEEDED TO USE
    # 1                       1
    # 2                       3
    # 3                       6
    # 4                       9
    # 5                       12
    # 6                       15

    def calculate_current_level(self):
        # called from level_up()
        if self.experience < 300:
            self.level = 1
            self.quantum_level = 1
            self.maximum_quantum_units = 2

        if self.experience >= 300 < 900:
            self.level = 2
            self.quantum_level = 1
            self.maximum_quantum_units = 4

        if self.experience >= 900 < 2700:
            self.level = 3
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 2700 < 6500:
            self.level = 4
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 6500 < 14000:
            self.level = 5
            self.quantum_level = 2
            self.maximum_quantum_units = 6

        if self.experience >= 14000 < 23000:
            self.level = 6
            self.quantum_level = 3
            self.maximum_quantum_units = 8

        if self.experience >= 23000 < 34000:
            self.level = 7
            self.quantum_level = 3
            self.maximum_quantum_units = 8

        if self.experience >= 34000 < 48000:
            self.level = 8
            self.quantum_level = 3
            self.maximum_quantum_units = 10

        if self.experience >= 48000 < 64000:
            self.level = 9
            self.quantum_level = 4
            self.maximum_quantum_units = 10

        if self.experience >= 64000 < 85000:
            self.level = 10
            self.quantum_level = 4
            self.maximum_quantum_units = 12

        if self.experience >= 85000 < 100000:
            self.level = 11
            self.quantum_level = 4
            self.maximum_quantum_units = 12

        if self.experience >= 100000 < 120000:
            self.level = 12
            self.quantum_level = 5
            self.maximum_quantum_units = 14

        if self.experience >= 120000 < 140000:
            self.level = 13
            self.quantum_level = 5
            self.maximum_quantum_units = 16

        if self.experience >= 140000 < 165000:
            self.level = 14
            self.quantum_level = 5
            self.maximum_quantum_units = 18

        if self.experience >= 165000 < 195000:
            self.level = 15
            self.quantum_level = 6
            self.maximum_quantum_units = 18

        if self.experience >= 195000 < 225000:
            self.level = 16
            self.quantum_level = 6
            self.maximum_quantum_units = 20

        if self.experience >= 225000 < 265000:
            self.level = 17
            self.quantum_level = 6
            self.maximum_quantum_units = 24

        if self.experience >= 265000 < 305000:
            self.level = 18
            self.quantum_level = 6
            self.maximum_quantum_units = 30

        if self.experience >= 305000 < 355000:
            self.level = 19
            self.quantum_level = 6
            self.maximum_quantum_units = 36

        if self.experience >= 355000:
            self.level = 20
            self.quantum_level = 6
            self.maximum_quantum_units = 1000

        return

    # LEVEL AND EXPERIENCE
    def asi_eligibility(self):
        if self.strength < 20 or self.dexterity < 20 or self.constitution < 20 or self.intelligence < 20 \
                or self.wisdom < 20 or self.charisma < 20:
            return True
        else:
            print(f"All abilities at maximum!")  # remove after testing
            return False

    def asi(self):
        # called from level_up()
        # Ability Score Improvement at levels 4, 8, 12, 16, and 19.
        # Fighters gain additional ASIs at the 6th and 14th levels
        # so, 4, 6, 8, 12, 14, 16, 19 for our purposes, since player is most like a fighter
        # also, if player goes up more than one level, by gaining a large amount of experience, asi is available

        while True:
            self.hud()
            tries = 0
            points = 2
            while True:
                self.hud()
                # print(f"Ability Score Improvement for level {self.level}")

                if tries > 1:
                    return

                ability_dict = self.__dict__  # create variable as actual copy of player dict attribute
                ability_lst = []  # list to be populated with all abilities < 20
                # the working dict and 'for' loop just takes the place of many 'if:' statements
                working_dict = {'strength': self.strength, 'dexterity': self.dexterity,
                                'constitution': self.constitution, 'intelligence': self.intelligence,
                                'wisdom': self.wisdom, 'charisma': self.charisma}

                # add all abilities < 20 in working dict to ability_lst to define attributes you are allowed to change:
                for key, value in working_dict.items():
                    if value < 20:
                        ability_lst.append(key)

                # this code should be reachable if stats are maxed out, and player level_up calls it:
                if not len(ability_lst):  # if ability list is empty, all stats at 20; no more improvements allowed
                    print(f"All of your abilities are at the maximum level!")
                    sleep(1.25)
                    return

                print(f"Ability Score Improvement\n"
                      f"Player level: {self.level}")
                print(f"Points to distribute: {points}")
                # create a subset ability dictionary from the ability list by indexing, and then print out
                ability_dict_subset_too = {}
                for ability in ability_lst:
                    if len(ability_lst):
                        ability_dict_subset_too[ability_lst.index(ability)] = ability
                for key, value in ability_dict_subset_too.items():
                    print(key + 1, ':', value.capitalize())  # add 1 to key since indexing begins at 0

                try:
                    ability_index = int(input(f"Enter the ability to improve.\n"
                                              f"(THIS IS PERMANENT!) : "))
                    ability_index -= 1  # indexing begins at zero...
                    ability_to_improve = (ability_dict_subset_too[ability_index])
                    old_score = ability_dict[ability_to_improve]
                    ability_dict[ability_to_improve] += 1
                    print(
                        f"Your {ability_to_improve} has been increased from {old_score} "
                        f"to {ability_dict[ability_to_improve]}!")
                    self.calculate_modifiers()
                    tries += 1
                    points -= 1
                    pause()
                    continue

                except (ValueError, KeyError):
                    print("Invalid entry..")
                    sleep(1)
                    continue

    def level_up(self, exp_award, monster_gold):
        # called from main loop after victory
        self.gold += monster_gold
        before_level = self.level
        before_quantum_level = self.quantum_level
        before_proficiency_bonus = self.proficiency_bonus
        self.experience += exp_award
        self.calculate_current_level()
        self.calculate_proficiency_bonus()
        after_proficiency_bonus = self.proficiency_bonus
        after_level = self.level
        level_multiplier = (after_level - before_level)  # in case player goes up more than 1 level
        after_quantum_level = self.quantum_level
        if after_level > before_level:
            if monster_gold > 0:
                print(f"You snarf {monster_gold} gold pieces.")
                sleep(1)
            print(f"You gain {exp_award} experience points.")
            sleep(2)
            gong()
            if level_multiplier > 1:
                print(f"You have gained {level_multiplier} experience levels!")
            elif level_multiplier == 1:
                print(f"You went up a level!!")
            sleep(2)
            print(f"You are now level {self.level}.")
            sleep(2)
            self.dungeon_theme()
            self.calculate_proficiency_bonus()  # according to DnD 5e
            gain_hit_points1 = (dice_roll(1, self.hit_dice) + self.constitution_modifier) * level_multiplier  # method 1
            gain_hit_points2 = (6 + self.constitution_modifier) * level_multiplier  # hp increase method 2
            hit_point_list = [gain_hit_points1, gain_hit_points2]
            gain_hit_points = max(hit_point_list)  # the highest of method 1 and 2
            self.hit_points += gain_hit_points  # you heal and gain max hp (previous HP + Hit Die roll + CON modifier)
            self.maximum_hit_points += gain_hit_points
            print(f"You gain {gain_hit_points} hit points")
            sleep(2.5)

            # Ability Score Improvement at levels 4, 6, 8, 12, 14, 16, 19
            # ASI logic
            # This logic also works for players going up more than one level,
            # e.g. vanquishing a monster with very high experience reward
            # Logic works by creating 2 lists and comparing whether the player's current level, or any levels between
            # their last level and current level are ASI eligible. Ranges are initially counterintuitive in python;
            # they do not include the last number in range, so I added +1 to end_range
            # Also, for the current purposes, I added +1 to start_range as well, since we don't want to award ASI
            # based on the previous experience level, only on current level and any eligible levels between.
            range_1 = range((before_level + 1), (after_level + 1), 1)  # enumerate lvls between, inc. after_level
            all_levels_between = list(range_1)  # create a list containing levels between, including after_level
            asi_levels = [4, 6, 8, 12, 14, 16, 19]
            # check if any levels between are ASI levels by comparing elements from both lists
            # number_of_asi_awards = sum of all_levels_between elements which exist in asi_levels
            number_of_asi_awards = sum(el in all_levels_between for el in asi_levels)
            asi_level_check = False
            if number_of_asi_awards > 0:
                asi_level_check = True

            # remove after testing:
            # print(f"Range between the before and after levels: {range_1}")  # remove after testing
            print(f"Levels between last and current (including current): {all_levels_between}")  # remove after testing
            print(f"ASI levels: {asi_levels}")  # remove after testing
            print(f"Number of ASI awards: {number_of_asi_awards}")  # remove after testing
            pause()  # remove after testing

            if asi_level_check:
                if self.asi_eligibility():  # ensure player has at least 1 ability score < 20
                    if number_of_asi_awards > 1:
                        print(f"You have earned {number_of_asi_awards} ability score improvements!")
                        pause()

                    asi_intro()
                    for i in range(number_of_asi_awards):
                        self.asi()

                    print(f"You savor the empowering abilities you have gained..\n"
                          f"And yet, the dungeon horde grows more powerful with you!")
                    pause()
                    self.hud()

            self.calculate_modifiers()

            if 5 in all_levels_between:  # players gain extra attack skill at level 5 # self.level == 5:
                self.extra_attack = True
                print("You gain the Extra Attack skill!!")  # this works in melee loop if level > 4, change to a boolean
                pause()
                self.hud()

            if after_proficiency_bonus > before_proficiency_bonus:
                print(f"Your proficiency bonus increases from {before_proficiency_bonus} to {after_proficiency_bonus}!")
                pause()
                self.hud()

            if after_quantum_level > before_quantum_level:
                print(f"Your Quantum knowledge level increases from {before_quantum_level} to {after_quantum_level}!")
                self.quantum_units = self.maximum_quantum_units
                pause()
                self.hud()

            self.hud()

        else:
            if monster_gold > 0:
                print(f"You snarf {monster_gold} gold pieces.")
                sleep(1)
            print(f"You gain {exp_award} experience points.")
            # print(f"You snarf {monster_gold} gold pieces and gain {exp_award} experience points")
            sleep(2)
            self.hud()

    # BATTLE AND PROXIMITY TO MONSTER OCCURRENCES

    def choose_to_play_again(self):
        cls()
        gong()
        typewriter(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
        sleep(4)
        self.in_proximity_to_monster = False
        self.in_dungeon = False
        self.in_town = False
        while True:
            cls()
            try_again = input("Do you wish to play again (y/n)? ").lower()
            if try_again == "y":
                sleep(1)
                cls()
                self.in_proximity_to_monster = False
                self.in_dungeon = False
                self.in_town = False
                # player_is_dead = False
                return True
            if try_again == "n":
                print(f"Farewell.")
                sleep(.5)
                cls()
                sys.exit()
            # if try_again not in ("y", "n"):
                # print("Please enter y or n ")
            #    sleep(.5)
            #    continue

    def encounter_logic(self):
        # called from main loop
        self.encounter = dice_roll(1, 20)
        # monster_encounter = dice_roll(1, 20)
        # print(f"Monster encounter roll: {monster_encounter}")
        # return monster_encounter
        # self.encounter = 15  # this will make it so there are no monsters

    def monster_introduction(self, monster):
        # called from main loop
        if monster.name in self.discovered_monsters:
            self.hud()  # placing a hud() here erases the dungeon description; more appropriate
            print(f"(TESTING) Discovered monsters: {self.discovered_monsters}")  # remove after testing
            print(f"You have encountered a {monster.name}. Challenge level: {monster.level}")
            # remove lvl after testing
            pause()
        else:
            self.hud()  # placing a hud() here erases the dungeon description; more appropriate
            print(f"{monster.introduction}")

            if self.encounter < 21:  # if not a boss
                self.discovered_monsters.append(monster.name)
            pause()

    def monster_likes_you_or_steals_from_you(self, monster):
        if self.encounter < 21:  # if not a boss, monster may like you or steal from you

            if self.monster_likes_you(monster):
                self.in_proximity_to_monster = False
                # player_1.event_logic()  # this will trigger an event without using (L)ook
                self.dungeon_description()
                return True

            if self.quick_move(monster):
                self.in_proximity_to_monster = False
                # player_1.event_logic()  # this will trigger an event without using (L)ook
                self.dungeon_description()
                return True  # if monster steals something he gets away clean, if not, battle

            else:
                return False

        else:
            return False

    def battle_menu_choices(self, monster):
        # main loop battle menu. a party of adventurers cannot evade
        while True:
            self.hud()
            monster.monster_data()

            if not self.sikira_ally and not self.torbron_ally and not self.magnus_ally and not self.vozzbozz_ally:
                battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                      "(G)iant Strength potion, (V)ial of Antidote,\n(Q)uantum Effects or "
                                      "(E)vade\nF/H/C/G/V/Q/E --> ").lower()

                if battle_choice in ('f', 'h', 'c', 'g', 'v', 'q', 'e'):
                    return battle_choice

                else:  # invalid inputs
                    print(f"The {monster.name} is not amused.")
                    sleep(.75)
                    self.hud()
                    continue

            else:  # a party of adventurers cannot evade
                battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                      "(G)iant Strength potion, (V)ial of Antidote,\n or (Q)uantum Effects\n"
                                      "F/H/C/G/V/Q --> ").lower()

                if battle_choice in ('f', 'h', 'c', 'g', 'v', 'q'):
                    return battle_choice

                else:  # invalid inputs
                    print(f"The {monster.name} is not amused.")
                    sleep(.75)
                    self.hud()
                    continue

    def check_for_boss(self, event):

        if event == "Elite Monster":
            self.encounter = 95
        if event == "Legendary Monster":
            self.encounter = 96
        elif event == "Undead Prophet":
            self.encounter = 97
        elif event == "King Boss":
            self.encounter = 98
        elif event == "Exit Boss":
            self.encounter = 99
        elif event == "Wicked Queen":
            self.encounter = 100
        else:
            return False

    def victory_statements(self, monster):
        statements_list = [f"You are victorious!", f"You have defeated the {monster.name}!"]
        if self.encounter > 20:  # if victory over boss
            gong()
            if monster.proper_name != "None":
                print(f"You have vanquished {monster.proper_name}! You are victorious!")
                self.vanquished_foes.append(monster.proper_name)
            else:
                print(f"You have vanquished the {monster.name}!")
            sleep(4)
            self.dungeon_theme()
        else:
            statement = random.choice(statements_list)
            print(statement)

    def victory_over_boss_logic(self):
        if self.encounter == 99:  # if dungeon level exit boss
            self.boss_hint_logic()

    def rndm_death_statement(self):
        # called from main loop
        rndm_statements = ["You have succumbed to your injuries!",
                           "Bravely you have fought. Bravely you have died. Rest in Peace."
                           ]
        print(f"{self.name} Level {self.level}")
        print(random.choice(rndm_statements))
        return

    def meta_monster_generator(self):
        # called from main loop
        monster = None

        if self.encounter < 11:  # regular monster
            monster = self.regular_monster_generator()

        # put testing monster here
            # from monster_module import Troll
            # monster = Troll()

        elif self.encounter == 100:  # final boss
            monster = self.wicked_queen_generator()
            gong()
            sleep(4)
            boss_battle_theme()
            pause()
            self.hud()

        elif self.encounter == 99:  # level exit boss fight
            monster = self.exit_boss_generator()
            gong()
            sleep(4)
            boss_battle_theme()
            pause()
            self.hud()

        elif self.encounter == 98:  # undead king
            monster = self.king_monster_generator()
            gong()
            sleep(4)
            mountain_king_theme()
            pause()
            self.hud()

        elif self.encounter == 97:  # undead prophet
            monster = self.undead_prophet_generator()
            gong()
            sleep(4)
            boss_battle_theme()
            pause()
            self.hud()

        elif self.encounter == 96:  # legendary monster
            monster = self.legendary_monster_generator()
            gong()
            sleep(4)
            boss_battle_theme()
            pause()
            self.hud()

        elif self.encounter == 95:  # elite
            monster = self.elite_monster_generator()
            gong()
            sleep(4)
            boss_battle_theme()
            pause()
            self.hud()

        return monster

    def wicked_queen_generator(self):
        # called from meta_monster_generator() if encounter == 100
        wicked_queen = WickedQueenJannbrielle()  # monster_dict([4][0])()
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"The Queen stands, approaches the party and readies herself for battle!")
        return wicked_queen

    def legendary_monster_generator(self):
        # called from meta_monster_generator() if encounter == 96
        rndm_boss_names = ['Sarlen', 'Sinedor', 'Birlendor', 'Lichtor', 'Renburr',
                           'Belorg', 'Sirlak', 'Gruldirren', 'Falldorren', 'Tilenbor', 'Durjinn',
                           'Morgenoth', 'Tergoam', 'Terdannor', 'Lorenqor', 'Worgoth',
                           'Hahrbinnor', 'Korrendor', 'Karbrath', 'Qintar', 'Wobard',
                           'Sorrikon', 'Dellbrion', 'Selanius', 'Qorron', 'Sorrendir',
                           'Mawleon', 'Sador', 'Qardormirr', 'Bendorn', 'Vallqedon',
                           'Merlkandon']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        boss_monster = monster_cls()
        first_name = random.choice(rndm_boss_names)
        boss_monster.proper_name = f"{first_name} the Legendary {boss_monster.name}"
        boss_monster.hit_points = math.ceil(boss_monster.hit_points * 2)
        boss_monster.experience_award = math.ceil(boss_monster.experience_award * 2)
        boss_monster.strength += 4
        boss_monster.dexterity += 4
        boss_monster.constitution += 4
        boss_monster.intelligence += 4
        boss_monster.wisdom += 4
        boss_monster.charisma += 4
        boss_monster.armor_class += 2
        boss_monster.resistances = ["All"]
        boss_monster.weapon_bonus = math.ceil(self.level * 2)
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"Before you stands {boss_monster.proper_name}!")
        return boss_monster

    def elite_monster_generator(self):
        # called from meta_monster_generator() if encounter == 95
        rndm_boss_names = ['Sarlongrath', 'Sundor', 'Birrenol', 'Sontor', 'Marburr',
                           'Belok', 'Sorlak', 'Grildorren', 'Falaur', 'Tildor', 'Durj',
                           'Morgenor', 'Talgram', 'Teldanoth', 'Linmat', 'Worcon',
                           'Hahrmon', 'Kardon', 'Corbrath', 'Willentor', 'Weggard',
                           'Norrikon', 'Fellbrion', 'Sajanus', 'Qorrat', 'Sorenmir',
                           'Kraw', 'Kullador', 'Qardrommir', 'Wiltendorn', 'Valwark',
                           'Morluk']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        boss_monster = monster_cls()
        first_name = random.choice(rndm_boss_names)
        boss_monster.proper_name = f"{first_name} the Elite {boss_monster.name}"
        boss_monster.hit_points = math.ceil(boss_monster.hit_points * 1.5)
        boss_monster.experience_award = math.ceil(boss_monster.experience_award * 1.5)
        boss_monster.strength += 2
        boss_monster.dexterity += 2
        boss_monster.constitution += 2
        boss_monster.intelligence += 2
        boss_monster.wisdom += 2
        boss_monster.charisma += 2
        boss_monster.armor_class += 2
        boss_monster.dot_multiplier = self.proficiency_bonus
        boss_monster.experience_award = 350 * self.level
        boss_monster.weapon_bonus = math.ceil(self.level * 1.5)
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"Before you stands {boss_monster.proper_name}!")
        return boss_monster

    def regular_monster_generator(self):
        # called from meta_monster_generator() if encounter < 11
        maximum_level = self.level  # (self.level + 1) makes it too hard
        minimum_level = 1

        if self.level > 2:
            minimum_level = (self.level - 2)  # this should keep it more challenging and fun

        regular_monster_key = random.randint(minimum_level, maximum_level)

        if self.encounter == 1:  # beta 5% chance of running into monsters that are +1 level to keep it challenging

            if self.level < 20:
                regular_monster_key = (self.level + 1)

            else:
                regular_monster_key = self.level

        regular_monster_cls = random.choice(monster_dict[regular_monster_key])
        regular_monster = regular_monster_cls()
        return regular_monster

    def undead_prophet_generator(self):
        # called from meta_monster_generator(), if encounter == 97
        rndm_prophet_names = ['Tacium', 'Amarrik', 'Arynd', 'Beldonnor', 'Forrg',
                              'Sambressorr', 'Jornav', 'Tyrnenn', 'Fenlor', 'Yagoddish', 'Borell',
                              'Ehrnador', 'Thaymorro', 'Gorrel', 'Aureor', 'Linus', 'Mattheus',
                              'Hahrus', 'Astorem', 'Chardast', 'Brendorin', 'Meradorn',
                              'Gorrikor', 'Nannukis', 'Torrolom', 'Ornelius', 'Geffenmor',
                              'Jorrbrialus', 'Koffengen', 'Jyrus', 'Jybrius', 'Tyrrendor',
                              'Forendilus']
        rndm_epithets = ['of the Evil Wisdom', 'the Lesser', 'the Elder', 'the Fierce', 'of the Eleven Elders',
                         'of the Twelve', 'of the Fell Elders', 'the Mad', 'the Blasphemous',
                         'of the Elders', 'the Fallen', 'the Insane', 'the Mad Magistrate',
                         'the Grand King-Priest', 'of the Seven Mages', 'the Bloodsoaked',
                         'the Accursed', 'the Abandoned', 'the Absolutionist', 'the Avenger', 'of the Seven Horns',
                         'the Blackhearted', 'the Blind', 'the Bloodthirsty', 'the Cruel',
                         'the Damned', 'the Foul', 'the Foulest', 'the Feared', 'the Fear-Inspiring'
                         ]

        undead_prophet = random.choice(undead_prophet_list)
        name = random.choice(rndm_prophet_names)
        epithet = random.choice(rndm_epithets)
        undead_prophet.proper_name = f"{name} {epithet}"
        undead_prophet.hit_points = math.ceil(self.maximum_hit_points * 1.5)
        undead_prophet.level = self.level
        undead_prophet.number_of_hd = self.level
        undead_prophet.weapon_bonus = self.wielded_weapon.damage_bonus
        undead_prophet.dot_multiplier = self.proficiency_bonus
        undead_prophet.experience_award = 350 * self.level

        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"The undead prophet, {name} {epithet} returns!")
        return undead_prophet

    def exit_boss_generator(self):
        # called from meta_monster_generator(), if encounter == 99
        rndm_boss_names = ['Gwarlek', 'Srentor', 'Borrnol', 'Sentollor', 'Morluk',
                           'Twinbelor', 'Sornog', 'Grenyor', 'Fallraur', 'Timboth', 'Surj',
                           'Morozzor', 'Tharbor', 'Tenbrok', 'Lorrius', 'Filwor',
                           'Hahrmon', 'Kardon', 'Corbrin', 'Billentor', 'Weggard',
                           'Norrus', 'Fellbrion', 'Sajanus', 'Qorag', 'Sorenmor',
                           'Kraw', 'Kullador', 'Qendor', 'Willenbor', 'Valwar',
                           'Moonror']

        # just in case I forget to make level 21 monsters.
        if self.level < 20:
            monster_key = (self.level + 1)
        else:
            monster_key = self.level
        monster_cls = random.choice(monster_dict[monster_key])
        exit_boss = monster_cls()
        exit_boss.hit_points = math.ceil(exit_boss.hit_points * 1.25)
        first_name = random.choice(rndm_boss_names)
        exit_boss.proper_name = f"{first_name} the Elite {exit_boss.name} guardian"
        # exit_boss.hit_points = math.ceil(self.maximum_hit_points * 1.5)
        exit_boss.level = self.level
        exit_boss.number_of_hd = self.level
        exit_boss.dot_multiplier = self.dungeon.level
        exit_boss.experience_award = 350 * self.level
        exit_boss.weapon_bonus = self.wielded_weapon.damage_bonus

        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"In the archway to the staircase leading down to {self.dungeon.name} "
              f"stands {exit_boss.proper_name}!\n"
              f"Without fear, without thought, the guardian looks upon you and readies itself for battle...")
        return exit_boss

    def king_monster_generator(self):
        # called from meta_monster_generator(), if encounter == 98
        rndm_king_names = ['Tartyrtum', 'Amarrok', 'Aaryn', 'Baldrick', 'Farrendal',
                           'Dinenlell', 'Jorn', 'Tyrne', 'Fen', 'Jagod', 'Bevel',
                           'Elrik', 'Thayadore', 'Grummthel', 'Aureus', 'Sylgor',
                           'Hahr', 'Astor', 'Cordast', 'Breckenborn', 'Megarrd',
                           'Gorrik', 'Nannuk', 'Borrodred', 'Metalbeard', 'Geffen',
                           'Jortindale', 'Koffgen', 'Tyrus', 'Tybrius', 'Tyr',
                           'Hammersthorn']
        rndm_epithets = ['the Wise', 'the Lesser', 'the Elder', 'the Fierce', 'of the Eleven', 'of the Twelve',
                         'of the Elders', 'the Brave', 'the Insane', 'the Great', 'the Grand Magistrate',
                         'the Grand King-Priest', 'of the Seven Riddles', 'the Strong', 'the Able', 'the Bloodsoaked',
                         'the Accursed', 'the Abandoned', 'the Absolutist', 'the Avenger', 'the Battle-weary',
                         'the Blackhearted', 'the Blind', 'the Bloodthirsty', 'the Conqueror', 'the Cruel',
                         'the Crusader', 'the Damned'
                         ]

        king_monster = random.choice(king_boss_list)
        name = random.choice(rndm_king_names)
        epithet = random.choice(rndm_epithets)
        king_monster.proper_name = f"{name} {epithet}"
        king_monster.hit_points = math.ceil(self.maximum_hit_points * 1.25)
        king_monster.level = self.level
        king_monster.number_of_hd = self.level
        king_monster.weapon_bonus = self.wielded_weapon.damage_bonus
        king_monster.dot_multiplier = self.dungeon.level
        king_monster.experience_award = 350 * self.level
        self.hud()  # this clears the screen at a convenient point, so that the automatic description is removed
        print(f"The undead King {king_monster.proper_name} returns!")
        return king_monster

    def monster_likes_you(self, monster):
        # called from main loop after encounter with regular monster
        if dice_roll(1, 20) > 19 and monster.intelligence > 12 and monster.charisma > 14 and self.charisma > 10:
            print(f"The {monster.name} likes you!")
            sleep(1)
            upgradeable = True

            while upgradeable:

                if self.armor.ac < 18 or self.shield.ac < 3 or self.wielded_weapon.damage_bonus < 15 or \
                        self.wielded_weapon.to_hit_bonus < 6 or self.boots.ac < 3 \
                        or self.hit_points < self.maximum_hit_points:
                    upgradeable = True

                else:
                    upgradeable = False

                if not upgradeable:
                    gold_gift = random.randint(100, 5000)
                    print(f"{monster.he_she_it.capitalize()} gives you {gold_gift} GP!")
                    self.gold += gold_gift
                    pause()
                    return True

                gift_item = dice_roll(1, 6)

                if gift_item == 1:
                    if self.armor.ac < 18:
                        if self.armor.name != padded_armor.name:
                            self.armor.ac += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.armor.name} "
                                  f"to AC {self.armor.ac}!")
                        else:
                            self.armor = leather_armor
                            print(f"{monster.he_she_it.capitalize()} gives you {self.armor.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 2:
                    if self.shield.ac < 3:
                        if self.shield.name != no_shield.name:
                            self.shield.ac += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.shield.name} "
                                  f"to AC {self.shield.ac}!")
                        else:
                            self.shield = buckler
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.shield.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 3:
                    if self.wielded_weapon.damage_bonus < 15:
                        if self.wielded_weapon.name != short_sword.name:
                            self.wielded_weapon.damage_bonus += 1
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.wielded_weapon.name} "
                                  f"damage bonus to + "
                                  f"{self.wielded_weapon.damage_bonus}!")
                            pause()
                            return True
                        else:
                            self.wielded_weapon = broad_sword
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.wielded_weapon.name}!")
                            pause()
                            return True
                    else:
                        continue

                if gift_item == 4:
                    if self.wielded_weapon.to_hit_bonus < 6:
                        if self.wielded_weapon.name != short_sword.name:
                            self.wielded_weapon.to_hit_bonus += 1
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.wielded_weapon.name} "
                                  f"to-hit bonus to + "
                                  f"{self.wielded_weapon.to_hit_bonus}!")
                            pause()
                            return True
                        else:
                            self.wielded_weapon = broad_sword
                            print(f"{monster.he_she_it.capitalize()} gives you a {self.wielded_weapon.name}!")
                            pause()
                            return True
                    else:
                        continue

                if gift_item == 5:
                    if self.boots.ac < 3:
                        if self.boots.name != leather_boots.name:
                            self.boots.ac += 1
                            self.calculate_armor_class()
                            print(f"{monster.he_she_it.capitalize()} enhances your {self.boots.name} "
                                  f"to AC {self.boots.ac}!")
                        else:
                            self.boots = elven_boots
                            print(f"{monster.he_she_it.capitalize()} gives you a pair of {self.boots.name}!")
                            self.calculate_armor_class()
                        pause()
                        return True
                    else:
                        continue

                if gift_item == 6:
                    if self.hit_points < self.maximum_hit_points:
                        self.hit_points = self.maximum_hit_points
                        print(f"{monster.he_she_it.capitalize()} heals you to full strength!")
                        pause()
                        return True
                    else:
                        continue

        else:
            return False

    def quick_move(self, monster):
        # called from main loop
        self.hud()
        quick_move_roll = dice_roll(1, 20)  # - self.stealth
        if quick_move_roll == 20:
            print(f"The {monster.name} makes a quick move...")
            sleep(1.5)
            # pack inventory logic:
            pack_item_types_to_steal = []
            belt_item_types_to_steal = [self.potions_of_strength, self.potions_of_healing,
                                        self.town_portals, self.elixirs, self.antidotes]
            for i in self.pack.keys():  # gather all available
                if len(self.pack[i]) > 0:  # item types to steal based on player's current item TYPES and put them
                    pack_item_types_to_steal.append(i)  # in available_item_types_to_steal = []

            if len(pack_item_types_to_steal) > 0:
                item_type = random.choice(pack_item_types_to_steal)  # Get random item *TYPE* you want to "steal"
                if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type" in their pack
                    # pop random item from that item type. -1 because indexes start at 0
                    stolen_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                    print(f"{monster.he_she_it.capitalize()} steals the {stolen_item.name}"
                          f"from your pack!")
                    pause()
                    return True  # True means monster gets away clean

            # if pack is empty, the thief moves to the belt.
            # Belt inventory is handled differently.
            # belt inventory logic:
            elif sum(belt_item_types_to_steal) > 0:
                item_string = ""
                # Define list of attributes you are allowed to change
                self_dict = self.__dict__  # create self_dict variable as actual copy of player dict attribute
                stealing_lst = []
                # the working dict and 'for' loop just takes the place of many 'if:' statements
                working_dict = {'potions_of_strength': self.potions_of_strength,
                                'potions_of_healing': self.potions_of_healing,
                                'town_portals': self.town_portals, 'elixirs': self.elixirs,
                                'antidotes': self.antidotes}
                # add all items > 0 in working dict to stealing list
                for key, value in working_dict.items():
                    if value > 0:
                        stealing_lst.append(key)
                random_stolen_item = random.choice(stealing_lst)
                # I am proud of this next bit of code :)
                grammar_dict = {'potions_of_strength': 'potion of strength',
                                'potions_of_healing': 'potion of healing',
                                'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir',
                                'antidotes': 'vial of antidote'}
                for key, value in grammar_dict.items():
                    if random_stolen_item == key:
                        item_string = value
                print(f"{monster.he_she_it.capitalize()} steals a {item_string} right off of your belt!")
                self_dict[random_stolen_item] -= 1
                pause()
                return True  # True means monster gets away clean
            else:
                print(f"You have nothing {monster.he_she_it} wants to steal!")
                pause()
                # sleep(2)
                return True  # Changing this to False means your inventory is empty and monster sticks around to fight
        else:
            return False  # False here means monster failed check, and he sticks around to fight; invisible to player

    def reduce_health(self, damage):
        # called from main loop after monster does damage to human player
        self.hit_points -= damage
        # if self.hit_points < 0:  # restore after testing
        #    self.hit_points = 0  # restore after testing
        return

    def check_dead(self):
        # called from main loop after damage and calculations
        # I am proud of this code...it was very difficult for me and took many hours
        if self.hit_points > 0:
            return False
        else:
            self.hud()
            if self.necrotic and self.poisoned:
                print(f"You are necrotic, poisoned, unconscious and moribund!")
            elif self.necrotic:
                print(f"You are necrotic, unconscious and moribund!")
            elif self.poisoned:
                print(f"You are poisoned, unconscious and moribund!")
            else:
                print(f"You are unconscious and moribund!")
            sleep(1)
            print(f"Death saving throw!")
            sleep(1)
            successes = 0
            fails = 0
            attempt = 0
            while successes < 3 or fails < 3:
                if successes == 3:
                    print(f"You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False  # player is NOT dead
                if fails >= 3:
                    print(f"Death saving throw failed!")
                    sleep(1)
                    return True  # player IS dead
                death_save = dice_roll(1, 20)
                attempt += 1
                print(f"Attempt {attempt}: {death_save}")
                sleep(1)
                if death_save == 20:
                    print(f"20 Roll! You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False  # player is NOT dead
                if death_save > 9:
                    successes += 1
                    if successes == 1:
                        print(f"{successes} Successful save..")
                    else:
                        print(f"{successes} Successful saves..")
                    sleep(1)
                if 10 > death_save > 1:
                    fails += 1
                    if fails == 1:
                        print(f"{fails} Failed save..")
                    else:
                        print(f"{fails} Failed saves..")
                    sleep(1)
                if death_save == 1:
                    fails += 2
                    print(f"Rolling a 1 adds 2 failed saves. ")
                    print(f"{fails} Failed saves..")
                    sleep(1)
            return True  # player IS dead

    def initiative(self, monster):
        # called from main loop after encountering monster
        self.hud()
        if self.level > 6:
            player_initiative = dice_roll(1, 20) + self.dexterity_modifier + self.proficiency_bonus
        else:
            player_initiative = dice_roll(1, 20) + self.dexterity_modifier
        if monster.level > 6:  # beta testing
            monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier + monster.proficiency_bonus
        else:
            monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier
        print(f"Your initiative: {player_initiative}\n{monster.name} initiative: {monster_initiative}")
        pause()
        if player_initiative >= monster_initiative:
            return True
        else:
            return False

    def melee(self, monster_name, monster_armor_class):
        # called from main loop if player chooses to (F)ight
        strength_bonus = 1
        if self.potion_of_strength_effect:
            strength_bonus = 1.33  # round(self.strength * .5)
        if self.quantum_strength_effect:
            strength_bonus = 2
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"You strike at the {monster_name}..")
        print(f"Melee Attack Roll: {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You awkwardly strike.")
            sleep(1)
            print(f"You miss..")
            pause()
            self.hud()
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"

        else:
            critical_bonus = 1
            hit_statement = "You hit!"
        print(f"Dexterity modifier {self.dexterity_modifier}\nProficiency bonus {self.proficiency_bonus}")
        if self.wielded_weapon.to_hit_bonus > 0:
            print(f"Weapon to hit bonus {self.wielded_weapon.to_hit_bonus}")
        roll_total = roll_d20 + self.proficiency_bonus + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus
        print(f"Your Total Attack Roll: {roll_total}")
        print(f"Monster armor class {monster_armor_class}")
        if roll_d20 == 20 or roll_d20 + self.proficiency_bonus + \
                self.dexterity_modifier + self.wielded_weapon.to_hit_bonus >= monster_armor_class:
            damage_roll = dice_roll((self.level * critical_bonus), self.hit_dice)
            damage_to_opponent = math.ceil(
                (damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus) * strength_bonus)
            if damage_to_opponent > 0:
                print(hit_statement)
                sleep(1)
                print(f"{self.level * critical_bonus}d{self.hit_dice} Damage Roll: {damage_roll}\n"
                      f"Strength modifier: {self.strength_modifier}")
                if self.wielded_weapon.damage_bonus > 0:
                    print(f"Weapon bonus: {self.wielded_weapon.damage_bonus}")
                if strength_bonus > 1:
                    print(f"* Strength Bonus: {strength_bonus}")
                print(f"Your Damage Total: {damage_to_opponent}")
                print(f"You do {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"Your attack is barely effective. You manage 1 point of damage.")  # zero damage result
                sleep(1)
                return 1
        elif self.extra_attack:  # self.level > 4
            print("You missed..")
            sleep(2)
            print("Extra Attack Skill chance to hit!")
            sleep(2)
            roll_d20 = dice_roll(1, 20)
            if roll_d20 == 20 or roll_d20 + self.proficiency_bonus + self.dexterity_modifier + \
                    self.wielded_weapon.to_hit_bonus >= monster_armor_class:
                damage_roll = dice_roll(self.level, self.hit_dice)
                damage_to_opponent = \
                    math.ceil((damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus)
                              * strength_bonus)
                print(f"You attack again for {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print("You miss again.")
                pause()
                self.hud()
                return 0
        else:
            print(f"You missed...")
            pause()
            self.hud()
            return 0

    def npc_melee(self, ally, monster_name, monster_armor_class):
        # called from npc_attack_logic() for npcs who use melee
        pronoun = 'his'
        if ally.name == "Si'Kira":
            pronoun = 'her'
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"{ally.name} strikes at the {monster_name} with {pronoun} {ally.wielded_weapon.name}..")
        print(f"Attack Roll: {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print(f"{ally.name} misses..")
            pause()
            self.hud()
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"
        else:
            critical_bonus = 1
            hit_statement = f"{ally.name} HITS!"
        print(f"Dexterity modifier {ally.dexterity_modifier}\nProficiency bonus {ally.proficiency_bonus}")
        if ally.wielded_weapon.to_hit_bonus > 0:
            print(f"Weapon to hit bonus {ally.wielded_weapon.to_hit_bonus}")
        roll_total = roll_d20 + ally.proficiency_bonus + ally.dexterity_modifier + ally.wielded_weapon.to_hit_bonus
        print(f"{ally.name} Total Attack Roll: {roll_total}")
        print(f"Monster armor class {monster_armor_class}")
        if roll_d20 == 20 or roll_d20 + ally.proficiency_bonus + \
                ally.dexterity_modifier + ally.wielded_weapon.to_hit_bonus >= monster_armor_class:
            damage_roll = dice_roll((ally.level * critical_bonus), ally.hit_dice)
            damage_to_opponent = math.ceil((damage_roll + ally.strength_modifier + ally.wielded_weapon.damage_bonus)
                                           * ally.strength_bonus)
            if damage_to_opponent > 0:
                print(hit_statement)
                sleep(1)
                print(f"{ally.level * critical_bonus}d{ally.hit_dice} Damage Roll: {damage_roll}\n"
                      f"Strength modifier: {ally.strength_modifier}")
                if ally.wielded_weapon.damage_bonus > 0:
                    print(f"Weapon bonus: {ally.wielded_weapon.damage_bonus}")
                if ally.strength_bonus > 1:
                    print(f"* Strength Bonus: {ally.strength_bonus}")
                print(f"{ally.name} Total Damage: {damage_to_opponent}")
                print(f"{ally.name} does {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"{ally.name}'s attack is barely effective. It does 1 point of damage.")  # zero damage result
                sleep(1)
                return 1
        elif ally.level > 4:
            print(f"{ally.name} missed..")
            sleep(2)
            print("Extra Attack Skill chance to hit!")
            sleep(2)
            roll_d20 = dice_roll(1, 20)
            if roll_d20 == 20 or roll_d20 + ally.proficiency_bonus + ally.dexterity_modifier + \
                    ally.wielded_weapon.to_hit_bonus >= monster_armor_class:
                damage_roll = dice_roll(ally.level, ally.hit_dice)
                damage_to_opponent = \
                    math.ceil((
                        damage_roll + ally.strength_modifier + ally.wielded_weapon.damage_bonus) * ally.strength_bonus)
                print(f"{ally.name} attacks again for {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"{ally.name} misses again.")
                pause()
                self.hud()
                return 0
        else:
            print(f"{ally.name}missed...")
            pause()
            self.hud()
            return 0

    def turn_undead(self, monster):
        # monster must make wisdom saving throw or be turned away
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            print(f"Turn Undead")
            sleep(1)
            self.hud()
            if "Turn Undead" not in monster.immunities and "All" not in monster.immunities and monster.undead:
                vulnerability_modifier = 0
                if "Turn Undead" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Turn Undead" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + \
                    self.wisdom_modifier + vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Saving Throw: {monster_roll}")
                # monster_mod = math.floor((monster.wisdom - 10) / 2)
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc > monster_total:  # with >= tie goes to player... with > tie goes to monster
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    # print(f"The {monster.name} runs in fear!!")
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} runs in fear!!")
                    else:
                        print(f"The {monster.name} runs in fear!!")
                    sleep(1.5)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} listens with deaf ears..")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Turn Undead!!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Turn Undead!!")
                        sleep(1)
                else:
                    print(f"Turn Undead is only effective against undead creatures!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Turn Undead is a Battle Effect only!")
            sleep(1)
            return

    def banish(self, monster):
        # monster must make a successful charisma saving throw or be banished from existence on this plane
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            print(f"Banish")
            sleep(1)
            self.hud()
            if "Banish" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Banish" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Banish" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Saving Throw: {monster_roll}")
                monster_charisma_modifier = math.floor((monster.charisma - 10) / 2)
                print(f"{monster.name} Charisma Modifier: {monster_charisma_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster_charisma_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.hud()
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    print(f"BE GONE!!")
                    sleep(1)
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} phases out of existence on this plane!!")
                    else:
                        print(f"The {monster.name} phases out of existence on this plane!!!!")
                    sleep(1)
                    print(f"You perceive a slight breeze as the air "
                          f"around you collapses into the brief void left behind..")
                    sleep(2)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is unfazed by your attempts!!")
                    else:
                        print(f"The {monster.name} is unfazed by your attempts!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Banish!!")
                else:
                    print(f"The {monster.name} is immune to Banish!!")
                sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Banish is a Battle Effect only!")
            sleep(1)
            return

    def fear(self, monster):
        # player wisdom vs monster wisdom. only works on living
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            print(f"Fear.")
            sleep(1)
            self.hud()
            if "Fear" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Fear" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Fear" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Saving Throw: {monster_roll}")
                # monster_mod = math.floor((monster.wisdom - 10) / 2)
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:  # with >= tie goes to player... with > tie goes to monster
                    self.quantum_units -= quantum_unit_cost
                    self.in_proximity_to_monster = False
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} runs in fear!!")
                    else:
                        print(f"The {monster.name} runs in fear!!")
                    sleep(1.5)
                    monster.gold = 0
                    # pause()
                    return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} ignores your wiles!!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if not monster.undead:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Fear!!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Fear!!")
                        sleep(1)
                else:
                    print(f"Fear is only effective against the living!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Turn Undead is a Battle Effect only!")
            sleep(1)
            return

    def quantum_purify(self, monster):
        # cures poisoned and necrotic condition
        # works only when poisoned or necrotic, but once engaged, also has powerful hit point healing!
        if monster is None:
            print(f"Purify")
        else:
            print(f"Purify (BATTLE)")
        sleep(1)
        quantum_unit_cost = 2
        self.hud()
        if not self.poisoned and not self.necrotic:
            print(f"Your flesh is not corrupted!")
            sleep(1)
            return 0
        else:
            print(f"You quiet your mind and grasp at the elusive Quantum Knowledge...")
            sleep(1)
            self.quantum_units -= quantum_unit_cost
            self.hud()
            print(f"You feel a cleansing of the flesh..")
            sleep(1)
            self.poisoned = False
            self.poisoned_turns = 0
            self.necrotic = False
            self.necrotic_turns = 0
            print(f"The foul corruption leaves your body..")
            sleep(1)
            if self.hit_points < self.maximum_hit_points:
                # number_of_dice = (3 + self.level)  # consider changing to self.quantum_level
                # heal = dice_roll(number_of_dice, 4) + number_of_dice + self.quantum_level
                if self.quantum_level < 3:
                    heal = math.ceil(self.maximum_hit_points * .66)
                else:
                    heal = math.ceil(self.maximum_hit_points * .75)
                print(f"You heal {heal} hit points")  # remove after testing
                self.hit_points += heal
                if self.hit_points > self.maximum_hit_points:
                    self.hit_points = self.maximum_hit_points
                # self.hud()
                print(f"Your wounds feel better!")
                sleep(1)
            pause()
            return 0

    def flesh_to_stone(self, monster):
        # like sleep and charm, but always successful.
        # player has 1 free crit, thereafter monster must pass Constitution saving throw
        # 2 failed saves after initial attack = permanent petrification for monster.
        # player gets exp reward, but no gold or loot
        quantum_unit_cost = 4
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            print(f"Flesh to Stone")
            sleep(1)
            self.hud()
            if "Flesh to Stone" not in monster.immunities and "All" not in monster.immunities:
                self.quantum_units -= quantum_unit_cost
                if "Flesh to Stone" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Flesh to Stone" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                print(f"Before the {monster.name} even realizes what is happening, its flesh ripples into a stone "
                      f"replica of its normal state!")
                sleep(1)
                input(f"Press (ENTER) to attack: ")
                self.hud()
                print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                sleep(1.5)
                damage_modifier = 2
                if "Flesh to Stone" in monster.vulnerabilities:
                    damage_modifier = 3
                # if "Flesh to Stone" in monster.resistances or "All" in monster.resistances:
                #    damage_modifier = 1
                total_fails = 0
                while True:
                    self.hud()
                    damage_to_monster = dice_roll((self.level * damage_modifier), self.hit_dice)
                    total_fails += 1
                    print(f"You inflict {damage_to_monster} hit points!")
                    pause()
                    self.hud()
                    monster.reduce_health(damage_to_monster)
                    if not monster.check_dead():
                        level_advantage = 0
                        if self.level > monster.level:
                            level_advantage = self.level - monster.level
                        player_dc = self.base_dc + self.proficiency_bonus + \
                            self.wisdom_modifier + vulnerability_modifier + level_advantage
                        print(f"Player base DC = {self.base_dc}\n"
                              f"Wisdom Modifier: {self.wisdom_modifier}\n"
                              f"Proficiency Bonus: {self.proficiency_bonus}")
                        if vulnerability_modifier != 0:
                            print(f"+ Monster Vulnerability Modifier: {vulnerability_modifier}")
                        if level_advantage > 0:
                            print(f"+ Level Advantage: {level_advantage}")
                        sleep(1)
                        print(f"DC Total: {player_dc}")
                        sleep(1)
                        monster_saving_throw = dice_roll(1, 20)
                        monster_total = monster_saving_throw + monster.constitution_modifier + resistance_modifier
                        print(f"Monster saving throw: {monster_saving_throw}")
                        sleep(1)
                        print(f"Monster Constitution Modifier: {monster.constitution_modifier}")
                        if resistance_modifier != 0:
                            print(f"Monster Resistance Modifier: {resistance_modifier}")
                        sleep(1)
                        print(f"Total: {monster_total}")
                        sleep(1)

                        if monster_total >= player_dc:  # dnd
                            print(f"The {monster.name} is restored!")
                            pause()
                            return 0  # no damage sent back because already sent to monster.reduce_health()
                        else:
                            if total_fails == 3:
                                print(f"The {monster.name} forever succumbs to the petrification of stone!")
                                sleep(1)
                                print(f"You are victorious!")
                                sleep(1)
                                self.in_proximity_to_monster = False  # monster is gone. no loot.
                                monster.gold = 0  # gold has been turned to stone
                                return 0
                            else:
                                print(f"It remains stone-petrified!")
                                sleep(1)
                                print(f"You attack again!")
                                sleep(1.5)
                                continue
                    else:
                        print(f"You have vanquished the {monster.name}!")
                        sleep(1)
                        monster.gold = 0  # gold has been turned to stone
                        self.in_proximity_to_monster = False  # monster is stone, no loot.
                        return 0  # no damage sent to main
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Flesh to Stone Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Flesh to Stone Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Flesh to Stone is a Battle Effect only!")
            sleep(1)
            return

    def gravity_well(self, monster):
        # like sleep and charm, but always successful.
        # initial damage is rolled and then player has 1 free crit,
        # thereafter monster must pass strength saving throw
        # player gets exp reward, but no gold or loot
        quantum_unit_cost = 5
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            print(f"Gravity Well")
            sleep(1)
            self.hud()
            if "Gravity Well" not in monster.immunities and "All" not in monster.immunities:
                self.quantum_units -= quantum_unit_cost
                if "Gravity Well" in monster.vulnerabilities:
                    vulnerability_modifier = 5

                print(f"Focusing the Quantum Weirdness on the ground beneath the {monster.name}, "
                      f"a growing void of crushing gravity opens between worlds!!")
                sleep(1)
                print(f"It is pulled in by the insatiable force!")
                sleep(1)
                initial_damage = dice_roll(10, 10)
                print(f"The aberrant void inflicts {initial_damage} hit points!")
                sleep(1.5)
                pause()
                monster.reduce_health(initial_damage)
                if not monster.check_dead():
                    damage_modifier = 3
                    if "Gravity Well" in monster.vulnerabilities:
                        damage_modifier = 4
                    if "Gravity Well" in monster.resistances or "All" in monster.resistances:
                        damage_modifier = 1
                    # total_fails = 0
                    while True:
                        self.hud()
                        print(f"The {monster.name} remains trapped in the gravity well!")
                        sleep(1)
                        input(f"Press (ENTER) to attack: ")
                        self.hud()
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        damage_to_monster = dice_roll((self.level * damage_modifier), self.hit_dice)
                        # total_fails += 1
                        print(f"You inflict {damage_to_monster} hit points!")
                        sleep(1.5)
                        self.hud()
                        monster.reduce_health(damage_to_monster)
                        if not monster.check_dead():
                            level_advantage = 0
                            if self.level > monster.level:
                                level_advantage = self.level - monster.level
                            player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                                vulnerability_modifier + level_advantage
                            print(f"Player base DC = {self.base_dc}\n"
                                  f"Wisdom Modifier: {self.wisdom_modifier}\n"
                                  f"Proficiency Bonus: {self.proficiency_bonus}")
                            if vulnerability_modifier != 0:
                                print(f"+ Monster Vulnerability Modifier: {vulnerability_modifier}")
                            if level_advantage > 0:
                                print(f"+ Level Advantage: {level_advantage}")
                            sleep(1)
                            print(f"DC Total: {player_dc}")
                            sleep(1)
                            monster_saving_throw = dice_roll(1, 20)
                            monster_total = monster_saving_throw + monster.strength_modifier
                            print(f"Monster saving throw: {monster_saving_throw}")
                            sleep(1)
                            print(f"Monster Strength Modifier: {monster.strength_modifier}")
                            sleep(1)
                            print(f"Total: {monster_total}")
                            sleep(1)

                            if monster_total >= player_dc:  # dnd
                                print(f"The {monster.name} breaks out of the gravitational hold!")
                                pause()
                                return 0  # no damage sent back because already sent to monster.reduce_health()
                            else:
                                print(f"It attempts to break free!")
                                sleep(1)
                                print(f"It is pulled back in!")
                                sleep(1.5)
                                continue

                        else:
                            print(f"You have vanquished the {monster.name}!")
                            sleep(1)
                            monster.gold = 0  # gold has been lost to the void
                            self.in_proximity_to_monster = False  # monster is gone, no loot.
                            return 0  # no damage sent to main

                else:
                    print(f"You have vanquished the {monster.name}!")
                    sleep(1)
                    monster.gold = 0  # gold has been lost to the void
                    self.in_proximity_to_monster = False  # monster is gone, no loot.
                    return 0  # no damage sent to main
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Gravity Well Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Gravity Well Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Gravity Well is a Battle Effect only!")
            sleep(1)
            return

    def hold_monster(self, monster):
        # like sleep and charm, but pits player wisdom against monster strength
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            print(f"Hold Monster")
            sleep(1)
            self.hud()
            if "Hold Monster" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Hold Monster" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Hold Monster" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                # turn_roll = dice_roll(1, 20)
                # player_total = (turn_roll + self.wisdom_modifier + self.proficiency_bonus + vulnerability_modifier)
                # The difficulty class ("DC") of the saving throw should be based on the caster:
                # 8 + proficiency bonus + casting ability modifier.
                # The GM rolls a d20 on behalf of the monster, adds the appropriate saving modifier based on
                # the monster's stats, and compares to the spellcaster's save DC.
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"{monster.name} Strength Modifier: {monster.strength_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.strength_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc > monster_total:
                    self.quantum_units -= quantum_unit_cost  # level 3 effect. uses 3 units
                    print(f"The {monster.name} is held fast by Quantum Forces!")
                    sleep(1)
                    input(f"Press (ENTER) to attack: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= difficulty_class:  #
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        #
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It has broken free!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} resists!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Hold Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Hold Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Hold Monster is a Battle Effect only!")
            sleep(1)
            return

    def quantum_web(self, monster):
        # web is a match of player's intuition as reflected by wisdom, vs the monster's ability to dodge
        # a web that is shooting toward it.
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            print(f"Web")
            sleep(1)
            self.hud()
            if "Web" not in monster.immunities and "All" not in monster.immunities:
                vulnerability_modifier = 0
                if "Web" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Web" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                # turn_roll = dice_roll(1, 20)
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + vulnerability_modifier)
                # print(f"Quantum Ability Check: {turn_roll}")
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                sleep(1)
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Dexterity Saving Throw: {monster_roll}")
                print(f"{monster.name} Dexterity Modifier: {monster.dexterity_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.dexterity_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_total >= monster_total:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} is webbed..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    sleeping_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {sleeping_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll > sleeping_difficulty_class:  #
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        # pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It broke free!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
                    print(f"The {monster.name} dodges!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Quantum Web Effect!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Quantum Web Effect!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Web is a Battle Effect only!")
            sleep(1)
            return

    def quantum_charm(self, monster):
        # Charm matches the player's Charisma vs the monster's wisdom;
        # your power of persuasion vs their perception
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            print(f"Charm")
            sleep(1)
            self.hud()
            if "Charm" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Charm" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Charm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                # turn_roll = dice_roll(1, 20)
                # total = (turn_roll + self.charisma_modifier + self.proficiency_bonus + vulnerability_modifier)
                # print(f"Quantum Ability Check: {turn_roll}\nCharisma Modifier: {self.charisma_modifier}\n"
                #      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier > 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.charisma_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Charisma Modifier: {self.charisma_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier != 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"{monster.name} Wisdom Modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is charmed..")
                    else:
                        print(f"The {monster.name} is charmed..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    charm_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {charm_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= charm_difficulty_class:
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        # pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It breaks free from your charm and comes to its senses!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is not persuaded by your charms!")
                    else:
                        print(f"The {monster.name} is not persuaded by your charms!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    print(f"The undead ignore your wiles!!")
                    sleep(1)
                else:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to being charmed!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to being charmed!")
                        sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Charm is a Battle Effect only!")
            sleep(1)
            return

    def quantum_sleep(self, monster):
        # sleep matches the player's intelligence vs the monster's wisdom;
        # your knowledge of quantum nature vs their perception
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            print(f"Sleep")
            sleep(1)
            self.hud()
            if "Sleep" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerability_modifier = 0
                if "Sleep" in monster.vulnerabilities:
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Sleep" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                # turn_roll = dice_roll(1, 20)
                # total = (turn_roll + self.intelligence_modifier + self.proficiency_bonus + vulnerability_modifier)
                # print(f"Quantum Ability Check: {turn_roll}\nIntelligence Modifier: {self.intelligence_modifier}\n"
                #      f"Proficiency Bonus: {self.proficiency_bonus}")
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.intelligence_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Intelligence Modifier: {self.intelligence_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerability_modifier > 0:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                print(f"Monster Roll: {monster_roll}")
                monster_total = monster_roll + monster.wisdom_modifier + resistance_modifier
                print(f"{monster.name} Wisdom modifier: {monster.wisdom_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:
                    self.quantum_units -= quantum_unit_cost
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is sleeping..")
                    else:
                        print(f"The {monster.name} is sleeping..")
                    sleep(1)
                    input(f"Press (ENTER) to vanquish: ")
                    self.hud()
                    finishing_move_roll = dice_roll(1, 20) + self.wielded_weapon.to_hit_bonus + self.dexterity_modifier
                    sleeping_difficulty_class = monster.armor_class
                    print(f"1d20 roll: {finishing_move_roll}")  # remove after testing ?
                    print(f"Difficulty Class: {sleeping_difficulty_class}")  # remove after testing ?
                    if finishing_move_roll >= sleeping_difficulty_class:
                        print(f"You raise your {self.wielded_weapon.name} and swing mightily..")
                        sleep(1.5)
                        pause()
                        return monster.hit_points  # return the total amount of monster hp, effectively killing it
                    else:
                        print(f"It woke up!!")
                        pause()
                        return 0
                else:
                    self.quantum_units -= quantum_unit_cost
                    print(f"The {monster.name} isn't sleepy!")
                    sleep(1)
                    pause()
                    return 0
            else:
                if monster.undead:
                    print(f"Undead do not sleep!!")
                    sleep(1)
                else:
                    if monster.proper_name != "None":
                        print(f"{monster.proper_name} is immune to Quantum Sleep!")
                        sleep(1)
                    else:
                        print(f"The {monster.name} is immune to Quantum Sleep!")
                        sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Sleep is a Battle Effect only!")
            sleep(1)
            return

    def quantum_strength(self, monster):
        # heal to full strength and get *2 melee damage multiplier (defined in melee())
        if monster is None:
            print(f"Quantum Strength")
        else:
            print(f"Quantum Strength (BATTLE)")
        sleep(1)
        self.hud()
        quantum_unit_cost = 2
        rndm_phrases = [
            "Drawing on all of your innate understanding, you draw out the Quantum Energies.",
            "Retrieving the memories of the effect, you calm yourself and harness the weird energies..",
            "Quietly retreating into the recesses of memory, you grasp at the weird energies.."
        ]
        phrase = random.choice(rndm_phrases)
        print(f"{phrase}")
        sleep(1)
        print(f"Great power courses through your body!")
        sleep(1)
        self.quantum_strength_effect = True
        self.quantum_units -= quantum_unit_cost
        self.quantum_strength_uses = -1  # to compensate for end of turn calculation
        if self.hit_points < self.maximum_hit_points:  # in the rare case player has hit point overage,
            self.hit_points = self.maximum_hit_points  # this will not disrupt that advantage
        pause()
        return 0

    def quantum_heal_wounds(self, monster):
        if monster is None:
            print(f"Quantum Heal")
        else:
            print(f"Quantum Heal (BATTLE)")
        sleep(1)
        self.hud()
        # perhaps use this math for higher healing effect:
        # number_of_dice = (3 + self.level - 1)  # 3 dice for lvl 1, 4 for lvl 2, 5 for lvl 3....
        # heal = dice_roll(number_of_dice, 4)  + (1 * number_of_dice)
        quantum_unit_cost = 1
        # number_of_dice = (3 + self.level + self.quantum_level)  # consider changing to self.quantum_level
        # heal = dice_roll(number_of_dice, 6) + number_of_dice + self.quantum_level
        if self.quantum_level < 3:
            heal = math.ceil(self.maximum_hit_points * .75)
        else:
            heal = math.ceil(self.maximum_hit_points * .90)
        if self.hit_points < self.maximum_hit_points:
            print(f"You feel restorative powers welling up within you..")
            sleep(1)
            print(f"You heal {heal} points..")  # remove after testing
            self.hit_points += heal
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points
            # self.hit_points += math.floor(self.maximum_hit_points * .5)  # round down for cure light wounds.
            self.quantum_units -= quantum_unit_cost
        else:
            print(f"You are at maximum health!")
            sleep(1)
        pause()
        return 0

    def protection_from_evil(self, monster):
        # everything but a natural 1 will succeed
        if monster is None:
            print(f"Protection from Evil")
        else:
            print(f"Protection from Evil (BATTLE)")
        sleep(1)
        quantum_unit_cost = 1
        self.hud()
        rndm_phrases = [
            "Concentrating and calming yourself, you attempt to harness your innate Quantum Knowledge..",
            "Quieting your mind, you focus inward to harness the Quantum Energies..",
            "The world around you becomes muted and still as you introspectively draw upon your innate Quantum Skill.."
        ]
        effect_phrase = random.choice(rndm_phrases)
        prot_roll = dice_roll(1, 20)
        print(f"{effect_phrase}")
        sleep(1.5)
        if prot_roll > 1:
            self.protection_effect = True
            self.protection_effect_uses = -1  # to compensate for end of turn calculation
            self.temp_protection_effect = (2 + self.quantum_level)
            self.quantum_units -= quantum_unit_cost
            print(f"You have succeeded!")
            sleep(1)
            print(f"You gain a Quantum Protection advantage + {self.temp_protection_effect}!")
            pause()
            return 0
        else:
            print(f"You are unable to glean the Quantum Effects..")
            self.quantum_units -= quantum_unit_cost
            pause()
            return 0

    def quantum_help1(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Quantum Missile: Multiple glowing projectiles, corresponding to your Quantum knowledge and randomness"
              f"\nare launched at your enemy. Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Quantum Sleep: Your knowledge of Quantum weirdness allows you to attempt to lull your enemy into a\n"
              f"dream-like and utterly vulnerable state. Initial success based on Player Intelligence vs Enemy Wisdom\n"
              f"Final success depends on Enemy AC.")
        print()
        print(f"Heal Wounds: Quantum actions at a subatomic level repair physical wounds, ignoring necrosis and "
              f"poison.\nEffectiveness based on Quantum Knowledge Level.")
        print()
        print(f"Protection from Evil: Through Quantum probabilities, reduce the chances of successful enemy Quantum\n"
              f"attacks and paralyzing effects. Effectiveness depends on Quantum Knowledge Level. Duration depends on\n"
              f"Constitution Modifier.")
        print()
        print(f"Turn Undead: Attempt to strike panic into the Undead by turning the very improbable forces responsible"
              f"\nfor their weird existence against them. Success based on Player Wisdom vs Enemy Wisdom")
        print()
        pause()
        return None

    def quantum_help2(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Web: Through improbabilities, shoot a giant web at your enemy, incapacitating them. Initial success\n"
              f"based on Player Wisdom vs Enemy Dexterity. Final success depends on Enemy AC.")
        print()
        print(f"Quantum Purify: Works only when poisoned or necrotic, but once engaged, purifies the flesh from these\n"
              f"effects and also increases Hit Points.")
        print()
        print(f"Quantum Strength: Harnessing Quantum Energies, your Strength and melee damage are increased\n"
              f"for a maximum duration based on your Quantum Knowledge level and Strength Modifier.")
        print()
        print(f"Quantum Scorch: Rays of intense flame strike your enemy. Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Quantum Charm: Use your powers of persuasion to lull your enemy into a vulnerable sleep. Initial\n"
              f"success based on Player Charisma vs Enemy Wisdom. Final success depends on Enemy AC.")
        print()
        pause()
        return None

    def quantum_help3(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Lightning: Harness an electrical storm to be cast at your enemy, causing burns and arcflash damage.\n"
              f"Success based on Player Wisdom vs Enemy AC.")
        print()
        print(f"Hold Monster: Employ Quantum Forces to hold and incapacitate your enemy. Success based on \n"
              f"Player Wisdom vs Enemy Strength. Final success depends on Enemy AC.")
        print()
        print(f"Phantasm: By Quantum Tunneling, create a terrifyingly debilitating mental illusion, capturing the\n"
              f"mind of your enemy and causing agonizing mental damage. Success based on Player Wisdom vs Enemy\n"
              f"Intelligence. (Undead are unbelieving)")
        print()
        print(f"Immolation: A winding trail of flame encircles your enemy, closing until forming a complete immersion\n"
              f"of deadly fire. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Vortex: A watery twister forms around your enemy, disorienting, and causing crushing damage.\n"
              f"Success based on Player Wisdom vs Enemy Strength.")
        print()
        pause()
        return None

    def quantum_help4(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Fireball: Through Spooky Action at a Distance, a Fireball forms, seemingly from out of your hands,\n"
              f"shooting at your enemy at moderate speed. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Flesh to Stone: 95% chance to petrify monster, after which player has 1 free crit, thereafter enemy\n"
              f"must pass Constitution saving throw. 2 failed saves after initial attack = permanent petrification.\n"
              f"Player gets exp reward, but no gold or loot.")
        print()
        print(f"Fear: Strike terror into the hearts of the living with Quantum Weirdness, sending them retreating.\n"
              f"Success based on Player Wisdom vs Enemy Wisdom. (Undead are unbelieving)")
        print()
        print(f"Finger of Death: Concentrating powerful Quantum Energies into a single finger, great pain and high\n"
              f"damage befall any enemy touched. Success based on Player Wisdom vs Enemy Constitution.")
        print()
        print(f"Banish: At the will of the Manipulator, a Quantum Tunnel between worlds claims the enemy's existence,\n"
              f"transferring it offworld. Success based on Player Wisdom vs Enemy Charisma.")
        print()
        pause()
        return None

    def quantum_help5(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"Disintegrate: A thin green ray springs from your pointing finger to your target.\n"
              f"On a failed save, the target takes devastating damage.The target is disintegrated if this damage\n"
              f"leaves it with 0 hit points. A disintegrated enemy and everything it is wearing and carrying, except\n"
              f"items protected by Quantum Weirdness, are reduced to a pile of fine gray dust. Player receives exp\n"
              f"reward but no Gold or Loot. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Ice Storm: A powerful squall of frozen death hurls toward your enemy causing overwhelming cold and\n"
              f"force damage. Success based on Player Wisdom vs Enemy Constitution.")
        print()
        print(f"Firestorm: Ice Storm counterpart, but encompassed of seething flame, causing high burn damage.\n"
              f"Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Gravity Well: 100% chance to successfully incapacitate your enemy in an impossible Quantum Gravity\n"
              f"Singularity which causes initial crushing damage. Player has 1 free crit. Target must make strength\n"
              f"saving throw. Upon failed save, enemy remains trapped and player gets additional free crit.\n"
              f"Enemy and all items are lost to the crushing gravity. Player gets exp reward, but no gold or loot\n"
              f"unless enemy item is protected by quantum weirdness.")
        print()
        pause()
        return None

    def quantum_help6(self, monster):
        cls()
        if monster is None:
            print("HELP")
        else:
            print("HELP (BATTLE)")
        print(f"Exp Level: {self.level}  Quantum Knowledge Level: {self.quantum_level}")
        print()
        print(f"QUANTUM MASTER EFFECTS")
        print()
        print(f"Quantum Word Kill: Through impossibly, unimaginably small probabilities, the Master utters a single\n"
              f"word. If the enemy has less than 100 Hit Points, death results instantly. No saving throw,\n"
              f"no defense possible.")
        print()
        print(f"Meteor Swarm: The Master pulls celestial matter from the heavens into the atmosphere above the enemy,\n"
              f"with amplified and compensatory gravity, for a devastating attack yielding extremely high force and\n"
              f"crushing damage. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Skeletal Remains: The Master pulls finite Quantum Energies from the ground, impossibly re-animating\n"
              f"fallen skeletal warriors lost to time and sending them forth as a stampeding army, resulting in\n"
              f"extreme force, bludgeoning, and melee damage. Success based on Player Wisdom vs Enemy Dexterity.")
        print()
        print(f"Negative Energy Plague: The Quantum Master harnesses Dark Energy and re-focuses it to form a\n"
              f"plague of mental agony causing severe damage to all living and undead creatures. Success based on\n"
              f"Player Wisdom vs Enemy Intelligence.")
        print()
        pause()
        return None

    def quantum_effects(self, monster):
        # called from main loop
        if self.quantum_units > 0:
            printable_quantum_book = {1: {1: "Quantum Missile",
                                          2: "Sleep",
                                          3: "Heal Wounds",
                                          4: "Protection from Evil",
                                          5: "Turn Undead"},
                                      2: {1: "Web",
                                          2: "Purify",
                                          3: "Strength",
                                          4: "Scorch",
                                          5: "Charm"},
                                      3: {1: "Lightning",
                                          2: "Hold Monster",
                                          3: "Phantasm",
                                          4: "Immolation",
                                          5: "Vortex"},
                                      4: {1: "Fireball",
                                          2: "Flesh to Stone",
                                          3: "Fear",
                                          4: "Finger of Death",
                                          5: "Banish"},
                                      5: {1: "Disintegrate",
                                          2: "Ice Storm",
                                          3: "Firestorm",
                                          4: "Gravity Well"},
                                      6: {1: "Quantum Word Kill",
                                          2: "Meteor Swarm",
                                          3: "Skeletal Remains",
                                          4: "Negative Energy Plague"}

                                      }
            quantum_book = {1: {0: self.quantum_help1,
                                1: self.quantum_missile,
                                2: self.quantum_sleep,
                                3: self.quantum_heal_wounds,
                                4: self.protection_from_evil,
                                5: self.turn_undead},
                            2: {0: self.quantum_help2,
                                1: self.quantum_web,
                                2: self.quantum_purify,
                                3: self.quantum_strength,
                                4: self.quantum_scorch,
                                5: self.quantum_charm},
                            3: {0: self.quantum_help3,
                                1: self.quantum_lightning,
                                2: self.hold_monster,
                                3: self.phantasm,
                                4: self.immolation,
                                5: self.vortex},
                            4: {0: self.quantum_help4,
                                1: self.fireball,
                                2: self.flesh_to_stone,
                                3: self.fear,
                                4: self.finger_of_death,
                                5: self.banish},
                            5: {0: self.quantum_help5,
                                1: self.disintegrate,
                                2: self.ice_storm,
                                3: self.fire_storm,
                                4: self.gravity_well},
                            6: {1: self.quantum_word_kill,
                                2: self.meteor_swarm,
                                3: self.skeletal_remains,
                                4: self.negative_energy_plague}
                            }
            while True:
                self.hud()
                try:
                    print(f"Your Quantum Knowledge level: {self.quantum_level}")
                    q_level = int(input(f"Quantum Level to cast: "))

                    if self.quantum_level >= q_level and self.quantum_units >= q_level:
                        # create key and value lists from nested dict in order to produce cleanly printable dictionary
                        key_lst = list(printable_quantum_book[q_level].keys())
                        value_list = list(printable_quantum_book[q_level].values())
                        working_dict = {key_lst[i]: value_list[i] for i in range(len(key_lst))}
                        for key, value in working_dict.items():
                            print(f"{key}: {value}")
                        q_to_cast = int(input(f"Number of Quantum Effect to cast (or 0 for HELP): "))
                        # noinspection PyArgumentList
                        quantum_function = (quantum_book[q_level][q_to_cast](monster))

                        if q_to_cast == 0:  # if HELP, call function and return here
                            quantum_function

                        else:  # if not HELP, return to main loop from function
                            return quantum_function

                    else:
                        if self.quantum_level < q_level:
                            print(f"You have not yet acquired that level of Quantum knowledge!")
                            sleep(1)
                            continue

                        if self.quantum_units < q_level:
                            print(f"You do not have enough Quantum Energy Units!")
                            continue

                except (ValueError, KeyError):
                    print(f"Invalid input")
                    sleep(.25)
                    return None  # creates condition for a continue statement in main loop so a turn is not wasted
        else:
            print(f"You have no Quantum unit energy!")
            pause()
            return None  # creates condition for a continue statement in main loop so a turn is not wasted

    def vozzbozz_meteor_swarm(self, monster):
        player_total = vozzbozz.base_dc + vozzbozz.wisdom_modifier + vozzbozz.proficiency_bonus
        print(f"Player base DC: {vozzbozz.base_dc}")
        print(f"Wisdom modifier: {vozzbozz.wisdom_modifier}")
        print(f"Proficiency bonus: {vozzbozz.proficiency_bonus}")
        print(f"Total: {player_total}")
        sleep(1)
        monster_roll = dice_roll(1, 20)
        monster_mod = monster.dexterity_modifier
        monster_total = monster_roll + monster_mod
        print(f"Monster Saving Throw: {monster_roll}")
        print(f"Monster Dexterity Modifier: {monster_mod}")
        print(f"Monster Total: {monster_total}")
        if player_total >= monster_total:
            critical_bonus = 1
            if dice_roll(1, 20) == 20:
                critical_bonus = 2
            number_of_dice = 20 * critical_bonus
            damage_to_opponent = dice_roll(number_of_dice, 6) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, 6) + (1 * number_of_dice)  # 2nd attack=force damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)

            print(f"Vozzbozz closes his eyes for a moment.")
            sleep(1)
            print(f"Upon opening them, they burn brighter than the sun!")
            pause()
            self.hud()
            print(f"With a world-shaking and awe-inspiring eruption, "
                  f"a swarm of burning meteors materializes above and falls upon your enemy!!")
            print(f"{number_of_dice}d8 + {number_of_dice}d8 force damage + 1 per die rolled: "
                  f"{damage_to_opponent}")
            print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"The great storm of fire and stone explodes directly on target in surreal "
                  f"glory and inflicts {total_damage_to_opponent} points of damage!")
            pause()
            self.hud()
            return total_damage_to_opponent
        else:
            critical_bonus = 1
            if dice_roll(1, 20) == 20:
                critical_bonus = 2
            number_of_dice = 20 * critical_bonus
            damage_to_opponent = (dice_roll(number_of_dice, 6) + (1 * number_of_dice) +
                                  dice_roll(number_of_dice, 6) + (1 * number_of_dice)) / 2  # 2nd attack=force damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz closes his eyes for a moment.")
                sleep(1)
                print(f"His focus is momentarily disrupted by the {monster.name}!")
                pause()
                self.hud()
                print(f"With a world-shaking and awe-inspiring eruption, "
                      f"a swarm of burning meteors materializes above and falls upon your enemy!!")
                print(f"{number_of_dice}d8 + {number_of_dice}d8 force damage + 1 per die rolled: "
                      f"{damage_to_opponent}")
                print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                print(f"The great storm of fire and stone explodes directly on target in surreal "
                      f"glory, but due to the interruption, it only inflicts {total_damage_to_opponent} points\n"
                      f"of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent

    def vozzbozz_word_kill(self, monster):
        # if monster < 100 hp, it dies
        print(f"Vozzbozz smiles for an instant, then his face is drained of its humanity..")
        sleep(1)
        self.hud()
        if monster.hit_points < 100:
            print(f"He cries out in a world-shaking voice..")
            sleep(1)
            print(f"SUPPLICIUM!!")
            sleep(1.5)
            print(f"The {monster.name} drops like a rock!!!")
            pause()
            return monster.hit_points
        else:
            print(f"The {monster.name} has too much life energy to succumb to the quantum word kill effect!")
            pause()
            return 0

    def vozzbozz_skeletal_remains(self, monster):
        print(f"Player Base DC: {vozzbozz.base_dc}")
        print(f"Wisdom modifier: {vozzbozz.wisdom_modifier}")
        print(f"Proficiency bonus: {vozzbozz.proficiency_bonus}")
        player_total = vozzbozz.base_dc + vozzbozz.wisdom_modifier + vozzbozz.proficiency_bonus
        print(f"Total: {player_total}")
        critical_bonus = 1
        if dice_roll(1, 20) == 20:
            critical_bonus = 2
        monster_roll = dice_roll(1, 20)
        monster_mod = monster.constitution_modifier
        monster_total = monster_roll + monster_mod
        print(f"Monster Saving Throw: {monster_roll}")
        print(f"Monster Constitution Modifier: {monster_mod}")
        print(f"Monster Total: {monster_total}")
        if player_total >= monster_total:
            #
            number_of_dice = 15 * critical_bonus
            damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # 2nd attack = force damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz forms a fist and then beckons the ground with his free hand..")
                sleep(1)
                print(f"Without warning, the ground swells with the thundering cacophony of countless skeletal\n"
                      f"warriors arising from an abysmal black chasm!!")
                sleep(1)
                print(f"Some upon skeletal horseback, others on foot, but with one mind and purpose, they swarm upon\n"
                      f"your enemy, thrusting ever forward in a voracious clashing of bone, steel and shield!!")
                pause()
                self.hud()
                print(f"{number_of_dice}d12 + {number_of_dice}d8 force damage + 1 per skeleton bludgeoning "
                      f"damage: {damage_to_opponent}")
                print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                # print(f"It hits for {total_damage_to_opponent} points of damage..")
                print(f"The great swarm of armor, axe, sword and spear inflicts "
                      f"{total_damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent
            else:
                print(f"For all of its fear-inspiring appearance, the skeletal horde"
                      f" fails to land any damage!")  # 0 damage
                sleep(1)
                return 0
        else:
            number_of_dice = 15 * critical_bonus
            damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice)  # no force damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
            print(f"Vozzbozz forms a fist and then beckons the ground with his free hand..")
            sleep(1)
            print(f"Without warning, the ground swells with the thundering cacophony of countless skeletal\n"
                  f"warriors arising from an abysmal black chasm!!")
            sleep(1)
            print(f"The {monster.name} distracts the Master for a moment..")
            pause()
            self.hud()
            print(f"The skeletal horde takes form but does not inflict damage to its fullest potential..")
            sleep(1)
            print(f"{number_of_dice}d12 roll + 1 per skeleton bludgeoning damage = {damage_to_opponent}")
            print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"It hits for {total_damage_to_opponent} points of damage..")
            pause()
            self.hud()
            return total_damage_to_opponent

    def vozzbozz_negative_energy_plague(self, monster):
        print(f"Player Base DC: {vozzbozz.base_dc}")
        print(f"Wisdom modifier: {vozzbozz.wisdom_modifier}")
        print(f"Proficiency bonus: {vozzbozz.proficiency_bonus}")
        player_total = vozzbozz.base_dc + vozzbozz.wisdom_modifier + vozzbozz.proficiency_bonus
        print(f"Total: {player_total}")
        sleep(1)
        monster_roll = dice_roll(1, 20)
        monster_mod = round((monster.intelligence - 10) / 2)
        monster_total = monster_roll + monster_mod
        print(f"Monster Saving Throw: {monster_roll}")
        print(f"Monster Intelligence Modifier: {monster_mod}")

        print(f"Monster Total: {monster_total}")
        critical_bonus = 1
        if dice_roll(1, 20) == 20:
            critical_bonus = 2
        if player_total >= monster_total:
            #
            number_of_dice = 15 * critical_bonus
            damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice) + \
                dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # 2nd attack = crushing damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            if damage_to_opponent > 0:
                print(f"Vozzbozz grasps at air, until his entire shape fades to a mere silhouette of blackness, with\n"
                      f"stars and celestial bodies floating through!!")
                sleep(1)
                print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                      f"from his hands toward your enemy!!")
                sleep(1)
                print(f"With universal abhorrence, the negative energy plague entangles the {monster.name}!!")
                sleep(1)
                print(f"{number_of_dice}d12 necrotic damage + {number_of_dice}d8 crushing damage + 1 per die "
                      f"rolled mental anguish: {damage_to_opponent}")
                print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
                print(f"The great, empty darkness inflicts "
                      f"{total_damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return total_damage_to_opponent
            else:
                print(f"For all of its fear-inspiring appearance, the plague"
                      f" fails to land any damage!")  # 0 damage
                sleep(1)
                return 0
        else:
            number_of_dice = 15 * critical_bonus
            damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice)  # no crushing damage
            melee_bonus = dice_roll(vozzbozz.level, vozzbozz.hit_dice)
            total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
            # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
            print(f"Vozzbozz grasps at air, until his entire shape fades to a mere silhouette of blackness, with\n"
                  f"stars and celestial bodies floating through!!")
            sleep(1)
            print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                  f"from his hands toward your enemy!!")
            sleep(1)
            print(f"The {monster.name} distracts Vozzbozz for just a moment..")
            pause()
            self.hud()
            print(f"The plague takes form but does not inflict damage to its fullest potential..")
            sleep(1)
            print(
                f"{number_of_dice}d12 necrotic damage + 1 per die rolled mental damage: {damage_to_opponent}")
            print(f"{vozzbozz.level}d{vozzbozz.hit_dice} Damage Bonus: {melee_bonus}")
            print(f"It hits for {total_damage_to_opponent} points of damage..")
            pause()
            self.hud()
            return total_damage_to_opponent

    def vozzbozz_attack(self, monster):
        print(f"Vozzbozz attacks with Quantum Energy!!")
        sleep(1)
        if monster.hit_points < 100:
            return self.vozzbozz_word_kill(monster)
        else:
            rndm_effect_lst = [self.vozzbozz_meteor_swarm, self.vozzbozz_skeletal_remains,
                               self.vozzbozz_negative_energy_plague]
            rndm_effect = random.choice(rndm_effect_lst)
            return rndm_effect(monster)

    def quantum_word_kill(self, monster):
        # everything but a natural 1 hits.
        # if monster < 100 hp, it dies
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Quantum Word Kill" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Quantum Word Kill" in monster.vulnerabilities:
                    vulnerable = True
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Word Kill.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Clearing your mind, you attempt to harness the weird energies...")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1 and not vulnerable:
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                else:
                    if monster.hit_points < 100:
                        print(f"SUPPLICIUM!!")
                        sleep(1.5)
                        return monster.hit_points
                    else:
                        print(f"The {monster.name} has too much life energy to succumb to the quantum effect!")
                        pause()
                        return 0
        else:
            print(f"Quantum Word Kill is a Battle Effect only..")
            sleep(1)
            return

    def disintegrate(self, monster):
        # A thin green ray springs from your pointing finger to a target that you can see within range.
        # A creature targeted by this spell must make a Dexterity saving throw.
        # On a failed save, the target takes 10d10 damage.
        # The target is disintegrated if this damage leaves it with 0 hit points.
        # A disintegrated creature and everything it is wearing and carrying, except magic items,
        # are reduced to a pile of fine gray dust.
        #
        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Disintegrate" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Disintegrate" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Disintegrate" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Disintegrate.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (10 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 10) + 40
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A thin, green ray springs from your hand and speeds toward your enemy!")
                        sleep(1)
                        print(f"{number_of_dice}d10 roll + 40 force damage: {damage_to_opponent}")
                        print(f"The {monster.name} suffers {damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        monster.reduce_health(damage_to_opponent)
                        if not monster.check_dead():
                            return 0  # damage already returned to reduce_health function
                        else:
                            if monster.proper_name != "None":
                                print(f"{monster.proper_name} is completely reduced to a pile of fine gray dust!!")
                            else:
                                print(f"The {monster.name} is completely reduced to a pile of fine, gray dust!!")
                            sleep(1.5)
                            monster.gold = 0

                            self.in_proximity_to_monster = False
                            # pause()
                            return 0
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    print(f"A thin, green ray springs from your hand and speeds toward your enemy!")
                    sleep(1)
                    print(f"The {monster.name} dodges!")
                    sleep(1)
                    pause()
                    self.hud()
                    return 0
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Disintegrate!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Disintegrate!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Disintegrate is a Battle Effect only..")
            sleep(1)
            return

    def fireball(self, monster):
        # everything but a natural 1 hits.
        # on a successful dexterity saving throw, monster takes 50% damage.
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            if "Fireball" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Fireball" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Fireball" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Fireball.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Fireball..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print(f"A tiny burning cinder, no larger than a grain of sand "
                          f"pops into existence and is snuffed out just as suddenly..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (5 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # print(f"Attack roll: {roll_d20}")
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A red-hot orb of dreadful flames forms from your hand and speeds toward your enemy!")
                        print(f"{number_of_dice}d8 roll + 1 per die: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The flaming ball of fire explodes on target and inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (5 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The Fireball takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d8 roll + 1 per die rolled / 2 = {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Fireball!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Fireball!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Fireball is a Battle Effect only..")
            sleep(1)
            return

    def finger_of_death(self, monster):
        # everything but a natural 1 hits.
        # on a successful constitution saving throw, monster takes 50% damage.
        quantum_unit_cost = 4
        if self.in_proximity_to_monster:
            if "Finger of Death" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Finger of Death" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Finger of Death" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Finger of Death.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies...... ")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (5 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (4 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Your hands throb with blinding Quantum Energy!")
                        sleep(1)
                        print(f"{number_of_dice}d8 roll + 4 * number of dice: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"You extend a white-hot finger, merely touching your enemy, inflicting "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Your effect fails to land any damage!")  # 0
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (5 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (4 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"Your hands throb with red-hot Quantum Energy..")
                    sleep(1)
                    # print(f"The effect takes form but does not to its fullest potential..")
                    print(f"{number_of_dice}d8 roll + 2 * number of dice rolled / 2 = {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    sleep(1)
                    print(f"You extend a glowing finger and touch your enemy, inflicting "
                          f"{total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Finger of Death!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Finger of Death!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Finger of Death is a Battle Effect only..")
            sleep(1)
            return

    def meteor_swarm(self, monster):
        # everything but a natural 1 hits.
        # on a successful dexterity saving throw, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Meteor Swarm" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Meteor Swarm" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Meteor Swarm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Meteor Swarm.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird Quantum Energies "
                    f"to create the Meteor Swarm..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print(f"A tiny burning cinder, no larger than a grain of sand "
                          f"pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier

                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # 2nd attack=force damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a world-shaking and awe-inspiring eruption, "
                              f"a swarm of burning meteors materializes above and falls upon your enemy!!")
                        print(f"{number_of_dice}d8 + {number_of_dice}d8 force damage + 1 per die rolled: "
                              f"{damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great storm of fire and stone explodes directly on target in surreal "
                              f"glory and inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # no force damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The Meteor Swarm takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d8 roll + 1 per die rolled = {damage_to_opponent}")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Meteor Swarm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Meteor Swarm!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Meteor Swarm is a Battle Effect only..")
            sleep(1)
            return

    def skeletal_remains(self, monster):
        # everything but a natural 1 hits.
        # on a successful dexterity saving throw, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Skeletal Remains" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Skeletal Remains" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Skeletal Remains" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Skeletal Remains.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Skeletal Remains..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print(f"A tiny jawbone pops into existence and is hurled upon your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # 2nd attack = force damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Before you or your enemy can see it, you both sense the ground swell with the\n"
                              f"thundering cacophony of countless skeletal warriors arising from a black chasm!!")
                        sleep(1)
                        print(f"Some on horseback, others on foot, but with one mind and purpose, they swarm upon\n"
                              f"your enemy, thrusting ever forward in a voracious clashing of bone, steel and shield!!")
                        sleep(1)
                        print(f"{number_of_dice}d12 + {number_of_dice}d8 force damage + 1 per skeleton bludgeoning "
                              f"damage: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        # print(f"It hits for {total_damage_to_opponent} points of damage..")
                        print(f"The great swarm of armor, axe, sword and spear inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, the skeletal horde"
                              f" fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice)  # no force damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The skeletal horde takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d12 roll + 1 per skeleton bludgeoning damage = {damage_to_opponent}")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Skeletal Remains!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Skeletal Remains!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Skeletal Remains is a Battle Effect only..")
            sleep(1)
            return

    def negative_energy_plague(self, monster):
        # everything but a natural 1 hits.
        # on a successful intelligence saving throw, monster takes 50% damage.
        quantum_unit_cost = 6
        if self.in_proximity_to_monster:
            if "Negative Energy Plague" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Negative Energy Plague" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Negative Energy Plague" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Negative Energy Plague.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(f"Clearing your mind, you attempt to harness the weird energies "
                      f"to create the Negative Energy Plague..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    # print(f"A tiny jawbone pops into existence and is hurled upon your enemy..")
                    # sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = round((monster.intelligence - 10) / 2)
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Intelligence Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice) + \
                        dice_roll(number_of_dice, 8) + (1 * number_of_dice)  # 2nd attack = crushing damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A harrowing and visceral vacuum of shear, black emptiness shoots forth "
                              f"from your hands toward your enemy!!")
                        sleep(1)
                        print(f"With universal abhorrence, the negative energy plague entangles the {monster.name}!!")
                        sleep(1)
                        print(f"{number_of_dice}d12 necrotic damage + {number_of_dice}d8 crushing damage + 1 per die "
                              f"rolled mental anguish: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great, empty darkness inflicts "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, the plague"
                              f" fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (15 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 12) + (1 * number_of_dice)  # no crushing damage
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The plague takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(
                        f"{number_of_dice}d12 necrotic damage + 1 per die rolled mental damage: {damage_to_opponent}")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It hits for {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Plague!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Plague!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Negative Energy Plague is a Battle Effect only..")
            sleep(1)
            return

    def ice_storm(self, monster):
        # everything but a natural 1 hits.
        # on a successful constitution saving throw, monster takes 50% damage.
        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Ice Storm" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Ice Storm" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Ice Storm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Ice Storm.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies "
                    f"to create the Ice Storm..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print(f"A single snowflake pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.constitution_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Constitution Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (10 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (4 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a crackling rumble, a frigid storm of ice and hail thrusts forth from your hand!!")
                        print(
                            f"{number_of_dice}d8 roll + {number_of_dice} + (4 * number of dice rolled): "
                            f"{damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The great freezing storm explodes on target and does "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (10 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, 8) + (4 * number_of_dice) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The storm does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(
                        f"{number_of_dice}d8 roll + (4 * number of dice rolled) / 2: {damage_to_opponent} (ROUNDED) ")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Ice Storm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Ice Storm!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Ice Storm is a Battle Effect only..")
            sleep(1)
            return

    def fire_storm(self, monster):
        # everything but a natural 1 hits.
        # on a successful dexterity saving throw, monster takes 50% damage.
        quantum_unit_cost = 5
        if self.in_proximity_to_monster:
            if "Fire Storm" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Fire Storm" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Fire Storm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Fire Storm.")
                sleep(1)
                self.hud()
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus + level_advantage)
                print(
                    f"Clearing your mind, you attempt to harness the weird energies "
                    f"to create the Fire Storm..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print(f"A single glowing ember pops into existence and falls on your enemy..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_total}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = monster.dexterity_modifier
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (10 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (4 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"With a deafening roar, a storm of searing hot flames thrusts forth from your hand!!")
                        print(
                            f"{number_of_dice}d8 roll + {number_of_dice} + (4 * number of dice rolled): "
                            f"{damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The scorching storm explodes on target and does "
                              f"{total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (10 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, 8) + (4 * number_of_dice) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    # damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The storm does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(
                        f"{number_of_dice}d8 roll + (4 * number of dice rolled) / 2 = {damage_to_opponent} (ROUNDED) ")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Fire Storm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Fire Storm!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Fire Storm is a Battle Effect only..")
            sleep(1)
            return

    def phantasm(self, monster):
        # phantasm matches your wisdom vs monster intelligence
        quantum_unit_cost = 3
        vulnerability_modifier = 0
        if self.in_proximity_to_monster:
            if "Phantasm" not in monster.immunities and "All" not in monster.immunities and not monster.undead:
                vulnerable = False
                if "Phantasm" in monster.vulnerabilities:
                    vulnerable = True
                    vulnerability_modifier = 5
                resistance_modifier = 0
                if "Phantasm" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Phantasm.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies "
                      f"to create the illusion..")
                sleep(1)
                print(f"Quantum Ability Check: {roll_d20}")  # anything but a natural 1 is success
                sleep(1)
                if roll_d20 == 1:
                    print(f"The Phantasm pops into existence as a cloudy blur, and promptly vanishes..")
                    sleep(1)
                    print("Your focus has failed..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC = {self.base_dc}\n"
                      f"Wisdom Modifier: {self.wisdom_modifier}\n"
                      f"Proficiency Bonus: {self.proficiency_bonus}")
                if vulnerable:
                    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                sleep(1)
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_mod = math.floor((monster.intelligence - 10) / 2)
                monster_total = monster_roll + monster_mod + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Intelligence Modifier: {monster_mod}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if player_dc >= monster_total:  # > tie goes to defender >= tie goes to player
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 8) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"The Phantasmal illusion takes form through weird Quantum "
                              f"tunneling and completely seizes the mind of your enemy!")
                        print(f"{number_of_dice}d8 roll + 1 per die: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"The terrible vision inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"For all of its fear-inspiring appearance, it fails to land any damage!")  # 0 damage
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 8) + (1 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The Phantasmal illusion takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d8 roll + 1 per die rolled / 2 = {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.undead:
                    print(f"Undead do not believe!!")
                    sleep(1)
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Phantasm!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Phantasmal Forces!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Phantasm is a Battle Effect only..")
            sleep(1)
            return

    def quantum_lightning(self, monster):
        # lightning matches player wisdom against monster AC
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Lightning" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Lightning" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Lightning" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Lightning.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The Lightning crackles into existence "
                          f"and spreads randomly, completely missing the {monster.name}..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 6) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"{number_of_dice} bolts of Quantum Lightning materialize from nothingness and "
                              f"hit their target!")
                        print(f"{number_of_dice}d6 roll + 1 arc damage per bolt: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"They do {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 6) + (1 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The lightning takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d6 roll + 1 per die rolled / 2 = {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It inflicts {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Lightning!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Lightning attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Lightning is a Battle Effect only..")
            sleep(1)
            return

    def immolation(self, monster):
        # immolation matches player wisdom against monster dexterity
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Immolation" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Immolation" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Immolation" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Immolation.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The wreath of flame crackles into existence "
                          f"and spreads wildly, completely missing your target..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                vulnerability_modifier = 0
                if vulnerable:
                    vulnerability_modifier = 5
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if vulnerability_modifier > 0:
                    print(f"Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_total = monster_roll + monster.dexterity_modifier + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Dexterity Modifier: {monster.dexterity_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_dc >= monster_total:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 6)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A serpentine trail of fire materializes from nothingness and "
                              f"wreathes your target in scorching flame!")
                        print(f"{number_of_dice}d6 roll: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                        print(f"It inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, 6) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The trail of fire takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d6 roll / 2: {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage Bonus: {melee_bonus}")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Immolation Effects!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Immolation attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Immolation is a Battle Effect only..")
            sleep(1)
            return

    def vortex(self, monster):
        # vortex matches player wisdom against monster strength
        quantum_unit_cost = 3
        if self.in_proximity_to_monster:
            if "Vortex" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Vortex" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Vortex" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Vortex.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                # player_total = (roll_d20 + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to harness the weird energies..")
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The watery twister materializes and spreads wildly, completely missing your target..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL HIT!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                vulnerability_modifier = 0
                if vulnerable:
                    vulnerability_modifier = 5
                level_advantage = 0
                if self.level > monster.level:
                    level_advantage = self.level - monster.level
                player_dc = self.base_dc + self.proficiency_bonus + self.wisdom_modifier + \
                    vulnerability_modifier + level_advantage
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")
                if vulnerability_modifier > 0:
                    print(f"Vulnerability Modifier: {vulnerability_modifier}")
                if level_advantage > 0:
                    print(f"Level Advantage: {level_advantage}")
                print(f"Total: {player_dc}")
                sleep(1)
                monster_roll = dice_roll(1, 20)
                monster_total = monster_roll + monster.strength_modifier + resistance_modifier
                print(f"Monster Saving Throw: {monster_roll}")
                print(f"Monster Strength Modifier: {monster.strength_modifier}")
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                sleep(1)
                if roll_d20 == 20 or player_dc >= monster_total:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 6)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"A twisting vortex of roaring water materializes from nothingness and "
                              f"wraps your target with impossible crushing force!")
                        sleep(1)
                        print(f"{number_of_dice}d6 roll: {damage_to_opponent}")
                        print(f"{self.level}d{self.hit_dice} Damage bonus: {melee_bonus}")
                        print(f"It inflicts {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"Through its own weirdness, the {monster.name} manages to "
                              f"avoid damage from the weird energy!")  # 0 dmg
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (3 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil(dice_roll(number_of_dice, 6) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The twister takes form but does not inflict damage to its fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d6 roll / 2: {damage_to_opponent} (ROUNDED)")
                    print(f"{self.level}d{self.hit_dice} Damage bonus: {melee_bonus}")
                    print(f"It does {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent
            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Vortex Effects!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Vortex attacks!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Vortex is a Battle Effect only..")
            sleep(1)
            return

    def quantum_missile(self, monster):
        # q_missile matches player wisdom vs monster AC
        quantum_unit_cost = 1
        if self.in_proximity_to_monster:
            if "Quantum Missile" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Quantum Missile" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Quantum Missile" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Quantum Missile.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to aim the "
                      f"Quantum Missile at the {monster.name}..")
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The projectiles go awry..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = f"Success!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")

                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    # number_of_dice = (3 + (self.level - 1)) * critical_bonus  #consider changing to self.quantum_level
                    number_of_dice = (1 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = (dice_roll(number_of_dice, 4) + (1 * number_of_dice))
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"{number_of_dice} glowing projectiles materialize from nothingness and "
                              f"hit their target!")
                        # print(f"(Quantum Missile = 3d4(dice) + 1 die for every level)")
                        print(f"{number_of_dice}d4 roll + 1 force damage per missile: {damage_to_opponent}\n"
                              f"{self.level}d{self.hit_dice} damage bonus: {melee_bonus}\n"
                              f"Total: {total_damage_to_opponent}")
                        print(f"They do {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"It blocks the glowing projectiles!")  # zero damage result
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (1 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 4) + (1 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The glowing projectiles take form but do not inflict damage to their fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d4 roll + 1 per die rolled / 2: {damage_to_opponent}\n"
                          f"{self.level}d{self.hit_dice} damage bonus: {melee_bonus}\n"
                          f"Total: {total_damage_to_opponent} (ROUNDED)")
                    print(f"They do {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent

            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to the Quantum Missile attack!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to the Quantum Missile attack!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Quantum Missile is a Battle Effect only..")
            sleep(1)
            return

    def quantum_scorch(self, monster):
        # scorch is player's wisdom vs monster AC
        quantum_unit_cost = 2
        if self.in_proximity_to_monster:
            if "Scorch" not in monster.immunities and "All" not in monster.immunities:
                vulnerable = False
                if "Scorch" in monster.vulnerabilities:
                    vulnerable = True
                resistance_modifier = 0
                if "Scorch" in monster.resistances or "All" in monster.resistances:
                    resistance_modifier = 3
                self.quantum_units -= quantum_unit_cost
                print(f"Scorch.")
                sleep(1)
                self.hud()
                roll_d20 = dice_roll(1, 20)  # attack roll
                player_total = (self.base_dc + self.wisdom_modifier + self.proficiency_bonus)
                print(f"Focusing your innate understanding, you attempt to Scorch the {monster.name}..")
                print(f"Quantum Ability Check: {roll_d20}")
                sleep(1)
                if roll_d20 == 1:
                    print("Your focus has failed..")
                    sleep(1)
                    print(f"The rays of flame fly off chaotically..")
                    pause()
                    self.hud()
                    return 0
                if roll_d20 == 20 or vulnerable:
                    critical_bonus = 2
                    hit_statement = "CRITICAL!!"
                else:
                    critical_bonus = 1
                    hit_statement = "Rays of scorching flame are summoned by Quantum Weirdness and hit your enemy!"
                print(f"Player Base DC: {self.base_dc}")
                print(f"Wisdom modifier: {self.wisdom_modifier}")
                print(f"Proficiency bonus: {self.proficiency_bonus}")

                print(f"Total: {player_total}")
                sleep(1)
                print(f"Monster armor class: {monster.armor_class}")
                monster_total = monster.armor_class + resistance_modifier
                if resistance_modifier != 0:
                    print(f"Monster Resistance Modifier: {resistance_modifier}")
                print(f"Monster Total: {monster_total}")
                if roll_d20 == 20 or player_total >= monster_total:
                    #
                    # number_of_dice = (3 + (self.level - 1)) * critical_bonus
                    number_of_dice = (1 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = dice_roll(number_of_dice, 6) + (1 * number_of_dice)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    if damage_to_opponent > 0:
                        print(hit_statement)
                        sleep(1)
                        print(f"Scorch = 3d6(dice) + 1 die for every level")
                        print(f"{number_of_dice}d6 roll "
                              f"({number_of_dice} rays + 1 force damage per ray): {damage_to_opponent}\n"
                              f"{self.level}d{self.hit_dice} bonus: {melee_bonus}\n"
                              f"Total: {total_damage_to_opponent}")
                        print(f"They do {total_damage_to_opponent} points of damage!")
                        pause()
                        self.hud()
                        return total_damage_to_opponent
                    else:
                        print(f"It dodges the scorching rays!")  # zero damage result
                        sleep(1)
                        return 0
                else:
                    number_of_dice = (1 + self.proficiency_bonus) * critical_bonus
                    damage_to_opponent = math.ceil((dice_roll(number_of_dice, 6) + (1 * number_of_dice)) / 2)
                    melee_bonus = dice_roll(self.level, self.hit_dice)
                    total_damage_to_opponent = math.ceil(damage_to_opponent + melee_bonus)
                    print("Your attempt to harness the Quantum weirdness lacks focus..")
                    sleep(1)
                    print(f"The scorching rays take form but do not inflict damage to their fullest potential..")
                    sleep(1)
                    print(f"{number_of_dice}d6 roll + 1 per die rolled / 2: {damage_to_opponent}\n"
                          f"{self.level}d{self.hit_dice} bonus: {melee_bonus}\n"
                          f"Total: {total_damage_to_opponent} (ROUNDED)")
                    print(f"They do {total_damage_to_opponent} points of damage..")
                    pause()
                    self.hud()
                    return total_damage_to_opponent

            else:
                if monster.proper_name != "None":
                    print(f"{monster.proper_name} is immune to Scorch!!")
                    sleep(1)
                else:
                    print(f"The {monster.name} is immune to Scorch!!")
                    sleep(1)
                self.quantum_units -= quantum_unit_cost
                print(f"You have wasted Quantum Energy!")
                sleep(1)
                pause()
                return 0
        else:
            print(f"Scorch is a Battle Effect only..")
            sleep(1)
            return

    def evade(self, monster):
        # called from main loop, using return value from battle_menu_choices(), (if player has no allies)
        if self.encounter < 21:
            print(f"You attempt a stealthy evasive maneuver..")
            sleep(1)
            monster_roll = dice_roll(1, 20)
            monster_total = monster_roll + monster.dexterity_modifier
            player_roll = dice_roll(1, 20)
            evade_success = player_roll + self.dexterity_modifier + self.stealth + self.proficiency_bonus
            if self.level > 3:
                evade_success += self.proficiency_bonus
            print(f"Stealth Check: {player_roll}")
            print(f"Dexterity Modifier: {self.dexterity_modifier}")
            print(f"Stealth bonus: {self.stealth}")
            if self.level > 3:
                print(f"Proficiency Bonus: {self.proficiency_bonus}")

            print(f"Total: {evade_success}")
            sleep(1)
            print(f"Enemy Roll: {monster_roll}")
            print(f"Enemy Dexterity Modifier: {monster.dexterity_modifier}")
            print(f"Enemy Total: {monster_total}")
            if evade_success >= monster_total or evade_success == 20:
                print(f"Your stealth and dexterity have served you well!")
                sleep(1)
                print(f"The {monster.name} looks at {monster.his_her_its} surroundings, and departs,"
                      f" obviously confused.")
                sleep(1)
                print(f"You have successfully evaded the {monster.name}!")
                pause()
                self.hud()
                return True

            else:
                print(f"The {monster.name} swiftly blocks your escape!")
                sleep(.5)
                print(f"You are rooted to the spot. You must stand your ground!")
                pause()
                self.hud()
                return False

        else:
            # bosses cannot be evaded.
            if monster.proper_name != "None":
                print(f"{monster.proper_name} is far too adept to be evaded!")
            else:
                print(f"The {monster.name} is far too adept to be evaded!!")
            sleep(.5)
            print(f"You are rooted to the spot. You must stand your ground!")
            pause()
            self.hud()
            return False

    # INVENTORY AND ITEMS

    def chemist_main(self):

        while True:
            self.hud()
            rndm_aroma = random.choice(rndm_aroma_lst)
            print(f"(In Town, Quantum Chemist Shop)")
            print(f"Jahns, the Fieldenberg quantum chemist is here, busying himself at the crucible.\n"
                  f"Mortars and pestles litter the counter and the smell of {rndm_aroma} fills the air...")

            if self.hit_points < self.maximum_hit_points:
                print("The aura fills your nostrils and lungs...healing you to full strength!")
                self.hit_points = self.maximum_hit_points
                pause()
                self.hud()
            print(f"Your gold: {self.gold} GP")
            chemist_choice = input(
                "(P)urchase quantum items, (S)ell quantum items, Display your (I)nventory, or "
                "(E)xit the chemist: ").lower()

            if chemist_choice == 'p':
                self.buy_chemist_items()
                continue

            elif chemist_choice == 's':
                self.sell_chemist_items()
                continue

            elif chemist_choice == 'i':
                self.inventory()
                continue

            elif chemist_choice == 'e':
                return

            else:
                continue

    def sell_chemist_items(self):
        # this code was written very early on and is extremely amateurish
        # in the future, clean this up by making a list of nonzero items into a dictionary
        while True:
            self.hud()

            if self.potions_of_healing == 0 and self.town_portals == 0 and \
                    self.potions_of_strength == 0 and self.elixirs == 0 and self.antidotes == 0:
                print(f"You have no quantum items to sell..")
                pause()
                return

            print(f"You currently carry the following quantum items:")
            print(f"1: Potions of Healing - Quantity: {self.potions_of_healing}")
            print(f"2: Scrolls of Town Portal - Quantity: {self.town_portals}")
            print(f"3: Potions of Strength - Quantity: {self.potions_of_strength}")
            print(f"4: Clarifying Elixirs - Quantity: {self.elixirs}")
            print(f"5: Poison Antidote Vials - Quantity: {self.antidotes}")
            print(f"Your gold: {self.gold} GP")
            type_to_sell = input(f"Pick item to sell by number, or go (B)ack: ").lower()

            if type_to_sell == 'b':
                return

            elif type_to_sell == '1':
                your_item = "potions"

                if self.potions_of_healing < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '2':
                your_item = "scrolls of town portal"

                if self.town_portals < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '3':
                your_item = "potions of strength"

                if self.potions_of_strength < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '4':
                your_item = "clarifying elixirs"

                if self.elixirs < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            elif type_to_sell == '5':
                your_item = "vials of antidote"

                if self.antidotes < 1:
                    print(f"You do not have any {your_item}..")
                    sleep(1)
                    continue

            else:
                print(f"Invalid..")
                continue

            try:
                number_of_items_to_sell = int(input(f"Enter number of {your_item} to sell: "))

                if type_to_sell == '1' and number_of_items_to_sell > 0:

                    if self.potions_of_healing >= number_of_items_to_sell:
                        self.potions_of_healing -= number_of_items_to_sell
                        gold_recieved = (healing_potion.sell_price * number_of_items_to_sell)
                        self.gold += gold_recieved
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '2' and number_of_items_to_sell > 0:

                    if self.town_portals >= number_of_items_to_sell:
                        self.town_portals -= number_of_items_to_sell
                        gold_recieved = (scroll_of_town_portal.sell_price * number_of_items_to_sell)
                        self.gold += gold_recieved
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '3' and number_of_items_to_sell > 0:

                    if self.potions_of_strength >= number_of_items_to_sell:
                        self.potions_of_strength -= number_of_items_to_sell
                        gold_recieved = (strength_potion.sell_price * number_of_items_to_sell)
                        self.gold += gold_recieved
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '4' and number_of_items_to_sell > 0:

                    if self.elixirs >= number_of_items_to_sell:
                        self.elixirs -= number_of_items_to_sell
                        gold_recieved = (elixir.sell_price * number_of_items_to_sell)
                        self.gold += gold_recieved
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                elif type_to_sell == '5' and number_of_items_to_sell > 0:

                    if self.antidotes >= number_of_items_to_sell:
                        self.antidotes -= number_of_items_to_sell
                        gold_recieved = (antidote.sell_price * number_of_items_to_sell)
                        self.gold += gold_recieved
                        print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                        pause()
                        continue

                    else:
                        print(f"Invalid.")
                        sleep(1)
                        continue

                else:
                    print(f"Invalid entry..")

            except ValueError:
                print("Invalid input")
                continue

    def buy_chemist_items(self):

        chemist_dict = {
            'Healing': [healing_potion],
            'Potions of Strength': [strength_potion],
            'Town Portal Implements': [scroll_of_town_portal],
            'Elixirs': [elixir],
            'Antidotes': [antidote]
        }
        while True:
            self.hud()
            print(f"Jahns has items for sale in the following categories:")
            # create a list of item types:
            item_type_lst = list(chemist_dict.keys())
            # create a dictionary from list of item types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Pick item type by number, Display your (I)nventory, or go (B)ack: ").lower()
            # if buy_or_exit not in ('i', 'p', 'b'):
            #    self.hud()
            #    continue
            if buy_or_exit == 'i':
                self.inventory()
                continue
            elif buy_or_exit == 'b':
                return
                # break
            elif buy_or_exit not in ('i', 'b'):
                try:
                    item_type_index_to_buy = int(buy_or_exit)
                    # item_type_index_to_buy = int(input(f"Enter the category of the item to buy by number: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    chemist_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (chemist_dict[item_type_to_buy]):
                        item_dict[item] = (chemist_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Pick item by number, Display your (I)nventory, or go (B)ack: ").lower()
                    # if buy_or_exit not in ('i', 'p', 'b'):
                    #    self.hud()
                    #    continue
                    if buy_or_exit == 'i':
                        self.inventory()
                        continue
                    elif buy_or_exit == 'b':
                        break
                    elif buy_or_exit not in ('i', 'b'):
                        try:
                            item_index_to_buy = int(buy_or_exit)
                            # item_index_to_buy = int(
                            #    input(f"Enter the number of the item you wish to consider for purchase: "))
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (chemist_dict[item_type_to_buy])[item_index_to_buy]

                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        # confirm_purchase = input(f"Purchase {sale_item.name} for {sale_item.buy_price} GP (y/n)? ")
                        # if confirm_purchase == 'y':

                        try:
                            number_of_items = int(input(f"How many would you like to buy: "))
                        except ValueError:
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        if number_of_items > 0:
                            purchase_price = sale_item.buy_price * number_of_items
                            if self.gold >= purchase_price:
                                if self.level >= sale_item.minimum_level:
                                    self.gold -= purchase_price
                                    # replace these if statements with dictionary in future
                                    if sale_item.name == 'Scroll of Town Portal':
                                        self.town_portals += number_of_items
                                    elif sale_item.name == 'Potion of Strength':
                                        self.potions_of_strength += number_of_items
                                    elif sale_item.name == 'Potion of Healing':
                                        self.potions_of_healing += number_of_items
                                    elif sale_item.name == 'Clarifying Elixir':
                                        self.elixirs += number_of_items
                                    elif sale_item.name == 'Vial of Antidote':
                                        self.antidotes += number_of_items
                                    self.hud()
                                    print(f"You buy {number_of_items} {sale_item.name}s")
                                    # (self.pack[sale_item.item_type]).append(sale_item)
                                    self.item_type_inventory(sale_item.item_type)
                                    pause()
                                    break
                                    # continue
                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            print(f"Zero..")
                            continue

    def item_management_sub_menu(self):
        while True:
            self.hud()
            item_to_manage = input(
                f"Manage (W)eapons, (A)rmor, (S)hields, (B)oots, (C)loaks, View your (I)nventory, or "
                f"(E)xit Item Management: ").lower()
            if item_to_manage == 'w':
                self.item_management('Weapons', self.wielded_weapon)
                continue
            elif item_to_manage == 'a':
                self.item_management('Armor', self.armor)
                continue
            elif item_to_manage == 's':
                self.item_management('Shields', self.shield)
                continue
            elif item_to_manage == 'b':
                self.item_management('Boots', self.boots)
                continue
            elif item_to_manage == 'c':
                self.item_management('Cloaks', self.cloak)
                continue
            elif item_to_manage == 'i':
                self.inventory()
                continue
            elif item_to_manage == 'e':
                return
            else:
                continue

    def blacksmith_main(self):
        while True:
            # you can make this into a dictionary, with each value being a function
            # something like
            # if blacksmith_choice in blacksmith_main_dict:
            #   blacksmith_function = (blacksmith_main_dict[blacksmith_choice])
            #   blacksmith_function()
            # elif blacksmith_choice == 'e':
            #   return
            self.hud()
            print(f"(In Town, Blacksmith Shop)")
            print(f"Lucino, the Fieldenberg blacksmith is here, hammering at his anvil.\n"
                  f"He notices you, grumbles, and continues hammering...")
            print(f"Your gold: {self.gold} GP")
            blacksmith_choice = input(
                "(P)urchase items, (L)iquidate items, (M)anage your inventory items, "
                "View (I)nventory, or (E)xit the blacksmith: ").lower()
            if blacksmith_choice == 'p':
                self.buy_blacksmith_items()
                continue
            elif blacksmith_choice == 'l':
                self.sell_blacksmith_items()
                continue
            elif blacksmith_choice == 'm':
                self.item_management_sub_menu()
            elif blacksmith_choice == 'i':
                self.inventory()
                continue
            elif blacksmith_choice == 'e':
                return
            else:
                continue

    def buy_blacksmith_items(self):

        blacksmith_dict = {
            'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                        quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
            'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
            'Shields': [buckler, kite_shield, quantum_tower_shield],
            'Boots': [elven_boots, ancestral_footsteps],
            'Cloaks': [elven_cloak]
        }
        while True:
            self.hud()
            print(f"Armory for sale:")
            # create a list of blacksmith item types:
            item_type_lst = list(blacksmith_dict.keys())
            # create a dictionary from list of blacksmith items types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Pick item type by number, Display your (I)nventory, or go (B)ack: ").lower()
            # if buy_or_exit not in ('i', 'p', 'b'):
            #    self.hud()
            #    continue
            if buy_or_exit == 'i':
                self.inventory()
                continue
            elif buy_or_exit == 'b':
                return
            elif buy_or_exit not in ('i', 'b'):
                try:
                    item_type_index_to_buy = int(buy_or_exit)
                    # item_type_index_to_buy = int(input(f"Enter the number of the category of the item to buy: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    blacksmith_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (blacksmith_dict[item_type_to_buy]):
                        item_dict[item] = (blacksmith_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Pick item by number, Display your (I)nventory, or go (B)ack: ").lower()
                    if buy_or_exit == 'i':
                        self.inventory()
                        continue
                    elif buy_or_exit == 'b':
                        break
                    elif buy_or_exit not in ('i', 'b'):
                        try:
                            item_index_to_buy = int(buy_or_exit)
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (blacksmith_dict[item_type_to_buy])[item_index_to_buy]
                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        confirm_purchase = input(
                            f"Purchase {sale_item.name} for {sale_item.buy_price} GP (y/n)? ").lower()
                        if confirm_purchase == 'y':
                            if self.gold >= sale_item.buy_price:
                                if self.level >= sale_item.minimum_level:
                                    if not self.duplicate_item(sale_item.item_type, sale_item):
                                        self.hud()
                                        print(f"You buy the {sale_item.name}")
                                        self.gold -= sale_item.buy_price
                                        (self.pack[sale_item.item_type]).append(sale_item)
                                        self.item_type_inventory(sale_item.item_type)
                                        pause()
                                        continue
                                    else:
                                        print(f"You already have a {sale_item.name}")
                                        pause()
                                        continue
                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            continue

    def item_management(self, item_type, current_item):
        self.hud()
        if len(self.pack[item_type]) > 0:
            print(f"Your current {item_type} inventory:")
            (self.pack[item_type]).sort(key=lambda x: x.buy_price)
            item_mgmt_dict = {}
            for item in (self.pack[item_type]):
                item_mgmt_dict[item] = (self.pack[item_type]).index(item)
            for key, value in item_mgmt_dict.items():
                print(value + 1, ':', key)  # value is index. indexing starts at zero, so add 1
            print()
        else:
            print(f"You have nothing in your {item_type} inventory..")
            pause()
            return
        old_item = current_item
        print(f"You are currently using: ")
        if item_type == 'Weapons':
            print(f"{self.wielded_weapon}, Sell Price: {self.wielded_weapon.sell_price} GP")

        elif item_type == 'Armor':
            print(f"{self.armor}, Sell Price: {self.armor.sell_price} GP")

        elif item_type == 'Shields':
            if self.shield.name != 'No Shield':
                print(f"{self.shield}, Sell Price: {self.shield.sell_price} GP")
            else:
                print(f"{self.shield.name}")
        elif item_type == 'Boots':
            print(f"{self.boots}, Sell Price: {self.boots.sell_price} GP")

        elif item_type == 'Cloaks':
            print(f"{self.cloak}, Sell Price: {self.cloak.sell_price} GP")
        swap_or_exit = input(f"(S)wap item, or go (B)ack: ").lower()
        if swap_or_exit == "b":
            return
        elif swap_or_exit == "s":

            try:
                new_item_index = int(input(f"Enter the number of the item from your inventory that you wish to use: "))
                new_item_index -= 1  # again, indexing starts at 0 so add 1
                if item_type == 'Weapons':
                    new_weapon = (self.pack[item_type])[new_item_index]  # SYNTAX FOR INDEX
                    print(f"{new_weapon}")
                    self.wielded_weapon = new_weapon
                elif item_type == 'Armor':
                    new_armor = (self.pack[item_type])[new_item_index]
                    print(f"{new_armor}")
                    self.armor = new_armor
                elif item_type == 'Shields':
                    new_shield = (self.pack[item_type])[new_item_index]
                    print(f"{new_shield}")
                    self.shield = new_shield
                elif item_type == 'Boots':
                    new_boots = (self.pack[item_type])[new_item_index]
                    print(f"{new_boots}")
                    self.boots = new_boots
                elif item_type == 'Cloaks':
                    new_cloak = (self.pack[item_type])[new_item_index]
                    print(f"{new_cloak}")
                    self.cloak = new_cloak
                # CALCULATE STEALTH AND ARMOR CLASS. NOTICE INDENT
                self.calculate_stealth()
                self.calculate_armor_class()
            except (IndexError, ValueError):
                print("Invalid entry..")
                sleep(1)
                return
            print(f"You are now using the {(self.pack[item_type])[new_item_index]}.")
            if old_item.name != 'No Shield':
                print(f"You place the {old_item.name} in your inventory.")
                (self.pack[item_type]).pop(new_item_index)  # INDEX SYNTAX
                (self.pack[item_type]).append(old_item)  # old_weapon represents an object, not an index
                # (self.pack[item_type]).sort(key=lambda x: x.buy_price)
                pause()
            else:
                print(f"You are well equipped.")
                pause()

    def sell_blacksmith_items(self):
        # sell_blacksmith_items() allows you to sell items from self.pack
        while True:
            cls()
            # self.hud()
            print(f"You have items eligible to sell in the following categories:")
            non_empty_item_type_lst = []
            # make a list of non-empty inventory item keys from player's pack inventory
            for key in self.pack:
                if len(self.pack[key]) > 0:
                    non_empty_item_type_lst.append(key)
            if len(non_empty_item_type_lst) < 1:
                print(f"Your inventory is empty")
                pause()
                return
            else:
                # print(non_empty_item_type_lst)  # remove after testing
                # make a dictionary from the non_empty item type list. index, and print
                item_type_dict = {}
                for item_type in self.pack:
                    if len(self.pack[item_type]) and item_type != 'Rings of Protection' and \
                            item_type != 'Rings of Regeneration':
                        item_type_dict[item_type] = non_empty_item_type_lst.index(item_type)
                for key, value in item_type_dict.items():
                    print(value + 1, ':', key)

                try:
                    print(f"Your gold: {self.gold} GP")
                    sell_or_exit = input("(S)ell items, (L)iquidate entire contents of pack, or go (B)ack: ").lower()
                    if sell_or_exit not in ('s', 'l', 'b'):
                        cls()
                        # self.hud()
                        continue
                    if sell_or_exit == 'l':
                        self.sell_everything()
                        return
                    if sell_or_exit == 'b':
                        break
                    item_type_index_to_sell = int(input(f"Enter the number of the category of the item to sell: "))
                    item_type_to_sell = non_empty_item_type_lst[item_type_index_to_sell - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
            while True:
                cls()
                # self.hud()
                persistent_item_type = item_type_to_sell
                print(f"Your {item_type_to_sell} inventory eligible for sale:")
                # self.item_type_inventory(item_type_to_sell)
                sell_all = []
                mgmt_dict = {}
                for item in (self.pack[item_type_to_sell]):
                    mgmt_dict[item] = (self.pack[item_type_to_sell]).index(item)
                for key, value in mgmt_dict.items():
                    print(value + 1, ':', key.name, '- Sell price:', key.sell_price, 'GP')
                    sell_all.append(key.sell_price)
                gold_for_all_items = sum(sell_all)
                if not len(sell_all):
                    # if gold_for_all_items == 0:
                    print(f"You have no {item_type_to_sell} to sell.")
                    pause()
                    break
                else:
                    print(f"Total sell price for all {item_type_to_sell}: {gold_for_all_items} GP")
                print(f"Your gold: {self.gold} GP")
                sell_or_exit = input(
                    f"Show entire (I)nventory, (S)ell an item, Sell (A)ll {item_type_to_sell} or go (B)ack: ").lower()
                if sell_or_exit not in ('i', 's', 'a', 'b'):
                    cls()
                    # self.hud()
                    continue
                elif sell_or_exit == 'a':

                    while True:
                        yes_or_no = input(f"Sell all {item_type_to_sell} for {gold_for_all_items} GP? ").lower()
                        if yes_or_no not in ('y', 'n'):
                            continue
                        elif yes_or_no == 'y':
                            print(f"You sell all of your {item_type_to_sell} for {gold_for_all_items} GP.")
                            self.gold += gold_for_all_items
                            (self.pack[item_type_to_sell]).clear()
                            pause()
                            break
                        elif yes_or_no == 'n':
                            break
                elif sell_or_exit == 'i':
                    self.inventory()
                    continue
                elif sell_or_exit == 'b':
                    break
                elif sell_or_exit == 's':

                    try:

                        item_index_to_sell = int(input(f"Enter the number of the item you wish to sell: "))
                        item_index_to_sell -= 1  # again, indexing starts at 0 and is awkward
                        sold_item = (self.pack[item_type_to_sell])[item_index_to_sell]
                    except (IndexError, ValueError):
                        print("Invalid entry..")
                        sleep(1)
                        continue
                    # sold_item = (self.pack[item_type_to_sell])[item_index_to_sell]
                    confirm_sale = input(f"Sell the {sold_item.name} for {sold_item.sell_price} GP (y/n)? ").lower()
                    if confirm_sale == 'y':
                        print(f"You sell the {sold_item.name} for {sold_item.sell_price} GP")
                        self.gold += sold_item.sell_price
                        (self.pack[item_type_to_sell]).pop(item_index_to_sell)
                        print(f"Your gold: {self.gold} GP")
                        pause()
                        cls()
                        # self.hud()
                        if len(self.pack[item_type_to_sell]) > 0:
                            self.item_type_inventory(item_type_to_sell)
                            print(f"Your gold: {self.gold} GP")
                            sell_again = input(
                                f"(S)ell more {persistent_item_type} (B)ack to main market menu or "
                                f"(E)xit to town: ").lower()
                            if sell_again == 's':
                                continue
                            elif sell_again == 'b':
                                break
                            else:
                                # if sell_again not in ('y', 'n'):
                                return
                        else:
                            # print(f"Your gold: {self.gold} GP")
                            print(f"Your {persistent_item_type} inventory is now empty.")
                            pause()
                            break
                    else:
                        continue

    def sell_everything(self):
        # this code took me many hours to come up with.
        # allows for liquidation of self.pack
        liquidate_lst = []
        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
        mgmt_dict = {}
        for each_category in item_type_lst:
            if len(self.pack[each_category]):
                for item in (self.pack[each_category]):
                    mgmt_dict[item] = (self.pack[each_category]).index(item)
        for key, value in mgmt_dict.items():
            print(key.name, '- Sell price:', key.sell_price, 'GP')
            liquidate_lst.append(key.sell_price)
        total = sum(liquidate_lst)
        print(f"Total: {total}")
        confirm_liquidate = input(f"Sell everything in your dungeoneer's pack for {total} GP? ").lower()
        if confirm_liquidate == 'y':
            for each_category in item_type_lst:
                (self.pack[each_category]).clear()
            print(f"You sell your entire armory inventory for {total} GP.")
            self.gold += total
            pause()
            return
        else:
            return

    def use_scroll_of_town_portal(self):
        if self.town_portals < 1:
            print(f"You have no scrolls!")
            sleep(1.25)
            return False
        else:
            self.hud()
            self.town_portals -= 1
            print(f"The quantum portal appears before you; a seemingly impossible tunneling between distant places..")
            sleep(1.5)
            return True

    def poison_ingestion(self):
        # called from fountain_event(),
        self.hud()
        self.dot_multiplier = self.dungeon.level
        self.dot_turns = dice_roll(1, 5)
        rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                 "An unnerving frailty spreads throughout your body...",
                                 "Pain and tenderness courses through your body.."
                                 ]
        poisoned_phrase = random.choice(rndm_poisoned_phrases)
        print(f"{poisoned_phrase}")
        sleep(1.5)
        print(f"You have been poisoned!")
        self.poisoned = True
        self.poisoned_turns = 0
        pause()
        self.hud()
        return self.poisoned

    def drink_potion_of_strength(self):
        self.hud()
        rndm_drinking_phrases = [
            "Tilting it to your lips, you drain the tiny blue vial and the strength of giants surges through you!",
            "Retrieving the vial from your belt, you pop the cork and down the sweet liquid...\n"
            "Great power and vitality  courses through your body!",
            "No sooner is the tincture running down your throat, than does the great\n"
            "and overwhelming strength and vitality fill your body! You feel invincible!"
        ]
        drink_phrase = random.choice(rndm_drinking_phrases)
        if self.potions_of_strength > 0:
            print(f"{drink_phrase}")
            self.potion_of_strength_effect = True
            self.potions_of_strength -= 1
            self.potion_of_strength_uses = -1  # to compensate for end of turn calculation
            if self.hit_points < self.maximum_hit_points:  # in the rare case player has hit point overage,
                self.hit_points = self.maximum_hit_points  # this will not disrupt that advantage
            pause()
            return self.potion_of_strength_effect
        else:
            print(f"You have no potions!")
            pause()
            return False

    def hint_event_1(self):
        # hint_events move the story along by subtle hints to the player, revealed over time in the game, as
        # they progress.
        # hint_events take place in the tavern (so far). they correspond to boss_clues:
        # hint_event_1 occurs after boss_clue_1, etc. the boss_clues occur after defeating the dungeon_exit boss
        # hint_event_1 is a meeting with vozzbozz, introduction to tor'bron the barbarian, and another hint
        # about the symbol of the wicked queen, which the player finds during boss_clue_1
        cls()
        print(f"As soon as she sees you, Jenna motions discreetly toward the hallway leading away from the bar.")
        sleep(1)
        print(f"You direct your eyes that way and casually make your way down the hall...")
        sleep(1)
        pause()
        cls()
        print(f"Jenna catches up to you at end of the hallway. \'Ye are {self.name}, are ye not?\'\n"
              f"Nodding and instinctively looking about for eavesdroppers, you re-focus on her concerned look.")
        if len(self.vanquished_foes):
            vanquished_foes = convert_list_to_string_with_commas_only(self.vanquished_foes)
            print(f"\'I know of ye.\' Your puzzled look speaks for you, as she continues,\n"
                  f"\'We 'ave 'eard of it.. how ye' 'ave defeated {vanquished_foes}...and others!\'")
        pause()
        cls()
        typewriter("\'There is somethin' ye should know!\' Her level of anxiety gives you pause; it seems out of\n"
                   "character for her.\n\'Ye should seek out Vozzbozz!\' Pausing with a far away look, she nods.\n"
                   "\'I'm headin' back to the bar, and we'll make like we never spoke o' this..\'\n"
                   "\'Vozzbozz is in the barroom. He's the one with the raven on 'is shoulder!\'\n"
                   "The meeting ends as abruptly as it began. Jenna disappears toward the bar as you slowly\n"
                   "start to follow a good distance behind, impatient and confused.\n")
        pause()
        cls()
        # meeting with vozzbozz and introduction to tor'bron
        typewriter_txt_file('hint_event_1.txt')
        pause()

        cls()
        typewriter(f"{self.name},\nThe guardian of {self.dungeon.name} has, in its possession, an ornate dagger "
                   f"of very fine craftsmanship.\nIt is imperative you retrieve it. Return here with it so that "
                   f"matters may progress.\n"
                   f"\n                                                     -V\n")
        self.boss_hint_1_event = True
        pause()
        return

    def hint_event_2(self):
        print(f"As soon as she sees you, Jenna directs your attention to the opposite side of the room by raising\n"
              f"her chin in that general direction.\nAt the very same booth as last time, sits the hulking barbarian, "
              f"Tor'bron.")
        sleep(2)
        print(f"You cautiously approach...")
        sleep(1)
        pause()
        cls()
        typewriter(f"\'Well! {self.name}!\', he bellows in his booming voice. \'Sit!\' Something in his dour demeanor\n"
                   f"tells you it is not an invitation, but an order. You marvel at the size and strength of the man.\n"
                   f"His jet black hair lays long on his head, and covers his body in a wiry patchwork.\n"
                   f"Long sideburns flank a strong jawbone, and his deep-set amber eyes burn with gripping intensity.\n"
                   f"\'And where is it? Do you have it?\', he asks, his tone tense and distrustful.\n"
                   f"You carefully retrieve the dagger and pass it to him across the table. Roughly and without "
                   f"regard,\n"
                   f"he swipes it from you, yanks it from its sheath and launches it across the room, over the heads\n"
                   f"of all the patrons on this side of the bar, until it abruptly lodges in the wall with a bang.")
        if len(self.vanquished_foes):
            vanquished_foes = convert_list_to_string_with_commas_only(self.vanquished_foes)
            typewriter(f"\'The slayer of {vanquished_foes}...\n...and others besides!\'\n")
        typewriter(f"\'When first I saw you, I was...\', he searches for the word. \'..skeptical!\'\n"
                   "But now, things are different! Now I know you are able-bodied and strong! Good! Very good, this!\' "
                   "He nods.\n"
                   "A sting of disrespect hits you. After the toil and struggle to retrieve the prized dagger, "
                   "you are\n"
                   "now realizing it was nothing more than a test to prove your mettle to this stranger!\n"
                   "\'You  must be Tor'bron!\', you say as you slide into the booth. His eyes\n"
                   f"narrow slightly and he takes a sip of ale. Continuing, you say, \'I heard Vozzbozz address you\n"
                   "the last time we saw each other. And may I add, I never doubted *your* abilities!\'\n"
                   "Still alert, he thinks about your words. His glowering slowly turns to what must be a smile.\n"
                   "Then, he laughs, a deep and hearty laugh. Instantly, he fiercely slams the table with his fist,\n"
                   "so that the entire room shakes and becomes silent. He raises his huge hand, pointing\n"
                   "straight at you. \'Good! Don't ever doubt them!\' And again he smiles and laughs as the tavern "
                   "ambience"
                   f"\ngradually returns. Reaching his tree-trunk arm toward you, he slams you on the shoulder with a"
                   f" heavy hand.\n"
                   f"You are thankful for the {self.armor.name.lower()} you wear; without it, the blow would "
                   f"undoubtedly "
                   "have been an injury!\nInstinctively reaching for the aching shoulder, you reply plainly, "
                   "\'I certainly will not..\'\n")
        pause()
        cls()
        # meet Tor'bron, get hints
        typewriter_txt_file('hint_event_2.txt')
        pause()
        cls()
        self.boss_hint_2_event = True
        return

    def hint_event_3(self):
        # another meeting with vozzbozz. meet Magnus the dwarf
        print(f"Upon entering, you are met with the familiar sites, sounds and smells of the inn. Scanning the bar\n"
              f"area, you immediately notice the nasty-looking knife, still lodged in the wall. Before you even have\n"
              f"time to react, Lazarus swiftly lands on your shoulder. \'The master awaits you!\', he says plainly,\n"
              f"in his smooth tone. Off to your left, Vozzbozz sits in his regular booth, across from a proud-looking\n"
              f"and rather stout dwarf.")
        sleep(1)
        print(f"You approach the booth, and as you arrive, Lazarus deftly glides to Vozzbozz' shoulder.")
        pause()
        cls()
        if self.armor.ac > 11:
            print(f"The heavily-armored dwarf looks at you with seeming disinterest and simply says,\n"
                  f"\'That be some decent {self.armor.name.lower()} ye got there, lad\'. He takes a sip of his ale.")
        print(f"The dwarf slides out of the booth and motions that you should take his place. He then slides in next\n"
              f"to Vozzbozz and across from you.\n")
        print(f"\'Ah, {self.name}! Meet my good friend, Magnus Stormbringer.\', says Vozzbozz curtly. "
              f"The dwarf promptly reaches his\n"
              f"hand across the table and takes yours with a firm, brief grip and a nod.\n"
              f"\'Well met\', he says, sincerely, in an alarmingly deep voice.")
        pause()
        cls()
        # another meeting, get hints
        typewriter_txt_file('hint_event_3.txt')
        pause()
        cls()
        self.boss_hint_3_event = True
        return

    def hint_event_logic(self):
        if self.boss_hint_1 and not self.boss_hint_1_event:
            return self.hint_event_1()
        if self.boss_hint_2 and not self.boss_hint_2_event:
            return self.hint_event_2()
        if self.boss_hint_3 and not self.boss_hint_3_event:
            return self.hint_event_3()
        if self.boss_hint_4 and not self.boss_hint_4_event:
            # return self.hint_event_4()
            print("hint 4 event")
        # if self.boss_hint_5 and not self.boss_hint_5_event:
            # return self.hint_event_5()
            # print("hint 5 event")
        # if self.boss_hint_6 and not self.boss_hint_6_event:
            # return self.hint_event_6()
            # print("hint 6 event")

    def talk_to_jenna(self):
        cls()
        opening_phrase = "\'Feelin' chatty, love?\', queries Jenna in a coy tone."

        if self.dungeon.level == 1:
            if self.town_portal_exists:
                opening_phrase = f"\'Feelin' chatty, love?\', queries Jenna in a coy tone.\nI've 'eard ye entered" \
                                 f" town through a portal. 'Tis good, sir. 'Cept a word o' caution:\n" \
                                 f"Make good use of yer time here while it's open. Ye don't want ta be wastin' yer\n" \
                                 f"portals, seein' as scrolls can be rare!"
            typewriter(f"{opening_phrase}\n")
            treasure_chest_discovery = f"level {self.dungeon.level} treasure chest"
            if treasure_chest_discovery not in self.discovered_interactives:
                typewriter(f"She continues, \'{self.dungeon.name} is full of dangers for the "
                           f"unwary,\n"
                           f"but there are treasures to be had as well. 'Tis said that there be a pit below the "
                           f"dungeon\n"
                           f"where ye may find gold, but it be full of monsters and fiends.\' ")
            else:
                typewriter(f"With a big, welcoming smile, she says, \'I 'eard it said ye 'ave found treasure in the "
                           f"pit below {self.dungeon.name}!\n"
                           f"Care to spend some o' that loot?\', she adds with a wink.")

            micro_boss_discovery = f"level {self.dungeon.level} micro boss"
            if micro_boss_discovery not in self.discovered_interactives:
                typewriter(f"Lowering her tone, she goes on, \'I've also 'eard it said that there's an elite enemy\n"
                           f"down there, just waitin' for unsuspectin' adventurers in a dead ended corridor!\n"
                           f"Take good care, now, and be wise!\' ")
            pause()

    def inn(self):

        self.hud()
        print(f"You have come upon the Slumbering Bear Inn- a handsome building with all the trimmings and character\n"
              f"one would expect of a tavern in a town such as this. Above the door hangs an angled sign\n"
              f"with *THE SLUMBERING BEAR* printed above an angry, roaring bear that appears to be "
              f"anything but sleepy...")
        pause()
        # tavern_theme()
        self.hint_event_logic()
        while True:
            self.hud()
            if self.boss_hint_1:
                print(f"(In Town, The Slumbering Bear Inn)")
                print(f"Jenna catches your gaze and nods discreetly. \'Let me know if ye be needin' anything, love.\'")
            else:
                print(f"The barroom is bustling as always, but Jenna, the barkeep, notices you and calls over,\n"
                      f"very matter-of-factly, \"What do ye be needin' love?\"")
            inn_choice = input(f"(R)oom for the evening - 10 GP\n(T)alk to Jenna\n(E)xit the inn\n"
                               f">: ").lower()
            if inn_choice == 'r':
                if self.hit_points < self.maximum_hit_points or self.quantum_units < self.maximum_quantum_units \
                        or self.necrotic or self.poisoned:
                    self.hud()
                    if self.gold >= 10:
                        self.gold -= 10
                        print(f"You find your way to your room, which is upstairs. "
                              f"The accommodations are clean, tidy and welcoming.")
                        sleep(1)
                        print(
                            f"Removing your armor and accoutrements, you wash up and fall into a deep, restful sleep.")
                        sleep(1)
                        print(f"Your body and mind feel better.")
                        sleep(1)
                        if self.hit_points < self.maximum_hit_points:
                            self.hit_points = self.maximum_hit_points
                        self.recover_quantum_energy()
                        self.poisoned = False
                        self.necrotic = False
                        self.end_of_turn_calculation()
                        continue
                    else:
                        print(f"You do not have enough gold!")
                        pause()
                        continue
                else:
                    print(f"Jenna chuckles as she shakes her head at you. \"Ye are in the pink, love!\"\n"
                          f"\"What ye be needin' a room fer?\" She hurries off to her busy routines...")
                    sleep(1.5)
                    print(f"You realize she's right! You are in perfect condition!")
                    pause()
                    continue
            elif inn_choice == 't':
                self.hud()
                self.talk_to_jenna()
                continue
            elif inn_choice == 'e':
                self.hud()
                print(f"You walk out the door, but not before turning to see Jenna's wink and bright smile.\n"
                      f"\"Don't be a stranger, now, love! Ye are always welcome!\"")
                sleep(1.25)
                pause()
                # town_theme()
                return
            else:
                continue

    def recover_quantum_energy(self):
        if self.quantum_units < self.maximum_quantum_units:
            self.quantum_units = self.maximum_quantum_units
            print(f"Your Quantum Energy is restored!")
        else:
            print(f"You are refreshed.")
        pause()
        return

    def drink_antidote(self):
        if self.antidotes > 0:
            self.hud()
            if not self.poisoned:
                print(f"You are not poisoned!")
                sleep(1)
                return False  # false means you do NOT use a turn
            else:
                print(f"You retrieve the amber vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.antidotes -= 1
                self.hud()
                print(f"You feel a vibrant sensation..")
                sleep(1)
                self.poisoned = False
                self.poisoned_turns = 0
                print(f"The poison has left your body..")
                sleep(1)

                pause()
                return True  # True means you DO use a turn
        else:
            print(f"You have no vials of antidote!")
            sleep(1)
            # pause()
            return False  # False means you do NOT use a turn

    def drink_elixir(self):
        if self.elixirs > 0:
            self.hud()
            if not self.necrotic:
                print(f"Your flesh is not corrupted!")
                sleep(1)
                return False  # false means you do NOT use a turn
            else:
                print(f"You retrieve the emerald vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.elixirs -= 1
                self.hud()
                print(f"You feel a cleansing of the flesh..")
                sleep(1)
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The foul corruption leaves your body..")
                sleep(1)
                pause()
                return True  # True means you DO use a turn
        else:
            print(f"You have no elixirs!")
            sleep(1)
            # pause()
            return False  # False means you do NOT use a turn

    def drink_healing_potion(self):
        self.hud()
        if self.potions_of_healing > 0:
            # if healing_potion in self.pack['Healing']:
            if self.hit_points >= self.maximum_hit_points:
                print(f"You are already at maximum health!")
                sleep(1)
                return False  # False means you don't waste a turn
            else:
                print(f"You retrieve the vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.potions_of_healing -= 1
                # number_of_dice = (1 + self.level)
                # heal = dice_roll(number_of_dice, 4) + number_of_dice
                heal = math.ceil(self.maximum_hit_points * .66)
                print(f"You heal {heal} hit points")  # remove after testing
                self.hit_points += heal
                if self.hit_points > self.maximum_hit_points:
                    self.hit_points = self.maximum_hit_points
                self.hud()
                print(f"Your vitality increases.")
                sleep(1)
                pause()
                return True  # True means you use up a turn
        else:
            print("You have no potions!")
            pause()
            return False  # False means you don't waste a turn

    def duplicate_item(self, item_type, possible_duplicate):
        duplicate_item_name_lst = []
        inv_dict = Counter(item for item in self.pack[item_type])
        # print(inv_dict)  # for testing
        for key, value in inv_dict.items():
            duplicate_item_name_lst.append(key.name)
        # print(duplicate_item_name_lst)  # for testing
        if possible_duplicate.name in duplicate_item_name_lst or \
                possible_duplicate.name == self.wielded_weapon.name or \
                possible_duplicate.name == self.armor.name or \
                possible_duplicate.name == self.shield.name or \
                possible_duplicate.name == self.boots.name:
            return True
        else:
            return False

    def item_type_inventory(self, item_type):  # list items in inventory by type

        if item_type != 'Town Portal Implements' and item_type != 'Elixirs' \
                and item_type != 'Potions of Strength' and item_type != 'Healing' \
                and item_type != 'Antidotes':  # if item not in belt inventory
            print(f"Your {item_type}:")
            self.pack[item_type].sort(key=lambda x: x.name)
            stuff_dict = Counter(item.name for item in self.pack[item_type])
            for key, value in stuff_dict.items():
                # print(key, ':    ', value, sep='')
                if value > 1:
                    print(value, ' ', key, 's', sep='')
                    # print(key, 's', ':    ', value, sep='')
                else:
                    print(value, ' ', key, sep='')
            number_of_items = len(self.pack[item_type])
            # print(f"You now have {number_of_items} items in your {item_type} inventory.")
            if number_of_items:
                return True
            else:
                # print(f"You currently have no {item_type} in your inventory.")
                return False
        elif item_type == 'Town Portal Implements':
            if self.town_portals > 0:
                print(f"You have {self.town_portals} Scrolls of Town Portal")
                return True
            else:
                print(f"You have no scrolls of town portal.")
                return False
        elif item_type == 'Potions of Strength':
            if self.potions_of_strength > 0:
                print(f"You have {self.potions_of_strength} Potions of Strength")
                return True
            else:
                print(f"You have no Potions of Strength.")
                return False
        elif item_type == 'Healing':
            if self.potions_of_healing > 0:
                print(f"You have {self.potions_of_healing} Potions of Healing")
                return True
            else:
                print(f"You have no potions of healing.")
                return False
        elif item_type == 'Elixirs':
            if self.elixirs > 0:
                print(f"You have {self.elixirs} Clarifying Quantum Elixirs")
                return True
            else:
                print(f"You have no Elixirs.")
                return False
        elif item_type == 'Antidotes':
            if self.antidotes > 0:
                print(f"You have {self.antidotes} Vials of Antidote")
                return True
            else:
                print(f"You have no Vials of Antidote.")
                return False

    def inventory(self):
        self.hud()
        print(
            f"You are wielding: \nA {self.wielded_weapon.name}. Damage bonus: {self.wielded_weapon.damage_bonus}, "
            f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}")
        if self.shield.name != 'No Shield':
            print(f"A {self.shield.name}. Armor class: {self.shield.ac}")
        print(
            f"You are wearing:\n{self.armor.name}. Armor class: {self.armor.ac}, Armor bonus: {self.armor.armor_bonus}")
        print(f"{self.cloak.name}. Stealth: {self.cloak.stealth}")
        if self.ring_of_reg.name != 'No Ring':
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != 'No Ring':
            print(f"A Ring of Protection + {self.ring_of_prot.protect} ")
        print(f"On your belt, you are carrying:")
        print(f"A coil of rope")  # like indiana jones and his whip.
        if self.town_portals > 0 or self.potions_of_healing > 0 or \
                self.potions_of_strength > 0 or self.elixirs > 0 or self.antidotes > 0:
            if self.potions_of_strength > 0:
                print(f"{self.potions_of_strength} Potions of Strength")
            if self.potions_of_healing > 0:
                print(f"{self.potions_of_healing} Potions of Healing")
            if self.town_portals > 0:
                print(f"{self.town_portals} Town Portal Scrolls")
            if self.elixirs > 0:
                print(f"{self.elixirs} Clarifying Elixirs")
            if self.antidotes > 0:
                print(f"{self.antidotes} Vials of Antidote")

        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
        print(f"Your dungeoneer's pack contains:")

        current_items = []
        for each_item in item_type_lst:
            if len(self.pack[each_item]) > 0:
                current_items.append(each_item)
                self.item_type_inventory(each_item)  # call the item_type_inventory for each item in inv.
                # print(current_items)  # for testing
        if not len(current_items):
            print(f"Nothing but cobwebs..")
            pause()
            return  # False  # don't know if this false is needed.
        else:
            pause()
            return

    def found_weapon_substitution(self, found_item):
        if self.wielded_weapon.damage_bonus < (self.level * 2) or self.wielded_weapon.to_hit_bonus < 3:
            # found_item.damage_bonus = self.level
            if found_item.name == self.wielded_weapon.name:
                if self.wielded_weapon.damage_bonus < (self.level * 2):
                    self.wielded_weapon.damage_bonus += 1  # = found_item.damage_bonus + 1
                    print(f"Quantum wierdness fills the air...\nYour {self.wielded_weapon.name} "
                          f"damage bonus is enhanced to + {self.wielded_weapon.damage_bonus}!")
                    pause()
                    return
                elif self.wielded_weapon.to_hit_bonus < 3:
                    self.wielded_weapon.to_hit_bonus += 1  # = found_item.damage_bonus + 1
                    print(f"Quantum wierdness fills the air...\nYour {self.wielded_weapon.name} "
                          f"to-hit bonus is enhanced to + {self.wielded_weapon.to_hit_bonus}!")
                    pause()
                    return
            else:
                print(f"You have found a {found_item.name}. Damage bonus: {found_item.damage_bonus}. "
                      f"To-hit bonus: {found_item.to_hit_bonus}.")
                print(f"You are currently wielding a {self.wielded_weapon.name}. "
                      f"Damage bonus: {self.wielded_weapon.damage_bonus}. "
                      f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}.")
            while True:
                replace_weapon = input(f"Do you wish to wield the {found_item.name} instead? y/n: ").lower()
                if replace_weapon == 'y':
                    old_weapon = self.wielded_weapon
                    self.wielded_weapon = found_item
                    print(f"You are now wielding the {found_item.name}")
                    print(f"Damage bonus: {self.wielded_weapon.damage_bonus}. "
                          f"To-hit bonus: {self.wielded_weapon.to_hit_bonus}")
                    if not self.duplicate_item(old_weapon.item_type,
                                               old_weapon):  # old_weapon not in self.pack['Weapons']:
                        (self.pack[found_item.item_type]).append(old_weapon)
                        print(f"You place the {old_weapon.name} upon your back..")

                    else:
                        print(f"You drop the {old_weapon.name}.")
                    pause()
                    return
                elif replace_weapon == 'n':
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} on your back.")
                    else:
                        print(f"You choose not to wield the {found_item.name}, but you cannot carry any more weapons "
                              f"of this type. You leave it.")
                    pause()
                    return False
                elif replace_weapon not in ("y", "n"):
                    continue
        else:
            print(f"Wielded_weapon.damage_bonus already >= self.level * 2 and/or, to-hit == 3!!!")  # rm after testing
            pause()
            return

    def found_armor_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if self.armor.ac < found_item.ac:
            print(f"You have found {found_item.name}!! Armor Class: {found_item.ac}")
            print(f"Your current {self.armor.name} Armor Class: {self.armor.ac}")

            while True:
                replace_armor = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_armor == 'y':
                    old_armor = self.armor
                    self.armor = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(found_item.item_type, old_armor):
                        (self.pack[found_item.item_type]).append(old_armor)
                        print(f"You place the {old_armor.name} upon your back..")
                    else:
                        print(f"You drop your {old_armor.name}.")
                    pause()
                    return
                elif replace_armor == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type, found_item):
                        # if found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} on your back.")

                    else:
                        print(f"However, you cannot carry any more armor of this type. You leave it.")
                    pause()
                    return
                elif replace_armor not in ("y", "n"):
                    continue
        else:
            print(f"Worn armor >= found item...")  # remove after testing
            pause()  # remove after testing
            return

    def found_shield_substitution(self, sub_item):
        if self.shield.ac < sub_item.ac:
            print(f"You have found a {sub_item.name}!! Armor Class: {sub_item.ac}")
            if self.shield.name == 'No Shield':
                print(f"You currently hold no shield in your off hand.")
            else:
                print(f"Your current {self.shield.name} Armor Class: {self.shield.ac}")
            while True:
                replace_shield = input(f"Do you wish to wield the {sub_item.name} instead? y/n: ").lower()
                if replace_shield == 'y':
                    old_shield = self.shield
                    self.shield = sub_item
                    print(f"You are now wielding the {sub_item.name}")
                    self.calculate_armor_class()
                    if old_shield.name == 'No Shield':
                        pause()
                        return
                    elif not self.duplicate_item(old_shield.item_type,
                                                 old_shield):  # old_shield not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(old_shield)
                        print(f"You place the {old_shield.name} on your back..")
                    else:
                        print(f"You drop the old {old_shield.name}.")
                    pause()
                    return
                elif replace_shield == 'n':
                    print(f"You choose not to wield the {sub_item.name}.")
                    if not self.duplicate_item(sub_item.item_type,
                                               sub_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(sub_item)
                        print(f"You place the {sub_item.name} on your back.")

                    else:
                        print(f"However, you cannot carry any more shields of this type. You leave it.")
                    pause()
                    return
                elif replace_shield not in ("y", "n"):
                    continue
        else:
            print(f"Wielded shield >= found item...")  # remove after testing
            pause()
            return

    def found_boots_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if self.boots.ac < found_item.ac:
            print(f"You have found a pair of {found_item.name}!! Armor Class: {found_item.ac}")
            print(f"Your current {self.boots.name} Armor Class: {self.boots.ac}")
            while True:
                replace_boots = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_boots == 'y':
                    old_boots = self.boots
                    self.boots = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(old_boots.item_type,
                                               old_boots):  # old_boots not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_boots)
                        print(f"You place the {old_boots.name} in your dungeoneer's pack..")

                    else:
                        print(f"You drop your {old_boots.name}.")
                    pause()
                    return
                elif replace_boots == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place them in your dungeoneer's pack.")

                    else:
                        print(f"However, you cannot carry any more boots like this. You leave them.")
                    pause()
                    return
                elif replace_boots not in ("y", "n"):
                    continue
        else:
            print(f"Worn boots >= found item...")  # remove after testing
            pause()  # remove after testing
            return

    def found_cloak_substitution(self, found_item):

        if self.cloak.stealth < math.ceil(self.dexterity * .25):
            if found_item.name == self.cloak.name:
                # found_item.stealth += 1
                self.cloak.stealth += 1
                self.calculate_stealth()
                print(f"Quantum wierdness fills the air...\nYour {self.cloak.name} is enhanced to stealth +"
                      f" {self.cloak.stealth}!")

                pause()
                return
            else:
                print(f"You have found a {found_item.name}!! Stealth: {found_item.stealth}")
                print(f"Your current {self.cloak.name} Stealth: {self.cloak.stealth}")
            while True:
                replace_cloak = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_cloak == 'y':
                    old_cloak = self.cloak
                    self.cloak = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_stealth()
                    if not self.duplicate_item(old_cloak.item_type,
                                               old_cloak):  # old_cloak not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_cloak)
                        print(f"You place the {old_cloak.name} in your dungeoneer's pack..")
                    else:
                        print(f"You drop your {old_cloak.name}.")
                    pause()
                    return
                elif replace_cloak == 'n':
                    print(f"You choose not to wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} in your dungeoneer's pack.")
                    else:
                        print(f"You cannot carry any more cloaks like this. You leave it.")  # can't carry any more
                    pause()
                    return
                elif replace_cloak not in ("y", "n"):
                    continue
        else:
            print(f"Stealth already >= .25 * dex...")  # remove after testing
            pause()  # remove after testing
            return

    def found_ring_of_reg_substitution(self, found_item):

        if self.ring_of_reg.name == default_ring_of_regeneration.name:
            # self.ring_of_regeneration and default class object has 0 regenerate
            self.ring_of_reg = found_item
            print(f"Quantum wierdness fills the air...")
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate} appears on your finger!")
            sleep(1)
            print(f"It becomes permanently affixed..fused to your flesh and bone!")
            self.regenerate()  # this is fair. this could save you from poison or necrosis
            pause()
            return

        elif self.ring_of_reg.regenerate < math.ceil(self.maximum_hit_points * .17):
            # old_ring = self.ring_of_reg
            self.ring_of_reg.regenerate = (self.ring_of_reg.regenerate + 1)
            print(f"Quantum wierdness fills the air...")
            print(f"Your {ring_of_regeneration.name} is enhanced to + {self.ring_of_reg.regenerate} !")
            pause()
            return

        else:
            print("Ring of reg already equal to or more than 17% of max hit points")  # remove after testing
            pause()  # remove after testing
            return

    def found_ring_of_prot_substitution(self, found_item):

        if self.ring_of_prot.name == default_ring_of_protection.name:  # default ring is transparent placeholder
            self.ring_of_prot = found_item
            # (self.pack[found_item.item_type]).append(found_item) you can't sell rings. new rule
            print(f"Quantum wierdness fills the air...")
            print(f"A Ring of Protection + {self.ring_of_prot.protect} appears on your finger!")
            sleep(1)
            print(f"Tunneling through realities, it permanently fuses to flesh and bone!")
            pause()
            return

        elif self.ring_of_prot.protect < math.ceil(self.wisdom * .20):
            self.ring_of_prot.protect += 1
            print(f"Quantum wierdness fills the air...")
            print(f"Your {ring_of_protection.name} is enhanced to + {self.ring_of_prot.protect} !")
            pause()
            return

        else:
            print("Ring of prot already equal to or more than 20% of wisdom")  # remove after testing
            pause()  # remove after testing
            return

    def loot(self):
        # Called from main loop

        if self.encounter < 21:  # regular monster
            loot_difficulty_class = 1  # 10
            treasure_chest_difficulty_class = 20
        else:  # boss
            loot_difficulty_class = 8
            treasure_chest_difficulty_class = 16

        # chance to get treasure chest
        possible_treasure_chest = dice_roll(1, 20)
        if self.encounter < 21:  # regular monster
            if possible_treasure_chest >= treasure_chest_difficulty_class:
                self.treasure_chest()
                return
        else:  # boss. function then continues to give regular loot after treasure chest
            if possible_treasure_chest >= treasure_chest_difficulty_class:
                self.treasure_chest()

        # regular loot
        loot_dict = new_top_level_loot_dict
        while True:
            # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
            loot_roll = dice_roll(1, 20)
            self.hud()
            print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
            pause()
            # item_class = random.choice(list(loot_dict.keys()))
            # new_item_instance = random.choice(loot_dict[item_class])()  # Calling class __init__ method
            if loot_roll >= loot_difficulty_class:
                key = random.choice(list(loot_dict.keys()))
                # rndm_item_index = random.randrange(len(loot_dict[key]))
                # found_item = loot_dict[key][rndm_item_index]
                found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                print(found_item)  # REMOVE AFTER TESTING *****************************************************

                if self.level >= found_item.minimum_level:
                    if found_item.item_type == 'Armor':
                        self.found_armor_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Shields':
                        self.found_shield_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Cloaks':
                        self.found_cloak_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Weapons':
                        self.found_weapon_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Regeneration':
                        self.found_ring_of_reg_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Protection':
                        self.found_ring_of_prot_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Boots':
                        self.found_boots_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Town Portal Implements':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.town_portals += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Healing':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_healing += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Potions of Strength':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_strength += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Elixirs':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.elixirs += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Antidotes':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.antidotes += 1
                        pause()
                        continue

                else:
                    print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                    pause()  # remove after testing
                    continue
            else:
                # extra chance for potion. this makes it a little too easy. consider restoring it with lower chances
                """extra_chance = dice_roll(1, 20)
                if extra_chance >= 11  # loot_difficulty_class:
                    print(f"You see a potion of healing!")
                    sleep(.5)
                    print(f"You grab it..")
                    self.potions_of_healing += 1
                    pause()
                    # continue
                self.hud()"""
                self.hud()
                return  # self.dungeon_description()

    def treasure_chest(self):
        # called from treasure_chest_event(),
        # also called from from loot()
        successful_tries = 0
        print(f"You see a treasure chest!")
        sleep(1.5)
        gold_roll = dice_roll(1, 20) * self.dungeon.level + 1
        print(f"Inside is {gold_roll} gold pieces!")
        self.gold += gold_roll
        sleep(1.5)
        pause()
        loot_difficulty_class = 7
        loot_dict = new_top_level_loot_dict
        while True:
            # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
            loot_roll = dice_roll(1, 20)
            self.hud()
            # print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
            # pause()
            if loot_roll >= loot_difficulty_class:
                successful_tries += 1
                key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                # rndm_item_index = random.randrange(len(loot_dict[key]))
                # found_item = loot_dict[key][rndm_item_index]
                found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                print(found_item)  # REMOVE AFTER TESTING *****************************************************
                if self.level >= found_item.minimum_level:
                    if found_item.item_type == 'Armor':
                        self.found_armor_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Shields':
                        self.found_shield_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Cloaks':
                        self.found_cloak_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Weapons':
                        self.found_weapon_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Regeneration':
                        self.found_ring_of_reg_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Protection':
                        self.found_ring_of_prot_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Boots':
                        self.found_boots_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Town Portal Implements':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.town_portals += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Healing':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_healing += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Potions of Strength':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_strength += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Elixirs':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.elixirs += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Antidotes':
                        print(f"You see a {found_item.name}!")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.antidotes += 1
                        pause()
                        continue
                else:
                    print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                    pause()  # remove after testing
                    continue
            else:
                if successful_tries == 0:
                    print(f"Besides the gold, there remains nothing but cobwebs...")
                    sleep(1)
                    pause()
                return

    def treasure_chest_event(self):
        # called from event_logic()
        # the treasure_chest_event() is explicitly placed in the dungeon object at specific coordinates.
        # Calls treasure_chest()
        # treasure_chest() can also be called from loot() and awarded after battle
        treasure_chest_discovery = f"level {self.dungeon.level} treasure chest"
        if treasure_chest_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(treasure_chest_discovery)
            return self.treasure_chest()

        else:
            self.dungeon_description()
            print(f"There is an empty treasure chest here.")
            # print(f"An empty treasure chest lies at your feet.")
            pause()
            return

    def quantum_treasure_chest_event(self):
        # called from event_logic()
        # quantum_treasure_chest_event is explicitly placed in the dungeon object at specific coordinates
        successful_tries = 0
        quantum_treasure_chest_discovery = f"level {self.dungeon.level} quantum treasure chest"
        if quantum_treasure_chest_discovery not in self.discovered_interactives:
            print(f"You see a treasure chest with a Quantum lock!")
            sleep(1)
            print(f"You feel dangerous levels of energy surging from it..")
            sleep(1)
            lock_dc = 10
            while True:
                prompt = input("Do you wish to attempt to (U)nlock it with your Quantum knowledge or (I)gnore (U/I): ")
                if prompt == 'i':
                    return
                if prompt == 'u':
                    break
                self.hud()
            quantum_roll = dice_roll(1, 20)
            total = quantum_roll + self.wisdom_modifier
            print(f"Quantum Ability Check Roll: {quantum_roll}")
            sleep(.5)
            print(f"Wisdom Modifier: {self.wisdom_modifier}")
            sleep(.5)
            print(f"Total: {total}")
            sleep(.5)
            print(f"Difficulty Class: {lock_dc}")
            sleep(.5)
            if total >= lock_dc:
                print(f"Success!")
                sleep(1.5)
                gold_roll = (dice_roll(1, 20) * self.dungeon.level) + 1
                print(f"Inside is {gold_roll} gold pieces!")
                self.gold += gold_roll
                sleep(1.5)
                pause()
                loot_difficulty_class = 7
                loot_dict = new_top_level_loot_dict
                while True:
                    # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ***********
                    loot_roll = dice_roll(1, 20)
                    self.hud()
                    print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
                    pause()
                    if loot_roll >= loot_difficulty_class:
                        successful_tries += 1
                        key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                        # rndm_item_index = random.randrange(len(loot_dict[key]))
                        # found_item = loot_dict[key][rndm_item_index]
                        found_item = random.choice(loot_dict[key])()  # Calling class __init__ method
                        print(found_item)  # REMOVE AFTER TESTING ****************************************************
                        if found_item.minimum_level - self.level <= 2:
                            if found_item.item_type == 'Armor':
                                self.found_armor_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Shields':
                                self.found_shield_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Cloaks':
                                self.found_cloak_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Weapons':
                                self.found_weapon_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Rings of Regeneration':
                                self.found_ring_of_reg_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Rings of Protection':
                                self.found_ring_of_prot_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Boots':
                                self.found_boots_substitution(found_item)
                                continue
                            elif found_item.item_type == 'Town Portal Implements':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.town_portals += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Healing':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.potions_of_healing += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Potions of Strength':
                                print(f"You see a {found_item.name} !")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.potions_of_strength += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Elixirs':
                                print(f"You see a {found_item.name}!")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.elixirs += 1
                                pause()
                                continue
                            elif found_item.item_type == 'Antidotes':
                                print(f"You see a {found_item.name}!")
                                sleep(.5)
                                print(f"You snarf it..")
                                self.antidotes += 1
                                pause()
                                continue
                        else:
                            print(f"You see {found_item.a_an} {found_item.name}.")
                            sleep(1)
                            print(f"Even with the Quantum Weirdness of the chest, you are unable to use it.")
                            sleep(1)
                            pause()
                            continue
                    else:
                        # done with loot
                        if successful_tries == 0:
                            print(f"Besides the gold, there remains nothing but cobwebs...")
                            sleep(1)
                            pause()
                        # add chest to discovered interactives list, so it is no longer interactive
                        self.discovered_interactives.append(quantum_treasure_chest_discovery)
                        self.hud()
                        return  # self.dungeon_description()
            else:
                print(f"Your innate Quantum understanding has failed you.")
                sleep(1)
                print(f"You are unable to open the Quantum lock...")
                sleep(1)
                print(f"A wave of Quantum energy shoots toward you!")
                damage = dice_roll(self.level, self.hit_dice)
                self.reduce_health(damage)
                print(f"You suffer {damage} hit points!")
                pause()
                return
        else:
            print(f"There is an empty Quantum treasure chest here.")
            pause()
            return

    def increase_random_ability(self):
        # I was unable to come up with this code on my own.
        # Thanks to Angus Nicolson from Stack Overflow!
        # By editing player.__dict__ directly,
        # or a variable which you derived from it (ability_dict in the code below),
        # you can edit your object's attributes.
        # create a dictionary from self.__dict__
        # Note: Editing ability_dict_subset will not change the object's attributes,
        # because it was made from a dict comprehension.
        # You need to edit self.__dict__ or ability_dict.
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Choose random attribute name
        random_attribute = random.choice(list(ability_dict_subset.keys()))
        print(f"Weird Quantum forces surge through your body..")
        sleep(1.5)
        print(f"You have gained unnatural {random_attribute}!")
        ability_dict[random_attribute] += 1
        self.calculate_modifiers()
        pause()

    def decrease_random_ability(self):
        # I was unable to come up with this code on my own.
        # Thanks to Angus Nicolson from Stack Overflow!
        # By editing player.__dict__ directly,
        # or a variable which you derived from it (ability_dict in the code below),
        # you can edit your object's attributes.
        # create a dictionary from self.__dict__
        # Note: Editing ability_dict_subset will not change the object's attributes,
        # because it was made from a dict comprehension.
        # You need to edit self.__dict__ or ability_dict.
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Choose random attribute name
        random_attribute = random.choice(list(ability_dict_subset.keys()))
        print(f"You feel as though you have been robbed at the most visceral level..")
        sleep(1.5)
        print(f"Your {random_attribute} has dropped!")
        ability_dict[random_attribute] -= 1
        self.calculate_modifiers()
        pause()

    def increase_lowest_ability(self):
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Find the minimum attribute name
        min_attribute = min(ability_dict_subset, key=ability_dict_subset.get)
        print()  # remove after testing
        print(f"Weird sensations surge through your body..")
        sleep(1.5)
        print(f"You have gained {min_attribute}!")
        # Add one to min attribute
        ability_dict[min_attribute] += 1
        self.calculate_modifiers()
        pause()

    def decrease_lowest_ability(self):
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Find the minimum attribute name
        min_attribute = min(ability_dict_subset, key=ability_dict_subset.get)
        # print(min_attribute)  # remove after testing
        print(f"Weird discomfort surges through your body..")
        sleep(1.5)
        print(f"You have lost {min_attribute}!")
        # subtract one from min attribute
        ability_dict[min_attribute] -= 1
        self.calculate_modifiers()
        pause()

    def wicked_queen_event(self):
        # called from event_logic()
        wicked_queen_discovery = f"level {self.dungeon.level} wicked queen"
        if wicked_queen_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(wicked_queen_discovery)
            cls()
            print_txt_file('queen_splash.txt')
            pause()
            cls()
            print(f"She smiles and flashes a forked tongue between gleaming fangs. Her impossibly smooth, milky-white"
                  f"\nskin shimmers beneath the torchlight. On her head sits a crown of many skulls. Her raven-black\n"
                  f"hair shines gloriously. Every muscle, vein, and bone of her lovely flesh draw you to her."
                  f"\nYou cannot help but stare at her regal face, with her strong jawline, black, pouting lips"
                  f" and eyes of\n"
                  f"deep obsidian. \'How could such beauty exist?', you find yourself marveling aloud!\n"
                  f"The undead queen hears you and looks straight at you with pure, wicked pride, her head held high."
                  f"\n")
            pause()
            return "Wicked Queen"
        else:
            return

    def legendary_monster_event(self):
        # called from event_logic()
        mini_boss_discovery = f"level {self.dungeon.level} mini boss"
        if mini_boss_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(mini_boss_discovery)
            return "Legendary Monster"
        else:
            return

    def elite_monster_event(self):
        # called from event_logic()
        micro_boss_discovery = f"level {self.dungeon.level} micro boss"
        if micro_boss_discovery not in self.discovered_interactives:
            self.discovered_interactives.append(micro_boss_discovery)
            return "Elite Monster"
        else:
            return

    def altar_event(self):
        altar_discovery = f"level {self.dungeon.level} altar"
        if altar_discovery not in self.discovered_interactives:
            rndm_occurrence_lst = [undead_prophet_returns, self.increase_random_ability, self.decrease_random_ability,
                                   undead_prophet_returns, self.increase_lowest_ability,
                                   self.lose_items, undead_prophet_returns, self.heal_event, undead_prophet_returns]
            rndm_occurrence = random.choice(rndm_occurrence_lst)

            rndm_altar_descriptions = ['There is a worn and crumbling altar of stone here. Carved into its\n'
                                       'cold surface are faded symbols from disgusting ancient religions.',
                                       'Here stands an altar of stone which has been abandoned long ago.\n'
                                       'Ancient and horrible religious symbols, now illegible, cover its cold surface.',
                                       'There is a mysterious, ancient, crumbling stone altar here.\n'
                                       'Inscribed upon its surface are countless half-worn\n'
                                       'disgusting symbols left behind by civilizations past.']
            rndm_altar_description = random.choice(rndm_altar_descriptions)
            print(f"{rndm_altar_description}")
            print(f"Along its sides are embedded ornate golden sculptures.")
            print(f"You shudder to think of the innocent lives lost to its many\n"
                  f"horrible false prophets and priests, now long dead.")
            throne_action = input(
                f"(R)emove gold, attempt to (D)emolish the altar, (V)andalize,  or (I)gnore: ").lower()
            if throne_action == 'v':
                print(f"With the hilt of your {self.wielded_weapon.name} you violate the ancient site\n"
                      f"with a bold warning message to any who would dare to revisit such evils upon the world...")
                sleep(1.5)
                print(f"As you finish, you stand to admire your work..")
                sleep(1.5)
                return rndm_occurrence()
            elif throne_action == 'r':
                difficulty_class = 14
                remove_gold_roll = dice_roll(1, 20)
                if remove_gold_roll + self.intelligence_modifier > difficulty_class:
                    gold_value = (random.randint(1, 5) * self.dungeon.level)
                    print(f"The sculpture comes out, though not without difficulty or damage.")
                    sleep(1)
                    print(f"It is worth {gold_value} GP!")
                    self.gold += gold_value
                    pause()
                    return
                else:
                    return "Undead Prophet"  # undead_prophet_returns()
            elif throne_action == 'd':
                print(f"Removing the hammer from your pack, you begin hacking at the crumbling stone..")
                primary_difficulty_class = 15
                demolish_roll = dice_roll(1, 20)
                if demolish_roll + self.strength_modifier > primary_difficulty_class:  # strength to topple
                    print(f"You succeed in toppling the upper portion!")
                    sleep(1)
                    print(f"Using your rope and timbers from the refuse, you set up rigging.\n"
                          f"Then, with minimal effort, you are able to pull the foundation stones out.")
                    sleep(1.5)
                    print(f"You successfully demolish the altar!")
                    sleep(1.5)
                    self.discovered_interactives.append(altar_discovery)
                    pause()
                    self.hud()
                    return self.increase_random_ability()
                else:
                    return "Undead Prophet"  # undead_prophet_returns()

            else:
                return  # ignore the altar
        else:
            print(f"The remains of a demolished ancient altar are here..Who would dare?")
            pause()
            return

    def throne_event(self):
        # because the throne has been stolen and repurposed by many kingdoms, it remains infinitely interactive.
        # however, the gems may only be pried once.
        # throne_discovery = f"level {self.dungeon.level} throne" # uncomment to only allow 1 interaction
        rndm_occurrence_lst = [nothing_happens, king_returns, self.increase_random_ability, self.teleporter_event,
                               nothing_happens, king_returns, self.increase_lowest_ability, self.lose_items,
                               king_returns, nothing_happens, self.heal_event, king_returns,
                               self.decrease_random_ability,
                               self.decrease_lowest_ability]
        rndm_occurrence = random.choice(rndm_occurrence_lst)
        rndm_throne_descriptions = ['There is a magnificent, gem-encrusted throne of gold here. Throughout its\n'
                                    'shimmering surface are countless runes and symbols.',
                                    'In the center of the room stands a majestic throne encrusted with many\n'
                                    'gems and jewels, all laid in gold. Ancient runes cover its glimmering surface.',
                                    'A great, golden throne, replete with many gems and inscribed with countless '
                                    'runes stands here.']
        rndm_throne_description = random.choice(rndm_throne_descriptions)
        print(f"{rndm_throne_description}")
        print(f"Judging by the sheer number of unique origins of the runes, this throne was undoubtedly")
        print(f"stolen from, and reclaimed by many different ancient kings, now long dead.")
        # pause()
        # if throne_discovery not in self.discovered_interactives:  # uncomment to only allow 1 interaction
        throne_action = input(f"(P)ry gems, attempt to (R)ead the Runes, (S)it on the throne or (I)gnore: ").lower()
        if throne_action == 's':
            print(f"You sit on the throne...")
            # self.discovered_interactives.append(throne_discovery)  # uncomment to only allow 1 interaction
            sleep(1.5)
            # self.regenerate()  # testing
            return rndm_occurrence()
            # return "King Boss"
        elif throne_action == 'p':
            gems_pried = f"level {self.dungeon.level} gems pried from throne"
            if gems_pried not in self.discovered_interactives:
                difficulty_class = 12
                pry_roll = dice_roll(1, 20)
                if pry_roll > difficulty_class:
                    gem_value = (random.randint(1, 15) * self.dungeon.level)
                    print(f"They pop out into your greedy hands!")
                    sleep(1.5)
                    print(f"They are worth {gem_value} GP!")
                    self.gold += gem_value
                    self.discovered_interactives.append(gems_pried)
                    pause()
                    return
                else:
                    return "King Boss"  # king_returns()
            else:
                print(f"There are no gems left to pry...")
                pause()
        elif throne_action == 'r':
            difficulty_class = 15
            read_roll = dice_roll(1, 20)
            if read_roll + self.wisdom_modifier > difficulty_class:  # wisdom to recognize language
                print(f"You recognize the ancient language!")
                sleep(1)
                translate = input(f"Do you want to attempt to translate it into the common tongue? (y/n): ").lower()
                if translate == 'y':
                    difficulty_class = 8
                    translate_roll = dice_roll(1, 20)
                    if translate_roll + self.intelligence_modifier > difficulty_class:  # intelligence to translate
                        rndm_ancient_wisdom = ["Do not withhold good from those to whom you should give it\n"
                                               "If it is within your power to help.",
                                               "Do not plot harm against your "
                                               "neighbor when he lives in a sense of security with you.",
                                               "The wise will inherit honor, but the stupid ones glorify "
                                               "dishonor.",
                                               "Do not enter the path of the wicked, and do not walk in "
                                               "the way of evil men.\nShun it, do not take it; "
                                               "Turn away from it, and pass it by.",
                                               "The way of the wicked is like "
                                               "the darkness;\nThey do not know what makes them stumble.",
                                               "Above all the things that you guard, safeguard your heart, "
                                               "For out of it are the sources of life.",
                                               "Drink water from your own "
                                               "cistern\nAnd flowing water from your own well."]
                        rndm_wisdom = random.choice(rndm_ancient_wisdom)
                        print(f"The literal translation is, '{rndm_wisdom}...'")
                        pause()
                        return self.increase_random_ability()
                    else:
                        return "King Boss"  # king_returns()  # unable to translate
                else:
                    return  # player chooses not to translate
            else:
                return "King Boss"  # king_returns()  # player unable to recognize runes
        else:
            return  # ignore the throne

    def heal_event(self):
        # healing event called from fountain
        hit_point_overage = ((6 * self.dungeon.level) + 1)
        print(f"You feel vitality bubbling up within you...")
        sleep(1.5)
        if self.poisoned or self.necrotic:
            print(f"Your flesh no longer crawls with agony..")
            sleep(1)
            self.poisoned = False
            self.poisoned_turns = 0
            self.necrotic = False
            self.necrotic_turns = 0
            print(f"The foul corruption leaves your body..")
            sleep(1)
        if self.hit_points < self.maximum_hit_points:
            print(f"The restorative powers heal you to full strength!")
            sleep(1)
            self.hit_points = self.maximum_hit_points
        else:
            self.hit_points += hit_point_overage
            print(f"Your hit points have been unnaturally raised to {self.hit_points}!")
            sleep(1)
            print(f"You wonder how long this advantage will last..")
            sleep(1)
        pause()
        return

    def lose_items(self):
        # pack items get lost first, then if belt_items_to_lose sum > 0, belt items get lost
        belt_item_types_to_lose = [self.potions_of_strength, self.potions_of_healing,
                                   self.town_portals, self.elixirs, self.antidotes]
        available_item_types_to_lose = []
        for i in self.pack.keys():  # gather all available
            if len(self.pack[i]) > 0:  # item types to lose based on player's current item TYPES and put them
                available_item_types_to_lose.append(i)  # in available_item_types_to_lose = []
        if len(available_item_types_to_lose) > 0:
            item_type = random.choice(available_item_types_to_lose)  # Get random item *TYPE* you want to "steal"
            if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type"
                # pop random item from that item type. -1 because indexes start at 0
                lost_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                print(f"Your load feels lighter..")
                sleep(1)
                print(f"The {lost_item.name} from your dungeoneer's pack is gone!")  # from your {item_type}")
                pause()
                return
        elif sum(belt_item_types_to_lose) > 0:
            # elif self.potions_of_strength > 0 or self.potions_of_healing > 0
            # or self.town_portals > 0 or self.elixirs > 0:
            item_string = ""
            # Define list of attributes you are allowed to change
            self_dict = self.__dict__  # create variable as actual copy of player dict attribute
            stealing_lst = []
            # the working dict and 'for' loop just takes the place of many 'if:' statements
            working_dict = {'potions_of_strength': self.potions_of_strength,
                            'potions_of_healing': self.potions_of_healing,
                            'town_portals': self.town_portals, 'elixirs': self.elixirs,
                            'antidotes': self.antidotes}
            # add all items > 0 in working dict to stealing list
            for key, value in working_dict.items():
                if value > 0:
                    stealing_lst.append(key)
            random_stolen_item = random.choice(stealing_lst)
            # I am proud of this next bit of code :)
            grammar_dict = {'potions_of_strength': 'potion of strength',
                            'potions_of_healing': 'potion of healing',
                            'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir',
                            'antidotes': 'vial of antidote'}
            for key, value in grammar_dict.items():
                if random_stolen_item == key:
                    item_string = value
            print(f"Your load feels lighter...")
            sleep(1)
            print(f"A {item_string} has disappeared from your belt!")
            self_dict[random_stolen_item] -= 1
            pause()
            return
        else:
            return nothing_happens()  # pack and belt inventory empty

    def fountain_event(self):
        # WHITE GREEN CLEAR RED BLACK
        # telengard has these 5 random events:
        # heal 3 * dungeon level + 1 hit points
        # poison 3 * dungeon level + 1 hit points
        # drunk
        # lose items
        # increase num of spells: Magic power SURGES through your body
        water_colors = ['white', 'green', 'bright green ', 'crystal clear',
                        'deep red', 'red', 'black', 'pitch black']
        water_color = random.choice(water_colors)
        print(f"A fountain flowing with {water_color} water is here.")
        sleep(1)
        print(f"The tranquil sound eases your mind.")
        sleep(1)
        drink = input(f"Do you wish to drink? ").lower()
        if drink == 'y':
            rndm_occurrence_list = [nothing_happens, self.recover_quantum_energy, self.poison_ingestion,
                                    self.increase_random_ability, self.lose_items, self.decrease_random_ability,
                                    self.increase_lowest_ability, self.heal_event, nothing_happens,
                                    self.decrease_lowest_ability]
            rndm_occurrence = random.choice(rndm_occurrence_list)
            rndm_occurrence()
        else:
            print("Ignore.")
            sleep(.25)
            return

    def teleporter_event(self):
        print(f"Zzzzzzap....You've been teleported.....")
        sleep(2)
        # self.dungeon_key += 1  # this will become random.randint(1, deepest dungeon level) in future
        # self.dungeon = dungeon_dict[self.dungeon_key]
        # self.x = random.randint(1, 18)
        # self.y = random.randint(1, 18)
        (self.x, self.y) = self.dungeon.teleporter_landing
        self.coordinates = (self.x, self.y)  # beta
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = self.dungeon.grid[self.y][self.x]
        # self.regenerate()  # testing
        # self.position = 0
        pause()
        self.hud()
        return

    def pit_event(self):
        # falling into pits lands you on the same dungeon level at the dungeon.pit_landing coordinates
        print(f"The ground here is slippery, and quite unsteady..")
        sleep(1.5)
        print(f"You see a pit..")
        sleep(1.5)
        pit_difficulty_class = 9
        pit_outcome = dice_roll(1, 20)
        if (pit_outcome + self.dexterity_modifier + self.intelligence_modifier) > pit_difficulty_class:
            print(f"It appears to be about 3 fathoms deep.")
            sleep(1)
            descend_or_not = input(f"Do you wish to descend (y/n)?: ").lower()
            if descend_or_not == 'y':
                self.in_a_pit = True
                print(f"Retrieving the rope from your belt, you deftly repel down the slick, "
                      f"treacherous pit walls.")
                # self.dungeon_key += 1
                # self.dungeon = dungeon_dict[self.dungeon_key]
                (self.x, self.y) = self.dungeon.pit_landing
                self.coordinates = (self.x, self.y)  # beta self.dungeon.pit_landing
                self.previous_x = self.x
                self.previous_y = self.y
                self.position = self.dungeon.grid[self.y][self.x]
                pause()
                self.hud()
                print(f"You have landed at the bottom of a pit. The foul, humid air hangs in a mist around you.")
                # print(self.dungeon.pit_intro)
                self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
                pause()
                return
            else:
                return
        else:
            print(f"The ground beneath your feet collapses!")
            sleep(1)
            # print(f"Desperately, you grope for a crag!")
            # sleep(1)
            # removed this code. now, either you fall in or you don't
            # if dice_roll(1, 20) >= 15:
            #    print(f"You succeed!")
            #    pause()
            #    return
            # else:
            self.in_a_pit = True
            print(f"You fall in!")
            damage = dice_roll(1, (3 * self.dungeon.level))  # dice_roll(1, self.dungeon.level)
            self.hit_points -= damage
            sleep(1)
            print(f"You suffer {damage} hit points..")
            sleep(1)
            pause()
            # falling into pits lands you on the same dungeon level, at the dungeon.pit_landing coordinates
            # self.dungeon_key += 1  # this can be used to land you on the next level down
            # self.dungeon = dungeon_dict[self.dungeon_key]  # this can be used to land you on the next level down
            (self.x, self.y) = self.dungeon.pit_landing
            self.coordinates = (self.x, self.y)  # beta
            self.previous_x = self.x
            self.previous_y = self.y
            self.position = self.dungeon.grid[self.y][self.x]
            self.hud()
            print(f"You have landed at the bottom of the pit. The foul, humid air hangs in a mist around you.")
            # print(self.dungeon.pit_intro)
            self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
            pause()
            return

    def staircase_description(self):
        # called from dungeon_description()
        # this is a 'description' of the spiral staircase, if player navigates to it *after* the map is initialized
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"The spiral staircase entrance to {self.dungeon.name} is here.")
        if self.dungeon.level > 1:
            previous_place = f"dungeon level {self.dungeon.level - 1}"
        else:
            previous_place = f"the town of Fieldenberg"
        print(f"The stairs lead up to {previous_place}. However, there is no returning;\n"
              f"The door has been locked and barricaded. You must continue onward!")

    def pit_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the pit landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"High above you is a wide, gaping hole leading up to "
              f"{self.dungeon.name}.")

    def elevator_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the elevator landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        # print(f"Mechanical Landing, {self.dungeon.name}")
        print(f"There is a landing for a mechanical contraption of ropes, pulleys and counterweights here.")
        print(f"The base is covered in an iron mesh, allowing the horribly foul air from deep below\n"
              f"{self.dungeon.casual_name} to escape to this level.")

    def teleporter_landing_description(self):
        # called from dungeon_description()
        # this is a 'description' of the teleporter landing.
        # it is not an 'event', since it is not really interactive, so it is called from dungeon_description()
        # and not from event_logic()
        print(f"The floor of {self.dungeon.name} has been scorched here, and there is a subtle, but discernible\n"
              f"bowl shape, about 3 yards across, which seems to have been perfectly carved from it.")

    def elevator_event(self):
        # elevators bring you 'up' from pits to main dungeon level: self.dungeon.elevator_landing
        # self.in_a_pit will be false at end of function
        # player must pass intelligence saving throw
        print(f"You feel a slight whirring..")
        sleep(1)
        difficulty_class = 9
        if dice_roll(1, 20) + self.intelligence_modifier >= difficulty_class:
            stay_or_jump = input(f"You see an elevation mechanism which can return you to the "
                                 f"main dungeon level.\nDo you wish to go back (U)p, or "
                                 f"(S)tay to explore this level further? ").lower()
            if stay_or_jump == 'u':
                print(f"A cage closes on your position.")
                sleep(1)
                print(f"You feel heavy for a moment..")
                sleep(2)
                self.hud()
                self.in_a_pit = False
                # self.dungeon_key -= 1  # this can be used for more powerful elevator, perhaps at advanced levels
                # self.dungeon = dungeon_dict[self.dungeon_key]  # when player has more experience?
                (self.x, self.y) = self.dungeon.elevator_landing
                self.coordinates = (self.x, self.y)
                self.previous_x = self.x
                self.previous_y = self.y
                self.position = self.dungeon.grid[self.y][self.x]
                print(f"You have arrived back at {self.dungeon.name}, dungeon level {self.dungeon.level}.")
                sleep(1)
                self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
                print(f"Watch your step.")
                sleep(1)
                pause()
                return
            else:
                return
        else:
            print(f"A cage closes upon you!")  # intelligence not enough to realize what is happening.
            sleep(1)
            print(f"You are being drawn upward!")
            sleep(2)
            self.hud()
            # self.dungeon_key -= 1
            # self.dungeon = dungeon_dict[self.dungeon_key]
            print(f"You have arrived back at {self.dungeon.name}, dungeon level {self.dungeon.level}.")
            sleep(2)
            self.in_a_pit = False
            (self.x, self.y) = self.dungeon.elevator_landing
            self.coordinates = (self.x, self.y)
            self.previous_x = self.x
            self.previous_y = self.y
            self.position = self.dungeon.grid[self.y][self.x]
            print(f"Watch your step.")
            sleep(1)
            self.dungeon_theme()  # dungeon_theme() method logic determines which musical theme to play
            pause()
            return

    def npc_defeats_monster_logic(self, monster, damage):
        # called from npc_attack_logic() to discern if npc defeats monster, and
        # monster dies mid-party-turn
        monster.reduce_health(damage)
        if monster.check_dead():
            self.hud()
            if self.encounter > 20:  # if fighting boss
                gong()
                if monster.proper_name != "None":
                    print(f"The party has vanquished {monster.proper_name}! "
                          f"You are victorious!")
                    self.vanquished_foes.append(monster.proper_name)
                else:
                    print(f"The party has vanquished the {monster.name}!")
                sleep(4)
                self.dungeon_theme()
            else:
                print(f"The party has defeated the {monster.name}..")

            return True
        else:
            return False

    def npc_attack_logic(self, monster):
        # called from main loop after player quantum or melee attack (or potion)
        if self.sikira_ally or self.vozzbozz_ally or self.torbron_ally or self.magnus_ally:
            victory = False
            if self.sikira_ally:
                if not sikira.retreating:
                    ally_dmg1 = self.npc_melee(sikira, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg1):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.torbron_ally:
                if not torbron.retreating:
                    ally_dmg2 = self.npc_melee(torbron, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg2):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.magnus_ally:
                if not magnus.retreating:
                    ally_dmg3 = self.npc_melee(magnus, monster.name, monster.armor_class)
                    if self.npc_defeats_monster_logic(monster, ally_dmg3):
                        victory = True
                        return victory
                    else:
                        victory = False

            if self.vozzbozz_ally:
                if not vozzbozz.retreating:
                    ally_dmg4 = self.vozzbozz_attack(monster)
                    if self.npc_defeats_monster_logic(monster, ally_dmg4):
                        victory = True
                        return victory
                    else:
                        victory = False

            return victory

        else:  # player has no NPC allies
            return

    def encounter_sikira_event(self):
        # called from event_logic()
        ally_discovery = f"level {self.dungeon.level} ally"
        rndm_orientation_lst = ["left", "right", "rear"]
        rndm_orientation = random.choice(rndm_orientation_lst)
        if ally_discovery not in self.discovered_interactives:
            # this is really an unnecessary check, but I decided to include it
            # just in case I forget to make level 21 monsters.
            if self.level < 20:
                monster_key = (self.level + 1)
            else:
                monster_key = self.level
            monster_cls = random.choice(monster_dict[monster_key])
            monster = monster_cls()
            self.hud()
            print(f"You see a beautiful Elven warrior here, battling an especially fierce {monster.name}.")
            print(f"Instinctively, you ready your {self.wielded_weapon.name} and rush to help.")
            print(f"The {monster.name} strikes at her wickedly, but she nimbly springs back, just out of reach.\n"
                  f"Noticing you, she motions to the {monster.name}'s {rndm_orientation} with a subtle twitch\n"
                  f"of her head, as she strikes back with her glorious, finely crafted sword.")
            pause()
            self.hud()
            print(f"Moving to the {monster.name}'s {rndm_orientation}, as directed, the {monster.name} suddenly"
                  f" senses your presence!\n"
                  f"{monster.attack_5_phrase}")
            print(f"The distraction serves as a perfect opportunity for attack, as she swings her great blade from\n"
                  f"a blind angle, felling her enemy with a single, precise cut. The {monster.name} falls dead\n"
                  f"without ever realizing it was in danger.")
            print(f"Placing your {self.wielded_weapon.name} on your back, you extend a hand. You remember a greeting\n"
                  f"that elves who visited Tinbar appreciated, and say, \'Well met, illuminated one!\'.")
            pause()
            self.hud()
            print(f"You immediately sense a shift in the air. The petite warrior's alabaster countenance falls to\n"
                  f"a twisted grimace and her crimson eyes burn with hate. Her blade is at your throat before you\n"
                  f"can even react. \'What did ye call me?\' she queries in a beautifully perfect voice, smoother\n"
                  f"than oil.")
            pause()
            self.hud()
            print(f"\'Forgive me, friend!\', you manage to respond. \'It was meant with deep respect! It is how\n"
                  f"elf-kind enjoy being greeted where I am from!..\'")
            print(f"\'I AM NOT ELF!\', she asserts, directly into your face. Your disarmed look speaks to your\n"
                  f"confusion, and she responds, \'I AM DROW! And I have no need of your assistance, nor of\n"
                  f"your life!\' You feel her blade move within a hair's breadth of your throat.")
            pause()
            self.hud()
            print(f"Again you plead, \'Please forgive my ignorance. I am from a far-off land. My name is {self.name}\n"
                  f"of Tinbar! My people and the Northern Library have all been destroyed by a terrible evil that\n"
                  f"I have been sent to seek out and destroy...she bears the mark of a crowned woman surrounded\n"
                  f"by skulls!\'")
            pause()
            self.hud()
            print(f"Her face and mood again shift, and she removes her blade and begins to smile! It is then that you\n"
                  f"begin to notice the signs you missed earlier; Her teeth, black and smooth as raven's claws,\n"
                  f"tiny fangs, deep red eyes and her unusually petite, yet athletic build. But how could a Drow have\n"
                  f"such purely white complexion, you wonder silently...Are they not grey-skinned?")
            pause()
            self.hud()
            print(f"\'Well. {self.name} of Tinbar, well met!\', she says with an evil chuckle. \'I am Si'Kira,\n"
                  f"Child of the Moon Forest. My people too, have all been slain. I also seek to destroy the\n"
                  f"wicked Queen Jannbrielle.\'. She sheathes her blade, and her long silver hair glistens gorgeously\n"
                  f"in the darkness, as does her wondrous armor.")
            pause()
            self.hud()
            print(f"\'Queen Jannbrielle..\', you repeat thoughtfully. Si'Kira looks at you as you say the name.\n"
                  f"\'I have met allies above who dare not even utter that word, and at last I learn it...\'\n"
                  f"\'Thank you for finally revealing the name of our common enemy, my good Drow!\' you say with\n"
                  f"a hint of humor.")
            pause()
            self.hud()
            print(f"Si'Kira laughs gleefully again. \'This is most interesting!\', she says, with sincere intrigue\n"
                  f"in her voice. \'How odd that our paths cross in such a way..and in such a place! I shall\n"
                  f"\'be accompanying you, {self.name} of Tinbar! For good or ill, we are bound in purpose and\n"
                  f"outcome.\'")
            pause()
            self.hud()
            print(f"\'I suppose..that settles it..?\', you say somewhat ironically.\n"
                  f"\'Aye. It does.\', says Si'Kira, plainly.")
            pause()
            self.hud()
            print(f"You cannot help but wish that you had a voice in the matter; Drow are notoriously wicked, and\n"
                  f"very clever, but you trust your instincts and move on, together.")
            self.sikira_ally = True
            pause()
        else:
            return

    def event_logic(self):
        # interactive events, items etc.
        # the event dictionary *key* is a tuple corresponding to
        # dungeon x y coordinates of an event or item e.g. (2, 3)
        # the event dictionary *value* is the corresponding player function.
        # if the player's coordinates exist as a key in event_dict,
        # the dictionary value is given the variable 'event_function'
        # finally, the proper function is called and any
        # function values are returned to the main program
        # using 'return event_function()'
        # monster_encounter = dice_roll(1, 20)
        self.coordinates = (self.x, self.y)
        event_dict = {self.dungeon.quantum_treasure_chest: self.quantum_treasure_chest_event,
                      self.dungeon.encounter_sikira: self.encounter_sikira_event,
                      self.dungeon.treasure_chest: self.treasure_chest_event,
                      self.dungeon.altar: self.altar_event,
                      self.dungeon.throne: self.throne_event,
                      self.dungeon.fountain: self.fountain_event,
                      self.dungeon.teleporter: self.teleporter_event,
                      self.dungeon.elevator: self.elevator_event,
                      self.dungeon.pit: self.pit_event,
                      self.dungeon.elite_monster: self.elite_monster_event,
                      self.dungeon.legendary_monster: self.legendary_monster_event,
                      self.dungeon.wicked_queen: self.wicked_queen_event,
                      self.dungeon.exit: self.dungeon_exit_event
                      }
        if self.coordinates in event_dict.keys():
            event_function = (event_dict[self.coordinates])  # (event_dict[self.coordinates])
            return event_function()
        else:
            return

        # NAVIGATION

    def town_navigation(self, player_name):
        if self.town_portal_exists or self.loaded_game:
            town_functions = input("(The Town of Fieldenberg)\n(S)ave, (Q)uit game, (R)estart game (I)nventory, "
                                   "(B)lacksmith, (C)hemist , (T)avern, or re-(E)nter dungeon --> ").lower()
        else:
            town_functions = input("(The Town of Fieldenberg)\n(S)ave, (Q)uit game, (R)estart game (I)nventory, "
                                   "(B)lacksmith, (C)hemist , (T)avern, or (E)nter dungeon --> ").lower()
        if town_functions == 'r':
            if are_you_sure():
                print("Restart")
                sleep(1.5)
                cls()
                self.in_town = False
                return "Restart"

        if town_functions == 'q':
            if are_you_sure():
                print(f"Exiting...")
                sleep(.5)
                cls()
                sys.exit()
        elif town_functions == 's':
            save_a_character = player_name + ".sav"
            if os.path.isfile(save_a_character):
                while True:
                    confirm_save = input(f"{player_name} already saved. Overwrite? (y/n) ").lower()
                    if confirm_save not in ('y', 'n'):
                        continue
                    elif confirm_save == 'n':
                        break
                    elif confirm_save == 'y':
                        print(f"Saving {self.name}...")
                        character_filename = self.name + ".sav"
                        with open(character_filename, 'wb') as player_save:
                            pickle.dump(self, player_save)
                            print(f"{self.name} saved.")
                            sleep(2)
                            break
            else:
                print(f"Saving {self.name}...")
                character_filename = self.name + ".sav"
                with open(character_filename, 'wb') as player_save:
                    pickle.dump(self, player_save)
                    print(f"{self.name} saved.")
                    sleep(2)

        elif town_functions == 'i':
            self.inventory()

        elif town_functions == 'b':
            print("You visit the blacksmith..")
            sleep(1.5)
            blacksmith_theme()
            self.blacksmith_main()
            town_theme()

        elif town_functions == 'c':
            print("You make your way to the chemist manipulator..")
            sleep(1.5)
            chemist_theme()
            self.chemist_main()
            town_theme()

        elif town_functions == 't':
            print(f"You make your way to the tavern..")
            sleep(1.25)
            tavern_theme()
            self.inn()
            town_theme()

        elif town_functions == 'e':
            # self.in_town = False
            # self.in_dungeon = True
            if self.town_portal_exists or self.loaded_game:
                print(f"You re-enter the portal.")
                # self.town_portal_exists = False  # beta 10/12/2022
            else:
                print("You make your descent..")
                # sleep(1)
                # print(f"BEWARE . . .")
            sleep(1)
            return 'e'

    def navigation(self, dungeon_command):
        if dungeon_command == 'w':
            self.hud()
            print("North")
            self.y -= 1
            sleep(.5)
            return
        elif dungeon_command == 'a':
            self.hud()
            print("West")
            self.x -= 1
            sleep(.5)
            return
        elif dungeon_command == 's':
            self.hud()
            print("South")
            self.y += 1
            sleep(.5)
            return
        elif dungeon_command == 'd':
            self.hud()
            print("East")
            self.x += 1
            sleep(.5)
            return
        elif dungeon_command == 'nw':
            self.hud()
            print("Northwest")
            self.y -= 1  # north
            self.x -= 1  # west
            sleep(.5)
            return
        elif dungeon_command == 'ne':
            self.hud()
            print("Northeast")
            self.y -= 1  # north
            self.x += 1  # east
            sleep(.5)
            return
        elif dungeon_command == 'se':
            self.hud()
            print("Southeast")
            self.y += 1  # south
            self.x += 1  # east
            sleep(.5)
            return
        elif dungeon_command == 'sw':
            self.hud()
            print("Southwest")
            self.y += 1  # south
            self.x -= 1  # west
            sleep(.5)
            return
        elif dungeon_command == 'l':
            # this will call dungeon_description().
            self.dungeon_description()
            self.coordinates = (self.x, self.y)
            self.position = self.dungeon.grid[self.y][self.x]
            return
        elif dungeon_command == 'map':
            self.display_map(self.dungeon.player_grid)  #
            pause()
            self.dungeon_description()
            return
        elif dungeon_command == 'm':
            self.item_management_sub_menu()
            return
        elif dungeon_command == 'i':
            self.inventory()
            return
        else:  # remove after testing
            print(f"This should be unreachable.")
            return

    def boss_clue_1(self):
        # player finds first clue about wicked queen boss
        self.hud()
        rndm_hint_list = ["a piece of parchment", "a torn piece of fabric", "a broken necklace", "a broken ring"]
        clue_item = random.choice(rndm_hint_list)
        print(f"On the ground before you lays {clue_item}. You carefully pick it up.")
        sleep(1)
        print(f"You see a symbol on it; A woman with a crown, surrounded by many skulls.")
        sleep(1)
        print(f"Without warning, it begins to deteriorate in your hands until it is nothing but ashes!")
        sleep(1)
        print(f"You ponder this, and commit the image to memory. You wonder if there is someone in town who can shed\n"
              f"light on the strange symbol.")
        pause()
        self.hud()
        self.boss_hint_1 = True
        return

    def boss_clue_2(self):
        self.hud()
        print("You see a nasty-looking knife in a hand-etched sheath of gold!")
        sleep(1)
        print("Turning it over in your hands reveals runes that are foreign to you, which cover its entire surface.")
        sleep(1)
        print(f"You carefully place the dagger on your belt.")
        pause()
        self.hud()
        self.boss_hint_2 = True
        return

    def boss_clue_3(self):
        self.hud()
        print("You hear the flapping of wings nearby...")
        sleep(1)
        print(f"You catch a glimpse of a flying creature overhead, just before it disappears into the darkness.")
        pause()
        self.hud()
        self.boss_hint_3 = True
        return

    def boss_clue_4(self):
        self.hud()
        print("You find a clue about the boss4")
        pause()
        self.hud()
        self.boss_hint_4 = True
        return

    def boss_hint_logic(self):
        # called from main loop, after exit bosses are defeated
        if not self.boss_hint_1:
            return self.boss_clue_1()
        if not self.boss_hint_2:
            return self.boss_clue_2()
        if not self.boss_hint_3:
            return self.boss_clue_3()
        if not self.boss_hint_4:
            return self.boss_clue_4()
        # if not self.boss_hint_5:
            # return self.boss_clue_5()
        # if not self.boss_hint_6:
            # eturn self.boss_clue_6()
        return

    def wide_open_space_logic(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        level_7_openness_phrase = f"This is a rather wide-open area of {self.dungeon.name}."
        level_8_openness_phrase = f"This is a wide open area of {self.dungeon.name}."
        if self.in_a_pit:
            level_7_openness_phrase = f"The pit seems rather wide open here."
            level_8_openness_phrase = f"The pit is wide open here."
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        perimeter = []
        if north_of_you != "*":
            perimeter.append("North")
        if south_of_you != "*":
            perimeter.append("South")
        if east_of_you != "*":
            perimeter.append("East")
        if west_of_you != "*":
            perimeter.append("West")
        if northeast_of_you != "*":
            perimeter.append("Northeast")
        if northwest_of_you != "*":
            perimeter.append("Northwest")
        if southeast_of_you != "*":
            perimeter.append("Southeast")
        if southwest_of_you != "*":
            perimeter.append("Southwest")
        openness = len(perimeter)
        if openness == 7:
            return level_7_openness_phrase
        if openness == 8:
            return level_8_openness_phrase
        else:
            return f"This is a non-descript area of {self.dungeon.name}."

    def atrium_check(self):
        # an atrium connects a corridor to a wide-open chamber.
        # called from automatic_dungeon_description_and_room_exit_finder() *after* intersection_check
        # this only works if intersection check is called first, and is False
        directions = []
        corridor_found = False
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        if northeast_of_you == "*" and northwest_of_you == "*" and north_of_you != "*":
            directions.append("Northern")
            corridor_found = True
            # return "Northern"
        if southeast_of_you == "*" and southwest_of_you == "*" and south_of_you != "*":
            directions.append("Southern")
            corridor_found = True
            # return "Southern"
        if northeast_of_you == "*" and southeast_of_you == "*" and east_of_you != "*":
            directions.append("Eastern")
            corridor_found = True
            # return "Eastern"
        if northwest_of_you == "*" and southwest_of_you == "*" and west_of_you != "*":
            directions.append("Western")
            corridor_found = True
            # return "Western"
        if corridor_found:
            return directions
        else:
            return False

    def intersection_check(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        northeast_of_you = self.dungeon.grid[self.y - 1][self.x + 1]
        northwest_of_you = self.dungeon.grid[self.y - 1][self.x - 1]
        southeast_of_you = self.dungeon.grid[self.y + 1][self.x + 1]
        southwest_of_you = self.dungeon.grid[self.y + 1][self.x - 1]
        if northeast_of_you == "*" and northwest_of_you == "*" and southeast_of_you == "*" and southwest_of_you == "*":
            return True
        else:
            return False

    def auto_intersection_description(self):
        # called from automatic_dungeon_description_and_room_exit_finder()
        intersection_name = self.dungeon.intersection_name
        if self.in_a_pit:
            intersection_name = self.dungeon.pit_intersection_name
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        if north_of_you != "*":
            exits_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        number_of_ways = len(exits_list)
        if number_of_ways > 1:
            # exits = convert_list_to_string_with_and(exits_list)
            description = f"You are in {intersection_name} which " \
                          f"forms a {number_of_ways}-way intersection."
            return description
        else:
            # this code is ostensibly unreachable
            exits = convert_list_to_string(exits_list)
            print(f"There appears to have been an intersection here at one time, but all except one corridor has "
                  f"collapsed. The only exit is to the {exits}")

    def automatic_dungeon_description_and_room_exit_finder(self):
        # I am very proud of this code. I wrote it all from scratch,
        # which is quite an accomplishment for me.
        # called from dungeon_description()
        multiple_corridors = False
        barrier_name = self.dungeon.barrier_name
        barrier_name_plural = self.dungeon.barrier_name_plural
        corridor_phrase = self.dungeon.corridor_phrase
        corridor_name = self.dungeon.corridor_name
        large_atrium_phrase = self.dungeon.large_atrium_phrase
        one_walled_atrium_phrase = self.dungeon.one_walled_atrium_phrase
        if self.in_a_pit:
            barrier_name = self.dungeon.pit_barrier_name
            barrier_name_plural = self.dungeon.pit_barrier_name_plural
            corridor_phrase = self.dungeon.pit_corridor_phrase
            corridor_name = self.dungeon.pit_corridor_name
            large_atrium_phrase = self.dungeon.pit_large_atrium_phrase
            one_walled_atrium_phrase = self.dungeon.pit_one_walled_atrium_phrase

        corridor_direction = ""
        auto_description_phrase = ""
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        walls_list = []

        if north_of_you != "*":
            exits_list.append("North")
        else:
            walls_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        else:
            walls_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        else:
            walls_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        else:
            walls_list.append("West")
        number_of_exits = len(exits_list)
        number_of_walls = len(walls_list)

        if number_of_walls == 0:  # 4-way intersection, large atrium, or wide-open area

            if not self.intersection_check():  # if you are not at an intersection

                if not self.atrium_check():  # and you are not in an atrium
                    auto_description_phrase = self.wide_open_space_logic()  # you must be in a wide open space

                else:  # you must be in a large atrium with 0 walls
                    auto_description_phrase = large_atrium_phrase
                    corridor_direction = self.atrium_check()

                    if len(corridor_direction) > 1:  # beta if more than 1 corridor
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)
                        multiple_corridors = True

                    else:  # only one corridor
                        corridor_direction = convert_list_to_string(corridor_direction)

            else:  # you must be at a 4-way intersection; intersections do not need to detect corridor_direction
                auto_description_phrase = self.auto_intersection_description()

        if number_of_walls == 1:  # 3-way intersection, wall-lined atrium, or against a wall

            if not self.intersection_check():  # if you are not at an intersection

                if not self.atrium_check():  # and you are not in an atrium lined with one wall
                    # you must be against a wall
                    direction = convert_list_to_string(walls_list)
                    auto_description_phrase = f"You are against {barrier_name} to the {direction}."

                else:  # you must be in an atrium lined with one wall
                    direction = convert_list_to_string(walls_list)
                    auto_description_phrase = f"{one_walled_atrium_phrase} The {direction} " \
                                              f"side is lined with {barrier_name}."
                    corridor_direction = self.atrium_check()

                    if len(corridor_direction) > 1:
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)
                        multiple_corridors = True

                    else:  # beta
                        corridor_direction = convert_list_to_string(corridor_direction)

            else:  # you must be at a 3-way intersection; intersections do not need to detect corridor_direction
                auto_description_phrase = self.auto_intersection_description()

        if number_of_walls == 2:  # corridor, corner, or corner-atrium
            e_w_walls = ['East', 'West']
            n_s_walls = ['North', 'South']

            # if there are walls to your east and west *or* to your north and south:
            if set(e_w_walls) == set(walls_list) or set(n_s_walls) == set(walls_list):  # you must be in a corridor:
                directions = convert_list_to_string_with_and(walls_list)
                auto_description_phrase = f"{corridor_phrase} " \
                                          f"There are {barrier_name_plural} to the {directions}."

            else:  # otherwise, you must be in a corner:
                directions = convert_list_to_string_with_and(walls_list)
                auto_description_phrase = f"You are in a corner. " \
                                          f"There are {barrier_name_plural} to the {directions}."

                if self.atrium_check():
                    corridor_direction = self.atrium_check()
                    # you can sometimes be in a corner and also be in an atrium. i.e. there are 2 proximal corridors.
                    # in that case, the atrium description is ignored, because it is not really an atrium
                    # by human definition, but corridor directions are still calculated:
                    if len(corridor_direction) > 1:
                        corridor_direction = convert_list_to_string_with_and(corridor_direction)  # beta
                        multiple_corridors = True

                    else:
                        corridor_direction = convert_list_to_string(corridor_direction)  # beta

        if number_of_walls == 3:  # 3 walls must be a dead end
            directions = convert_list_to_string_with_and(walls_list)
            auto_description_phrase = f"This is a dead end. " \
                                      f"There are {barrier_name_plural} to the {directions}."

        if number_of_walls == 4:  # this must never happen! :P
            directions = convert_list_to_string_with_and(walls_list)
            print(f"Ostensibly, you are in a cell. "
                  f"There are {barrier_name_plural} to the {directions}.\n"
                  f"You are completely trapped due to a programming error. The grid should never "
                  f"have been created\nwith coordinates that place you in such a predicament. "
                  f"Placing you back at staircase..")
            pause()
            (self.x, self.y) = self.dungeon.staircase
            self.coordinates = (self.x, self.y)
            return

        # finally, print auto_description_phrase and exits:
        if number_of_exits > 1:
            exits = convert_list_to_string_with_and(exits_list)
            print(f"{auto_description_phrase} Exits are to the {exits}.")

            # if there are corridors, calculate which exits lead to them and print out:
            if corridor_direction != "":  # you must be at an atrium, or corner-atrium

                if not self.dungeon_level_exit_check():  # if player is not proximal to dungeon_level exit

                    if multiple_corridors:
                        print(f"The {corridor_direction} exits each lead to {corridor_name}.")
                    else:
                        print(f"The {corridor_direction} exit leads to {corridor_name}.")

                else:  # player IS proximal to the dungeon_level exit
                    if multiple_corridors:
                        print(f"The {corridor_direction} exits each lead to corridors.")
                        dungeon_exit_direction = self.dungeon_level_exit_check()
                        print(f"The {dungeon_exit_direction} corridor leads to a staircase.."
                              f"*IT IS THE EXIT OF {self.dungeon.name}!*")
                        #
                    else:
                        corridor_direction = self.dungeon_level_exit_check()
                        print(f"The {corridor_direction} corridor leads to a staircase.."
                              f"*IT IS THE EXIT OF {self.dungeon.name}!*")
                        #
            else:  # you must be at an intersection. intersections are auto-described above.
                # just check to see if player is proximal to the dungeon_level_exit:
                if self.dungeon_level_exit_check():
                    corridor_direction = self.dungeon_level_exit_check()
                    print(f"The {corridor_direction} corridor leads to a staircase.."
                          f"*IT IS THE EXIT OF {self.dungeon.name}!*")
                    #
        else:  # you must be at a dead end
            exits = convert_list_to_string(exits_list)
            print(f"{auto_description_phrase} The only exit is to the {exits}.")

    def you_cannot_go_that_way(self):
        # called from dungeon_description()
        barrier_name = self.dungeon.barrier_name
        if self.in_a_pit:
            barrier_name = self.dungeon.pit_barrier_name
        random_statement_list = [f"The {barrier_name} blocks your way...", "You cannot go that way...",
                                 f"The {barrier_name} prevents movement in that direction..."]
        random_statement = random.choice(random_statement_list)
        print(random_statement)
        self.x = self.previous_x
        self.y = self.previous_y
        self.coordinates = (self.x, self.y)
        self.position = self.dungeon.grid[self.y][self.x]

    def dungeon_level_exit_check(self):
        # called from dungeon_description()
        north_of_you = (self.x, (self.y - 1))
        west_of_you = ((self.x - 1), self.y)
        south_of_you = (self.x, (self.y + 1))
        east_of_you = ((self.x + 1), self.y)
        level_exit = self.dungeon.exit
        if north_of_you == level_exit:
            return "Northern"
        if west_of_you == level_exit:
            return "Western"
        if east_of_you == level_exit:
            return "Eastern"
        if south_of_you == level_exit:
            return "Southern"
        else:
            return False

    def navigation_position_coordinates(self):
        # called from end of each navigation turn in main loop
        self.position = self.dungeon.grid[self.y][self.x]
        self.coordinates = (self.x, self.y)

    def navigation_turn_initialize(self):
        # called from main loop at beginning of each navigation turn while in dungeon
        self.coordinates = (self.x, self.y)
        self.previous_x = self.x
        self.previous_y = self.y

    def dungeon_description(self):
        # meta-function called from navigation() and main loop
        self.hud()
        north_south = ""
        east_west = ""
        if self.x > 9:
            east_west = "eastern"
        elif self.x < 10:
            east_west = "western"
        if self.y > 9:
            north_south = "South"
        elif self.y < 10:
            north_south = "North"

        # You cannot go that way; Player has hit a dungeon wall and is returned to previous position
        if self.position == "*":  # asterisk represents barrier
            self.you_cannot_go_that_way()

        # call the automatic description function
        self.automatic_dungeon_description_and_room_exit_finder()

        # Dungeon logical descriptions. They correspond to dungeon instance coordinates and events.
        # They are printed out after automatic description function
        if self.coordinates == self.dungeon.staircase:
            self.staircase_description()
        if self.coordinates == self.dungeon.elevator_landing:
            self.elevator_landing_description()
        if self.coordinates == self.dungeon.teleporter_landing:
            self.teleporter_landing_description()
        if self.coordinates == self.dungeon.pit_landing:
            self.pit_landing_description()

        # self.coordinates = (self.x, self.y)  # commented out. seems to be unnecessary at this point in program.

        # print out dungeon level and coordinates before returning
        if self.in_a_pit:
            # assuming pit landing coordinates are at 1, 14:
            print(f"(In a pit below {self.dungeon.name}) Coordinates: {self.x, (self.y - 13)}")
        else:
            if self.coordinates != self.dungeon.exit:
                print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}, "
                      f"{north_south}{east_west} region) Coordinates: {self.coordinates}")
        return

    def display_map(self, maps):
        if self.in_a_pit:
            print(f"You are in uncharted territory..")
            sleep(1)
            return
        else:
            cls()
            print("You look at the map..")
            print(f"Position key: {self.position}")  # remove after testing

            self.coordinates = (self.x, self.y)
            print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}) Coordinates: {self.coordinates}")

            if self.coordinates != self.dungeon.staircase:
                self.dungeon.player_grid[self.y][self.x] = "X"
                for element in range(0, 20):
                    print(*maps[element])
                # replace the X with a dot after printing map so that it doesn't leave a trail of x's:
                self.dungeon.player_grid[self.y][self.x] = "."
                print(f"S = Staircase X = your position E = Exit")

            else:
                for element in range(0, 20):
                    print(*maps[element])
                print(f"S = Staircase E = Exit\nYou are currently at the staircase.")

            # place the next line in the main file to leave a trail of x's throughout the map to see where you've been.
            # player_1.dungeon.player_grid[player_1.y][player_1.x] = "x"
            return

    def dungeon_exit_event(self):
        # dungeon dictionary in dungeons.py file
        print(f"You approach the exit. With quiet resolve, you turn to briefly look\n"
              f"behind you, and then continue onward, toward your goal.")
        sleep(2)
        # the deepest dungeon level will have no exit, so there should be no chance of a KeyError by adding 1.
        # at end of game, transport player back to dungeon level 1 with:
        # self.dungeon_key = 1
        # self.dungeon = dungeon_dict[self.dungeon_key]
        self.dungeon_key += 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        (self.x, self.y) = self.dungeon.staircase  # simplified with tuple instead of self.x = and self.y =
        self.coordinates = (self.x, self.y)  # beta testing
        # for a while, self.coordinates would be set after first move. otherwise, the intro would be printed 1st,
        # followed by the staircase description, which was awkward. after migrating to automatic_description, this
        # seems to no longer be the case
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = 0
        pause()
        return "Exit Boss"


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
# removed code:
'''
item_type_key_lst = ['Weapons', 'Healing', 'Armor', 'Shields', 'Boots', 'Cloaks',
                             'Rings of Regeneration',
                             'Rings of Protection', 'Town Portal Implements']

if len(self.pack):
                stolen_item = random.choice(self.pack[random.choice(item_type_key_lst)])
                self.pack.pop(stolen_item)
                # stolen_item = random.choice(self.pack)
                print(f"He steals your {stolen_item}!")

                item_type_key_lst = ['Weapons', 'Healing', 'Armor', 'Shields', 'Boots', 'Cloaks',
                             'Rings of Regeneration',
                             'Rings of Protection', 'Town Portal Implements']
        # found_item = random.choice(loot_dict[random.choice(item_type_key_lst)])



                '''
'''   def inventory_old(self):
       while True:
           if len(self.pack):
               self.hud()
               print("Your pack contains:")
               print("Item                       Quantity")
               print()
               self.pack.sort(key=lambda x: x.damage_bonus)
               stuff_dict = Counter(item.name for item in self.pack)
               for key, value in stuff_dict.items():
                   print(key, 's', ':    ', value, sep='')
                   # print(value, ':', key)
               print()
           else:
               print("Your pack is empty")
           print(f"Your current wielded weapon: "
                 f"{self.wielded_weapon}\n"
                 f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                 f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
           if not len(self.pack):
               return
           inventory_choice = input(f"(S)ubstitute wielded weapon or (E)xit: ").lower()
           if inventory_choice not in ('s', 'e'):
               continue
           if inventory_choice == 'e':
               return
           if inventory_choice == 's':
               self.hud()
               # stuff = Counter(item.name for item in self.pack)
               # items = [item for item in self.pack if item.item_type == "weapon"]
               self.pack.sort(key=lambda x: x.damage_bonus)
               # stuff = Counter(item.name for item in items)
               stuff = {}
               for item in self.pack:
                   # if getattr(item, item.item_type) == "weapon":
                   stuff[item] = self.pack.index(item)
               for key, value in stuff.items():
                   print(value, ':', key)
               old_weapon = self.wielded_weapon
               print(f"Your current wielded weapon: "
                     f"{self.wielded_weapon}\n"
                     f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                     f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
               try:
                   new_weapon = int(input(f"Enter the number of the weapon from your pack you wish to wield: "))
                   # try:
                   self.wielded_weapon = self.pack[new_weapon]
               except (IndexError, ValueError):
                   print("Invalid entry..")
                   sleep(1)
                   break
               print(f"You remove the {self.pack[new_weapon]} from your pack and are now wielding it.\n"
                     f"You place the {old_weapon} in your pack.")
               self.pack.pop(new_weapon)
               self.pack.append(old_weapon)
               self.pack.sort(key=lambda x: x.damage_bonus)
               sleep(1)
               if not len(self.pack):
                   print("Your pack is now empty.")
                   sleep(1)
                   return
           else:
               print("Your pack is empty..see if this statement is ever seen")
               return'''

'''elif found_item.item_type != 'Armor' and found_item.item_type != 'Shields' and found_item.item_type != 
'Cloaks' and found_item.item_type != 'Rings of Protection' and found_item.item_type != 
'Rings of Regeneration' and found_item.item_type != 'Weapons' and found_item.item_type != 
'Healing' and found_item.item_type != 'Town Portal Implements' and found_item not in \

                            self.pack[
                                found_item.item_type]: '''
'''if sale_item_key == 'i':
        self.hud()
        inventory_from_blacksmith = self.item_type_inventory('Weapons')
        if not inventory_from_blacksmith:
            print(f"Your weapons inventory is empty")
        os.system('pause')
        self.hud()
        continue'''

'''old blacksmith buy items code
sale_item = (sale_items_dict[sale_item_key])
            if self.gold >= sale_item.sell_price and sale_item not in (
                    self.pack[
                        'Weapons']) and sale_item != self.wielded_weapon and self.level >= sale_item.minimum_level:
                self.hud()
                print(f"You buy a {sale_item}")
                self.gold -= sale_item.buy_price
                (self.pack[sale_item.item_type]).append(sale_item)
                number_of_items = len(self.pack[sale_item.item_type])
                print(f"You now have {number_of_items} items in your {sale_item.item_type} inventory:")
                (self.pack[sale_item.item_type]).sort(key=lambda x: x.name)
                stuff_dict = Counter(item.name for item in self.pack[sale_item.item_type])
                for key, value in stuff_dict.items():
                    print(key)
                    # print(key, 's', ':    ', value, sep='')
                pause()
                continue
            elif self.gold < sale_item.sell_price:
                print(f"You do not have enough gold")
                sleep(1)
                self.hud()
                continue
            elif self.level < sale_item.minimum_level:
                print(f"The minimum level requirement is {sale_item.minimum_level}. You are level {self.level}")
                sleep(1)
                self.hud()
                continue
            else:
                print(f"You already have a {sale_item}")
                sleep(1)
                self.hud()
                continue'''
'''sale_items_dict = {'1': short_sword,
                           '2': broad_sword,
                           '3': quantum_sword
                           }'''
'''    def weapon_management(self):
    self.hud()
    if len(self.pack['Weapons']) > 0:
        print(f"Your current weapon inventory:")
        print(f"(Sorted by highest damage bonus)")
        (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus, reverse=True)
        weapon_mgmt_dict = {}
        for item in (self.pack['Weapons']):
            weapon_mgmt_dict[item] = (self.pack['Weapons']).index(item)
        for key, value in weapon_mgmt_dict.items():
            print(value + 1, ':', key)  # value is index. indexing starts at zero, so add 1
        print()

    else:
        print(f"You have nothing in your weapons inventory..")
        pause()
        return
    old_weapon = self.wielded_weapon
    print(f"Your current wielded weapon: "
          f"{self.wielded_weapon}\n"
          f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
          f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
    wield_or_exit = input(f"(S)wap wielded weapon, or go (B)ack: ").lower()
    if wield_or_exit == "b":
        return
    elif wield_or_exit == "s":
        try:
            new_weapon_index = int(input(f"Enter the number of the weapon you wish to wield: "))
            new_weapon_index -= 1  # again, indexing starts at 0 and is awkward
            self.wielded_weapon = (self.pack['Weapons'])[new_weapon_index]  # SYNTAX FOR INDEX
            # self.wielded_weapon = self.pack['Weapons']new_weapon  # find syntax...on the right track
        except (IndexError, ValueError):
            print("Invalid entry..")
            sleep(1)
            return
        print(f"You remove the {(self.pack['Weapons'])[new_weapon_index]} from your back and are now wielding it.\n"
              f"You place the {old_weapon} on your back.")

        (self.pack['Weapons']).pop(new_weapon_index)  # INDEX SYNTAX
        (self.pack['Weapons']).append(old_weapon)  # old_weapon represents an object, not an index
        (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus)
        # self.pack.append(old_weapon)  # for the old list inventory method
        pause()'''
'''    def print_weapon_stats(self, weapon):
        print(f"{weapon.name}:")
        print(f"Damage bonus: {weapon.damage_bonus}")
        print(f"To hit: {weapon.to_hit_bonus}")
        print(f"Sell price: {weapon.sell_price}")
        print(f"Minimum level requirement: {weapon.minimum_level}")

    def print_armor_stats(self, armor):  # should be deprecated
        print(f"{armor.name}:")
        print(f"AC: {armor.ac}")
        print(f"Sell Price: {armor.sell_price}")
        print(f"Minimum level requirement: {armor.minimum_level}")

    def print_shield_stats(self, shield):  # should be deprecated
        print(f"{shield.name}:")
        print(f"AC: {shield.ac}")
        print(f"Sell Price: {shield.sell_price}")
        print(f"Minimum level requirement: {shield.minimum_level}")

    def print_boots_stats(self, boots):  # should be deprecated
        print(f"{boots.name}:")
        print(f"AC: {boots.ac}")
        print(f"Sell Price: {boots.sell_price}")
        print(f"Minimum level requirement: {boots.minimum_level}")'''
'''    def alternate_sell_chemist_items(self):  # redo this and make default if possible
        chemist_sell_dict = {
            'Healing': [healing_potion],
            'Town Portal Implements': [scroll_of_town_portal],
        }
        while True:
            # create a list of item types:
            item_type_lst = list(chemist_sell_dict.keys())
            # create a dictionary from list of item types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            sell = input("Display your (I)nventory, (P)ick item type, or go (B)ack: ").lower()
            if sell not in ('i', 'p', 'b'):
                self.hud()
                continue
            elif sell == 'i':
                self.inventory()
                continue
            elif sell == 'b':
                return
                # break
            elif sell == 'p':
                try:
                    item_type_index_to_buy = int(input(f"Enter the category of the item to sell by number: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue'''
'''            elif self.potions_of_healing > 0 and self.town_portals > 0:
                potion_or_scroll = dice_roll(1, 20)
                if potion_or_scroll > 10:
                    print(f"He steals a potion of healing.")
                    self.potions_of_healing -= 1
                    pause()
                    return True
                else:
                    print(f"He steals a scroll of town portal.")
                    self.town_portals -= 1
                    pause()
                    return True
            # if player has one or the other, potions are stolen first,
            elif self.potions_of_healing > 0:
                print(f"He steals a potion of healing.")
                self.potions_of_healing -= 1
                pause()
                return True
            elif self.town_portals > 0:
                print(f"He steals a scroll of town portal.")
                self.town_portals -= 1
                pause()
                return True'''
'''quantum_item_list = [self.potions_of_healing, self.town_portals]
            for quantum_item in quantum_item_list:
                if quantum_item < 1:
                    quantum_item_list.remove(quantum_item)
            print(quantum_item_list)
            if len(quantum_item_list):
                stolen_item = random.choice(quantum_item_list)
                if stolen_item == self.potions_of_healing:
                    print(f"He steals a potion of healing.")
                    quantum_item_list.remove(self.potions_of_healing)
                    self.potions_of_healing -= 1

                    pause()
                    return True
                elif stolen_item == self.town_portals:
                    print(f"He steals a scroll of town portal.")
                    quantum_item_list.remove(self.town_portals)
                    self.town_portals -= 1

                    pause()
                    return True'''
'''#elif self.position == ".":
#    print(f"You are in a rather wide open area of {self.dungeon.name}. There are exits in each direction...")

#    return
# DEAD ENDs - Only 1 exit!
# 1 exit to the north
        elif self.position == "1":
            print("You are at a dead end. Exit is to the north...")
            # sleep(1.5)
            return
        # 2 exit to the south
        elif self.position == "2":
            print("You are at a dead end. Exit is to the south...")
            # sleep(1.5)
            return
        # 3 exit to the east
        elif self.position == "3":
            print("You are at a dead end. Exit is to the east...")
            # sleep(1.5)
            return
        # 4 exit to the west
        elif self.position == "4":
            print("You are at a dead end. Exit is to the west...")
            # sleep(1.5)
            return
        # STRAIGHT HALLWAYs:

        # 5 exits north and south
        elif self.position == "5":
            print("You are in a corridor. Exits are to the North and South...")
            # sleep(1.5)
            return
        # 6 exits east and west
        elif self.position == "6":
            print("You are in a corridor. Exits are to the East and West...")
            # sleep(1.5)
            return
        # CORNERS:
        # 7 exits to the south and east UPPER LEFT
        elif self.position == "7":
            print(f"You are in a corner. Exits are to the South and East.")
            return
            # 8 exits to the north and east LOWER LEFT
        elif self.position == "8":
            print(f"You are in a corner. Exits are to the North and East.")
            return
            # 9 exits to the south and west UPPER RIGHT
        elif self.position == "9":
            print(f"You are in a corner. Exits are to the South and West.")
            return
            # "-" exits to the north and west LOWER RIGHT
        elif self.position == "-":
            print(f"You are in a corner. Exits are to the North and West.")
            return

        # WALLS:
        # |  exits to the south. east and west  NORTH WALL
        elif self.position == "|":
            print(f"You are against a wall to the North. Exits are to the South, East and West.")
            return
            # / exits to the north, east and west SOUTH WALL
        elif self.position == "/":
            print(f"You are against a wall to the South. Exits are to the North, East and West.")
            return
            # ( exits to the north, south and east WEST WALL
        elif self.position == "(":
            print(f"You are against a wall to the West. Exits are to the North, South and East.")
            return
            # ) exits to the north, south and west EAST WALL
        elif self.position == ")":
            print(f"You are against a wall to the East. Exits are to the North, South and West.")
            return'''
'''            elif sale_item_key == 'w':
                self.item_management('Weapons', self.wielded_weapon)
                # self.weapon_management()
                continue
            elif sale_item_key == 'a':
                self.item_management('Armor', self.armor)
                continue
            elif sale_item_key == 's':
                self.item_management('Shields', self.shield)
                continue
            elif sale_item_key == 'b':
                self.item_management('Boots', self.boots)
                continue
            elif sale_item_key == 'c':
                self.item_management('Cloaks', self.cloak)
                continue'''
'''                    if self.strength < 19:
                        ability_lst.append('strength')
                    if self.dexterity < 19:
                        ability_lst.append('dexterity')
                    if self.constitution < 19:
                        ability_lst.append('constitution')
                    if self.intelligence < 19:
                        ability_lst.append('intelligence')
                    if self.wisdom < 19:
                        ability_lst.append('wisdom')
                    if self.charisma < 19:
                        ability_lst.append('charisma')'''
'''                        if self.strength < 20:
                            ability_lst.append('strength')
                        if self.dexterity < 20:
                            ability_lst.append('dexterity')
                        if self.constitution < 20:
                            ability_lst.append('constitution')
                        if self.intelligence < 20:
                            ability_lst.append('intelligence')
                        if self.wisdom < 20:
                            ability_lst.append('wisdom')
                        if self.charisma < 20:
                            ability_lst.append('charisma')'''
'''print(f"You may choose:\n1. Improve 1 ability by 2 points\nor\n"
                      f"2. Improve 2 abilities by 1 point ")
                one_or_two = input(f"Your choice (1 / 2): ")
                if one_or_two not in ('1', '2'):
                    continue
                elif one_or_two == '1':
                    self.hud()
                    ability_dict = self.__dict__  # create variable as actual copy of player dict attribute
                    # create ability list
                    ability_lst = []
                    # create a working dictionary for all abilities
                    working_dict = {'strength': self.strength, 'dexterity': self.dexterity,
                                    'constitution': self.constitution, 'intelligence': self.intelligence,
                                    'wisdom': self.wisdom, 'charisma': self.charisma}
                    for key, value in working_dict.items():
                        if value < 19:
                            ability_lst.append(key)
                    # add all keys for values less than 19 to the ability list
                    if not len(ability_lst):  # if list is empty, no more improvements allowed
                        print(f"You cannot improve any of your abilities by 2. "
                              f"You can max out a 19 score with option 2.")
                        pause()
                        continue
                    # create a subset ability dictionary from ability list by indexing, and then print out
                    # this dictionary is the resulting abilities with indexed keys corresponding to each
                    ability_dict_subset_too = {}
                    for ability in ability_lst:
                        if len(ability_lst):
                            ability_dict_subset_too[ability_lst.index(ability)] = ability
                            # ability_dict_subset_too[ability] = ability_lst.index(ability)  # <-reverses key and value!
                    for key, value in ability_dict_subset_too.items():
                        print(key + 1, ':', value.capitalize())  # add one because indexing starts at zero
                    try:
                        one_ability = int(
                            input(f"Enter the number of the ability you wish to improve by 2 points. "
                                  f"(NOTE: This is permanent!): "))
                        one_ability -= 1  # subtract one because indexing starts at 0
                        ability_to_improve = (ability_dict_subset_too[one_ability])
                        old_score = ability_dict[ability_to_improve]
                        ability_dict[ability_to_improve] += 2
                        print(f"Your {ability_to_improve} has been increased from "
                              f"{old_score} to {ability_dict[ability_to_improve]}!")
                        print(f"The dungeon horde also grows in power...")
                        self.calculate_modifiers()
                        # pause()
                        return
                    except(ValueError, KeyError):
                        print("Invalid entry..")
                        sleep(1)
                        continue'''
''' def necrotic_dot(self, dot_multiplier):
        self.dot_multiplier = dot_multiplier
        self.hud()
        rndm_necrotic_phrases = ["You feel absolute dread and withering overcoming you..",
                                 "An unnerving pain, planted like a seed, germinates within you...",
                                 "Agony creeps into your very veins..."
                                 ]
        necrotic_phrase = random.choice(rndm_necrotic_phrases)
        print(f"{necrotic_phrase}")
        sleep(1.5)
        print(f"Necrotic forces ravage through your body!")
        self.necrotic = True
        self.necrotic_turns = 0

        pause()

        self.hud()
        return self.necrotic'''
'''            elif self.potions_of_healing > 0 and self.potions_of_strength > 0 and self.town_portals > 0 
and self.elixirs > 0:
                potion_or_scroll = dice_roll(1, 4)
                if potion_or_scroll == 1:
                    print(f"He steals a potion of healing.")
                    self.potions_of_healing -= 1
                    pause()
                    return True
                elif potion_or_scroll == 2 and self.potions_of_strength > 0:
                    print(f"He steals a potion of strength.")
                    self.potions_of_strength -= 1
                    pause()
                    return True
                elif potion_or_scroll == 3 and self.town_portals > 0:
                    print(f"He steals a scroll of town portal.")
                    self.town_portals -= 1
                    pause()
                    return True
                elif potion_or_scroll == 4 and self.town_portals > 0:
                    print(f"He steals a clarifying elixir.")
                    self.elixirs -= 1
                    pause()
                    return True
            # if player has one or the other- make this into lists and dictionaries in the future!

            elif self.potions_of_healing > 0:
                print(f"He steals a potion of healing.")
                self.potions_of_healing -= 1
                pause()
                return True
            elif self.potions_of_strength > 0:
                print(f"He steals a potion of strength.")
                self.potions_of_strength -= 1
                pause()
                return True
            elif self.elixirs > 0:
                print(f"He steals a clarifying elixir.")
                self.elixirs -= 1
                pause()
                return True
            elif self.town_portals > 0:
                print(f"He steals a scroll of town portal.")
                self.town_portals -= 1
                pause()
                return True
'''

"""            if found_item.name == 'Full Plate Armor' and found_item.name == self.armor.name:
                found_item.ac += 1
                print(
                    f"Quantum wierdness fills the air...\nYour {self.armor.name} is enhanced 
                    to armor class {found_item.ac}!")
                self.armor.ac = found_item.ac
                self.calculate_armor_class()
                pause()
                return
            else:"""

"""    def damage_while_paralyzed(self, monster_number_of_hd, monster_hit_dice):
        paralyze_damage = dice_roll(monster_number_of_hd, monster_hit_dice)
        self.reduce_health(paralyze_damage)
        print(f"You suffer {paralyze_damage} hit points!!")
        pause()"""

"""    def meta_monster_function(self, monster):
        melee_or_quantum = dice_roll(1, 20)
        if monster.quantum_energy and melee_or_quantum > 10 and not self.poisoned \
                and not self.necrotic:
            if not monster.can_poison and not monster.necrotic:
                damage_to_player = monster.quantum_energy_attack(self)
                self.reduce_health(damage_to_player)
                self.calculate_potion_of_strength()  # pots of str have 5 uses; battle & nav
                self.calculate_protection_effect()
                self.regenerate()
                self.calculate_poison()  # poison wears off after 5 turns of battle/nav
                self.calculate_necrotic_dot()
            elif monster.can_poison and monster.necrotic:  # if monster has both poison
                poison_or_necrotic = dice_roll(1, 20)  # and necrotic damage,
                if poison_or_necrotic > 10:  # greater than 10 for poison
                    self.poison_attack(monster.name, monster.dot_multiplier)
                else:
                    self.necrotic_attack(monster)
            elif monster.can_poison:  # otherwise, if it can only poison, then attempt poison
                self.poison_attack(monster.name, monster.dot_multiplier)
                self.calculate_potion_of_strength()  # pots of str have 5 uses; battle & nav
                self.calculate_protection_effect()
                self.regenerate()
                self.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                self.calculate_necrotic_dot()
            elif monster.necrotic:  # otherwise if it only has necrotic, then attempt necrotic
                self.necrotic_attack(monster)
                self.calculate_potion_of_strength()  # pots of str have 5 uses; battle & nav
                self.calculate_protection_effect()
                self.regenerate()
                self.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                self.calculate_necrotic_dot()
        else:
            # if it has neither, then melee attack
            damage_to_player = monster.swing(monster.name, self.armor_class)
            self.reduce_health(damage_to_player)
            self.calculate_potion_of_strength()  # pots of str have 5 uses; battle & nav
            self.calculate_protection_effect()
            self.regenerate()
            self.calculate_poison()  # poison wears off after 5 turns of battle/navigation
            self.calculate_necrotic_dot()"""

"""    def poison_attack(self, monster_name, monster_dot_multiplier):
        difficulty_class = (self.constitution + self.constitution_modifier)
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {monster_name} hisses in evil glee..")
        print(f"Attack roll---> {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You dodge!")
            sleep(1)
            print(f"And you perceive it was attempting to poison you!")
            pause()
            self.hud()
            return False
        else:
            print(f"Your Constitution: {self.constitution}\nYour Constitution Modifier: {self.constitution_modifier}\n")
            if roll_d20 == 20 or roll_d20 >= difficulty_class:  # self.constitution + self.constitution_modifier:
                # return True
                # self.hud()
                self.dot_multiplier = monster_dot_multiplier
                rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                         "An unnerving frailty spreads throughout your body...",
                                         "Pain and tenderness courses through your body.."
                                         ]
                poisoned_phrase = random.choice(rndm_poisoned_phrases)
                print(f"{poisoned_phrase}")
                sleep(1.5)
                print(f"You have been poisoned!")
                self.poisoned = True
                self.poisoned_turns = 0
                # self.calculate_poison()
                pause()
                # self.dungeon_description()
                # self.hud()
                return self.poisoned
            else:
                print(f"You swiftly dodge its poison attack!")
                sleep(1)
                pause()
                self.hud()
                return False

    def necrotic_attack(self, monster):
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {monster.name} attempts to harness its innate understanding of quantum necrosis..")
        print(f"Attack roll---> {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You dodge the deadly necrotic attack!")
            sleep(1)
            pause()
            self.hud()
            return False
        else:
            player_roll = (dice_roll(1, 20))
            print(f"Your roll: {player_roll}\nYour Constitution Modifier: {self.constitution_modifier}\n")
            if roll_d20 == 20 or roll_d20 >= player_roll + self.constitution_modifier:
                self.dot_multiplier = monster.dot_multiplier
                rndm_necrotic_phrases = ["You feel morbid dread and withering overcoming you..",
                                         "An unnerving pain, planted like a seed, germinates within you...",
                                         "Agony creeps into your very veins..."
                                         ]
                necrotic_phrase = random.choice(rndm_necrotic_phrases)
                print(f"{necrotic_phrase}")
                sleep(1.5)
                print(f"Necrotic forces ravage through your body!")
                self.necrotic = True
                self.necrotic_turns = 0
                pause()
                self.hud()
                return self.necrotic
            else:
                print(f"You swiftly dodge its death-dealing necrotic attack!")
                sleep(1)
                pause()
                self.hud()
                return False"""

"""turn_roll = dice_roll(1, 20)
player_total = (turn_roll + self.wisdom_modifier + self.proficiency_bonus + vulnerability_modifier)
print(f"Quantum Ability Check: {turn_roll} + Wisdom Modifier: {self.wisdom_modifier}\n"
      f"Proficiency Bonus: {self.proficiency_bonus}")
if vulnerability_modifier > 0:
    print(f"Monster Vulnerability Modifier: {vulnerability_modifier}")
sleep(1)
print(f"Total: {player_total}")
sleep(1)
monster_roll = dice_roll(1, 20)
print(f"Monster Saving Throw: {monster_roll}")
print(f"{monster.name} Constitution Modifier: {monster.constitution_modifier}")
monster_total = monster_roll + monster.constitution_modifier
print(f"Monster Total: {monster_total}")
sleep(1)
if player_total >= monster_total:"""

"""            else:
self.quantum_units -= quantum_unit_cost  # level 2 effect. uses 2 units
print(f"The {monster.name} resists!")
sleep(1)
pause()
return 0"""

"""print("Your focus has failed..")
                    sleep(1)
                    print(f"The Lightning crackles into existence and shoots toward your target..")
                    sleep(1)
                    print(f"For all of its awe-inspiring energy, it fails to land any damage!")
                    pause()
                    self.hud()
                    return 0"""

"""print("Your focus has failed..")
                    sleep(1)
                    print(f"The Fireball is forced into existence through Quantum Weirdness..")
                    sleep(1)
                    print(f"..and is extinguished in a puff of smoke!")
                    pause()
                    self.hud()
                    return 0"""
"""description_dict = {
            ".": f"You are in a rather wide open area of {self.dungeon.name}. There are exits in each direction...",
            "1": f"You are at a dead end. The only exit is to the North...",
            "2": f"You are at a dead end. The only exit is to the South...",
            "3": f"You are at a dead end. The only exit is to the East...",
            "4": f"You are at a dead end. The only exit is to the West...",
            "5": f"This is a corridor of {self.dungeon.name}. Exits are to the North and South...",
            "6": f"You are in a corridor of {self.dungeon.name}. Exits are to the East and West...",
            "7": f"You are in a corner. Exits are to the South and East.",
            "8": f"You are in a corner. Exits are to the North and East.",
            "9": f"You are in a corner. Exits are to the South and West.",
            "-": f"You are in a corner. Exits are to the North and West.",
            "|": f"You are against a {self.dungeon.barrier_name} to the North. Exits are to the South, East and West.",
            "/": f"You are against a {self.dungeon.barrier_name} to the South. Exits are to the North, East and West.",
            "(": f"You are against a {self.dungeon.barrier_name} to the West. Exits are to the North, South and East.",
            ")": f"You are against a {self.dungeon.barrier_name} to the East. Exits are to the North, South and West.",
            "T": f"You are in a chamber of {self.dungeon.name} that seems to have been "
                 f"re-purposed as a sort of throne room.",
            "L": f"You are on a slick patch of ground. High above you is a wide, gaping hole leading up to "
                 f"dungeon level {self.dungeon.level - 1}.",
            "P": f"You are in a pit. Slime covers the ground beneath, and a putrid mist fills the air."
        }"""
"""# DEAD END Only 1 exit!
        # 1 exit to the north
        # 2 exit to the south
        # 3 exit to the east
        # 4 exit to the west
        # STRAIGHT HALLWAY:
        # 5 exits north and south
        # 6 exits east and west
        # CORNERS:
        # 7 exits to the south and east UPPER LEFT
        # 8 exits to the north and east LOWER LEFT
        # 9 exits to the south and west UPPER RIGHT
        # - exits to the north and west LOWER RIGHT
        # WALLS:
        #   exits to the south. east and west  NORTH WALL
        # / exits to the north, east and west SOUTH WALL
        # > exits to the north, south and east WEST WALL
        # < exits to the north, south and west EAST WALL
        # ^ <> v dungeon exit in the indicated direction!
        # T throne room
        # L Pit landing
        # P in a Pit"""
"""    def dungeon_room_exit_finder(self, description_phrase):
        # called from dungeon_description()
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        if north_of_you != "*":
            exits_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        number_of_ways = len(exits_list)
        if number_of_ways > 1:
            exits_list.insert(-1, 'and')  # add "and" before last element to be more naturally readable
            exits = str(', '.join(exits_list[:-2]) + ' ' + ' '.join(exits_list[-2:]))
            if description_phrase != "":
                print(f"{description_phrase} Exits are to the {exits}.")
            else:
                print(f"Exits are to the {exits}.")
        else:
            separator = ""
            exits = (separator.join(exits_list))
            if description_phrase != "":
                print(f"{description_phrase} The only exit is to the {exits}.")
            else:
                print(f"The only exit is to the {exits}.")"""
"""
    def dungeon_intersection_logic(self):
        # called from dungeon_description()
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        exits_list = []
        if north_of_you != "*":
            exits_list.append("North")
        if south_of_you != "*":
            exits_list.append("South")
        if east_of_you != "*":
            exits_list.append("East")
        if west_of_you != "*":
            exits_list.append("West")
        number_of_ways = len(exits_list)
        if number_of_ways > 1:
            exits_list.insert(-1, 'and')
            exits = str(', '.join(exits_list[:-2]) + ' ' + ' '.join(exits_list[-2:]))
            print(f"You are at a {number_of_ways}-way intersection. Corridors lead off to the {exits}.")
        else:
            # this code is ostensibly unreachable, unless "I" is added to the self.dungeon.grid in the wrong place:
            separator = ""
            exits = (separator.join(exits_list))
            print(f"There appears to have been an intersection here at one time, but all except one corridor has "
                  f"collapsed. The only exit is to the {exits}")"""
"""        if number_of_walls == 1:
            if not self.intersection_check():  # if you are not at an intersection
                separator = ""
                direction = (separator.join(walls_list))  # simplify printing of list
                auto_description_phrase = f"There is a {self.dungeon.barrier_name} to the {direction}."
            else:  # you are at an intersection
                auto_description_phrase = self.auto_intersection_description()"""
"""    def chamber_opening_logic(self):
        # called from dungeon_description()
        north_of_you = self.dungeon.grid[self.y - 1][self.x]
        west_of_you = self.dungeon.grid[self.y][self.x - 1]
        south_of_you = self.dungeon.grid[self.y + 1][self.x]
        east_of_you = self.dungeon.grid[self.y][self.x + 1]
        direction = ""
        if north_of_you == "H":
            direction = "Northern"
        elif west_of_you == "H":
            direction = "Western"
        elif east_of_you == "H":
            direction = "Eastern"
        elif south_of_you == "H":
            direction = "Southern"
        print(f"The {direction} exit leads to a corridor.")"""
"""    def dungeon_level_exit_direction_logic(self):
        # called from dungeon_description()
        # direction = ""
        # if self.position == ">":
        #    direction = "East"
        # elif self.position == "<":
        #    direction = "West"
        # elif self.position == "^":
        #    direction = "North"
        # elif self.position == "v":
        #    direction = "South"
        description = ""
        # self.automatic_dungeon_description_and_room_exit_finder(description)
        # print(f"You see the dungeon exit to the {direction}!!")
        print(f"It is the exit of {self.dungeon.name}!")
        return"""
"""            # exits_list.insert(-1, 'and')  # add "and" before last element to be more naturally readable
            # exits = str(', '.join(exits_list[:-2]) + ' ' + ' '.join(exits_list[-2:]))"""
"""# if self.position == "I":
#    self.dungeon_intersection_logic()
# if self.intersection_check():
#    description = self.auto_intersection_description()
#    self.automatic_dungeon_description_and_room_exit_finder(description)

# chamber openings are described above, and then the direction in which the corridor lies is calculated by
# chamber_opening_logic()
# if self.position == "O":
#    self.chamber_opening_logic()

# ^ <> v dungeon level EXIT in the indicated direction!
# if self.position == ">" or self.position == "<" or self.position == "^" or self.position == "v":
#    self.dungeon_level_exit_direction_logic()"""
"""# Dungeon generic descriptions. These description_dict keys and values
        # correspond to self.position strings on the grid.
        # If player position corresponds to the dictionary key,
        # The description phrase is defined and then passed to automatic_dungeon_description_and_room_exit_finder()
        # which calculates exits and prints out 1. the description phrase as well as
        # 2. automatic descriptions and
        # 3.exits
        # otherwise, description is an empty string by default, and automatic_dungeon_description_and_room_exit_finder()
        # does all the work
        # if self.position in description_dict:
        #    description = (description_dict[self.position])"""
"""
        # description_dict = {
            # ".": f"This is a wide-open, dimly lit area of {self.dungeon.name}.",

            # "H": f"This is a tunneled corridor of {self.dungeon.name}.",

            # "O": f"You are standing in the entryway to a large, open chamber.",

            # "T": f"You are in a chamber of {self.dungeon.name} that seems to have been "
            #     f"re-purposed as a sort of throne room.",
            # "P": f"Slime covers the ground beneath your feet, and a putrid mist fills the air.",
            # "S": ""  # "" is simply for logical readability
        # } #"""


"""loot_dict = {
    'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
    'Shields': [buckler, kite_shield, quantum_tower_shield],
    'Boots': [elven_boots, ancestral_footsteps],
    'Cloaks': [elven_cloak],
    'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
    'Elixirs': [elixir],
    'Healing': [healing_potion],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal],
    'Potions of Strength': [strength_potion],
    'Antidotes': [antidote]
}"""
"""    def chance_for_a_treasure(self, encounter):
        possible_treasure_chest = dice_roll(1, 20)
        if encounter < 21:  # regular monster
            loot_difficulty_class = 15
            if possible_treasure_chest > loot_difficulty_class:
                self.treasure_chest_event()
                return
        else:  # boss
            loot_difficulty_class = 8
            if possible_treasure_chest > loot_difficulty_class:  # == 20:
                if self.dungeon.level < 3:
                    self.treasure_chest_event()
                    return
                else:
                    quantum_or_standard = dice_roll(1, 20)
                    if quantum_or_standard > 11:
                        self.quantum_treasure_chest_event()
                        return
                    else:
                        self.treasure_chest_event()
                        return"""

"""loot_dict = {
    'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
    'Shields': [buckler, kite_shield, quantum_tower_shield],
    'Boots': [elven_boots, ancestral_footsteps],
    'Cloaks': [elven_cloak],
    'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
    'Elixirs': [elixir],
    'Healing': [healing_potion],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal],
    'Potions of Strength': [strength_potion],
    'Antidotes': [antidote]
}"""
# place armor first here; it is first in pack.
# otherwise it seems to give unexpected argument warning
"""loot_dict = {
    'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
    'Shields': [buckler, kite_shield, quantum_tower_shield],
    'Boots': [elven_boots, ancestral_footsteps],
    'Cloaks': [elven_cloak],
    'Weapons': [short_axe, broad_sword, great_sword, elvish_great_sword,
                quantum_sword, battle_axe, great_axe, elvish_great_axe, quantum_axe],
    'Elixirs': [elixir],
    'Healing': [healing_potion],
    'Rings of Regeneration': [ring_of_regeneration],
    'Rings of Protection': [ring_of_protection],
    'Town Portal Implements': [scroll_of_town_portal],
    'Potions of Strength': [strength_potion],
    'Antidotes': [antidote]
}"""
"""print(f"You see a treasure chest!")
            sleep(1.5)
            # gold_difficulty_class = 8
            # if dice_roll(1, 20) >= gold_difficulty_class:
            #    successful_tries += 1
            gold_roll = dice_roll(1, 20) * self.dungeon.level + 1
            print(f"Inside is {gold_roll} gold pieces!")
            self.gold += gold_roll
            sleep(1.5)
            pause()
            loot_difficulty_class = 7
            loot_dict = top_level_loot_dict
            while True:
                # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
                loot_roll = dice_roll(1, 20)
                self.hud()
                # print(f"Loot roll ---> {loot_roll}")  # remove after testing ?
                # pause()
                if loot_roll >= loot_difficulty_class:
                    successful_tries += 1
                    key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                    rndm_item_index = random.randrange(len(loot_dict[key]))
                    found_item = loot_dict[key][rndm_item_index]
                    print(found_item)  # REMOVE AFTER TESTING *****************************************************
                    if self.level >= found_item.minimum_level:
                        if found_item.item_type == 'Armor':
                            self.found_armor_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Shields':
                            self.found_shield_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Cloaks':
                            self.found_cloak_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Weapons':
                            self.found_weapon_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Rings of Regeneration':
                            self.found_ring_of_reg_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Rings of Protection':
                            self.found_ring_of_prot_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Boots':
                            self.found_boots_substitution(found_item)
                            continue
                        elif found_item.item_type == 'Town Portal Implements':
                            print(f"You see a {found_item.name} !")
                            sleep(.5)
                            print(f"You snarf it..")
                            self.town_portals += 1
                            pause()
                            continue
                        elif found_item.item_type == 'Healing':
                            print(f"You see a {found_item.name} !")
                            sleep(.5)
                            print(f"You snarf it..")
                            self.potions_of_healing += 1
                            pause()
                            continue
                        elif found_item.item_type == 'Potions of Strength':
                            print(f"You see a {found_item.name} !")
                            sleep(.5)
                            print(f"You snarf it..")
                            self.potions_of_strength += 1
                            pause()
                            continue
                        elif found_item.item_type == 'Elixirs':
                            print(f"You see a {found_item.name}!")
                            sleep(.5)
                            print(f"You snarf it..")
                            self.elixirs += 1
                            pause()
                            continue
                        elif found_item.item_type == 'Antidotes':
                            print(f"You see a {found_item.name}!")
                            sleep(.5)
                            print(f"You snarf it..")
                            self.antidotes += 1
                            pause()
                            continue
                    else:
                        print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                        pause()  # remove after testing
                        continue
                else:
                    if successful_tries == 0:
                        print(f"Besides the gold, there remains nothing but cobwebs...")
                        sleep(1)
                        pause()
                    self.discovered_interactives.append(treasure_chest_discovery)
                    self.hud()
                    return  # self.dungeon_description()"""
"""    def boss_clue_5(self):
        self.hud()
        print("You find a clue about the boss5")
        pause()
        self.hud()
        self.boss_hint_5 = True
        return

    def boss_clue_6(self):
        self.hud()
        print("You find a clue about the boss6")
        pause()
        self.hud()
        self.boss_hint_6 = True
        return"""
"""    if os.name == 'nt':
        try:
            p = Path(__file__).with_name('sad_cello_darren_curtis.wav')
            with p.open('r') as sad_cello:
                if sad_cello.readable():
                    winsound.PlaySound('sad_cello_darren_curtis.wav',
                                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        except FileNotFoundError:
            pass"""
# print(f"Missing sad cello theme or bad file path.")
# pause()
# if os.name == 'nt':
#    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\sad_cello_darren_curtis.wav',
#                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
"""if os.name == 'nt':
    try:
        p = Path(__file__).with_name('town_(tavern)_loop_by_alexander_nakarada.wav')
        with p.open('r') as theme_song:
            if theme_song.readable():
                winsound.PlaySound('town_(tavern)_loop_by_alexander_nakarada.wav',
                                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    except FileNotFoundError:
        pass
    # winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\town_(tavern)_loop_by_alexander_nakarada.wav',
    #                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    # place these files in same directory. use following syntax:
    # winsound.PlaySound('town_(tavern)_loop_by_alexander_nakarada.wav',
    # winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\gong.wav', winsound.SND_ASYNC)
"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\blacksmith_theme_2.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\chemist_theme.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\mountain_king.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\creepy_dungeon_theme_loop.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\boss_battle_2.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
"""
"""    if os.name == 'nt':
        winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\silvermandsound_the medieval_banquet.wav',
                           winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
"""
"""cls()
            try:
                p = Path(__file__).with_name('introduction.txt')
                with p.open('r') as intro:
                    if intro.readable():
                        typing(intro.read())

            except FileNotFoundError:
                print(f"Missing introduction.txt or bad file path.")
            pause()"""
"""cls()
        try:
            p = Path(__file__).with_name('splash_art.txt')
            with p.open('r') as splash:
                if splash.readable():
                    print(splash.read())

        except FileNotFoundError:
            print(f"Missing splash_art.txt or bad file path.")
            # pause()"""
"""        try:
            p = Path(__file__).with_name('hint_event_1.txt')
            with p.open('r') as hint_file:
                if hint_file.readable():
                    typing(hint_file.read())
                    pause()
        except FileNotFoundError:
            print(f"Missing hint_event_1.txt or bad file path.")"""
"""        try:
            p = Path(__file__).with_name('hint_event_2.txt')
            with p.open('r') as hint_file:
                if hint_file.readable():
                    typing(hint_file.read())
                    pause()
        except FileNotFoundError:
            print(f"Missing hint_event_2.txt or bad file path.")"""
"""        try:
            p = Path(__file__).with_name('hint_event_3.txt')
            with p.open('r') as hint_file:
                if hint_file.readable():
                    typing(hint_file.read())
                    pause()
        except FileNotFoundError:
            print(f"Missing hint_event_3.txt or bad file path.")"""
"""confirm_quit = input(f"Quit game? (y/n) ").lower()
                if confirm_quit not in ('y', 'n'):
                    continue
                elif confirm_quit == 'n':
                    break
                elif confirm_quit == 'y':"""
"""cls()
            print(f"                                  *Ability Score Improvement*")
            print()
            print(
                f"You may choose to improve a single ability score, such as strength, and increase it by 2 points.\n"
                f"\n"
                f"                           *OR*\n"
                f"\n"
                f"You may choose to improve two ability scores, such as charisma and constitution, by 1 point each.\n"
                f"\n"
                f"NOTES: \n"
                f"* Ability *modifiers* improve with each ascending even-numbered score, therefore, if unsure,\n"
                f"  it is generally recommended to apply 1 point to odd-numbered ability scores and apply \n"
                f"2 points to even-numbered scores.\n"
                f"* When your Constitution modifier increases by 1, your hit point maximum increases by 1 for each\n"
                f"  level you have attained.\n"
                f"                         *The maximum score for any ability is 20*"
                f"\n")
            pause()
"""
"""if self.level == 4 or self.level == 6 or self.level == 8 or self.level == 12 \
                    or self.level == 14 or self.level == 16 or self.level == 19 or asi_level_check:"""
"""    def display_map(self, maps):
        if self.in_a_pit:
            print(f"You are in uncharted territory..")
            sleep(1)
            return
        else:
            cls()
            print("You look at the map..")
            print(f"Position key: {self.position}")  # remove after testing
            self.coordinates = (self.x, self.y)
            print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}) Coordinates: {self.coordinates}")
            # if self.position != 0 and self.coordinates != self.dungeon.staircase:
            if self.coordinates != self.dungeon.staircase:
                self.dungeon.player_grid[self.y][self.x] = "X"

            for element in range(0, 20):
                print(*maps[element])

            # replace the X with a dot after printing so that it doesn't leave a trail:
            if self.coordinates != self.dungeon.staircase:
                self.dungeon.player_grid[self.y][self.x] = "."

            self.position = self.dungeon.grid[self.y][self.x]
            if self.coordinates != self.dungeon.staircase:
                print(f"S = Staircase X = your position E = Exit")
            else:
                print(f"S = Staircase E = Exit\nYou are currently at the staircase.")
            # place the next line in the main file to leave a trail of x's throughout the map to see where you've been.
            # player_1.dungeon.player_grid[player_1.y][player_1.x] = "x"
            return"""