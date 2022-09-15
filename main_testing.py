"""The global keyword is the tool that Python provides for you to opt out of encapsulation
and break the natural scope of a variable. Encapsulation means that each of your components is a logical,
self-contained unit that should work as a black box and performs one thing
(note: this one thing is conceptual and may consist of many, possibly non-trivial, sub-steps)
without mutating global state or producing side effects.
The reason is modularity: if something goes wrong in a program (and it will), having strong encapsulation makes it very
 easy to determine where the failing component is.

Encapsulation makes code easier to refactor, maintain and expand upon.
If you need a component to behave differently, it should be easy to remove it or adjust it without these modifications
 causing a domino effect of changes across other components in the system.

Basic tools for enforcing encapsulation include classes, functions, parameters and the return keyword.
Languages often provide modules, namespaces and closures to similar effect, but the end goal is always to limit scope
 and allow the programmer to create loosely-coupled abstractions.

Functions take in input through parameters and produce output through return values.
You can assign the return value to variables in the calling scope. You can think of parameters as "knobs" that adjust
 the function's behavior. Inside the function, variables are just temporary storage used by the function needed to
  generate its one return value then disappear.

Ideally, functions are written to be pure and idempotent; that is, they don't modify global state and produce
the same result when called multiple times. Python is a little less strict about this than other languages, and it's
natural to use certain in-place functions like sort and random.shuffle. These are exceptions that prove the rule
 (and if you know a bit about sorting and shuffling, they make sense in these contexts due to the algorithms used
 and the need for efficiency).

An in-place algorithm is impure and non-idempotent, but if the state that it modifies is limited to its parameter(s)
and its documentation and return value (usually None) support this, the behavior is predictable and comprehensible."""
# MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]
# introduction_file = open("trett.txt", "r")
# if introduction_file.readable():
#    print(introduction_file.read())

import pickle
from player_module_testing import *
from monster_module import *
from typing_module import *
# import random
import os
import winsound
from dungeons import *


def pause():
    os.system('pause')


def sleep(seconds):
    time.sleep(seconds)


def encounter_logic():
    monster_encounter = dice_roll(1, 20)
    return monster_encounter


def gong():
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\gong.wav',
                       winsound.SND_ASYNC)


