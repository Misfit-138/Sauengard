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
import random
import os
import winsound
from dungeons import *


def pause():
    os.system('pause')


def sleep(seconds):
    time.sleep(seconds)


winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\originalsound.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
os.system('cls')
typing("Welcome to Sauengard.")
print("")
print("")
os.system('pause')
winsound.PlaySound(None, winsound.SND_ASYNC)
os.system('cls')

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
                # x = player_1.x
                # y = player_1.y
                print(dungeon.name)
                print(player_1.x)  # remove after testing
                print(player_1.y)  # remove after testing
                loaded_game = True
                time.sleep(1)
        else:
            print(f"Could not find {player_name} ")
            time.sleep(1.5)
            continue
    if new_game_or_load == 's':
        player_name = input("Thy name, noble sire? ")
        accept_stats = ""
        while accept_stats != "y":
            player_1 = Player(player_name)
            os.system('cls')
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
            # current_dungeon_map = player_1.dungeon.grid
            # current_player_map = player_1.dungeon.player_grid
            player_1.x = player_1.dungeon.starting_x
            player_1.y = player_1.dungeon.starting_y
            player_1.position = 0
            # player_1.current_dungeon_level = player_1.dungeon.level
            # player_1.current_dungeon_level_name = player_1.dungeon.name
            player_1.hud()
    print(f"You enter the town of Fieldenberg.")
    time.sleep(1.5)
    # player_1.hud()
    in_town = True
    in_dungeon = False
    # town_portal = False
    discovered_monsters = []
    winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\town_theme.wav',
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    while in_town:
        player_1.hud()
        town_functions = input(
            "You are in town.\n(S)ave, (Q)uit game, (M)arket, (I)nventory, (B)lacksmith, (C)hemist or ("
            "E)nter dungeon "
            "--> ").lower()
        '''        if town_functions == 'r':
            print("Restart")
            time.sleep(2)
            os.system('cls')
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
        elif town_functions == 'm':
            print("You visit the seller's market..")
            sleep(1.5)
            player_1.sell_items()
        elif town_functions == 'b':
            print("You visit the blacksmith..")
            sleep(1.5)
            player_1.blacksmith_main()
        elif town_functions == 'c':
            print("You make your way to the chemist manipulator.")
            time.sleep(1.5)
            player_1.chemist_main()
        elif town_functions == 'e':
            in_town = False
            in_dungeon = True
            if town_portal or loaded_game:
                print(f"You re-enter the portal.")
                # town_portal = False
            else:
                print("You enter the dungeon..")
            time.sleep(1)
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\creepy_dungeon_theme.wav',
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

            # DUNGEON NAVIGATION LOOP:

            while in_dungeon:
                previous_x = player_1.x
                previous_y = player_1.y
                #player_1.regenerate()
                #player_1.loot()  # for testing
                encounter = dice_roll(1, 20)
                player_1.hud()
                if player_1.position == 0:
                    player_1.dungeon_description(previous_x, previous_y)
                print(f"{player_1.dungeon.name}")
                dungeon_command = input(
                    "(Q)uit, Town (P)ortal, (H)ealing potion, (M)anage weapons, (I)nventory or WASD to navigate. --> ").lower()
                if dungeon_command not in ('w', 'a', 's', 'd', 'map', 'p', 'h', 'm', 'i', 'q'):
                    print("Unknown command")
                    time.sleep(.25)
                    continue
                if dungeon_command == 'p':
                    if player_1.use_scroll_of_town_portal():
                        in_town = True
                        in_dungeon = False
                        town_portal = True
                        break
                    else:
                        continue
                elif dungeon_command == 'q':
                    print("Quit game..")
                    while True:
                        confirm_quit = input("Are you sure? (y/n) ").lower()
                        if confirm_quit not in ('y', 'n'):
                            continue
                        elif confirm_quit == 'y':
                            exit()
                        elif confirm_quit == 'n':
                            break
                elif dungeon_command == 'h':
                    player_1.drink_healing_potion()
                    time.sleep(1)
                    player_1.hud()
                elif dungeon_command == 'm':
                    player_1.item_management('Weapons', player_1.wielded_weapon)
                    continue
                elif dungeon_command == 'i':
                    player_1.inventory()
                elif dungeon_command == 'w' or 'a' or 's' or 'd' or 'map':
                    if dungeon_command == 'w':
                        player_1.hud()
                        print("North")
                        player_1.y -= 1
                    if dungeon_command == 'a':
                        player_1.hud()
                        print("West")
                        player_1.x -= 1
                    if dungeon_command == 's':
                        player_1.hud()
                        print("South")
                        player_1.y += 1
                    if dungeon_command == 'd':
                        player_1.hud()
                        print("East")
                        player_1.x += 1
                    if dungeon_command == 'map':
                        player_1.display_map(player_1.dungeon.player_grid)  #
                        pause()
                        continue
                    # !!!!!!!!!!!!!!!! V NOTE the INDENT V !!!!!!!!!!!!!!!!
                    player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]  # note indent
                    player_1.dungeon_description(previous_x, previous_y)
                    sleep(1.5)
                    if player_1.position == "E":
                        encounter = 99
                        player_1.next_dungeon()
                player_1.regenerate()
                # eventually, make encounter a returned boolean from navigation function?
                if encounter > 10:

                    print("This should create monster now..")
                    # monster dictionary imported from monster module. keys correspond to difficulty
                    # in proximity to monster loop contains battle loop within it
                    in_proximity_to_monster = True
                    player_is_dead = False
                    while in_proximity_to_monster:
                        if player_is_dead:
                            # if player_1.check_dead():
                            winsound.PlaySound(None, winsound.SND_ASYNC)
                            player_1.hud()
                            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\sound.wav',
                                               winsound.SND_ASYNC)
                            print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                            time.sleep(2)
                            in_proximity_to_monster = False
                            in_dungeon = False
                            in_town = False
                            while True:
                                try_again = input("Do you wish to play again (y/n)? ").lower()
                                if try_again == "y":
                                    time.sleep(1)
                                    os.system('cls')
                                    break  # break out of prox to monster, dungeon and town up to top loop
                                if try_again == "n":
                                    print(f"Farewell.")
                                    exit()
                                if try_again not in ("y", "n"):
                                    print("Please enter y or n ")
                                    time.sleep(.5)
                                    continue
                        if not in_proximity_to_monster:
                            break

                        monster_key = random.randint(1, (player_1.level + 1))
                        monster_cls = random.choice(monster_dict[monster_key])
                        monster = monster_cls()  # create a monster object from the random class
                        if encounter == 99:
                            monster = Ghoul()  # for testing. change logic to be a boss 1 level above player
                        player_1.hud()
                        print(discovered_monsters)  # remove after testing
                        if monster.name in discovered_monsters:
                            print(f"You have encountered a level {monster.level} {monster.name}.")
                            time.sleep(2)
                        else:
                            print(f"{monster.introduction}")
                            discovered_monsters.append(monster.name)
                            os.system('pause')
                        if player_1.monster_likes_you(monster.name, monster.intelligence):
                            in_proximity_to_monster = False
                            break
                        if player_1.quick_move(monster.name):
                            in_proximity_to_monster = False
                            break  # if monster steals something he gets away clean, if not, battle
                        # PLAYER INITIATIVE, MONSTER INITIATIVE
                        player_initiative = dice_roll(1, 20) + player_1.dexterity_modifier
                        monster_initiative = dice_roll(1, 20) + monster.dexterity_modifier
                        print(f"Your initiative: {player_initiative}\nMonster initiative: {monster_initiative}")
                        time.sleep(1)
                        if monster_initiative > player_initiative:
                            attack_or_steal = dice_roll(1, 20)
                            if attack_or_steal > player_1.armor_class:  # (player_1.dexterity + player_1.dexterity_modifier):
                                player_1.hud()
                                print(f"You are caught off guard!")
                                melee_or_quantum = dice_roll(1, 100)
                                if monster.quantum_energy and melee_or_quantum > 50:
                                    damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                     player_1.dexterity_modifier,
                                                                                     player_1.ring_of_prot.protect)
                                    player_1.reduce_health(damage_to_player)
                                else:
                                    damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                if player_1.check_dead():  # if player  dead

                                    print(f"You were caught off guard!")
                                    time.sleep(1.5)
                                    print(f"You died!")
                                    player_is_dead = True
                                    continue
                            else:
                                print(f"The {monster.name} attacks!")
                                time.sleep(1.5)
                                print(f"You dodge, swiftly foiling its advantage!")
                                os.system('pause')

                        # ********************************* BATTLE LOOP ***********************************************
                        while True:
                            player_1.hud()
                            print(
                                f"Lvl {monster.level} {monster.name} {monster.hit_points} hp {monster.number_of_hd}d{monster.hit_dice}")
                            battle_choice = input("(F)ight, (H)ealing potion, (C)ast or (E)vade\nF/H/C/E --> ").lower()
                            if battle_choice == "e":
                                evade_success = player_1.evade(monster.name, monster.dexterity)
                                if evade_success:
                                    in_proximity_to_monster = False  # get out of battle loop
                                    break

                            elif battle_choice == "c":
                                player_1.hud()
                                print(f"Cast")
                                continue
                            elif battle_choice == 'h':
                                if healing_potion not in player_1.pack['Healing Potions']:
                                    print(f"You have no potions....")
                                    time.sleep(1)
                                    continue
                                else:
                                    player_1.drink_healing_potion()
                                    time.sleep(1)
                                    # ********MONSTER TURN AFTER YOU SWIG POTION***********************
                                    # if not monster.check_dead():
                                    melee_or_quantum = dice_roll(1, 20)
                                    if monster.quantum_energy and melee_or_quantum > 10:
                                        damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                         player_1.dexterity_modifier,
                                                                                         player_1.ring_of_prot.protect)
                                        player_1.reduce_health(damage_to_player)
                                    else:
                                        damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                        player_1.reduce_health(damage_to_player)

                                    if not player_1.check_dead():  # if player not dead
                                        if dice_roll(1, 20) > 17 and monster.can_paralyze:
                                            time.sleep(1)
                                            player_1.is_paralyzed = monster.paralyze(player_1.wisdom,
                                                                                     player_1.ring_of_prot.protect)
                                            if player_1.is_paralyzed:
                                                player_1.damage_while_paralyzed(monster.number_of_hd,
                                                                                monster.hit_dice)
                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You regain your faculties.")
                                                os.system('pause')
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
                                    # else:  # if monster not dead
                                    #    break

                            elif battle_choice == "f":
                                print(f"Fight.")
                            else:
                                print(f"The {monster.name} is not amused.")
                                time.sleep(1)
                                player_1.hud()
                                continue  # if player enters anything other than the above
                            # player's turn:
                            damage_to_monster = player_1.swing(player_1.name, player_1.level, player_1.dexterity,
                                                               player_1.strength, player_1.weapon_bonus, monster.level,
                                                               monster.name, monster.dexterity, monster.armor_class)
                            monster.reduce_health(damage_to_monster)  # take returned damage to monster
                            if monster.check_dead():
                                player_1.hud()
                                print(f"It died..")
                                time.sleep(1.5)
                                player_1.level_up(monster.experience_award, monster.gold)
                                in_proximity_to_monster = False
                                player_1.loot()

                                break

                            # monster turn:

                            if not monster.check_dead():
                                melee_or_quantum = dice_roll(1, 100)
                                if monster.quantum_energy and melee_or_quantum > 50:
                                    damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                     player_1.dexterity_modifier,
                                                                                     player_1.ring_of_prot.protect)
                                    player_1.reduce_health(damage_to_player)
                                else:
                                    damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                if not player_1.check_dead():  # if player not dead
                                    if monster.can_paralyze:  # dice_roll(1, 20) > 17 and monster.can_paralyze:
                                        time.sleep(1)
                                        player_1.is_paralyzed = monster.paralyze(player_1.wisdom,
                                                                                 player_1.ring_of_prot.protect)
                                        if player_1.is_paralyzed:
                                            player_1.damage_while_paralyzed(monster.number_of_hd, monster.hit_dice)
                                        if not player_1.check_dead():  # if player not dead
                                            print(f"You regain your faculties.")
                                            os.system('pause')
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
                            else:
                                break
                else:  # NEW..test
                    continue
        #

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
