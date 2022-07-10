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
the same result when called multiple times. Python is a little less strict about this than other languages and it's
natural to use certain in-place functions like sort and random.shuffle. These are exceptions that prove the rule
 (and if you know a bit about sorting and shuffling, they make sense in these contexts due to the algorithms used
 and the need for efficiency).

An in-place algorithm is impure and non-idempotent, but if the state that it modifies is limited to its parameter(s)
and its documentation and return value (usually None) support this, the behavior is predictable and comprehensible."""
# MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]
from player_class_module import *
from monster_class_module import *
import random
import os

while True:
    player_name = input("Enter Player name: ")
    accept_stats = ""
    while accept_stats != "y":
        os.system('cls')
        # 0name,1level,2experience,3gold,4weapon+,5armor,6shield,7armor_class,8strength,
        # 9dexterity,10constitution,11intelligence,12wisdom,13charisma,14hit_points15is_paralyzed
        player_stats = [player_name, 1, 0, 0, 0, 0, 0, 10, *random.sample(range(3, 19), 6),
                        0, 0, False]  # zero is placeholder for hit points is_paralyzed = False
        # print(player_stats)
        # hit_points at level one = 10 + self.constitution_modifier (index 10 is constitution)
        hit_points = 10 + round((player_stats[10] - 10) / 2)
        player_stats[14] = hit_points  # make player_stats index 14 equal to 10 + con modifier
        player_stats[15] = hit_points
        print(player_stats)
        player_1 = Player(*player_stats)  # sending stats to Player Class and create player_1 as Player class object
        print(f"Name: {player_1.name}")
        print(f"Level: {player_1.level}")
        print(f"Experience: {player_1.experience}")
        print(f"Gold: {player_1.gold}")
        print(f"Weapon + {player_1.weapon}")
        print(f"Armor Class {player_1.armor_class}")
        print(f"Shield + {player_1.shield}")
        print(f"Constitution {player_1.constitution}")
        print(f"Intelligence: {player_1.intelligence}")
        print(f"Wisdom: {player_1.wisdom}")
        print(f"Strength: {player_1.strength}")
        print(f"Dexterity: {player_1.dexterity}")
        print(f"Charisma: {player_1.charisma}")
        print(f"Hitpoints: {player_1.hit_points}")
        accept_stats = input("Accept stats y/n ?")
    # a while loop's 'else' part runs if no break occurs and the condition is false
    if accept_stats == "y":
        in_town = True
        in_dungeon = False
        while in_town:
            town_functions = input(
                "You are in town. (Q)uit game, (R)estart the game, (B)lacksmith, (C)hemist or (E)nter dungeon")
            if town_functions == 'r':
                print("Restart")
                in_town = False
                break
            if town_functions == 'q':
                print("Exiting..")
                exit()
            if town_functions == 'b':
                print("You visit the blacksmith")

            if town_functions == 'c':
                print("You visit the quantum chemist")
            if town_functions == 'e':
                in_town = False
                in_dungeon = True
                print("You enter the dungeon")
                while in_dungeon:
                    encounter = dice_roll(1, 20)
                    dungeon_command = input("Town (P)ortal, (H)ealing potion or WASD to navigate.")
                    if dungeon_command == 'p':
                        in_town = True
                        in_dungeon = False
                        break
                    if dungeon_command == 'h':
                        player_1.hit_points += 10
                    if dungeon_command == 'w' or 'a' or 's' or 'd':
                        if dungeon_command == 'w':
                            print("You go north")
                        if dungeon_command == 'a':
                            print("You go west")
                        if dungeon_command == 's':
                            print("You go south")
                        if dungeon_command == 'd':
                            print("You go east")
                        if dungeon_command not in ('w', 'a', 's', 'd', 'p', 'h'):
                            print("Unknown command")
                            continue
                    if encounter > 12:
                        print("This should create monster now..")
                        dungeon_level = 1

                        MONSTERS = [Ghoul]
                        LEGENDARY_MONSTERS = [Dragon]
                        # def create_monster():
                        #    return random.choice(MONSTERS)
                        # in proximity loop contains battle loop within it
                        in_proximity_to_monster = True

                        # ************ OFFLOAD AS MUCH OF THIS LOGIC AS POSSIBLE TO THE OTHER MODULES!!! **************
                        while in_proximity_to_monster:
                            if player_1.check_dead():
                                print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                                in_proximity_to_monster = False
                                in_dungeon = False
                                in_town = False
                                while True:
                                    try_again = input("Do you wish to play again (y/n)?").lower()

                                    if try_again == "y":
                                        break
                                    if try_again == "n":
                                        exit()
                                    if try_again not in ("y", "n"):
                                        print("Please enter 'y' or 'n'")
                                        continue
                            if not in_proximity_to_monster:
                                break
                            monster_cls = random.choice(MONSTERS)
                            monster_level = dungeon_level + random.randint(0, 2)
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
                            monster = monster_cls(*monster_stats)  # send stats to class and create 'monster' as object
                            print(f"You have encountered a level {monster_level} {monster.name}.")
                            if dice_roll(1, 20) == 20:  # (player_1.dexterity + player_1.dexterity_modifier):
                                attack_or_steal = dice_roll(1, 20)
                                if attack_or_steal > 16:  # (player_1.dexterity + player_1.dexterity_modifier):
                                    print(f"You are caught off guard! It attacks!")
                                    damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity,
                                                                     monster.strength,
                                                                     monster.weapon,
                                                                     player_1.level, player_1.hit_points,
                                                                     player_1.dexterity,
                                                                     player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                    if player_1.check_dead():  # if player  dead
                                        print(f"You were caught off guard! Testing Sauengard statement")
                                        #in_proximity_to_monster = False
                                        #in_dungeon = False
                                        #in_town = False
                                        break
                                else:
                                    print(f"The {monster.name} makes a quick move. He steals an item from your pack.")
                                    in_proximity_to_monster = False
                                    break
                            # battle loop
                            while True:
                                choice = input("Fight Cast or Evade?\n F/E").lower()
                                if choice == "e":
                                    evade_success = player_1.evade(monster.name, monster.dexterity)
                                    if evade_success:
                                        in_proximity_to_monster = False
                                        # in_town = True
                                        break
                                    else:
                                        print(f"You are rooted to the spot! You must stand your ground!")
                                elif choice == "c":
                                    print(f"Cast")
                                    continue
                                elif choice == "f":
                                    print(f"Fight.")
                                else:
                                    continue  # if player enters anything other than e or f
                                # player's turn:
                                damage_to_monster = player_1.swing(player_1.name, player_1.level, player_1.dexterity,
                                                                   player_1.strength, player_1.weapon, monster.level,
                                                                   monster.name, monster.dexterity, monster.armor_class)
                                monster.reduce_health(damage_to_monster)  # take returned damage to monster
                                if not monster.check_dead():  # if monster is not dead
                                    print(f"{monster.name} is not dead.")
                                    print(f"It has {monster.hit_points} hit points.")

                                else:
                                    print(f"It has {monster.hit_points} hit points.")
                                    print(f"It died..")
                                    player_1.level_up(monster.experience_award, monster.gold)
                                    in_proximity_to_monster = False
                                    break
                                if not in_proximity_to_monster:
                                    break

                                print(f"You currently have {player_1.hit_points} hit points, "
                                      f"{player_1.gold} gold, and {player_1.experience} experience. "
                                      f"You are level {player_1.level}")

                                # monster turn:
                                if not monster.check_dead():  # if monster is not dead
                                    damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity,
                                                                     monster.strength,
                                                                     monster.weapon,
                                                                     player_1.level, player_1.hit_points,
                                                                     player_1.dexterity,
                                                                     player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                    if not player_1.check_dead():  # if player not dead

                                        if dice_roll(1, 20) > 17 and monster.undead and monster.can_paralyze:
                                            print(f"It lurches forward, grabbing your arm!")
                                            player_1.is_paralyzed = monster.paralyze(monster.name, monster.level,
                                                                                     monster.wisdom,
                                                                                     monster.wisdom_modifier,
                                                                                     monster.dexterity,
                                                                                     monster.strength,
                                                                                     monster.weapon,
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

                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You are alive")
                                            else:
                                                print("You are dead and paralyzed!")
                                                #in_proximity_to_monster = False
                                                #in_dungeon = False
                                                #in_town = False
                                                break
                                        '''if monster.can_drain:
                                            level_drain = monster.drain(monster.wisdom, monster.wisdom_modifier,
                                                                        player_1.level, player_1.wisdom,
                                                                        player_1.wisdom_modifier)
                                            if level_drain:  # try to offload this logic
                                                print("It drains a level!\nYou go down a level!!")
                                                player_1.level -= 1
                                                player_1.experience *= .50
                                                if player_1.level < 1:
                                                    print(f"You have died from drainage!!!!!")
                                                    in_proximity_to_monster = False
                                                    in_dungeon = False
                                                    in_town = False
                                                    break

                                            else:
                                                print(f"You have {player_1.hit_points} out of a maximum "
                                                      f"{player_1.maximum_hit_points} hit points, and"
                                                      f" {player_1.experience} experience. "
                                                      f"You are level {player_1.level}")
                                                continue'''
                                    else:
                                        print(f"You have died.")
                                        #in_proximity_to_monster = False
                                        #in_dungeon = False
                                        #in_town = False
                                        break
                                    print(
                                        f"You have {player_1.hit_points} hit points of a maximum "
                                        f"{player_1.maximum_hit_points}, and "
                                        f"{player_1.experience} experience. You are level {player_1.level}")
                                else:
                                    break
