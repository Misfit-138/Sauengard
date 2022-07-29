from dice_roll_module import *

successes = 0
fails = 0
attempt = 0
while successes < 3 or fails < 3:
    if successes == 3:
        print(f"You are revived!")
        break
    if fails >= 3:
        print(f"Death saving throw failed!")
        break
    death_save = dice_roll(1, 20)
    attempt += 1
    print(f"Attempt {attempt}: {death_save}")

    if death_save == 20:
        print(f"You are revived!")

        hit_points = 1
        break
    if death_save > 9:
        successes += 1
        print(f"{successes} Successful saves..")

    if 10 > death_save > 1:
        fails += 1
        print(f"{fails} Failed saves..")

    if death_save == 1:
        fails += 2
        print(f"Rolling a 1 adds 2 failed saves. ")
        print(f"{fails} Failed saves..")
