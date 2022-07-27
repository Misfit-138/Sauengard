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

import pickle
from player_class_test import *
#from player_class_module import *
from monster_module import *
#from monster_class_module import *
from typing_module import *
import random
import os
import winsound


'''def hud():
    os.system('cls')
    print(f"                                                                     Name: {player_1.name}")
    print(f"                                                                     Level: {player_1.level}")
    print(f"                                                                     Experience: {player_1.experience}")
    print(f"                                                                     Gold: {player_1.gold}")
    print(f"                                                                     Weapon + {player_1.weapon_bonus}")
    # print(f"                                                                     Equipped weapon: {player_1.weapon_name}")
    print(f"                                                                     Armor Class {player_1.armor_class}")
    print(f"                                                                     Shield + {player_1.shield}")
    print(f"                                                                     Strength: {player_1.strength}")
    print(f"                                                                     Dexterity: {player_1.dexterity}")
    print(f"                                                                     Constitution {player_1.constitution}")
    print(f"                                                                     Intelligence: {player_1.intelligence}")
    print(f"                                                                     Wisdom: {player_1.wisdom}")
    print(f"                                                                     Charisma: {player_1.charisma}")
    print(f"                                                                     Hit points: {player_1.hit_points}/"
          f"{player_1.maximum_hit_points}")
    if player_1.boots == 0:
        print(f"                                                                     Boots: Leather")
    else:
        print(
            f"                                                                     Boots: Elven Boots + {player_1.boots}")
    if player_1.cloak == 0:
        print(f"                                                                     Cloak: none")
    else:
        print(
            f"                                                                     Cloak: Elven Cloak + {player_1.boots}")'''

