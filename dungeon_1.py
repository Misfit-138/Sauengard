# map
dungeon_1_map = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
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
x = 1
y = 3
position = 0
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
# *  exits to the south. east and west  NORTH WALL
#  exits to the north, east and west SOUTH WALL
#  exits to the north, south and east WEST WALL
#  exits to the north, south and west EAST WALL
