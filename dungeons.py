"""         ".": f"You are in a rather wide open area of {self.dungeon.name}. There are exits in each direction...",
            "1": f"You are at a dead end. The only exit is to the North...",
            "2": f"You are at a dead end. The only exit is to the South...",
            "3": f"You are at a dead end. The only exit is to the East...",
            "4": f"You are at a dead end. The only exit is to the West...",
            "5": f"This is a tunnel corridor of {self.dungeon.name}. Exits are to the North and South...",
            "6": f"You are in a corridor of {self.dungeon.name}. Exits are to the East and West...",
            "7": f"You are in a corner. Exits are to the South and East.",
            "8": f"You are in a corner. Exits are to the North and East.",
            "9": f"You are in a corner. Exits are to the South and West.",
            "-": f"You are in a corner. Exits are to the North and West.",
            "|": f"You are against a {self.dungeon.barrier_name} to the North. Exits are to the South, East and West.",
            "/": f"You are against a {self.dungeon.barrier_name} to the South. Exits are to the North, East and West.",
            "(": f"You are against a {self.dungeon.barrier_name} to the West. Exits are to the North, South and East.",
            ")": f"You are against a {self.dungeon.barrier_name} to the East. Exits are to the North, South and West.",
            "T": f"You are in a chamber of {self.dungeon.name} that seems to have been "
                 f"re-purposed as a sort of throne room.",
            "L": f"You are on a slick patch of ground. High above you is a wide, gaping hole leading up to "
                 f"dungeon level {self.dungeon.level - 1}.\"
"""


# maps
class Dungeon:

    def __init__(self):
        self.name = ""
        self.level = 0
        self.starting_x = 0
        self.starting_y = 0
        self.name = ""
        self.level = 0
        self.barrier_name = ""
        self.treasure_chest = None
        self.quantum_treasure_chest = None
        self.encounter_sikira = None
        self.altar = None
        self.throne = None
        self.throne2 = None
        self.fountain = None
        self.fountain2 = None
        self.teleporter = None
        self.teleporter2 = None
        self.teleporter_landing = None
        self.staircase = None
        self.elevator = None
        self.elevator_landing = None
        self.pit = None
        self.pit2 = None
        self.pit_landing = None
        self.exit = None
        self.grid = []
        self.player_grid = []

    def __repr__(self):
        return self.name


