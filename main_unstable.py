# Dungeon Crawler by Jules Pitsker
# (C)opyright 2022
# Blacksmith theme: 'Viking Intro loop' by Alexander Nakarada complete permission granted in YouTube
# Dungeon theme: 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
# complete permission granted in YouTube
# Chemist Theme: 'Might and Magic' by Alexander Nakarada complete permission granted in YouTube
# Town theme: 'Tavern Loop 1' by Alexander Nakarada complete permission granted in YouTube
# boss battle theme: 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony Creative commons license reuse ok
# Tavern theme 'The Medieval Banquet / Silvermansound No Copyright. Royalty Free Music
# Pit theme Jules Pitsker
# Telengard
# MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]


from player_module_testing import *
import pickle
from monster_module import *
from typing_module import typing
import os
import winsound
from dungeons import *

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
                # dungeon_key = player_1.dungeon_key
                dungeon = dungeon_dict[player_1.dungeon_key]
                print(dungeon.name)
                print(player_1.coordinates)  # remove after testing
                player_1.loaded_game = True
                time.sleep(1)
        else:
            print(f"Could not find {player_name} ")
            time.sleep(1.5)
            continue

    if new_game_or_load == 's':
        accept_stats = ""
        while accept_stats != 'y':
            player_1 = character_generator()
            player_1.hud()
            accept_stats = input(f"Accept character and continue? (y/n): ").lower()
        if accept_stats == "y":
            player_1.dungeon_key = 1
            player_1.dungeon = dungeon_dict[player_1.dungeon_key]
            # x,y is a numeric tuple corresponding to a classic grid with x and y coordinates
            # coordinates is set to x,y
            (player_1.x, player_1.y) = player_1.dungeon.staircase
            # 'position' corresponds to ASCII grids. 0 is the initialization position.
            # Thereafter, it is a string based on where the player lands in the ASCII grid,
            # '*' = border, '.' = wide open area, '7' = northwest corner, etc
            # the ASCII grid 'position' is used for display_map() and for dungeon_description()
            player_1.position = 0
            player_1.hud()

    print(f"You enter the town of Fieldenberg.")
    time.sleep(1.5)
    player_1.in_town = True
    # player_1.in_dungeon = False  # should be unneeded. defined as False in Player class and after portal use
    discovered_monsters = []
    town_theme()

    while player_1.in_town:
        player_1.hud()
        command = player_1.town_navigation(player_name)
        if command == 'e':
            player_1.in_town = False
            player_1.town_portal_exists = False
            player_1.in_dungeon = True
            player_1.hud()
            player_1.dungeon_theme()
            navigation_list = ['w', 'a', 's', 'd', 'ne', 'nw', 'se', 'sw', 'l', 'map', 'm', 'i']
            # DUNGEON NAVIGATION LOOP:
            player_is_dead = False
            while player_1.in_dungeon:
                if player_is_dead:
                    cls()
                    gong()
                    print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                    time.sleep(4)
                    player_1.in_proximity_to_monster = False
                    player_1.in_dungeon = False
                    player_1.in_town = False
                    while True:
                        try_again = input("Do you wish to play again (y/n)? ").lower()
                        if try_again == "y":
                            time.sleep(1)
                            cls()
                            player_1.in_proximity_to_monster = False
                            player_1.in_dungeon = False
                            player_1.in_town = False
                            player_is_dead = False
                            break
                        if try_again == "n":
                            print(f"Farewell.")
                            exit()
                        if try_again not in ("y", "n"):
                            # print("Please enter y or n ")
                            time.sleep(.5)
                            continue
                if not player_1.in_dungeon:
                    break
                player_1.coordinates = (player_1.x, player_1.y)
                player_1.previous_x = player_1.x
                player_1.previous_y = player_1.y
                # player_1.loot(0)  # for testing
                # player_1.asi()  # for testing
                if player_1.position == 0:  # 0 is the initialization position
                    print(player_1.dungeon.intro)
                    # set player position, which also removes intro condition
                    player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]

                dungeon_command = input(
                    "(L)ook at surroundings, use (MAP), (C)larifying elixir,\n"
                    "(Quit), Town (P)ortal, (H)ealing potion, (M)anage inventory,\n"
                    "(G)iant strength potion, (V)ial of Antidote, (I)nventory,\n"
                    "(Q)uantum effects, or W-A-S-D to navigate. --> ").lower()

                if dungeon_command == 'p':
                    if player_1.use_scroll_of_town_portal():
                        town_theme()
                        player_1.in_town = True
                        player_1.in_dungeon = False
                        player_1.town_portal_exists = True
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

                elif dungeon_command == "q":
                    player_1.hud()
                    monster = None  # quantum_effects needs monster parameter, but player is not in battle at this point
                    if player_1.quantum_units > 0:
                        player_1.quantum_effects(monster)

                elif dungeon_command == 'g':
                    if not player_1.drink_potion_of_strength():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'v':
                    if not player_1.drink_antidote():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'h':
                    if not player_1.drink_healing_potion():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command == 'c':
                    if not player_1.drink_elixir():
                        continue  # if you have no potions, don't waste a turn!

                elif dungeon_command in navigation_list:
                    player_1.navigation(dungeon_command)

                else:
                    print("Unknown command..")
                    sleep(.25)
                    player_1.dungeon_description()
                    continue  # continue means you do not waste a turn

                # ***** END OF NAVIGATION choice *************************************************************
                # !!!!!!!!!!!!!!!! V NOTE the INDENT below V !!!!!!!!!!!!!!!!
                # ******************************************************************************************
                # NAVIGATION CALCULATIONS:
                player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]  # note indent
                player_1.coordinates = (player_1.x, player_1.y)  #
                # ENCOUNTER LOGIC IS DETERMINED *BEFORE* event_logic(), BUT CAN BE RE-ASSIGNED BASED ON
                # RETURNED VALUES FROM event_logic()
                encounter = encounter_logic()
                # encounter = 15  # testing: this will make no monsters except bosses
                # EVENT LOGIC IS DETERMINED BEFORE end_of_turn_calculation() AND player_1.check_dead(),
                # IN CASE PLAYER SUFFERS DAMAGE, ETC
                event = player_1.event_logic()  # trigger any events corresponding to self.coordinates
                if event == "Undead Prophet":
                    encounter = 97
                elif event == "King Boss":
                    encounter = 98
                elif event == "Exit Boss":
                    encounter = 99
                # META CALCULATION FUNCTION FOR REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                # this is also called after monster melee, necro, poison and quantum attack
                # as well as after turning/banishing, etc., and player victory
                player_1.end_of_turn_calculation()
                if player_1.check_dead():  # player can die of necrosis/poison/event damage after calculations
                    player_is_dead = True
                    continue
                # LASTLY, dungeon_description()
                player_1.dungeon_description()  # this seems to work best when put LAST
                # if player_1.position == "E":
                #    encounter = 99  # dungeon level boss conditional
                #    player_1.next_dungeon()
                # ***********************************************************************************************>>>>
                if encounter < 11 or encounter > 20:  # < 11 = normal monster. > 20 = boss
                    monster = ""  # to prevent monster from being undefined
                    # monster dictionary imported from monster module. keys correspond to difficulty levels
                    # IN PROXIMITY TO MONSTER LOOP *contains battle loop within it*
                    player_1.in_proximity_to_monster = True
                    player_is_dead = False
                    while player_1.in_proximity_to_monster:
                        if player_is_dead:
                            break
                        if not player_1.in_proximity_to_monster:
                            break
                        # eventually offload this into a meta-monster generator function: ****************************
                        if encounter < 11:  # regular monster
                            monster = player_1.regular_monster_generator()
                            # monster = HobgoblinCaptain()  # testing
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
                        # ************************************************************************************
                        print(discovered_monsters)  # remove after testing
                        if monster.name in discovered_monsters:
                            print(f"You have encountered a level {monster.level} {monster.name}.")
                            # remove lvl after testing
                            pause()
                        else:
                            print(f"{monster.introduction}")
                            if encounter < 21:  # if not a boss
                                discovered_monsters.append(monster.name)
                            pause()
                        if encounter < 21:  # if not a boss, monster may like you or steal from you
                            if player_1.monster_likes_you(monster.name, monster.intelligence):
                                player_1.in_proximity_to_monster = False
                                # player_1.event_logic()  # this will trigger an event without using (L)ook
                                player_1.dungeon_description()
                                break
                            if player_1.quick_move(monster.name):
                                player_1.in_proximity_to_monster = False
                                # player_1.event_logic()  # this will trigger an event without using (L)ook
                                player_1.dungeon_description()
                                break  # if monster steals something he gets away clean, if not, battle

                        # PLAYER INITIATIVE, MONSTER INITIATIVE
                        player_initiative = player_1.initiative()
                        monster_initiative = monster.initiative()
                        print(f"Your initiative: {player_initiative}\nMonster initiative: {monster_initiative}")
                        pause()
                        # IF MONSTER GOES FIRST:
                        if monster_initiative > player_initiative:
                            player_1.hud()
                            # player_1.meta_monster_function(monster)
                            monster.meta_monster_function(player_1)
                            # I tried to offload this code, but the breaks and continues are pretty tangled
                            if not player_1.check_dead():  # if player not dead
                                if monster.can_paralyze:  # dice_roll(1, 20) > 17 and monster.can_paralyze:
                                    monster.paralyze(player_1)
                                    if not player_1.check_dead():  # if player not dead
                                        print(f"You regain your faculties.")
                                        pause()
                                        # continue
                                    else:
                                        print("You are dead and paralyzed!")
                                        player_is_dead = True
                                        break
                            else:  # you died
                                player_1.rndm_death_statement()
                                time.sleep(3)
                                player_is_dead = True
                                break
                        # OTHERWISE, PLAYER PROMPT and enter BATTLE LOOP
                        # ********************************* BATTLE LOOP ***********************************************
                        while True:
                            if not player_1.in_proximity_to_monster:
                                break
                            player_1.hud()
                            monster.monster_data()
                            battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                                  "(G)iant Strength potion, (V)ial of Antidote,\n(Q)uantum Effects or "
                                                  "(E)vade\nF/H/C/G/V/Q/E --> ").lower()

                            # these choices count as turns, and are therefore followed by monster's turn:
                            if battle_choice == 'e' or battle_choice == 'h' or battle_choice == 'g' or \
                                    battle_choice == 'v' or battle_choice == 'c' or battle_choice == 'q':
                                if battle_choice == "e":
                                    if player_1.evade(monster, encounter):
                                        # if encounter > 20:  # if evading a boss at this point,
                                        #    player_1.dungeon_theme()  # go back to dungeon theme song
                                        player_1.in_proximity_to_monster = False  # get out of battle loop and prox loop
                                        break
                                elif battle_choice == 'h':
                                    if not player_1.drink_healing_potion():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == 'g':
                                    if not player_1.drink_potion_of_strength():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == 'v':
                                    if not player_1.drink_antidote():
                                        continue  # if you have no potions, don't waste a turn!
                                elif battle_choice == 'c':
                                    if not player_1.drink_elixir():
                                        continue  # if you have no potions, don't waste a turn!
                                # PLAYER QUANTUM ATTACK
                                elif battle_choice == "q":
                                    player_1.hud()
                                    if player_1.quantum_units > 0:
                                        damage_to_monster = player_1.quantum_effects(monster)
                                        # if invalid input during quantum effect, None is returned:
                                        if damage_to_monster is None:  # invalid input
                                            continue  # should not waste a turn
                                        # If monster is successfully turned, stone-petrified, fearful,
                                        # disintegrated, lost to gravity well or banished, etc., experience is gained,
                                        # but player gets no gold or loot:
                                        if not player_1.in_proximity_to_monster:
                                            # CALCULATE REGENERATION/POTION OF STR/POISON/NECROSIS/PROT EFFECT:
                                            player_1.end_of_turn_calculation()
                                            if player_1.check_dead():  # you can die from poison or necrosis,
                                                player_is_dead = True  # right after victory, following calculations
                                                break
                                            if encounter > 20:  # if fighting a boss, go back to regular music
                                                gong()
                                                sleep(4)
                                                player_1.dungeon_theme()
                                                if encounter == 99:
                                                    player_1.boss_hint_logic()
                                            player_1.level_up(monster.experience_award, monster.gold)
                                            # player_1.event_logic()  # this will trigger an event without using (L)ook
                                            player_1.dungeon_description()  # has worked well for a while
                                            # pause()
                                            break
                                        # otherwise, calculate damage:
                                        # if total monster hit points is returned from quantum_effects(),
                                        # then monster will die instantly and player gets loot
                                        monster.reduce_health(damage_to_monster)
                                        if monster.check_dead():
                                            player_1.hud()
                                            if encounter > 20:  # if fighting boss
                                                gong()
                                                if monster.proper_name != "None":
                                                    print(f"You have vanquished {monster.proper_name}! "
                                                          f"You are victorious!")
                                                    player_1.vanquished_foes.append(monster.proper_name)
                                                else:
                                                    print(f"You have vanquished the {monster.name}!")
                                                sleep(4)
                                                player_1.dungeon_theme()
                                            else:
                                                print(f"You have defeated the {monster.name}..")
                                            # CALCULATE REGENERATION/POTION OF STR/POISON/NECROSIS/PROT EFFECT:
                                            player_1.end_of_turn_calculation()
                                            pause()
                                            if player_1.check_dead():  # you can die from poison or necrosis,
                                                player_is_dead = True  # right after victory, following calculations
                                                player_1.in_proximity_to_monster = False
                                                break
                                            player_1.level_up(monster.experience_award, monster.gold)
                                            player_1.in_proximity_to_monster = False
                                            player_1.loot(encounter)
                                            if encounter > 20:  # if you kill the boss, you get extra chance for loot
                                                if encounter == 99:  # level exit boss
                                                    player_1.boss_hint_logic()
                                                player_1.loot(encounter)  # 8 difficulty class
                                            player_1.dungeon_description()  # beta works so far
                                            break

                                    else:
                                        print(f"You have no Quantum unit energy!")
                                        pause()
                                        continue  # if you have no QU, don't waste a turn!
                                # ****MONSTER TURN AFTER YOU SWIG POTION, fail to evade, or cast quantum attack******
                                #
                                player_1.hud()
                                monster.meta_monster_function(player_1)
                                if not player_1.check_dead():  # if player not dead
                                    # I tried to offload this code, but the breaks and continues are pretty tangled
                                    if monster.can_paralyze:  # dice_roll(1, 20) > 17 and monster.can_paralyze:
                                        sleep(1)
                                        monster.paralyze(player_1)
                                        # pause()
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
                                # player_1.hud()  # commented out and seemed like it worked fine beta
                                # continue  # commented out and it seemed to work fine beta

                            # FIGHT: player chooses melee:
                            elif battle_choice == "f":
                                print(f"Fight.")
                                # player chooses melee:
                                damage_to_monster = player_1.melee(monster.name, monster.armor_class)
                                monster.reduce_health(damage_to_monster)
                                # in the future, check_dead function can encompass the following if--else statements.
                                # just pass encounter parameter
                                if monster.check_dead():
                                    player_1.hud()
                                    if encounter > 20:  # if fighting boss
                                        gong()
                                        if monster.proper_name != "None":
                                            print(f"You have vanquished {monster.proper_name}! You are victorious!")
                                            player_1.vanquished_foes.append(monster.proper_name)
                                        else:
                                            print(f"You have vanquished the {monster.name}!")
                                        sleep(4)
                                        player_1.dungeon_theme()
                                    else:
                                        print(f"You are victorious..")
                                    pause()
                                    # CALCULATE REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                                    player_1.end_of_turn_calculation()
                                    if player_1.check_dead():
                                        player_is_dead = True
                                        player_1.in_proximity_to_monster = False
                                        break
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot(encounter)
                                    if encounter > 20:  # if you kill the boss, you get extra chance for loot
                                        if encounter == 99:  # if exit boss has been defeated,
                                            player_1.boss_hint_logic()  # give main boss hints
                                        player_1.loot(encounter)  # 8 difficulty class: better chance at loot
                                    player_1.dungeon_description()  # beta works so far
                                    break

                                # monster turn if still alive after player melee attack:
                                else:
                                    monster.meta_monster_function(player_1)
                                    # I tried to offload this code, but the breaks and continues are pretty tangled
                                    if not player_1.check_dead():  # if player not dead
                                        if monster.can_paralyze:  # dice_roll(1, 20) > 17 and monster.can_paralyze:
                                            monster.paralyze(player_1)
                                            # pause()
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

                            else:  # invalid inputs
                                print(f"The {monster.name} is not amused.")
                                time.sleep(1)
                                player_1.hud()
                                continue
                            #
                else:  # if encounter condition False
                    continue
        else:  # if player is in town and does not (E)nter dungeon
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

