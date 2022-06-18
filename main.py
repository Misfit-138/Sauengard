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
from monster_class_module import Monster
import random
import os
# from swing_function import swing
from current_player import *

# player_stats = [18,17,16,15,14]
player_name = input("Enter Player name: ")
# player_stats = (player_name,18,18,18,18,18)
# the asterisk * before the random function passes the parameters without
# the brackets

accept_stats = ""
while accept_stats != "y":
    os.system('cls')
    # name,level,gold,sword,armor,shield,constitution,intelligence,wisdom,strength,dexterity
    # player_stats = (player_name,1,0,0,0,0,*random.sample(range(3, 19), 5), 18)
    player_stats = [player_name, 1, 0, 0, 0, 0, *random.sample(range(3, 19), 5), 0]
    # print(player_stats)
    con = round(player_stats[6] * 1.2)
    player_stats[11] = con
    player_1 = Player(*player_stats)  # sending stats to Player Class
    print(f"Name: {player_1.name}")
    print(f"Level: {player_1.level}")
    print(f"Gold: {player_1.gold}")
    print(f"Sword + {player_1.sword}")
    print(f"Armor + {player_1.armor}")
    print(f"Shield + {player_1.shield}")
    print(f"Constitution {player_1.constitution}")
    print(f"Intelligence: {player_1.intelligence}")
    print(f"Wisdom: {player_1.wisdom}")
    print(f"Strength: {player_1.strength}")
    print(f"Dexterity: {player_1.dexterity}")
    print(f"Hitpoints: {player_1.hitpoints}")
    # thisdict.update({"color": "red"})
    # hitpoints_modifier = (player_1.constitution - 10) / 2
    # hitpoints = player_1.constitution + hitpoints_modifier
    print(f"Hitpoints: {player_1.hitpoints}")
    accept_stats = input("Accept stats y/n ?")
# current_player.update({'Name': player_1.name})
'''print(f"Level: {player_1.level}")
    print(f"Gold: {player_1.gold}")
    print(f"Sword + {player_1.sword}")
    print(f"Armor + {player_1.armor}")
    print(f"Shield + {player_1.shield}")
    print(f"Constitution {player_1.constitution}")
    print(f"Intelligence: {player_1.intelligence}")
    print(f"Wisdom: {player_1.wisdom}")
    print(f"Strength: {player_1.strength}")
    print(f"Dexterity: {player_1.dexterity}")'''

'''player_1.swing(player_1.dexterity, player_1.strength, player_1.sword)  # call swing function and send stats
pres_a_key = input()
# name,level,gold,sword,armor,shield,constitution,intelligence,wisdom,strength,dexterity
monster_stats = ("Kobold",1,0,0,0,0,*random.sample(range(3, 18), 5))
monster = Monster(*monster_stats)  # send stats to Monster class
monster.swing(monster.dexterity, monster.strength, monster.sword)'''

'''
monsters = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
"Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", "Dragon"]
random_monster = random.randint(0, 19)
        experience_points = (random_monster + 1) * 100
        Monster_MAX_Hitpoints = random.uniform(0.8, 1.2) * Character_MAX_Hitpoints
        Monster_Hitpoints = Monster_MAX_Hitpoints
        os.system('cls')
        print("You have encountered a ", (monsters[random_monster])) '''

# name, dexterity, strength, sword

player_1.swing(player_name, player_1.dexterity, player_1.strength, player_1.sword, player_1.hitpoints)

print(player_1.hitpoints)
print
