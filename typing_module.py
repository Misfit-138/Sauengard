import time
import random
import sys


def typing(message):
    print("")
    # print(message) # Eliminate this after testing...
    for word in message:
        time.sleep(0.02)  # (random.choice([0.1, 0.09, 0.08, 0.07, 0.06]))
        sys.stdout.write(word)
        sys.stdout.flush()
    time.sleep(.1)
    return ""
