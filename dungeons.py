# Sauengard © Copyright 2022 by Jules Pitsker
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.

"""

Copyright 2022, JULES PITSKER  (pitsker@proton.me)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. All advertising materials mentioning features or use of this software must
   display the following acknowledgement:
     This product includes software developed by Jules Pitsker.

4. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Thanks to the following STACK OVERFLOW members:
The Spider, Anentropic, The Thonnu and Optimal: for helping me get my footing during my first days of learning python
Yarik0urWorld: for help with python list syntax
Angus Nicolson: for self.__dict__ code snippet and explanation
Liju and snakecharmerb: for explanation of hashable objects
Pawel Pietraszko: for assistance with initializing new object instances every time player gets new item
triplee: for assistance with Path syntax

Thanks to @LearntoCodeGCSE for the 2D array video.

SOUND/MUSIC:
Main theme: "Soul's Departure" Royalty Free Music by Darren Curtis
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Blacksmith Theme: 'Viking Intro loop' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Dungeon Themes: 'Dragon Quest', 'Dragon Song', 'Medieval Metal', 'Cinematic Celtic Metal', by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Chemist Theme: 'Might and Magic' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Fieldenberg Theme: 'Tavern Loop 1' by Alexander Nakarada
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Boss battle theme: 'Dragon Castle' / Epic Orchestral Battle Music by Makai Symphony
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Tavern Theme: 'The Medieval Banquet' by Silverman Sound is under a Creative Commons license (CC BY 3.0)
Music promoted by BreakingCopyright: http://bit.ly/Silvermansound_Medieval

Pit theme: 'Epic 39' by Jules Pitsker
Creative Commons Attribution License 4.0 International (CC BY 4.0)

Hall of the Mountain King by Kevin MacLeod http://incompetech.com
Creative Commons Attribution License 4.0 International (CC BY 4.0)
Free Download / Stream: https://bit.ly/hall-of-the-mountain-king
Music promoted by Audio Library https://youtu.be/2RDX5sVEfs4
PC Boot up sounds: Eirikr / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Floppy Disk Insert Sound: Joseph Sardin (BigSoundBank.com)
Creative Commons CC0 1.0 Universal (CC0 1.0)

Floppy Disk Drive R/W Sounds: Dennis Johansson (MrAuralization / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)

Gong: juskiddink / Freesound.org
Creative Commons Attribution License 3.0 (CC BY 3.0)

Clacky Keyboard: Denis McDonald (denismcdonald / Freesound.org)
Creative Commons Attribution License 3.0 (CC BY 3.0)"""


# atrium: an open-roofed entrance hall or central court

class Dungeon:

    def __init__(self):
        self.name = "A Dungeon"
        self.casual_name = "the dungeon"
        self.level = 0
        self.barrier_name = "a stone wall"
        self.barrier_name_plural = "stone walls"
        self.pit_barrier_name = "a wall of putrid moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.staircase = (0, 0)
        self.treasure_chest = (0, 0)
        self.quantum_treasure_chest = (0, 0)
        self.encounter_sikira = (0, 0)
        self.altar = (0, 0)
        self.throne = (0, 0)
        self.fountain = (0, 0)
        self.teleporter = (0, 0)
        self.teleporter_landing = (0, 0)
        self.elevator = (0, 0)
        self.elevator_landing = (0, 0)
        self.pit = (0, 0)
        self.pit_landing = (0, 0)
        self.elite_monster = (0, 0)  # 4, 10
        self.legendary_monster = (0, 0)
        self.wicked_queen = (0, 0)
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
        self.barrier_name = "a stone wall of tombs"
        self.barrier_name_plural = "walls of tombs"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of ancient masonry."  # of {self.casual_name}
        self.corridor_name = f"a tunneled corridor"
        self.pit_description_phrase = f"Slime covers the ground beneath your feet, and a putrid mist fills the air."
        self.pit_corridor_phrase = "You are in a narrow passage."
        self.pit_corridor_name = "a cramped passage"
        self.intersection_name = "a domed chamber"
        self.pit_intersection_name = "a large, open cavity"
        self.large_atrium_phrase = "You are standing in a large, vaulted atrium."
        self.one_walled_atrium_phrase = "You are standing in an atrium."
        self.pit_large_atrium_phrase = "You are standing in a large cavity."
        self.pit_one_walled_atrium_phrase = "You are standing in a cavity."
        self.staircase = (6, 18)
        self.treasure_chest = (3, 16)
        self.quantum_treasure_chest = (99, 99)
        self.encounter_sikira = (99, 99)
        self.altar = (99, 99)
        self.throne = (99, 99)
        self.fountain = (99, 99)
        self.teleporter = (99, 99)
        self.teleporter_landing = (99, 99)
        self.elevator = (4, 18)
        self.elevator_landing = (8, 5)
        self.pit = (10, 7)
        self.pit_landing = (1, 14)  # always 1, 14
        self.elite_monster = (99, 99)  # 4, 10
        self.legendary_monster = (99, 99)
        self.wicked_queen = (99, 99)
        self.exit = (10, 0)
        # S = STAIRCASE C = CORRIDOR, P = PIT-opening, L = PIT LANDING ^ = ELEVATOR V = ELEVATOR LANDING . = OPEN AREA
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "E", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "C", "C", "C", "V", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "P", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "*", ".", ".", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", "L", "C", ".", ".", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", "C", "*", ".", ".", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", "C", "*", "*", ".", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", "C", "C", "C", "^", "*", "S", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E", ".", ".", ".", ".", ".", ".", ".", ".", "."],
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
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is called first and is more active
        self.intro = "You descend the crumbling steps of a deep, spiral staircase, finding yourself in a dense,\n" \
                     "dark atmosphere more oppressive than any you have ever known. Taking a moment to adjust to the " \
                     "thick gloom,\n" \
                     "you hear a disturbance from above, as the great door is slammed and barred shut!\n" \
                     "As the echoes throughout the emptiness linger, you hear the muffled scraping of a mighty " \
                     "chain\n" \
                     "being quickly wrestled into place, and finally, locked and released with a thud.\n" \
                     "Blackness and the stench of filth surround you.  BEWARE . . .\n"


