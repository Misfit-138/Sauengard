import random

a = 0
while a < 20:
    print(random.randint(1, 20))
    a += 1

b = random.sample(range(3, 19), 5)
print(b)
