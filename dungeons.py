# DEAD END Only 1 exit!
# 1 exit to the north
# 2 exit to the south
# 3 exit to the east
# 4 exit to the west
# STRAIGHT HALLWAY:
# 5 exits north and south
# 6 exits east and west
# CORNERS:
# 7 exits to the south and east UPPER LEFT
# 8 exits to the north and east LOWER LEFT
# 9 exits to the south and west UPPER RIGHT
# - exits to the north and west LOWER RIGHT
# WALLS:
# \  exits to the south. east and west  NORTH WALL
# / exits to the north, east and west SOUTH WALL
# > exits to the north, south and east WEST WALL
# < exits to the north, south and west EAST WALL


# maps
class Dungeon:

    def __init__(self):
        self.name = ""
        self.level = 0
        # self.position = 0
        self.starting_x = 0
        self.starting_y = 0
        self.grid = []
        self.player_grid = []

    def __repr__(self):
        return self.name


class Dungeon1(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Catacombs"
        self.level = 1
        # self.event = (2, 3)
        self.barrier_name = "wall of smooth, precisely quarried stone"
        self.throne = (2, 3)
        self.fountain = (3, 3)
        self.teleporter = (4, 3)
        self.teleporter_landing = (1, 3)  # NA for level one
        self.staircase = (1, 3)
        self.pit = (1, 4)
        self.pit_landing = (1, 4)
        self.start = (1, 3)
        self.starting_x = 1
        self.starting_y = 3
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],  # 1
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 2
            ["*", "(", "T", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],  # 3
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 4
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 5
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 6
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 7
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 8
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 9
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 10
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 11
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 12
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 13
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 14
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 15
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 16
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 17
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        self.intro = "You descend the crumbling steps of a deep, spiral staircase, finding yourself in a\n" \
                     "darkness more dense than any you have ever known. Taking a moment to adjust to the thick gloom,\n" \
                     "you hear a disturbance from above, as the great door is slammed and barred shut!\n" \
                     "As the echoes throughout the emptiness linger, you hear the muffled scraping of a mighty chain\n" \
                     "being quickly wrestled into place, and finally, locked and released with a thud.\n" \
                     "This is the entrance of the catacombs. Blackness and the stench of filth surround you."


dungeon_1 = Dungeon1()


class Dungeon2(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Lower Catacombs"
        self.level = 2
        self.barrier_name = "wall comprised of smooth stone"
        self.throne = (2, 3)
        self.fountain = (3, 3)
        self.teleporter = (4, 3)
        self.teleporter_landing = (1, 3)
        self.staircase = (1, 3)
        self.pit = (1, 4)
        self.pit_landing = (1, 4)
        self.start = (1, 3)
        self.starting_x = 1
        self.starting_y = 3
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],  # 1
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 2
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],  # 3
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 4
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 5
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 6
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 7
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 8
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 9
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 10
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 11
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 12
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 13
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 14
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 15
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 16
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 17
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        self.intro = "You find yourself at the bottom of a deep, spiral staircase..\n" \
                     "The echo from the door above being locked behind you still echoes throughout the emptiness.\n" \
                     "This is the entrance of the lower catacombs. The gloom and stench of filth surround you."


dungeon_2 = Dungeon2()


class Dungeon3(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "Dungeon level 3"
        self.level = 3
        self.barrier_name = "wall comprised of smooth stone"
        self.throne = (2, 3)
        self.fountain = (3, 3)
        self.teleporter = (4, 3)
        self.teleporter_landing = (1, 3)
        self.staircase = (7, 1)
        self.pit = (1, 4)
        self.pit_landing = (1, 4)
        self.start = (7, 1)
        self.starting_x = 7
        self.starting_y = 1
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],  # 1
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 2
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],  # 3
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 4
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 5
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 6
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 7
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 8
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 9
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 10
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 11
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 12
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 13
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 14
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 15
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 16
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 17
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        self.intro = "You find yourself at the bottom of a deep, spiral staircase..\n" \
                     "The echo from the door above being locked behind you still echoes throughout the emptiness.\n" \
                     "This is the entrance of the lower catacombs. The gloom and stench of filth surround you."


dungeon_3 = Dungeon3()

dungeon_dict = {1: dungeon_1,
                2: dungeon_2,
                3: dungeon_3}

# print(dungeon_dict[1])

'''dungeon_1_map = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "0"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "0"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "E"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "0"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "0"],
                 ["0", ".", ".", ".", ".", ".", ".", ".", "0"],
                 ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]

dungeon_1_player_map = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", "S", ".", ".", ".", ".", ".", ".", "E"],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", ".", ".", "."]]

'''

# starting position
# x = 1
# y = 3
# position = 0
'''self.grid = [["*", "*", "*", "*", "*", "*", "*", "*", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", ".", ".", ".", ".", ".", ".", ".", "*"],
                     ["*", "*", "*", "*", "*", "*", "*", "*", "*"]]
        self.player_grid = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", "S", "E"],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."],
                            [".", ".", ".", ".", ".", ".", ".", ".", "."]]'''