def blacksmith_theme():
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\blacksmith_theme_2.wav',
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def chemist_theme():
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\chemist_theme.wav',
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def mountain_king_theme():
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\mountain_king.wav',
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def dungeon_theme():
    winsound.PlaySound(
        'C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\dungeon_theme_2.wav',
        winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def boss_battle_theme():
    winsound.PlaySound(
        'C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\boss_battle_2.wav',
        winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def town_theme():
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\town_theme_2.wav',
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\originalsound.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
cls()
typing("Welcome to Sauengard.")
print("")
print("")
pause()
winsound.PlaySound(None, winsound.SND_ASYNC)
cls()
player_1 = ""  # to get rid of undefined warning
player_name = ""  # to get rid of undefined warning
while True:
    town_portal = False
    loaded_game = False
    new_game_or_load = input("(S)tart a new character or (L)oad a saved one? ").lower()
    if new_game_or_load not in ('s', 'l'):
        continue
    if new_game_or_load == 'l':
        player_name = input("Enter name of saved character: ")
        load_a_character = player_name + ".sav"
        if os.path.isfile(load_a_character):
            print(f"{player_name} found.")
            with open(load_a_character, 'rb') as saved_player:
                player_1 = pickle.load(saved_player)
                time.sleep(1)
                print(f"{player_name} read.")
                time.sleep(1)
                dungeon_key = player_1.dungeon_key
                dungeon = dungeon_dict[player_1.dungeon_key]
                print(dungeon.name)
                print(player_1.coordinates)  # remove after testing
                loaded_game = True
                time.sleep(1)
        else:
            print(f"Could not find {player_name} ")
            time.sleep(1.5)
            continue
    if new_game_or_load == 's':
        player_name = input("Thy name, noble sire? ")
        accept_stats = ""
        player_1 = Player(player_name)
        while accept_stats != "y":
            cls()
            print(f"Strength: {player_1.strength}")
            print(f"Dexterity: {player_1.dexterity}")
            print(f"Constitution {player_1.constitution}")
            print(f"Intelligence: {player_1.intelligence}")
            print(f"Wisdom: {player_1.wisdom}")
            print(f"Charisma: {player_1.charisma}")
            print(f"Hitpoints: {player_1.hit_points}")
            print(f"Strength modifier: {player_1.strength_modifier}")
            print(f"Constitution modifier: {player_1.constitution_modifier}")
            print(f"Intelligence modifier: {player_1.intelligence_modifier}")
            print(f"Wisdom modifier: {player_1.wisdom_modifier}")
            print(f"Charisma modifier: {player_1.charisma_modifier}")
            print(f"Proficiency bonus: {player_1.proficiency_bonus}")
            accept_stats = input("Ok to continue? ").lower()
        # a while loop's 'else' part runs if no break occurs and the condition is false
        if accept_stats == "y":
            player_1.dungeon_key = 1
            player_1.dungeon = dungeon_dict[player_1.dungeon_key]
            (player_1.x, player_1.y) = player_1.dungeon.staircase
            player_1.position = 0
            player_1.hud()
    print(f"You enter the town of Fieldenberg.")
    time.sleep(1.5)
    # player_1.hud()
    in_town = True
    in_dungeon = False
    # town_portal = False
    discovered_monsters = []
    town_theme()
    while in_town:
        player_1.hud()
        town_functions = input(
            "You are in town.\n(S)ave, (Q)uit game, (I)nventory, (B)lacksmith, (C)hemist , (T)avern, or ("
            "E)nter dungeon "
            "--> ").lower()
        '''        if town_functions == 'r':
            print("Restart")
            time.sleep(2)
            cls()
            in_town = False
            break'''
        if town_functions == 'q':
            print("Exiting..")
            exit()
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
                        print(f"Saving {player_1.name}...")
                        character_filename = player_1.name + ".sav"
                        with open(character_filename, 'wb') as player_save:
                            pickle.dump(player_1, player_save)
                            print(f"{player_1.name} saved.")
                            time.sleep(2)
                            break
            else:
                print(f"Saving {player_1.name}...")
                character_filename = player_1.name + ".sav"
                with open(character_filename, 'wb') as player_save:
                    pickle.dump(player_1, player_save)
                    print(f"{player_1.name} saved.")
                    time.sleep(2)
        elif town_functions == 'i':
            player_1.inventory()

        elif town_functions == 'b':
            print("You visit the blacksmith..")
            sleep(1.5)
            blacksmith_theme()
            player_1.blacksmith_main()
            town_theme()

        elif town_functions == 'c':
            print("You make your way to the chemist manipulator..")
            time.sleep(1.5)
            chemist_theme()
            player_1.chemist_main()
            town_theme()
        elif town_functions == 't':
            player_1.inn()

        elif town_functions == 'e':
            in_town = False
            in_dungeon = True
            if town_portal or loaded_game:
                print(f"You re-enter the portal.")
                # town_portal = False
            else:
                print("You enter the dungeon..")
            time.sleep(1)
            player_1.hud()
            dungeon_theme()

            # DUNGEON NAVIGATION LOOP:
            player_is_dead = False
            while in_dungeon:
                # if player_1.check_dead():
                #    player_is_dead = True
                # continue
                if player_is_dead:
                    # winsound.PlaySound(None, winsound.SND_ASYNC)
                    cls()
                    # player_1.hud()
                    gong()
                    print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                    time.sleep(4)
                    in_proximity_to_monster = False
                    in_dungeon = False
                    in_town = False
                    # player_is_dead = False
                    # break
                    while True:
                        try_again = input("Do you wish to play again (y/n)? ").lower()
                        if try_again == "y":
                            time.sleep(1)
                            cls()
                            in_proximity_to_monster = False
                            in_dungeon = False
                            in_town = False
                            player_is_dead = False
                            break
                        if try_again == "n":
                            print(f"Farewell.")
                            exit()
                        if try_again not in ("y", "n"):
                            # print("Please enter y or n ")
                            time.sleep(.5)
                            continue
                if not in_dungeon:
                    break
                # player_1.hud()
                player_1.coordinates = (player_1.x, player_1.y)
                player_1.previous_x = player_1.x
                player_1.previous_y = player_1.y
                # player_1.loot(0)  # for testing
                # encounter = dice_roll(1, 20)
                # player_1.asi()
                if player_1.position == 0:  # 0 is the initialization position
                    print(player_1.dungeon.intro)
                    # set player position, which also removes intro condition
                    player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]

                dungeon_command = input(
                    "(L)ook at surroundings, use (MAP), (C)larifying elixir,\n"
                    "(Quit), Town (P)ortal, (H)ealing potion, (M)anage inventory,\n"
                    "(G)iant strength potion, (I)nventory or WASD to navigate. --> ").lower()

                if dungeon_command == 'p':
                    if player_1.use_scroll_of_town_portal():
                        town_theme()
                        in_town = True
                        in_dungeon = False
                        town_portal = True
                        break
                    else:
                        continue  # if you have no scrolls, don't waste a turn

                elif dungeon_command == 'quit':
                    print("Quit game..")
                    while True:
                        confirm_quit = input("Are you sure? (y/n) ").lower()
                        if confirm_quit not in ('y', 'n'):
                            continue
                        elif confirm_quit == 'y':
                            exit()
                        elif confirm_quit == 'n':
                            break

                elif dungeon_command == 'g':
                    if not player_1.drink_potion_of_strength():
                        continue  # if you have no potions, don't waste a turn!
                elif dungeon_command == 'h':
                    if not player_1.drink_healing_potion():
                        continue  # if you have no potions, don't waste a turn!
                elif dungeon_command == 'c':
                    if not player_1.drink_elixir():
                        continue  # if you have no potions, don't waste a turn!
                elif dungeon_command == 'm':
                    player_1.item_management_sub_menu()
                    # continue
                elif dungeon_command == 'i':
                    player_1.inventory()
                elif dungeon_command == 'w' or dungeon_command == 'a' or dungeon_command == 's' \
                        or dungeon_command == 'd' or dungeon_command == 'l' or dungeon_command == 'map':
                    if dungeon_command == 'w':
                        player_1.hud()
                        print("North")
                        player_1.y -= 1
                        sleep(.5)
                    if dungeon_command == 'a':
                        player_1.hud()
                        print("West")
                        player_1.x -= 1
                        sleep(.5)
                    if dungeon_command == 's':
                        player_1.hud()
                        print("South")
                        player_1.y += 1
                        sleep(.5)
                    if dungeon_command == 'd':
                        player_1.hud()
                        print("East")
                        player_1.x += 1
                        sleep(.5)
                    if dungeon_command == 'l':
                        player_1.dungeon_description()
                        player_1.coordinates = (player_1.x, player_1.y)
                        player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]
                        # player_1.event_logic()
                        # pause()
                        # continue
                    if dungeon_command == 'map':
                        player_1.display_map(player_1.dungeon.player_grid)  #
                        pause()
                        player_1.dungeon_description()
                        # player_1.event_logic()
                        # continue
                else:
                    print("Unknown command..")
                    sleep(.25)
                    player_1.dungeon_description()
                    continue  # continue means you do not use a turn
                # ***** END OF NAVIGATION TURN *************************************************************
                # !!!!!!!!!!!!!!!! V NOTE the INDENT below V !!!!!!!!!!!!!!!!
                # ******************************************************************************************

                player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]  # note indent
                player_1.coordinates = (player_1.x, player_1.y)  #
                # encounter = player_1.event_logic()
                encounter = encounter_logic()
                event = player_1.event_logic()
                if event == "King Boss":
                    encounter = 98
                elif event == "Undead Prophet":
                    encounter = 97
                # print(encounter)
                player_1.regenerate()
                player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                player_1.calculate_necrotic_dot()  # same as poison
                if player_1.check_dead():
                    player_is_dead = True
                    continue
                player_1.dungeon_description()  # this seems to work best when put last

                if player_1.position == "E":
                    # monster = player_1.dungeon.boss
                    encounter = 99  # dungeon level boss conditional
                    player_1.next_dungeon()
                # ***********************************************************************************************>>>>
                # eventually, make encounter a returned boolean from navigation function?
                if encounter < 10 or encounter > 20:
                    monster = ""  # just to prevent monster from being undefined
                    # monster dictionary imported from monster module. keys correspond to difficulty
                    # in proximity to monster loop contains battle loop within it
                    in_proximity_to_monster = True
                    player_is_dead = False
                    while in_proximity_to_monster:
                        if player_is_dead:
                            break
                        if not in_proximity_to_monster:
                            break
                        # monster_key = random.randint(1, player_1.level)  # (player_1.level + 1)
                        # monster_cls = random.choice(monster_dict[monster_key])
                        # monster = monster_cls()  # create a monster object from the random class
                        if encounter < 10:  # regular monster
                            monster = player_1.regular_monster_generator()
                            # monster = Specter()  # testing
                        elif encounter == 99:  # level exit boss fight
                            monster = player_1.exit_boss_generator()
                            gong()
                            sleep(4)
                            boss_battle_theme()
                            pause()
                            player_1.hud()
                        elif encounter == 98:  # undead king
                            monster = player_1.king_monster_generator()
                            gong()
                            sleep(4)
                            mountain_king_theme()
                            pause()
                            player_1.hud()
                        elif encounter == 97:  # undead prophet
                            monster = player_1.undead_prophet_generator()
                            gong()
                            sleep(4)
                            boss_battle_theme()
                            pause()
                            player_1.hud()
                        print(discovered_monsters)  # remove after testing
                        if monster.name in discovered_monsters:
                            print(f"You have encountered a level {monster.level} {monster.name}.")
                            # remove lvl after testing
                            pause()
                        else:
                            print(f"{monster.introduction}")
                            discovered_monsters.append(monster.name)
                            pause()
                        if encounter < 21:  # if not a boss, monster may like you or steal from you
                            if player_1.monster_likes_you(monster.name, monster.intelligence):
                                in_proximity_to_monster = False
                                player_1.dungeon_description()
                                break
                            if player_1.quick_move(monster.name):
                                in_proximity_to_monster = False
                                player_1.dungeon_description()
                                break  # if monster steals something he gets away clean, if not, battle

                        # PLAYER INITIATIVE, MONSTER INITIATIVE
                        player_initiative = dice_roll(1, 20) + player_1.dexterity_modifier
                        monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier
                        print(f"Your initiative: {player_initiative}\nMonster initiative: {monster_initiative}")
                        pause()
                        if monster_initiative > player_initiative:
                            player_1.hud()
                            melee_or_quantum = dice_roll(1, 20)
                            if monster.quantum_energy and melee_or_quantum > 10:
                                damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                 player_1.wisdom_modifier,
                                                                                 player_1.ring_of_prot.protect)
                                player_1.reduce_health(damage_to_player)
                                player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                player_1.regenerate()
                                player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                player_1.calculate_necrotic_dot()
                            else:
                                damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                player_1.reduce_health(damage_to_player)
                                player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                player_1.regenerate()
                                player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                player_1.calculate_necrotic_dot()
                            if player_1.check_dead():  # if player  dead
                                print(f"You were caught off guard!")
                                time.sleep(1.5)
                                print(f"You died!")
                                player_is_dead = True
                                continue
                        # ********************************* BATTLE LOOP ***********************************************
                        while True:
                            if not in_proximity_to_monster:
                                break
                            player_1.hud()
                            if monster.proper_name == "None":
                                print(f"Lvl {monster.level} {monster.name} AC: {monster.armor_class} "
                                      f"HP: {monster.hit_points} ({monster.number_of_hd}d{monster.hit_dice})")
                            else:
                                print(f"{monster.proper_name} AC: {monster.armor_class} "
                                      f"HP: {monster.hit_points} ({monster.number_of_hd}d{monster.hit_dice})")
                            battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir, "
                                                  "(G)iant Strength potion, (Q)uantum attack or "
                                                  "(E)vade\nF/H/C/G/Q/S --> ").lower()

                            # these choices count as turns, and are therefore followed by monster's turn:
                            if battle_choice == 'e' or battle_choice == 'h' or battle_choice == 'g' or \
                                    battle_choice == 'c' or battle_choice == 'q':
                                if battle_choice == "e":
                                    if player_1.evade(monster.name, monster.dexterity):
                                        if encounter > 20:  # if evading a boss at this point,
                                            dungeon_theme()  # go back to dungeon theme song
                                        in_proximity_to_monster = False  # get out of battle loop, regardless of monster
                                        break
                                elif battle_choice == 'h':
                                    if not player_1.drink_healing_potion():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == 'g':
                                    if not player_1.drink_potion_of_strength():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == 'c':
                                    if not player_1.drink_elixir():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == "q":
                                    player_1.hud()
                                    if player_1.quantum_units > 0:
                                        damage_to_monster = player_1.cast(monster)
                                        monster.reduce_health(damage_to_monster)
                                        if monster.check_dead():
                                            player_1.hud()
                                            if encounter > 20:  # if fighting boss
                                                gong()
                                                print(f"You have vanquished {monster.proper_name}! You are victorious!")
                                                sleep(4)
                                                dungeon_theme()
                                            else:
                                                print(f"It died..")

                                            player_1.regenerate()
                                            player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                            player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                            player_1.calculate_necrotic_dot()
                                            pause()
                                            if player_1.check_dead():  # you can die from poison or necrosis,
                                                player_is_dead = True  # right after victory, following calculations
                                                in_proximity_to_monster = False
                                                break
                                            player_1.level_up(monster.experience_award, monster.gold)
                                            in_proximity_to_monster = False
                                            player_1.loot(encounter)
                                            if encounter > 20:  # if you kill the boss, you get extra chance for loot
                                                player_1.loot(encounter)  # 8 difficulty class
                                            break
                                    else:
                                        print(f"You have no Quantum unit energy!")
                                        pause()
                                        continue  # if you have no QU, don't waste a turn!
                                # ****MONSTER TURN AFTER YOU SWIG POTION, fail evade or cast******
                                # elif not monster.check_dead():
                                player_1.hud()
                                player_1.meta_monster_function(monster)
                                if not player_1.check_dead():  # if player not dead
                                    if dice_roll(1, 20) > 17 and monster.can_paralyze:
                                        sleep(1)
                                        player_1.is_paralyzed = monster.paralyze(player_1.wisdom,
                                                                                 player_1.ring_of_prot.protect)
                                        if player_1.is_paralyzed:
                                            player_1.damage_while_paralyzed(monster.number_of_hd,
                                                                            monster.hit_dice)
                                        if not player_1.check_dead():  # if player not dead
                                            print(f"You regain your faculties.")
                                            pause()
                                            continue
                                        else:
                                            print("You are dead and paralyzed!")
                                            player_is_dead = True
                                            break
                                else:
                                    print(f"You died!")
                                    time.sleep(3)
                                    player_is_dead = True
                                    break
                                player_1.hud()
                                continue
                            # FIGHT:
                            elif battle_choice == "f":
                                print(f"Fight.")

                                # player's turn:
                                damage_to_monster = player_1.swing(monster.name, monster.armor_class)
                                monster.reduce_health(damage_to_monster)
                                if monster.check_dead():
                                    player_1.hud()
                                    if encounter > 20:  # if fighting boss
                                        gong()
                                        print(f"You have vanquished {monster.proper_name}! You are victorious!")
                                        sleep(4)
                                        dungeon_theme()
                                    else:
                                        print(f"It died..")
                                    pause()
                                    player_1.regenerate()
                                    player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                    player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                    player_1.calculate_necrotic_dot()
                                    if player_1.check_dead():
                                        player_is_dead = True
                                        in_proximity_to_monster = False
                                        break
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    in_proximity_to_monster = False
                                    player_1.loot(encounter)
                                    if encounter > 20:  # if you kill the boss, you get extra chance for loot
                                        player_1.loot(encounter)  # 8 difficulty class
                                    break

                                # monster turn if still alive:
                                else:
                                    player_1.meta_monster_function(monster)
                                    if not player_1.check_dead():  # if player not dead
                                        if monster.can_paralyze:  # dice_roll(1, 20) > 17 and monster.can_paralyze:
                                            time.sleep(1)
                                            player_1.is_paralyzed = monster.paralyze(player_1.wisdom,
                                                                                     player_1.ring_of_prot.protect)
                                            if player_1.is_paralyzed:
                                                player_1.damage_while_paralyzed(monster.number_of_hd, monster.hit_dice)
                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You regain your faculties.")
                                                pause()
                                                continue
                                            else:
                                                print("You are dead and paralyzed!")
                                                player_is_dead = True
                                                break
                                    else:  # you died
                                        player_1.rndm_death_statement()
                                        time.sleep(3)
                                        player_is_dead = True
                                        break
                                    player_1.hud()
                                #else:  # pretty sure this code is unreachable
                                    #break
                            else:  # invalid inputs
                                print(f"The {monster.name} is not amused.")
                                time.sleep(1)
                                player_1.hud()
                                continue
                            #
                else:  # if encounter condition False
                    continue

