import random

a = 0
while a < 20:
    print(random.randint(1, 20))
    a += 1

b = random.sample(range(3, 19), 5)
print(b)
keepGameRunning = True
while keepGameRunning:
    navigate = input("Which way to navigate or E to enter dungeon")
    if navigate not in ('e'):
        print(f"You are navigating")
    else:
        keepGameRunning = False
print("You enter the dungeon")

