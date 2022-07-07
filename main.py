"""The global keyword is the tool that Python provides for you to opt out of encapsulation
and break the natural scope of a variable. Encapsulation means that each of your components is a logical,
self-contained unit that should work as a black box and performs one thing
(note: this one thing is conceptual and may consist of many, possibly non-trivial, sub-steps)
without mutating global state or producing side effects.
The reason is modularity: if something goes wrong in a program (and it will), having strong encapsulation makes it very
 easy to determine where the failing component is.

Encapsulsation makes code easier to refactor, maintain and expand upon.
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

from player_class_module import *
from monster_class_module import *
import random
import os
while True:
    player_name = input("Enter Player name: ")
    accept_stats = ""
    while accept_stats != "y":
        os.system('cls')
        # 0name,1level,2experience,3gold,4weapon+,5armor,6shield,7armor_class,8strength,9dexterity,10constitution,11intelligence,12wisdom,13charisma,14hit_points15is_paralyzed
        player_stats = [player_name, 1, 0, 0, 0, 0, 0, 10, *random.sample(range(3, 19), 6),
                        0, False]  # zero is placeholder for hit points is_paralyzed = False
        # print(player_stats)
        hit_points = 10 + round((player_stats[
                                     10] - 10) / 2)  # hit_points at level one = 10 + self.constitution_modifier (index 10 is constitution)
        player_stats[14] = hit_points  # make player_stats index 14 equal to 10 + con modifier

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
    if accept_stats == "y":
        in_town = True
        in_dungeon = False
        while in_town:
            town_functions = input("What do you wish to do or E to enter dungeon")
            if town_functions not in 'e':
                if town_functions == 'b':
                    print(f"You are in town, buying stuff")
                else:
                    print("You are in town doing stuff")
            else:
                in_town = False
                in_dungeon = True
                print("You enter the dungeon")
                while in_dungeon:
                    dungeon_command = input("Town (P)ortal or WASD or (F)ight")
                    if dungeon_command not in 'p':
                        if dungeon_command == 'w' or 'a' or 's' or 'd':
                            print(f"You are navigating")
                        elif dungeon_command == 'f':
                            print("This should start the create monster function now..")
                            dungeon_level = 1
                    else:
                        in_dungeon = False
                        in_town = True
                        break




                        # MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
                        #            "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]
                        MONSTERS = [Dragon]

                        # def create_monster():
                        #    return random.choice(MONSTERS)
                        # in proximity loop contains battle loop within it
                        in_proximity_to_monster = True

                        # def fight_or_evade(dexterity):
                        #    pass

                        # ************ OFFLOAD AS MUCH OF THIS LOGIC AS POSSIBLE TO THE OTHER MODULES!!! **************************
                        while in_proximity_to_monster:
                            if player_1.check_dead():
                                print(f"Another adventurer has fallen prey to the Sauengard Dungeon!")
                                break
                            if not in_proximity_to_monster:
                                break
                            monster_cls = random.choice(MONSTERS)
                            monster_level = dungeon_level + random.randint(0, 2)
                            # monster_stats list index:
                            # 0level, 1experience_award, 2gold, 3weapon_bonus, 4armor,5shield,6armor_class,7strength,8dexterity,9constitution,10intelligence,11wisdom,12charisma,13hit_points,14can_paralyze, 15can_drain, 16undead,17human_player_level
                            monster_stats = [monster_level, 0, 0, 0, 0, 0, 0, *random.sample(range(3, 18), 6), 0, False, False,
                                             False, player_1.level]
                            monster_hit_points = (monster_stats[9])  # equal to constitution (index 9) for now..
                            monster_stats[13] = round(monster_hit_points)  # make index 13 = constitution for now
                            monster = monster_cls(*monster_stats)  # send stats to monster class and create 'monster' as object
                            print(f"You have encountered a level {monster_level} {monster.name}.")
                            if dice_roll(1, 20) == 20:  # (player_1.dexterity + player_1.dexterity_modifier):
                                attack_or_steal = dice_roll(1, 20)
                                if attack_or_steal > 16:  # (player_1.dexterity + player_1.dexterity_modifier):
                                    print(f"You are caught off guard! It attacks!")
                                    damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity, monster.strength,
                                                                     monster.weapon,
                                                                     player_1.level, player_1.hit_points, player_1.dexterity,
                                                                     player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                    if not player_1.check_dead():  # if player not dead
                                        print(f"You are alive")
                                    else:
                                        continue
                                else:
                                    print(f"The {monster.name} makes a quick move. He steals an item from your pack.")
                                    continue
                                    # break
                            # battle loop
                            while True:
                                choice = input("Fight or Evade?\n F/E").lower()
                                if choice == "e":
                                    evade_success = player_1.evade(monster.name, monster.dexterity)
                                    if evade_success:
                                        in_proximity_to_monster = False
                                        in_town = True
                                        break
                                    else:
                                        print(f"You are rooted to the spot! You must stand your ground!")
                                elif choice == "f":
                                    print(f"Fight.")
                                else:
                                    continue  # if player enters anything other than e or f

                                    # place logic here: if dice roll and dexterity > monster then player's turn, else monster gets the jump
                                    # if dice_roll(1, 20) + player_1.dexterity_modifier > monster.dexterity:
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
                                    in_proximity_to_monster = False  # change this back after testing
                                    in_town = True
                                    break
                                if not in_proximity_to_monster:
                                    in_town = True
                                    break

                                print(
                                    f"You currently have {player_1.hit_points} hitpoints, {player_1.gold} gold, and {player_1.experience} experience. You are level {player_1.level}")

                                # monster turn:
                                if not monster.check_dead():  # if monster is not dead
                                    damage_to_player = monster.swing(monster.name, monster.level, monster.dexterity, monster.strength,
                                                                     monster.weapon,
                                                                     player_1.level, player_1.hit_points, player_1.dexterity,
                                                                     player_1.armor_class)
                                    player_1.reduce_health(damage_to_player)
                                    if not player_1.check_dead():  # if player not dead
                                        print(f"You are alive")
                                        if monster.undead and monster.can_paralyze:
                                            player_1.is_paralyzed = monster.paralyze(monster.name, monster.level, monster.dexterity,
                                                                                     monster.strength,
                                                                                     monster.weapon,
                                                                                     player_1.level, player_1.hit_points, player_1.dexterity,
                                                                                     player_1.armor_class, player_1.wisdom,
                                                                                     player_1.wisdom_modifier)
                                            player_1.reduce_health(damage_to_player)
                                            if not player_1.check_dead():  # if player not dead
                                                print(f"You are alive")

                                        if monster.undead and monster.can_drain:
                                            level_drain = monster.drain(player_1.level, player_1.wisdom,
                                                                        player_1.wisdom_modifier)
                                            if level_drain:  # if level_drain True
                                                print("It drains a level!\nYou go down a level!!")
                                                player_1.level -= 1
                                                if player_1.level <= 0:
                                                    print(f"You have died from drainage!!!!!")
                                                    in_proximity_to_monster = False
                                                    break

                                            else:
                                                print(
                                                    f"You have {player_1.hit_points} hitpoints, and {player_1.experience} experience. You are level {player_1.level}")
                                                continue
                                    else:
                                        print(f"You have died.")
                                        break
                                    print(
                                        f"You have {player_1.hit_points} hitpoints, and {player_1.experience} experience. You are level {player_1.level}")
                                else:
                                    break
