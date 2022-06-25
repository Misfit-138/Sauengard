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
from  dragon_module import *
from player_class_module import *
from monster_class_module import *
import random
import os

# player_stats = [18,17,16,15,14]
player_name = input("Enter Player name: ")
# player_stats = (player_name,18,18,18,18,18)
# the asterisk * before the random function passes the parameters without
# the brackets

accept_stats = ""
while accept_stats != "y":
    os.system('cls')
    # 0name,1level,2experience,3gold,4sword,5armor,6shield,7constitution,8intelligence,9wisdom,10strength,11dexterity,12charisma
    # player_stats = (player_name,1,0,0,0,0,*random.sample(range(3, 19), 5))
    player_stats = [player_name, 1, 0, 0, 0, 0, 0, *random.sample(range(3, 19), 6),
                    0]  # zero is placeholder for hit points- index 13
    # print(player_stats)
    con = round(player_stats[7] * 1.2)  # add 20% to constitution (index 7)
    player_stats[13] = con  # make index 13 (hitpoints) 20% more than constitution
    print(player_stats)
    player_1 = Player(*player_stats)  # sending stats to Player Class
    print(f"Name: {player_1.name}")
    print(f"Level: {player_1.level}")
    print(f"Experience: {player_1.experience}")
    print(f"Gold: {player_1.gold}")
    print(f"Sword + {player_1.sword}")
    print(f"Armor + {player_1.armor_class}")
    print(f"Shield + {player_1.shield}")
    print(f"Constitution {player_1.constitution}")
    print(f"Intelligence: {player_1.intelligence}")
    print(f"Wisdom: {player_1.wisdom}")
    print(f"Strength: {player_1.strength}")
    print(f"Dexterity: {player_1.dexterity}")
    print(f"Charisma: {player_1.charisma}")
    print(f"Hitpoints: {player_1.hit_points}")
    accept_stats = input("Accept stats y/n ?")

dungeon_level = 1

MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
            "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]


def random_monster():
    return random.choice(MONSTERS)


# monsters have Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma

#monster_cls = random_monster()
monster_cls = Dragon
monster_level = dungeon_level + random.randint(0, 2)
#  level0, experience_award1, gold2, sword3, armor4, shield5, constitution6, strength7, dexterity8, hitpoints9
monster_stats = [monster_level, 0, random.randint(0, 300), 0, 0, 0, *random.sample(range(3, 18), 3), 0, player_1.level]  # added a zeros at end for hitpoints
# #monster_stats = [monster_cls, monster_level, 200, random.randint(0, 300), 0, 0, 0, *random.sample(range(3, 18), 3), 0]  # added a zero at end for hitpoints placeholder
monster_con = round(monster_stats[6] * 1.2)  # add 20% to constitution (index 7)
monster_stats[9] = monster_con  # make index 9 (hitpoints) 20% more than constitution
# name0, level1, experience_award2, gold3, sword4, armor5, shield6, constitution7, strength8, dexterity9, hitpoints10
#monster = Monster(*monster_stats)  # send stats to Monster class and create 'monster' as object
monster = monster_cls(*monster_stats)  # send stats to monster class and create 'monster' as object
print(f"You have encountered a level {monster_level} {monster.name}")
print(monster_stats)
damage_to_monster = player_1.swing(player_1.name, player_1.level, player_1.dexterity, player_1.strength, player_1.sword,
                                   monster.level,
                                   monster.name, monster.dexterity, monster.armor_class)  # send stats to player's swing function
monster.reduce_health(damage_to_monster)
if monster.check_dead() == False:
    print(f"{monster.name} is not dead.")
else:
    print(f"It died..")
    player_1.experience += monster.experience_award
    player_1.gold += monster.gold
print(f"You have {player_1.hit_points} hitpoints, {player_1.gold} gold, and {player_1.experience} experience. You are level {player_1.level}")
# name, level, dexterity, strength, sword, player_level, player_hp

damage_to_player = monster.swing(monster.name, monster_level, monster.dexterity, monster.strength, monster.sword,
                                 player_1.level, player_1.hit_points, player_1.dexterity)
player_1.reduce_health(damage_to_player)
if player_1.check_dead() == False:
    print(f"You are alive")
else:
    print(f"You have died.")
    exit()
print(f"You have {player_1.hit_points} hitpoints, and {player_1.experience} experience. You are level {player_1.level}")
