
class Dungeon:

    def __init__(self):
        self.name = ""
        self.casual_name = ""
        self.level = 0
        self.staircase = (0, 0)
        self.barrier_name = ""
        self.barrier_name_plural = ""
        self.pit_barrier_name = ""
        self.pit_barrier_name_plural = ""
        self.corridor_phrase = ""
        self.corridor_name = ""
        self.pit_description_phrase = ""
        self.pit_corridor_phrase = ""
        self.pit_corridor_name = ""
        self.large_atrium_phrase = ""
        self.one_walled_atrium_phrase = ""
        self.pit_large_atrium_phrase = ""
        self.pit_one_walled_atrium_phrase = ""
        self.treasure_chest = (0, 0)
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
        self.elevator = (0, 0)
        self.elevator_landing = (0, 0)
        self.pit = (0, 0)
        self.pit2 = (0, 0)
        self.pit_landing = (0, 0)
        self.exit = (0, 0)
        self.grid = []
        self.player_grid = []

    def __repr__(self):
        return self.name


class Dungeon1(Dungeon):

    def __init__(self):
        super().__init__()
        self.name = "The Fieldenberg Catacombs"
        self.casual_name = "the catacombs"
        self.level = 1
        self.staircase = (16, 3)
        self.barrier_name = "a wall of tombs"
        self.barrier_name_plural = "walls of tombs"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        # an open-roofed entrance hall or central court
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.treasure_chest = (14, 2)
        self.quantum_treasure_chest = (99, 99)
        self.encounter_sikira = (99, 99)
        self.altar = (99, 99)
        self.throne = (99, 99)
        self.fountain = (99, 99)
        self.teleporter = (99, 99)
        self.teleporter_landing = (99, 99)
        self.elevator = (4, 18)
        self.elevator_landing = (9, 3)
        self.pit = (15, 3)
        self.pit_landing = (1, 14)
        self.micro_boss = (18, 2)  # migrate to elite, legendary monsters logic and change name!
        self.exit = (19, 3)

        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", ".", ".", ".", "*", "C", "C", "C", "C", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 1
            ["*", "*", "*", "*", "*", "C", "*", "*", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 2
            ["*", "C", "C", "C", "C", "C", "C", ".", ".", ".", ".", ".", ".", ".", ".", ".", "S", ".", ".", "E"],  # 3
            ["*", "*", "*", "*", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 4
            ["*", ".", ".", ".", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 5
            ["*", ".", ".", ".", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 6
            ["*", ".", ".", ".", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 7
            ["*", ".", ".", ".", "*", "C", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 8
            ["*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 9
            ["*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 10
            ["*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 11
            ["*", ".", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 13
            ["*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 14
            ["*", ".", "*", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 16
            ["*", "C", "*", "*", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 17
            ["*", "C", "C", "C", ".", "*", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*"],  # 18
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
        self.intro = "You descend the crumbling steps of a deep, spiral staircase, finding yourself in a dense\n" \
                     "darkness more oppressive than any you have ever known. Taking a moment to adjust to the thick " \
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
        self.casual_name = "the lower catacombs"
        self.level = 2
        self.staircase = (1, 3)
        self.barrier_name = "a wall of tombs"
        self.barrier_name_plural = "walls of tombs"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry of {self.casual_name}."
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity opening."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity opening."
        self.treasure_chest = (2, 14)
        self.quantum_treasure_chest = (1, 2)
        self.altar = (1, 2)
        self.throne = (2, 3)
        self.fountain = (3, 3)
        self.teleporter = (4, 3)
        self.teleporter_landing = (1, 3)
        self.elevator = (4, 18)
        self.elevator_landing = (5, 5)
        self.pit = (1, 4)
        self.pit_landing = (1, 14)
        self.exit = (19, 3)
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
            ["*", "8", "/", "/", "/", "/", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 13
            ["*", "7", "|", "|", "9", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 14
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 15
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 16
            ["*", "(", "P", "P", ")", "*", "(", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ")", "*"],  # 17
            ["*", "8", "/", "/", "-", "*", "8", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "-", "*"],  # 18
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
        self.barrier_name = "wall of slick, black stone"
        self.barrier_name_plural = "walls of slick, black stone"
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