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
from player_class_module import Player
import random
# player_stats = [18,17,16,15,14]
player_name = input("Enter Player name: ")
# player_stats = (player_name,18,18,18,18,18)
# the asterisk * before the random function passes the parameters without
# the brackets
player_stats = (player_name, *random.sample(range(6, 18), 5))
print(player_stats)

player_1 = Player(*player_stats)  # sending stats to Player Class
print(f"Name: {player_1.name}")
print(f"Constitution {player_1.constitution}")
print(player_1.intelligence)
print(player_1.wisdom)
print(player_1.strength)
print(player_1.dexterity)
#if player_1.dexterity > 12:
#    print("Great dexterity!!")
player_1.swing(player_1.dexterity, player_1.strength)