class Dungeon1(Dungeon):

    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Catacombs"
        self.level = 1
        self.staircase = (16, 3)
        self.barrier_name = "wall of tombs"
        self.treasure_chest = (2, 14)
        self.quantum_treasure_chest = (0, 0)
        self.encounter_sikira = (0, 0)
        self.altar = (0, 0)
        self.throne = (0, 0)
        self.throne2 = (0, 0)
        self.fountain = (0, 0)
        self.fountain2 = (0, 0)
        self.teleporter = (0, 0)
        self.teleporter2 = (0, 0)
        self.teleporter_landing = (0, 0)
        self.elevator = (4, 18)
        self.elevator_landing = (0, 0)
        self.pit = (0, 0)
        self.pit2 = (0, 0)
        self.pit_landing = (1, 14)
        self.exit = (19, 3)
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "C", "H", "H", "H", "C", "*", "|", "|", "|", "|", "|", "|", "|", "C", "*"],  # 1
            ["*", "*", "*", "*", "*", "H", "*", "*", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 2
            ["*", "D", "H", "H", "H", "I", "*", ".", ".", "O", ".", ".", ".", ".", ".", ".", "S", ".", ">", "E"],  # 3
            ["*", "*", "*", "*", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 4
            ["*", "C", "|", "C", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 5
            ["*", "|", ".", "|", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 6
            ["*", "|", ".", "|", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 7
            ["*", "|", ".", "|", "*", "H", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 8
            ["*", "|", ".", ".", "3", "O", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 9
            ["*", "|", ".", ".", ".", "|", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 10
            ["*", "|", ".", ".", ".", "|", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 11
            ["*", "C", "|", "|", "|", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 13
            ["*", "C", "|", "|", "C", "*", "C", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 14
            ["*", "|", "P", "P", "|", "*", "|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 15
            ["*", "|", "P", "P", "|", "*", "|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 16
            ["*", "|", "P", "P", "|", "*", "|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", "*"],  # 17
            ["*", "C", "|", "|", "C", "*", "C", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "C", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
#             0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
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
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = "You descend the crumbling steps of a deep, spiral staircase, finding yourself in a\n" \
                     "darkness more dense than any you have ever known. Taking a moment to adjust to the thick " \
                     "gloom,\n" \
                     "you hear a disturbance from above, as the great door is slammed and barred shut!\n" \
                     "As the echoes throughout the emptiness linger, you hear the muffled scraping of a mighty " \
                     "chain\n" \
                     "being quickly wrestled into place, and finally, locked and released with a thud.\n" \
                     "This is the entrance of the catacombs. Blackness and the stench of filth surround you."


dungeon_1 = Dungeon1()


class Dungeon2(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Lower Catacombs"
        self.level = 2
        self.staircase = (1, 3)
        self.barrier_name = "wall of smooth, precisely quarried stone"
        self.treasure_chest = (2, 14)
        self.quantum_treasure_chest = (1, 2)
        self.altar = (1, 2)
        self.throne = (2, 3)
        self.throne2 = (2, 4)
        self.fountain = (3, 3)
        self.fountain2 = (3, 4)
        self.teleporter = (4, 3)
        self.teleporter2 = (4, 4)
        self.teleporter_landing = (1, 3)
        self.elevator = (5, 4)
        self.elevator_landing = (5, 5)
        self.pit = (1, 4)
        self.pit2 = (1, 5)
        self.pit_landing = (1, 6)
        self.exit = (19, 3)
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],  # 1
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 2
            ["*", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],  # 3
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 4
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 5
            ["*", "L", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 6
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
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = f"The door above closes solidly. You find yourself in a deeper level of the catacombs.\n" \
                     f"Thick, oppressive gloom and disturbing sounds fill the air."


dungeon_2 = Dungeon2()


class Dungeon3(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Deep Catacombs"
        self.level = 3
        # self.boss = Shadow()
        # self.king = Orc()
        self.barrier_name = "wall of slick, black stone"
        self.treasure_chest = (2, 14)
        self.quantum_treasure_chest = (1, 2)
        self.altar = (1, 2)
        self.throne = (2, 3)
        self.throne2 = (2, 4)
        self.fountain = (3, 3)
        self.fountain2 = (3, 4)
        self.teleporter = (4, 3)
        self.teleporter2 = (4, 4)
        self.teleporter_landing = (1, 3)
        self.staircase = (1, 3)  # same as start...get rid of start?
        self.elevator = (5, 4)
        self.elevator_landing = (5, 5)
        self.pit = (1, 4)
        self.pit2 = (1, 5)
        self.pit_landing = (1, 6)
        # self.start = (7, 1)
        self.exit = (19, 3)
        # self.starting_x = 7
        # self.starting_y = 1
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "7", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "9", "*"],  # 1
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 2
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ">", "E"],  # 3
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 4
            ["*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 5
            ["*", "L", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 6
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
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = "You find yourself at the bottom of a deep, spiral staircase..\n" \
                     "The echo from the door above being locked behind you still echoes throughout the emptiness.\n" \
                     "This is the entrance of the deepest catacombs. The gloom and stench of filth surround you."


dungeon_3 = Dungeon3()

dungeon_dict = {1: dungeon_1,
                2: dungeon_2,
                3: dungeon_3}

# blank grid with pit in lower left at 1, 14.
"""self.grid = [
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
            ["*", "8", "/", "/", "/", "/", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 13
            ["*", "7", "|", "|", "9", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 14
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 15
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 16
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 17
            ["*", "8", "/", "/", "-", "*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
            """