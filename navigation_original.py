# map
dungeonMap = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
              ["0", ".", ".", "1", ".", ".", ".", ".", "0"],
              ["0", ".", ".", "2", ".", ".", ".", "1", "0"],
              ["0", ".", ".", "4", ".", ".", ".", "5", "E"],
              ["0", ".", ".", ".", "1", ".", ".", ".", "0"],
              ["0", ".", ".", "1", "*", ".", ".", ".", "0"],
              ["0", "8", ".", "3", ".", ".", ".", ".", "0"],
              ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

playerMap = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["S", ".", ".", ".", ".", ".", ".", ".", "E"],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]


# Displaying the map
def displayMap(maps):
    for x in range(0, 8):
        print(maps[x])


# selecting a map
mapChoice = dungeonMap

displayMap(playerMap)

# initialising the players position
position = mapChoice[0][0]


def main(mapChoice, playerMap, position):
    # players starting position
    x = 0
    y = 3
    # players inventory
    key = False
    sword = False

    print(mapChoice[y][x])
    position = 0
    while position != "E":

        previousX = x
        previousY = y

        movement = input("N,S,E,W,MAP").upper()

        if movement == "N":
            y = y - 1

        if movement == "S":
            y = y + 1

        if movement == "E":
            x = x + 1

        if movement == "W":
            x = x - 1

        if movement == "MAP":
            displayMap(playerMap)

        position = mapChoice[y][x]
        playerMap[y][x] = "X"

        if position == "0" or position == "1":
            print("You hit a wall, you stumble in the darkness back to your previous position...")
            x = previousX
            y = previousY
            position = mapChoice[y][x]

        if position == ".":
            print("You are in a dark corridor, there are doors leading in each direction...")

        if position == "*":
            print("In the darkness you see a dull glint..")
            print("You go over to inspect and realise that the object is a sword..")
            print("You pick it up and holster it in you belt")
            sword = True

        if position == "2":
            print("You enter a room with an old mage at a table....")
            print("They tell you that in order to pass, you will need to answer their riddle...")
            print("What has a bed but does not sleep, and a mouth but does not eat?")
            guess = input().upper()
            if guess != "RIVER":
                print(
                    "You anger the mage, they summon an enormous gust of wind, pushing you back out of the door, into the previous room")
                x = previousX
                y = previousY
                print("You are back outside the Mage's room...")
                position = mapChoice[y][x]

            else:
                print("You may pass through my room....")

        if position == "3":
            if key == False:
                print("you come across a door, but do not have a key for it...")
                x = previousX
                y = previousY
                print("You go back to the previous room")
                position = mapChoice[y][x]
            else:
                print("you come across a dimly lit door...")
                print("fumbling around in the dark, you find the keyhole...")
                print("You open the door, and walk through into the darkness....")

        if position == "4":
            print("You find a small crack in the wall...You could easily squeeze through...")
            print("as you squeeze through the gap you feel a rip and your inventory falls out of the rip")
            print("You have lost everything...is it worth going back?")
            print("You are the other side of the gap now...its up to you if you should continue on...")
            key = False
            sword = False

        if position == "5":
            print("You can see the exit up ahead, but one final challenge remains...")
            print("A troll appears before you, in order to leave you must present the code...")
            print("Did you find any letters on your travels?")
            guess = input().upper()
            if guess != "ZORK":
                print(
                    "The troll is seriously unimpressed, it makes a grab for you, but you dive back into the previous room")
                x = previousX
                y = previousY
                position = mapChoice[y][x]
            else:
                print("The troll is even more annoyed you got his password right")
                print("He makes a grab for you...")
                if sword == True:
                    print("Using the sword you slash at the troll who recoils in horror!")
                    print("The troll flees, leaving you to exit in peace...")
                else:
                    print("You dive out of his grasp and back into the last room")
                    print("Something tells me that troll isnt going to let you out without a fight!")
                    x = previousX
                    y = previousY
                    position = mapChoice[y][x]

        if position == "8":
            print("You find a small rusty key on the floor, you pick it up and put it in your pocket")
            key = True

    print("you made it out alive!!!")


main(mapChoice, playerMap, position)