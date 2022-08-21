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
        self.position = 0
        self.starting_x = 0
        self.starting_y = 0
        self.grid = []
        self.player_grid = []

    def __repr__(self):
        return self.name


class Dungeon1(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "Dungeon Level 1"
        self.level = 1

        self.position = 0
        self.starting_x = 1
        self.starting_y = 3
        self.grid = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
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
        self.event = self.grid[2][3]


dungeon_1 = Dungeon1()


class Dungeon2(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "Dungeon level 2"
        self.level = 2
        self.position = 0
        self.starting_x = 2
        self.starting_y = 2
        self.grid = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
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


dungeon_2 = Dungeon2()


class Dungeon3(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "Dungeon level 3"
        self.level = 3
        self.position = 0
        self.starting_x = 7
        self.starting_y = 1
        self.grid = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],
            ["*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]
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