# removed code:

'''                if player_1.position == ".":
                    print("You are in a dark corridor, there are doors leading in each direction...")
                    sleep(1.5)
                if player_1.position == "E":
                    print("You found the exit...")
                    player_1.dungeon_key += 1
                    player_1.dungeon = dungeon_dict[player_1.dungeon_key]
                    # current_dungeon_map = player_1.dungeon.grid
                    # current_player_map = player_1.dungeon.player_grid
                    x = player_1.dungeon.starting_x
                    y = player_1.dungeon.starting_y
                    player_1.position = 0
                    player_1.current_dungeon_level = player_1.dungeon.level
                    player_1.current_dungeon_level_name = player_1.dungeon.name
                    pause()'''
'''elif town_functions == 'm':
            print("You visit the seller's market..")
            sleep(1.5)
            player_1.sell_items()'''
'''                            else:
                                print(f"The {monster.name} attacks!")
                                time.sleep(1.5)
                                print(f"You dodge, swiftly foiling its advantage!")
                                os.system('pause')'''
'''# if player_1.check_dead():
                            winsound.PlaySound(None, winsound.SND_ASYNC)
                            cls()
                            #player_1.hud()
                            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\sound.wav',
                                               winsound.SND_ASYNC)
                            print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                            time.sleep(2)
                            in_proximity_to_monster = False
                            in_dungeon = False
                            in_town = False
                            player_is_dead = False
                            while True:
                                try_again = input("Do you wish to play again (y/n)? ").lower()
                                if try_again == "y":
                                    time.sleep(1)
                                    cls()
                                    break  # break out of prox to monster, dungeon and town, up to top loop
                                if try_again == "n":
                                    print(f"Farewell.")
                                    exit()
                                if try_again not in ("y", "n"):
                                    print("Please enter y or n ")
                                    time.sleep(.5)
                                    continue'''
"""                                if monster.quantum_energy and melee_or_quantum > 10:
                                    damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                     player_1.wisdom_modifier,
                                                                                     player_1.ring_of_prot.protect)
                                    player_1.reduce_health(damage_to_player)
                                    player_1.calculate_potion_of_strength()  # potions of str have 5 uses; battle & nav
                                    player_1.regenerate()
                                    player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                    player_1.calculate_necrotic_dot()
                                else:
                                    damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                    player_1.calculate_potion_of_strength()  # potions of str have 5 uses; battle & nav
                                    player_1.regenerate()
                                    player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                    player_1.calculate_necrotic_dot()"""

"""                if dungeon_command not in ('w', 'a', 's', 'd', 'l', 'e', 'map', 'p', 'g', 'h', 'm', 'i', 'q'):
                    print("Unknown command")
                    time.sleep(.25)
                    player_1.dungeon_description()
                    continue
"""
"""#if dungeon_command not in ('w', 'a', 's', 'd', 'l', 'c', 'map', 'p', 'g', 'h', 'm', 'i', 'quit'):
                #    print("Unknown command")
                #    time.sleep(.25)
                #    player_1.dungeon_description()
                #    continue"""