class Dungeon2(Dungeon):
    def __init__(self):
        super().__init__()
        self.name = "The Abandoned Dwarf Tunnels"
        self.casual_name = "the abandoned tunnels"
        self.level = 2
        self.barrier_name = "a wall of cut stone"
        self.barrier_name_plural = "walls of cut stone"
        self.pit_barrier_name = "a wall of moist earth"
        self.pit_barrier_name_plural = "walls of moist earth"
        self.corridor_phrase = f"This is a corridor of {self.casual_name}."
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
        self.staircase = (7, 12)
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
        self.elite_monster = (99, 99)  # 4, 10
        self.legendary_monster = (99, 99)
        self.wicked_queen = (99, 99)
        self.exit = (10, 0)
        self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "C", "*", "C", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "C", "C", "C", "C", "C", "C", "C", "C", "*", "*", "*", "*", "*", "*", "*", "C", "*"],  # 6
            ["*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "*", "C", "*"],  # 7
            ["*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "C", "C", "C", "C", "E"],  # 8
            ["*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "C", "*"],  # 9
            ["*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", "C", "*"],  # 10
            ["*", "*", "*", "C", "*", "*", ".", ".", ".", "*", "*", ".", ".", ".", "C", "C", "*", "*", "C", "*"],  # 11
            ["*", "*", "*", "C", "C", "C", ".", "S", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", "C", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", "C", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", ".", "C", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", ".", "*", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
        self.player_grid = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "E"],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        # the intro is similar to the staircase description. however, the intro is more of an active description
        self.intro = f"The door above closes solidly. You find yourself in a deeper level of the dungeons.\n" \
                     f"This is the Sauengard realm abandoned by the dwarves many ages ago.\n" \
                     f"Thick, oppressive gloom and disturbing sounds fill the air.\n"


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
            ["*", "*", "*", "*", "*", "C", "C", "C", "*", "*", "*", "C", "C", "C", "C", "C", "C", "C", "C", "*"],  # 1
            ["*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "*"],  # 2
            ["*", "S", "C", "C", "C", "C", "C", ".", ".", ".", "*", "C", "*", "*", ".", ".", ".", "C", "+", "E"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", ".", ".", ".", "*", "C", "*"],  # 4
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "C", "*", "*", ".", ".", ".", "*", "C", "*"],  # 5
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "C", "*", "C", "*", "*", ".", ".", ".", "*", "C", "*"],  # 6
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "*", "*", "*", ".", ".", "*", "C", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "C", "C", "C", "*", ".", ".", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "*", "*", "*", "C", "*", "*", "C", "C", "C", "*"],  # 9
            ["*", "*", "*", "*", "C", "C", "*", ".", ".", ".", "*", "C", "C", "C", "*", "*", "*", "*", "C", "*"],  # 10
            ["*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "C", "*", "*", "*", "*", "*", "*", "C", "*"],  # 11
            ["*", "*", "*", "*", "*", "C", "C", "*", "C", "C", "*", "C", "C", ".", ".", "*", "*", ".", ".", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "C", "*", "*", "C", "*", "*", "*", ".", ".", "*", "*", ".", ".", "*"],  # 13
            ["*", "C", "C", ".", ".", "*", "C", "*", "*", "C", "*", "C", "C", ".", ".", "*", "*", ".", ".", "*"],  # 14
            ["*", "C", "*", ".", ".", "*", "C", "*", ".", ".", "*", "C", "*", "*", "C", "*", "*", ".", ".", "*"],  # 15
            ["*", "C", "*", ".", ".", "*", "C", "*", ".", ".", "*", "C", "*", "*", "C", "*", "*", ".", ".", "*"],  # 16
            ["*", "C", "*", "*", "C", "*", "C", "*", "*", "C", "*", "C", "*", "*", "C", "*", "*", ".", ".", "*"],  # 17
            ["*", "C", "C", "C", "L", "*", "C", "C", "C", "C", "C", "C", "C", "C", "C", "*", ".", ".", ".", "*"],  # 18
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
        self.intro = "You find yourself at the bottom of a deep, spiral staircase..\n" \
                     "The echo from the door above being locked behind you still echoes throughout the emptiness.\n" \
                     "This is the entrance of the deepest catacombs. The gloom and stench of filth surround you."


dungeon_dict = {1: Dungeon1(),
                2: Dungeon2(),
                3: Dungeon3()
                }

# blank grid with pit in lower left at 1, 14.
"""self.grid = [
            # 0    1    2    3    4    5    6    7    8    9   10    11   12   13   14   15   16   17   18   19
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 0
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 1
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 2
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 3
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 4
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 5
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 6
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 7
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 8
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 9
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 10
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 11
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 12
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 13
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 14
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 15
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 16
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 17
            ["*", ".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],  # 18
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]  # 19
            """