# "E:\C64\Telengard\telengard.wav"
# winsound.PlaySound('e:\\C64\\Telengard\\telengard.wav', winsound.SND_ASYNC)
# winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\sound.wav',winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
# winsound.PlaySound('C:\\Users\\Pitsk\\Music\\creepy_dungeon_theme.wav', winsound.SND_ASYNC)
winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\originalsound.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
os.system('cls')
typing("Welcome to Sauengard.")
print("")
# typing("Enjoy the music.")
print("")
os.system('pause')
winsound.PlaySound(None, winsound.SND_ASYNC)
os.system('cls')

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
            # 0name,1level,2experience,3gold,4weapon+,5armor,6shield,7armor_class,8strength,
            # 9dexterity,10constitution,11intelligence,12wisdom,13charisma,14hit_points15is_paralyzed16boots,17cloak
            # 18weapon_name
            # player_stats = [player_name, 1, 0, 0, 0, 0, 0, 10, *random.sample(range(3, 19), 6),
            #                0, 0, False, 0, 0]  # zero is placeholder for hit points is_paralyzed = False
            # player_stats = [player_name, 1, 0, 0, 0, 0, 0, 10, 15, 14, 13, 12, 8, 10, 0, 0, False, 0, 0, "sword"]

            # hit_points at level one = 10 + self.constitution_modifier (index 10 is constitution)
            # hit_points = 10 + round((player_stats[10] - 10) / 2)
            # player_stats[14] = hit_points  # make player_stats index 14 equal to 10 + con modifier
            # player_stats[15] = hit_points
            # print(player_stats)
            # player_1 = Player(player_name)
            # player_1 = Player(*player_stats)  # sending stats to Player Class and create player_1 as Player class object
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
            # os.system('pause')
            accept_stats = input("Accept stats y/n ? ").lower()
        # a while loop's 'else' part runs if no break occurs and the condition is false
        if accept_stats == "y":
            player_1.hud()

    print(f"You enter the town of Fieldenberg.")
    # print(f"Your pack contains {player_1.pack}")
    #player_1.pack.append(healing_potion)
    time.sleep(1.5)
    player_1.hud()
    in_town = True
    in_dungeon = False
    while in_town:
        town_functions = input(
            "You are in town. (S)ave, (Q)uit game, (R)estart the game, (I)nventory, (B)lacksmith, (C)hemist or ("
            "E)nter dungeon "
            "--> ").lower()
        if town_functions == 'r':
            print("Restart")
            time.sleep(2)
            os.system('cls')
            in_town = False
            break
        if town_functions == 'q':
            print("Exiting..")
            exit()
        if town_functions == 's':
            print(f"Saving {player_1.name}...")
            character_filename = player_1.name + ".sav"

            with open(character_filename, 'wb') as player_save:
                pickle.dump(player_1, player_save)
                print(f"{player_1.name} saved.")
                time.sleep(2)
        if town_functions == 'i':
            player_1.hud()
            player_1.inventory()
            os.system('pause')
            player_1.hud()
        if town_functions == 'b':
            player_1.hud()
            print("You visit the blacksmith")
            at_blacksmith = True
            #while at_blacksmith:
            #    buy_or_exit = input("(B)uy items or (E)xit --> ").lower()
            #    if buy_or_exit == 'e':
            #        break
            #    if buy_or_exit == 'b':
            player_1.blacksmith_sale()
            player_1.hud()
        if town_functions == 'c':
            player_1.hud()
            print("You visit the quantum chemist. He heals you to full strength.")
            time.sleep(1.5)
            player_1.hit_points = player_1.maximum_hit_points
            player_1.hud()
        if town_functions == 'e':
            in_town = False
            in_dungeon = True
            player_1.hud()
            print("You enter the dungeon..")
            time.sleep(1)
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\creepy_dungeon_theme.wav',
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
            while in_dungeon:
                encounter = dice_roll(1, 20)
                dungeon_command = input(
                    "Town (P)ortal, (H)ealing potion, (I)nventory or WASD to navigate. --> ").lower()
                if dungeon_command == 'p':
                    in_town = True
                    in_dungeon = False
                    player_1.hud()
                    print(f"The portal appears before you; a seemingly impossible gateway between distant places..")
                    time.sleep(2)
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    break
                if dungeon_command == 'h':
                    player_1.hud()
                    print("You chug a healing potion.")
                    player_1.hit_points += 10
                    print(f"You have {player_1.hit_points} hit points.")
                    time.sleep(1)
                    player_1.hud()
                if dungeon_command == 'i':
                    player_1.inventory()
                if dungeon_command == 'w' or 'a' or 's' or 'd':
                    if dungeon_command == 'w':
                        player_1.hud()
                        print("You go north")
                        player_1.regenerate()
                    if dungeon_command == 'a':
                        player_1.hud()
                        print("You go west")
                        player_1.regenerate()
                    if dungeon_command == 's':
                        player_1.hud()
                        print("You go south")
                        player_1.regenerate()
                    if dungeon_command == 'd':
                        player_1.hud()
                        print("You go east")
                        player_1.regenerate()
                if dungeon_command not in ('w', 'a', 's', 'd', 'p', 'h', 'i'):
                    player_1.hud()
                    print("Unknown command")
                    continue
                if encounter > 12:
                    player_1.hud()
                    print("This should create monster now..")
                    dungeon_level = 1
                    # monster dictionary. keys correspond to difficulty
                    monster_dict = {
                        1: [Kobold, Goblin, WingedKobold],
                        2: [Shadow, Skeleton, Drow, Orc, Ghoul]
                    }
                    loot_dict = {

                    }
                    # MONSTERS = [Ghoul]

                    # def create_monster():
                    #    return random.choice(MONSTERS)
                    # in proximity loop contains battle loop within it
                    in_proximity_to_monster = True

                    # ************ OFFLOAD AS MUCH OF THIS LOGIC AS POSSIBLE TO THE OTHER MODULES!!! **************
                    while in_proximity_to_monster:
                        if player_1.check_dead():
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
                                    break
                                if try_again == "n":
                                    exit()
                                if try_again not in ("y", "n"):
                                    print("Please enter y or n ")
                                    time.sleep(.5)
                                    continue
                        if not in_proximity_to_monster:
                            break

                        monster_key = random.randint(1, (player_1.level + 1))
                        monster_cls = random.choice(monster_dict[monster_key])
                        # monster_level = dungeon_level  # + random.randint(0, 2)
                        monster_level = player_1.level
                        # monster_cls = "MonsterLevel", player_1.level
                        # monster_stats list index:
                        # 0level, 1experience_award, 2gold, 3weapon_bonus, 4armor,5shield,6armor_class,7strength,
                        # 8dexterity,9constitution,10intelligence,11wisdom,12charisma,13hit_points,14can_paralyze,
                        # 15can_drain, 16undead,17human_player_level, 18difficulty_class, 19proficiency,
                        # 20damage, 21challenge_rating
                        monster_stats = [monster_level, 0, 0, 0, 0, 0, 0, *random.sample(range(3, 18), 6), 0, False,
                                         False,
                                         False, player_1.level, 0, 0, 0, 0]
                        monster_hit_points = (monster_stats[9])  # equal to constitution (index 9) for now..
                        monster_stats[13] = round(monster_hit_points)  # make index 13(hp) = constitution for now
                        monster = monster_cls()
                        #monster = monster_cls(*monster_stats)  # send stats to class and create 'monster' as object
                        player_1.hud()
                        print(f"{monster.introduction}")
                        # print(f"You have encountered a level {monster.level} {monster.name}.")
                        print(f"{monster.constitution_modifier} {monster.hit_points}")
                        # time.sleep(2.5)
                        os.system('pause')
                        # if dice_roll(1, 20) > 0:  # == 20 and player_1.charisma > 15:
                        if player_1.monster_likes_you(monster.name, monster.intelligence):
                            in_proximity_to_monster = False
                            break
                        if dice_roll(1, 20) == 20:  # (player_1.dexterity + player_1.dexterity_modifier):
                            attack_or_steal = dice_roll(1, 20)
                            if attack_or_steal > 16:  # (player_1.dexterity + player_1.dexterity_modifier):
                                player_1.hud()
                                print(f"The {monster.name} attacks with blinding speed! You are caught off guard!")
                                damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity,
                                                                 monster.strength,
                                                                 monster.weapon_bonus,
                                                                 player_1.level, player_1.hit_points,
                                                                 player_1.dexterity,
                                                                 player_1.armor_class)
                                player_1.reduce_health(damage_to_player)
                                if player_1.check_dead():  # if player  dead
                                    player_1.hud()
                                    print(f"You were caught off guard!")
                                    time.sleep(1.5)
                                    # in_proximity_to_monster = False
                                    # in_dungeon = False
                                    # in_town = False
                                    continue
                            else:
                                player_1.hud()
                                print(f"The {monster.name} makes a quick move...")
                                time.sleep(1.5)
                                player_1.quick_move()
                                time.sleep(1.5)
                                in_proximity_to_monster = False
                                break
                        # battle loop
                        while True:
                            player_1.hud()
                            choice = input("Fight Cast or Evade?\n F/C/E --> ").lower()
                            if choice == "e":
                                evade_success = player_1.evade(monster.name, monster.dexterity)
                                if evade_success:
                                    in_proximity_to_monster = False
                                    # in_town = True
                                    break
                                else:
                                    player_1.hud()
                                    print(f"The {monster.name} swiftly blocks your escape.")
                                    time.sleep(.5)
                                    print(f"You are rooted to the spot. You must stand your ground!")
                                    time.sleep(.5)
                                    print(f"You raise your {player_1.wielded_weapon}..")
                                    time.sleep(1)
                            elif choice == "c":
                                player_1.hud()
                                print(f"Cast")
                                continue
                            elif choice == "f":
                                player_1.hud()
                                print(f"Fight.")
                            else:
                                player_1.hud()
                                print(f"The {monster.name} is not amused.")
                                time.sleep(1)
                                player_1.hud()
                                continue  # if player enters anything other than e or f
                            # player's turn:
                            damage_to_monster = player_1.swing(player_1.name, player_1.level, player_1.dexterity,
                                                               player_1.strength, player_1.weapon_bonus, monster.level,
                                                               monster.name, monster.dexterity, monster.armor_class)
                            monster.reduce_health(damage_to_monster)  # take returned damage to monster
                            if not monster.check_dead():  # if monster is not dead
                                # print(f"{monster.name} is not dead.")
                                print(f"It has {monster.hit_points} hit points.")
                                time.sleep(2)
                            else:
                                player_1.hud()
                                # print(f"It has {monster.hit_points} hit points.")
                                print(f"It died..")
                                time.sleep(2)
                                player_1.level_up(monster.experience_award, monster.gold)
                                in_proximity_to_monster = False

                                break
                            if not in_proximity_to_monster:
                                break

                            '''print(f"You currently have {player_1.hit_points} hit points, "
                                  f"{player_1.gold} gold, and {player_1.experience} experience. "
                                  f"You are level {player_1.level}")'''

                            # monster turn:
                            if not monster.check_dead():  # if monster is not dead
                                damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity,
                                                                 monster.strength,
                                                                 monster.weapon_bonus,
                                                                 player_1.level, player_1.hit_points,
                                                                 player_1.dexterity,
                                                                 player_1.armor_class)
                                player_1.reduce_health(damage_to_player)
                                if not player_1.check_dead():  # if player not dead

                                    if dice_roll(1, 20) > 17 and monster.undead and monster.can_paralyze:
                                        print(f"It lurches forward, grabbing your arm!")
                                        time.sleep(1)
                                        player_1.is_paralyzed = monster.paralyze(monster.name, monster.level,
                                                                                 monster.wisdom,
                                                                                 monster.wisdom_modifier,
                                                                                 monster.dexterity,
                                                                                 monster.strength,
                                                                                 monster.weapon_bonus,
                                                                                 player_1.level,
                                                                                 player_1.hit_points,
                                                                                 player_1.dexterity,
                                                                                 player_1.armor_class,
                                                                                 player_1.wisdom,
                                                                                 player_1.wisdom_modifier)
                                        if player_1.is_paralyzed:
                                            paralyze_damage = dice_roll(monster.number_of_hd, monster.hit_dice)
                                            player_1.reduce_health(paralyze_damage)
                                            print(f"You suffer {paralyze_damage} hit points!!")
                                            time.sleep(1)
                                        if not player_1.check_dead():  # if player not dead
                                            print(f"You regain your faculties.")
                                            time.sleep(2)
                                            continue
                                        else:
                                            print("You are dead and paralyzed!")
                                            # in_proximity_to_monster = False
                                            # in_dungeon = False
                                            # in_town = False
                                            break

                                else:
                                    print(f"You died!")
                                    time.sleep(3)
                                    # in_proximity_to_monster = False
                                    # in_dungeon = False
                                    # in_town = False
                                    break
                                player_1.hud()

                            else:
                                break