"""melee_or_quantum = dice_roll(1, 20)
                            if monster.quantum_energy and melee_or_quantum > 10:
                                damage_to_player = monster.quantum_energy_attack(monster.name,
                                                                                 player_1.wisdom_modifier,
                                                                                 player_1.ring_of_prot.protect, 
                                                                                 player_1.temp_protection_effect)
                                player_1.reduce_health(damage_to_player)
                                player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                player_1.calculate_protection_effect()
                                player_1.regenerate()
                                player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                player_1.calculate_necrotic_dot()
                            else:
                                damage_to_player = monster.swing(monster.name, player_1.armor_class)
                                player_1.reduce_health(damage_to_player)
                                player_1.calculate_potion_of_strength()  # potions of strength have 5 uses; battle & nav
                                player_1.calculate_protection_effect()
                                player_1.regenerate()
                                player_1.calculate_poison()  # poison wears off after 5 turns of battle/navigation
                                player_1.calculate_necrotic_dot()
                            if player_1.check_dead():  # if player  dead
                                print(f"You were caught off guard!")
                                time.sleep(1.5)
                                print(f"You died!")
                                player_is_dead = True
                                continue"""

"""player_1.is_paralyzed = monster.paralyze(player_1.wisdom,
                                                                                 player_1.ring_of_prot.protect)
                                        if player_1.is_paralyzed:
                                            player_1.damage_while_paralyzed(monster.number_of_hd,
                                                                            monster.hit_dice)"""
