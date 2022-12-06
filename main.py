# Sauengard © Copyright 2022 by Jules Pitsker
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.

# sad_cello_theme(): "Soul's Departure" Royalty Free Music by Darren Curtis
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# blacksmith_theme(): 'Viking Intro loop' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# dungeon_theme(): 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# chemist_theme(): 'Might and Magic' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# town_theme(): 'Tavern Loop 1' by Alexander Nakarada
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# boss_battle_theme(): 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

# tavern_theme(): 'The Medieval Banquet' by Silverman Sound is under a Creative Commons license (CC BY 3.0)
# Music promoted by BreakingCopyright: http://bit.ly/Silvermansound_Medieval

# Pit theme 'Epic 39' by Jules Pitsker
# Creative Commons Attribution License 4.0 International (CC BY 4.0)

from player_module import cls, town_theme, gong, sleep, pause, teletype, \
    dungeon_command_choices, quit_game, game_start, os_check, initial_loading_screen, loading_screen, \
    random_floppy_rw_sound

os_check()
initial_loading_screen()

while True:

    player_1 = game_start()
    loading_screen()
    print(f"You enter the town of Fieldenberg.")
    sleep(1.5)
    player_1.in_town = True
    player_1.in_dungeon = False  # defined as False after portal use
    town_theme()

    # in_town loop:
    while player_1.in_town:
        player_1.hud()
        command = player_1.town_navigation()
        if command == "Restart":
            break
        if command == 'e':
            player_1.in_town = False
            player_1.town_portal_exists = False
            player_1.in_dungeon = True
            player_1.hud()
            player_1.dungeon_description()
            # random_floppy_loading_sound()
            # sleep(2)
            player_1.dungeon_theme()
            navigation_list = ['w', 'a', 's', 'd', 'ne', 'nw', 'se', 'sw', 'l', 'map', 'm', 'i', 'stay']

            # DUNGEON NAVIGATION LOOP:
            player_is_dead = False
            while player_1.in_dungeon:

                if player_is_dead:

                    if player_1.choose_to_play_again():
                        break

                if not player_1.in_dungeon:
                    break

                player_1.navigation_turn_initialize()
                # player_1.loot()  # for testing
                # player_1.asi()  # for testing

                if player_1.position == 0:  # 0 is the game/level start position
                    # player_1.hud()
                    cls()
                    teletype(player_1.dungeon.intro)
                    pause()

                    # set player position, which also removes intro condition
                    player_1.position = player_1.dungeon.grid[player_1.y][player_1.x]
                    player_1.dungeon_description()

                dungeon_command = dungeon_command_choices()

                if dungeon_command == 'p':
                    if player_1.use_scroll_of_town_portal():
                        town_theme()
                        player_1.in_town = True
                        player_1.in_dungeon = False
                        player_1.town_portal_exists = True
                        break
                    else:
                        continue  # if you have no scrolls, don't waste a turn

                elif dungeon_command == 'r':
                    if player_1.restart():
                        break
                    else:
                        player_1.dungeon_description()
                        continue

                elif dungeon_command == 'quit':
                    if not quit_game():
                        player_1.dungeon_description()
                        continue

                elif dungeon_command == "q":
                    player_1.hud()
                    monster = None  # quantum_effects needs monster parameter, but player is not in battle at this point
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
                    player_1.dungeon_navigation(dungeon_command)

                else:
                    print("Unknown command..")
                    sleep(.25)
                    player_1.dungeon_description()
                    continue  # continue means you do not waste a turn

                # ***** END OF NAVIGATION choice *************************************************************
                # NAVIGATION position and coordinate CALCULATIONS:
                player_1.navigation_position_coordinates()
                # ENCOUNTER LOGIC IS DETERMINED *BEFORE* event_logic(), BUT CAN BE RE-ASSIGNED BASED ON
                # RETURNED VALUES FROM event_logic()
                player_1.encounter_logic()
                # player_1.encounter = 96  should make no monsters at all
                # EVENT LOGIC IS DETERMINED BEFORE end_of_turn_calculation() AND player_1.check_dead(),
                # IN CASE PLAYER SUFFERS DAMAGE, ETC.
                event = player_1.event_logic()  # trigger any events corresponding to self.coordinates
                player_1.check_for_boss(event)  # check if event should trigger a boss encounter
                # META CALCULATION FUNCTION FOR REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                # this is also called after monster melee, necro, poison and quantum attack
                # as well as after turning/banishing, and player victory, etc.,
                player_1.end_of_turn_calculation()
                if player_1.check_dead():  # player can die of necrosis/poison/event damage after calculations
                    player_is_dead = True
                    continue
                # LASTLY, dungeon_description()
                player_1.dungeon_description()  # this seems to work best when put LAST

                if player_1.encounter < 11 or player_1.encounter > 20:  # < 11 = normal monster. > 20 = boss
                    player_1.in_proximity_to_monster = True
                    player_is_dead = False

                    # IN PROXIMITY TO MONSTER LOOP *contains battle loop within it*
                    while player_1.in_proximity_to_monster:

                        if player_is_dead:
                            break

                        if not player_1.in_proximity_to_monster:
                            break

                        # create a monster based on player_1.encounter: < 11 = normal monster. > 20 = boss
                        monster = player_1.meta_monster_generator()
                        player_1.monster_introduction(monster)

                        if player_1.monster_likes_you_or_steals_from_you(monster):
                            break

                        # PLAYER INITIATIVE, MONSTER INITIATIVE
                        human_goes_first = player_1.initiative(monster)

                        # IF MONSTER GOES FIRST:
                        if not human_goes_first:
                            player_1.hud()
                            monster.meta_monster_function(player_1)

                            if not player_1.check_dead():  # if player not dead

                                if monster.can_paralyze and monster.paralyze(player_1):
                                    if not player_1.check_dead():  # if player not dead
                                        print(f"You regain your faculties.")
                                        pause()

                                    else:
                                        print("You are dead and paralyzed!")
                                        player_is_dead = True
                                        break

                            else:  # you died
                                player_1.rndm_death_statement()
                                pause()
                                player_is_dead = True
                                break

                            # at this point, monster still has initiative
                            # therefore, if player has npc allies and monster has multi_attack or lesser_multi_attack,
                            # monster attacks npc allies:
                            player_1.monster_attacks_npc_meta(monster)

                        # OTHERWISE, PLAYER PROMPT and enter BATTLE LOOP
                        # ********************************* BATTLE LOOP ***********************************************
                        while True:
                            if not player_1.in_proximity_to_monster:
                                break
                            battle_choice = player_1.battle_menu_choices(monster)

                            # these choices count as turns, and are therefore followed by monster's turn:
                            battle_choice_turn_list = ['e', 'h', 'g', 'v', 'c', 'q']
                            if battle_choice in battle_choice_turn_list:

                                if battle_choice == "e":
                                    if player_1.evade(monster):
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
                                        # allies heal and no longer retreat:
                                        player_1.npc_calculation()

                                        if player_1.check_dead():  # you can die from poison or necrosis,
                                            player_is_dead = True  # right after victory, following calculations
                                            break

                                        if player_1.encounter > 20:  # if victory over a boss by quantum 'turning':
                                            gong()
                                            sleep(4)
                                            player_1.dungeon_theme()
                                            player_1.victory_over_boss_logic()

                                        player_1.level_up(monster.experience_award, monster.gold)
                                        player_1.dungeon_description()
                                        break

                                    # otherwise, calculate damage:
                                    # if total monster hit points is returned from quantum_effects(),
                                    # then monster will die instantly and player gets loot
                                    monster.reduce_health(damage_to_monster)
                                    if monster.check_dead():
                                        player_1.hud()
                                        player_1.victory_statements(monster)
                                        # CALCULATE REGENERATION/POTION OF STR/POISON/NECROSIS/PROT EFFECT:
                                        player_1.end_of_turn_calculation()
                                        # allies heal and no longer retreat:
                                        player_1.npc_calculation()
                                        pause()

                                        if player_1.check_dead():  # you can die from poison or necrosis,
                                            player_is_dead = True  # right after victory, following calculations
                                            player_1.in_proximity_to_monster = False
                                            break

                                        player_1.level_up(monster.experience_award, monster.gold)
                                        player_1.in_proximity_to_monster = False
                                        player_1.loot()
                                        player_1.victory_over_boss_logic()
                                        player_1.dungeon_description()
                                        break

                                # if monster is still alive after quantum attack, and player has allies,
                                # npc allies attack monster:
                                if player_1.npc_attack_logic(monster):  # if npc ally defeats monster
                                    player_1.end_of_turn_calculation()
                                    player_1.npc_calculation()  # allies heal and no longer retreat
                                    pause()

                                    if player_1.check_dead():  # player can die of poison/necrosis
                                        player_is_dead = True
                                        player_1.in_proximity_to_monster = False
                                        break

                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()
                                    player_1.dungeon_description()
                                    break

                                # ****MONSTER TURN AFTER YOU SWIG POTION, fail to evade, or cast quantum attack******
                                #
                                player_1.hud()
                                monster.meta_monster_function(player_1)
                                if not player_1.check_dead():  # if player not dead

                                    if monster.can_paralyze and monster.paralyze(player_1):

                                        if not player_1.check_dead():
                                            print(f"You regain your faculties.")
                                            pause()
                                            # if monster has multi_attack, then attack npc
                                            player_1.monster_attacks_npc_meta(monster)
                                            continue

                                        else:
                                            print("You are dead and paralyzed!")
                                            player_is_dead = True
                                            break

                                else:
                                    print(f"You died!")
                                    sleep(3)
                                    player_is_dead = True
                                    break

                                # if player has npc allies, monster attacks them
                                player_1.monster_attacks_npc_meta(monster)

                            # FIGHT: player chooses melee:
                            elif battle_choice == "f":
                                print(f"Fight.")
                                damage_to_monster = player_1.melee(monster.name, monster.armor_class)
                                monster.reduce_health(damage_to_monster)

                                # in the future, check_dead function can encompass the following if--else statements.
                                # just pass encounter parameter
                                if monster.check_dead():
                                    player_1.hud()
                                    player_1.victory_statements(monster)
                                    pause()
                                    # CALCULATE REGENERATION/POTION OF STRENGTH/POISON/NECROSIS/PROTECTION EFFECT:
                                    player_1.end_of_turn_calculation()
                                    # npc allies heal and no longer retreat:
                                    player_1.npc_calculation()

                                    if player_1.check_dead():
                                        player_is_dead = True
                                        player_1.in_proximity_to_monster = False
                                        break

                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()
                                    player_1.dungeon_description()
                                    break

                                # if monster still alive after player melee attack and player has allies
                                # npc allies attack monster
                                if player_1.npc_attack_logic(monster):  # if npc ally defeats monster
                                    player_1.end_of_turn_calculation()
                                    # allies heal and no longer retreat:
                                    player_1.npc_calculation()
                                    pause()

                                    if player_1.check_dead():
                                        player_is_dead = True
                                        player_1.in_proximity_to_monster = False
                                        break

                                    player_1.level_up(monster.experience_award, monster.gold)
                                    player_1.in_proximity_to_monster = False
                                    player_1.loot()
                                    player_1.victory_over_boss_logic()
                                    player_1.dungeon_description()  # beta works so far
                                    break

                                # monster turn if still alive after player melee attack:
                                else:
                                    monster.meta_monster_function(player_1)

                                    # I tried to offload this code, but the breaks and continues are pretty tangled
                                    if not player_1.check_dead():  # if player not dead

                                        if monster.can_paralyze and monster.paralyze(player_1):

                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You regain your faculties.")
                                                pause()
                                                # if monster has multi_attack, then attack npc
                                                player_1.monster_attacks_npc_meta(monster)
                                                continue

                                            else:
                                                print("You are dead and paralyzed!")
                                                player_is_dead = True
                                                break

                                    else:  # you died
                                        player_1.rndm_death_statement()
                                        sleep(3)
                                        player_is_dead = True
                                        break

                                    player_1.hud()

                                # if player has npc allies, monster attacks them:
                                player_1.monster_attacks_npc_meta(monster)

                            else:  # invalid inputs. this should be unreachable, since creating battle_menu_choices()
                                print(f"Invalid input.")
                                sleep(1)
                                player_1.hud()
                                continue
                            #
                else:  # encounter condition False; no monster, continue
                    continue
        else:  # player is in town and does NOT (E)nter dungeon; continue
            continue

    """player_initiative = player_1.initiative()
                            monster_initiative = monster.initiative()
                            print(f"Your initiative: {player_initiative}\nMonster initiative: {monster_initiative}")
                            pause()"""
    """                        if encounter < 11:  # regular monster
                                monster = player_1.regular_monster_generator()
                                # monster = Shadow()  # HobgoblinCaptain()  # testing
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
                                player_1.hud()"""
    """                if event == "Legendary Monster":
                        player_1.encounter = 95
                    if event == "Elite Monster":
                        player_1.encounter = 96
                    if event == "Undead Prophet":
                        player_1.encounter = 97
                    elif event == "King Boss":
                        player_1.encounter = 98
                    elif event == "Exit Boss":
                        player_1.encounter = 99
                    elif event == "Wicked Queen":
                        player_1.encounter = 100"""
    """#player_1.hud()
                                #monster.monster_data()
                                #battle_choice = input("(F)ight, (H)ealing potion, (C)larifying elixir,\n"
                                #                      "(G)iant Strength potion, (V)ial of Antidote,\n(Q)uantum Effects 
                                or "
                                #                      "(E)vade\nF/H/C/G/V/Q/E --> ").lower()
    """
    """                        if player_1.encounter < 21:  # if not a boss, monster may like you or steal from you
                                if player_1.monster_likes_you(monster):
                                    player_1.in_proximity_to_monster = False
                                    # player_1.event_logic()  # this will trigger an event without using (L)ook
                                    player_1.dungeon_description()
                                    break
                                if player_1.quick_move(monster):
                                    player_1.in_proximity_to_monster = False
                                    # player_1.event_logic()  # this will trigger an event without using (L)ook
                                    player_1.dungeon_description()
                                    break  # if monster steals something he gets away clean, if not, battle"""
    """cls()
                        gong()
                        print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                        sleep(4)
                        player_1.in_proximity_to_monster = False
                        player_1.in_dungeon = False
                        player_1.in_town = False
                        while True:
                            try_again = input("Do you wish to play again (y/n)? ").lower()
                            if try_again == "y":
                                sleep(1)
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
                                sleep(.5)
                                continue"""
    """    if new_game_or_load == 'l':
            player_name = input("Enter name of saved character: ")
            load_a_character = player_name + ".sav"
            if os.path.isfile(load_a_character):
                print(f"{player_name} found.")
                with open(load_a_character, 'rb') as saved_player:
                    player_1 = pickle.load(saved_player)
                    sleep(1)
                    print(f"{player_name} read.")
                    sleep(1)
                    dungeon = dungeon_dict[player_1.dungeon_key]  # remove after testing
                    print(dungeon.name)  # remove after testing
                    print(player_1.coordinates)  # remove after testing
                    player_1.loaded_game = True
                    sleep(1)
            else:
                print(f"Could not find {player_name} ")
                sleep(1.5)
                continue"""
    """else:
                                        print(f"You have no Quantum unit energy!")
                                        pause()
                                        continue  # if you have no QU, don't waste a turn!"""