"""                    if dungeon_command == 'w':
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
                        # this will call dungeon_description().
                        # after returning, event_logic() will be called at end of navigation turn
                        # which will trigger any events corresponding to player self.coordinates
                        player_1.dungeon_description()
                        player_1.coordinates = (player_1.x, player_1.y)
                        player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]
                    if dungeon_command == 'map':
                        player_1.display_map(player_1.dungeon.player_grid)  #
                        pause()
                        player_1.dungeon_description()
                        # player_1.event_logic()
                        # continue"""
"""elif dungeon_command == 'w' or dungeon_command == 'a' or dungeon_command == 's' \
                        or dungeon_command == 'd' or dungeon_command == 'l' or dungeon_command == 'map' or \
                        dungeon_command == 'ne' or dungeon_command == 'nw' or dungeon_command == 'se' or \
                        dungeon_command == 'sw':"""
"""                elif dungeon_command == 'm':
                    player_1.item_management_sub_menu()
                    # continue
                elif dungeon_command == 'i':
                    player_1.inventory()"""
# player_name = input("Thy name, noble sire? ")
"""accept_stats = ""
# player_1 = Player(player_name)

while accept_stats != "y":
    player_1 = character_generator()
    cls()
    print(f"Name: {player_1.name}")
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
if accept_stats == "y":"""