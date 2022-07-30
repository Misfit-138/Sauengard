"""Choose a challenge rating (CR) for your trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)
• Multi-Target Damage = 3 x CR (or 1d6 per CR)
A monster usually dies or is destroyed when it drops to 0 Hit Points.
A monster’s Hit Points are presented both as a die expression and as an average number.
For example, a monster with 2d8 Hit Points has 9 Hit Points on average (2 × 4½).

Difficulty Class (DC) is something that’s used a lot. Whether that’s Saving Throws or Ability Checks.
Even Armor Class is a kind of DC. To put it simply, a DC determines how hard something is to do.
Whether that’s climbing a rope, evading a breath weapon, or swinging an ax, different actions have different DCs.

To determine whether you beat a DC, you need to roll equal to or higher than said DC.
But choosing how hard one is, is easier said than done. For example, walking across a treacherous rope bridge without
falling might take a DC 15 Dexterity (Acrobatics) check, but resisting a Wolf knocking you prone takes
a DC 11 Strength Saving Throw.

Many spells require Saving Throws and ability checks to negate but don’t even tell you what the DC is.
That’s because the DC equals 8 + Your Spellcasting Modifier + Your Proficiency Bonus.
And most other classes or features that require Saving Throws typically tell you how to calculate the DC or even
tell you what the DC is outright!

But what if it’s something you make that requires a DC to be set, like an ability check? For that,
you can use the following values as a guide (DMG p. 238):

TASK	            DC
Very easy	        5
Easy	            10
Moderate	        15
Hard	            20
Very Hard	        25
Nearly Impossible	30

A few things to know; however, a natural 20 doesn’t mean you automatically succeed.
You still have to add your bonuses, but it usually results in the most favorable outcome,
even though you can’t crit on ability checks. Likewise,
a natural 1 doesn’t mean automatic failure or a critical failure.
You could still pass the check if your bonuses are high enough. And on the note of failing a Check, the DM could still
have it succeed, but just at a cost (e.g., you leap across the chasm, but you break your leg on the ledge as you didn’t
land properly).

As you can see, it’s not that bad when you think about it. A DC is just a minimum result needed to perform a particular
task and succeed with minimal loss. And so with that, I hope you roll high and low in the best of moments!
A monster’s size determines the die used to calculate its Hit Points, as shown in the Hit Dice by Size table.

Table: Size Categories
Size	Space	Examples
Tiny	2½ by 2½ ft.	Imp, Sprite
Small	5 by 5 ft.	    Giant Rat, Goblin
Medium	5 by 5 ft.	    Orc, Werewolf
Large	10 by 10 ft.	Hippogriff, Ogre
Huge	15 by 15 ft.	Fire Giant, Treant
Gargantuan 20 by 20 ft. or more Kraken, Purple Worm

Table: Hit Dice by Size
Monster Size	Hit Die	Average HP
                         per Die
Tiny	        d4	       2½
Small	        d6	       3½
Medium	        d8	       4½
Large	        d10	       5½
Huge	        d12	       6½
Gargantuan	    d20	       10½

A monster’s Constitution modifier also affects the number of Hit Points it has.
Its Constitution modifier is multiplied by the number of Hit Dice it possesses,
and the result is added to its Hit Points.
For example, if a monster has a Constitution of 12 (+1 modifier)
and 2d8 Hit Dice, it has 2d8 + 2 Hit Points (average 11).

Adult Red Dragon
Huge dragon, chaotic evil
Armor Class 19 (Natural Armor)
Hit Points 256 (19d12+133)
Speed 40 ft., climb 40 ft., fly 80 ft.
STR 27 (+8)
DEX 10 (+0)
CON 25 (+7)
INT 16 (+3)
WIS 13 (+1)
CHA 21 (+5)
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st
# MONSTERS = ["Gnoll", "Kobold", "Skeleton", "Hobbit", "Zombie", "Orc", "Fighter", "Mummy", "Elf", "Ghoul", "Dwarf",
# "Troll", "Wraith", "Ogre", "Minotaur", "Giant", "Specter", "Vampire", "Balrog", Dragon]
"""

import random
import time

from dice_roll_module import dice_roll

'''Choose a challenge rating (CR) for your custom trap, object, effect, or creature
between 1 and 30. Write down its statistics from the following formulas:
• AC = 12 + ½ CR (or choose between 10 and 20 based on the story)
• DC = 12 + ½ CR
• Hit Points = 20 × CR
• Attack Bonus = 3 + ½ CR
• Proficient Saves or Skills = 3 + ½ CR
• Single-Target Damage = 7 × CR (or 2d6 per CR)'''


# # monsters have Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma


class Monster:

    def __init__(self):
        self.monster = "Super class"
        self.level = 0
        self.experience_award = 0
        self.gold = 0
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.armor_class = 0
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.hit_points = 0
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.hit_dice = 0  # tiny d4, small d6, medium d8, large d10, huge d12, gargantuan d20
        self.number_of_hd = self.level
        self.human_player_level = 0
        self.difficulty_class = 0
        self.proficiency_bonus = 0  # 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 0
        self.dexterity_modifier = 0
        self.strength_modifier = 0
        self.constitution_modifier = 0
        self.wisdom_modifier = 0
        self.attack_1 = 0
        self.attack_1_phrase = ""
        self.attack_2 = 0
        self.attack_2_phrase = ""
        self.attack_3 = 0
        self.attack_3_phrase = ""
        self.attack_4 = 0
        self.attack_4_phrase = ""
        self.attack_5 = 0
        self.attack_5_phrase = ""
        self.quantum_attack_1 = 0
        self.quantum_attack_1_phrase = ""
        self.quantum_attack_2 = 0
        self.quantum_attack_2_phrase = ""
        self.quantum_attack_3 = 0
        self.quantum_attack_3_phrase = ""
        self.quantum_attack_4 = 0
        self.quantum_attack_4_phrase = ""
        self.quantum_attack_5 = 0
        self.quantum_attack_5_phrase = ""
        self.introduction = ""
        self.paralyze_phrase = ""
        self.is_discovered = False

    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def swing(self, name, player_armor_class):
        attack_bonus = random.randint(1, 100)
        if attack_bonus <= 50:
            attack_bonus = self.attack_1
            attack_phrase = self.attack_1_phrase
        if attack_bonus > 50 <= 75:
            attack_bonus = self.attack_2
            attack_phrase = self.attack_2_phrase
        if attack_bonus > 75 <= 85:
            attack_bonus = self.attack_3
            attack_phrase = self.attack_3_phrase
        if attack_bonus > 85 <= 95:
            attack_bonus = self.attack_4
            attack_phrase = self.attack_4_phrase
        if attack_bonus > 95:
            attack_bonus = self.attack_5
            attack_phrase = self.attack_5_phrase
        roll20 = dice_roll(1, 20)
        print(f"The {name} attacks! (It rolls {roll20})")
        if roll20 == 1:
            print(f"..it awkwardly strikes and you easily block.")
            time.sleep(2)
            return 0
        print(f"Dexterity modifier {self.dexterity_modifier}")
        print(f"Your armor class ---> {player_armor_class}")
        if roll20 + self.dexterity_modifier >= player_armor_class:
            damage_roll = dice_roll(self.number_of_hd, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus + self.weapon_bonus)
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1)
                print(f"{name} rolls {self.hit_dice} sided hit dice---> {damage_roll}")
                print(f"Strength modifier---> {self.strength_modifier}\nAttack bonus---> {attack_bonus}")
                print(f"It does {damage_to_opponent} points of damage!")
                time.sleep(2.5)
                return damage_to_opponent
            else:
                print(f"The {name} strikes, but you block the attack!")  # zero damage to player result
                time.sleep(2)
                return 0  # 0 points damage to player
        else:
            print(f"It missed..")
            time.sleep(2)
            return 0

    def quantum_energy_attack(self, name, player_dexterity_modifier):
        attack_bonus = random.randint(1, 100)
        if attack_bonus <= 50:
            attack_bonus = self.quantum_attack_1
            attack_phrase = self.quantum_attack_1_phrase
        if attack_bonus > 50 <= 75:
            attack_bonus = self.quantum_attack_2
            attack_phrase = self.quantum_attack_2_phrase
        if attack_bonus > 75 <= 85:
            attack_bonus = self.quantum_attack_3
            attack_phrase = self.quantum_attack_3_phrase
        if attack_bonus > 85 <= 95:
            attack_bonus = self.quantum_attack_4
            attack_phrase = self.quantum_attack_4_phrase
        if attack_bonus > 95:
            attack_bonus = self.quantum_attack_5
            attack_phrase = self.quantum_attack_5_phrase
        player_roll20 = roll20 = dice_roll(1, 20)
        roll20 = dice_roll(1, 20)
        print(f"The {name} attacks with Quantum Energy! (It rolls {roll20})")
        if roll20 == 1:
            print(f"..its attempts to procure the universal forces fail miserably.")
            time.sleep(2)
            return 0
        print(f"Wisdom modifier {self.wisdom_modifier}")
        print(f"Your roll: {player_roll20} + dexterity modifier ---> {player_dexterity_modifier}. Total: {player_roll20 + player_dexterity_modifier}")
        if roll20 + self.wisdom_modifier >= player_roll20 + player_dexterity_modifier:
            damage_roll = dice_roll(self.number_of_hd, self.hit_dice)
            damage_to_opponent = round(damage_roll + self.wisdom_modifier + attack_bonus)
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1)
                print(f"{name} rolls {self.hit_dice} sided hit dice---> {damage_roll}")
                print(f"Wisdom modifier---> {self.wisdom_modifier}\nAttack bonus---> {attack_bonus}")
                print(f"It does {damage_to_opponent} points of damage!")
                time.sleep(2.5)
                return damage_to_opponent
            else:
                print(
                    f"The {name} strikes with Quantum Powers, but you dodge the attack!")  # zero damage to player result
                time.sleep(2)
                return 0  # 0 points damage to player
        else:
            print(f"It fails to harness the mysterious Quantum energies..")
            time.sleep(2)
            return 0

    def paralyze(self, human_player_wisdom):
        print(self.paralyze_phrase)
        #print(f"It lurches forward, grabbing your arm!")
        paralyze_chance = dice_roll(1, 20)

        if paralyze_chance > 18 or paralyze_chance > 17 and (self.wisdom + self.wisdom_modifier) >= (
                human_player_wisdom):

            print("You're paralyzed!!")
            time.sleep(1)
            print("As you stand, frozen and defenseless, it savagely gores you!")
            time.sleep(1)
            return True
        else:
            print("You ignore its wiles and break free from its grip!")
            return False


class Quasit(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = 25  # MM says it should be 200 exp?!
        self.gold = self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(4, 6)
        self.dexterity = random.randint(16, 17)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(9, 10)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # tiny
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It polymorphs into toad form.."
        self.attack_2 = 0
        self.attack_2_phrase = "It polymorphs into centipede form and rears up.."
        self.attack_3 = 1
        self.attack_3_phrase = "It polymorphs into bat form and darts at you with gaping jaws!."
        self.attack_4 = 3
        self.attack_4_phrase = "Croaking in disturbing malice, it swings its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "With blinding speed, it kicks with its hind claws.."
        self.introduction = f"You have encountered a {self.name}.\n" \
                            f"Its large, lidless eyes stare blankly at you as it quickly readjusts its pointed ears\n" \
                            f"with a continual twitching. Its long, serpentine tail wags with its sinews and scales\n" \
                            f"as it lets out a high pitched, fiendish and wretched cry. The air around it becomes hazy.."
        self.is_discovered = False

    name = "Quasit"


class Kobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = 25
        self.gold = self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(6, 8)
        self.dexterity = random.randint(14, 15)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(7, 8)
        self.wisdom = random.randint(7, 8)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # small
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It thrusts forward and bites with its jaws!"
        self.attack_3 = 2
        self.attack_3_phrase = "It raises its sling, in an attempt to bludgeon you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, it kicks with its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "It whips its tail!"
        self.introduction = f"You have encountered a {self.name}."
        self.is_discovered = False

    name = "Kobold"


class Cultist(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = 50
        self.gold = self.level * 373 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(10, 12)
        self.dexterity = random.randint(11, 13)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  #
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(8, 10) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "He swings his gleaming scimitar!"
        self.attack_3 = 2
        self.attack_3_phrase = "It throws an acrid powder at you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, he swings his scimitar.."
        self.attack_5 = 3
        self.attack_5_phrase = "Crying out with insane hatred, he raises his scimitar with both hands in a mighty blow!"
        self.introduction = f"You have encountered a Cultist adorned with a foul robe speckled with disgusting \n" \
                            f" symbols. With face hidden in the deep shadow of his cowl, you see his insane eyes burn\n" \
                            f"in the darkness. His loyalties long since revealed, he cries out in sworn allegiance\n " \
                            f"to some dark Quantum Manipulator..."
        self.is_discovered = False

    name = "Cultist"


class Goblin(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = self.level * 50
        self.gold = self.level * 200 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(7, 9)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(9, 11)
        self.wisdom = random.randint(7, 9)
        self.charisma = random.randint(7, 9)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 6  # mm
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its scimitar.."
        self.attack_2 = 1
        self.attack_2_phrase = "It feints to the side and swings!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its scimitar wildly!"
        self.attack_4 = 2
        self.attack_4_phrase = "It raises its scimitar overhead with both hands for a mighty blow.."
        self.attack_5 = 3
        self.attack_5_phrase = "Its scimitar flashes with impossible speed!"
        self.introduction = f"You have encountered a {self.name}."
        self.is_discovered = False

    name = "Goblin"


class WingedKobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = 50
        self.gold = self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(6, 8)
        self.dexterity = random.randint(15, 17)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(8, 10)
        self.wisdom = random.randint(6, 8)
        self.charisma = random.randint(6, 8)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # mm
        self.number_of_hd = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It thrusts forward and bites with its jaws!"
        self.attack_3 = 3
        self.attack_3_phrase = "It raises its spear!"
        self.attack_4 = 3
        self.attack_4_phrase = "It kicks with its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its spear!"
        self.introduction = f"You have encountered a {self.name}."
        self.is_discovered = False

    name = "Winged Kobold"


class Shadow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 100
        self.gold = 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(5, 6)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(12, 14)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(9, 11)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = True
        self.can_drain = False
        self.undead = True
        self.quantum_energy = True
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 2
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(15, 17)
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        # melee:
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its elongated claws..."
        self.attack_2 = 0
        self.attack_2_phrase = "It raises its arms, lost in blackness, and swings silently..wickedly.."
        self.attack_3 = 1
        self.attack_3_phrase = "It darts forward, rushing with speed, and yet without any sound.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!"
        self.attack_5 = 3
        self.attack_5_phrase = "It thrusts forward and attacks, attempting to envelope you in its dark form!!"
        self.quantum_attack_1 = 1
        self.quantum_attack_1_phrase = "Its form slithers and strikes at you with its terrible outstretched claws\n" \
                                       "in perfect silence. The quantum necrotic aura of its form sends\n" \
                                       "a shockwave through you! "
        self.quantum_attack_2 = 1
        self.quantum_attack_2_phrase = "It thrusts forward, its maw gaping with impossible blackness\n" \
                                       "as the air crackles.."
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "Its amorphous form strikes at you, unleashing terrible necrotic malice.\n" \
                                       "You feel the hairs of your body quivering.."
        self.quantum_attack_4 = 2
        self.quantum_attack_4_phrase = "With a silent scream, it releases a torrent of\n" \
                                       "quantum necrotic energy that rushes toward you!!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "Its looming form towers over you..\n" \
                                       "it clutches you with necrotic malice!"
        self.introduction = f"You have encountered a {self.name}..an unnatural abomination with form,\n " \
                            f"and yet without form.. Its body rises up, absorbing all ambient light into an\n" \
                            f"endless darkness. And yet, somehow, you intuitively catch glimpses of its actual form\n" \
                            f"beneath- impossibly long, bony, outstretched arms extending from wispy black rags,\n" \
                            f"and the hints of a humanoid, skull face, forever grimacing in confusion over its\n" \
                            f"own existence..\nYou feel the air crackle with quantum energy.."
        self.paralyze_phrase = "Rising menacingly and with both clawed, shadowy hands, it reaches out, and you\n" \
                               "feel your motor skills quivering.."
        self.is_discovered = False

    name = "Shadow"


class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 100
        self.gold = 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(9, 11)
        self.dexterity = random.randint(13, 15)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(5, 7)
        self.wisdom = random.randint(7, 9)
        self.charisma = random.randint(5, 6)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = True
        self.quantum_energy = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 1  # mm
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(11, 13) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its shortsword..."
        self.attack_2 = 1
        self.attack_2_phrase = "It raises its shortsword and swings mightily.."
        self.attack_3 = 2
        self.attack_3_phrase = "It darts forward with unnerving speed, sword in bony hand.."
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts forward with its heavy, iron spear!"
        self.attack_5 = 3
        self.attack_5_phrase = "Reaching over its back, it produces a battle axe and strikes wildly!!"
        self.introduction = f"From the ground rises a skeleton warrior. Its battle-scarred and weary weaponry still\n" \
                            f"in hand, it fearlessly hammers its shield with sword, taunting an attack. A full-toothed\n" \
                            f"grin forever emblazoned on its bony countenance, it shouts an absent, yet echoing\n" \
                            f"battle-cry at you from behind its slack, gaping jaw!\n" \
                            f"The air bristles with Quantum Energy.."
        self.is_discovered = False

    name = "Skeleton"


class Drow(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 100
        self.gold = self.level * 300 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(9, 11)
        self.dexterity = random.randint(13, 14)
        self.constitution = random.randint(9, 11)
        self.intelligence = random.randint(10, 12)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(12, 13)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = True
        self.difficulty_class = 2
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 1  # mm
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(12, 14) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It raises its shortsword.."
        self.attack_3 = 2
        self.attack_3_phrase = "It raises its flail.."
        self.attack_4 = 2
        self.attack_4_phrase = "It strikes with its shortsword with blinding speed!"
        self.attack_5 = 3
        self.attack_5_phrase = "It strikes with its shortsword with blinding speed!!"
        self.quantum_attack_1 = 2
        self.quantum_attack_1_phrase = "It releases weird quantum flames from its outstretched hand!!"
        self.quantum_attack_2 = 2
        self.quantum_attack_2_phrase = "Weird electrical energies dance over its form as it unleashes a volley\n" \
                                       "of flames and lightning from both of its outstreched hands!"
        self.quantum_attack_3 = 2
        self.quantum_attack_3_phrase = "It cries out in its own foul tongue, harnessing the quantum energies and\n" \
                                       "hurling a wall of crackling lightning toward you!"
        self.quantum_attack_4 = 3
        self.quantum_attack_4_phrase = "Placing its hands together and fidgeting wildly, it releases a growing\n" \
                                       "orb of energy which rushes straight at you!"
        self.quantum_attack_5 = 3
        self.quantum_attack_5_phrase = "Crying out wildly, it raises, and then lowers, its arms, shooting \n" \
                                       "the weirdness of entangled quantum flames and energies at you!"
        self.introduction = f"You have encountered a {self.name}."
        self.is_discovered = False

    name = "Drow"


class Troglodyte(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 50
        self.gold = 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 2
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(13, 15)
        self.dexterity = random.randint(9, 11)
        self.constitution = random.randint(13, 15)
        self.intelligence = random.randint(6, 7)
        self.wisdom = random.randint(9, 11)
        self.charisma = random.randint(5, 7)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # mm
        self.number_of_hd = 2  # mm says 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(12, 14)
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its greataxe.."
        self.attack_2 = 1
        self.attack_2_phrase = "It swings its greataxe with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its mace!"
        self.attack_4 = 2
        self.attack_4_phrase = "It thrusts mightily forward with its javelin!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its greataxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a Troglodyte. "
        self.is_discovered = False

    name = "Troglodyte"


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 100
        self.gold = 200 + round(random.uniform(1, 100)) * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(14, 16)
        self.dexterity = random.randint(11, 14)
        self.constitution = random.randint(14, 16)
        self.intelligence = random.randint(6, 8)
        self.wisdom = random.randint(10, 12)
        self.charisma = random.randint(9, 11)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        self.quantum_energy = False
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 12  # MM says should be 1d12
        self.number_of_hd = 1  # mm
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = (random.randint(11, 13)) + self.constitution_modifier
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(12, 12)
        self.attack_1 = 1  # attack bonus
        self.attack_1_phrase = "It thrusts mightily forward with its javelin!.."
        self.attack_2 = 2
        self.attack_2_phrase = "It swings its greataxe with blinding speed!"
        self.attack_3 = 2
        self.attack_3_phrase = "It swings its greataxe with blinding speed!"
        self.attack_4 = 3
        self.attack_4_phrase = "It roars and swings its greataxe with murderous rage!"
        self.attack_5 = 3
        self.attack_5_phrase = "It raises its greataxe overhead with both hands for a mighty blow.."
        self.introduction = f"You have encountered a savage Orc. Stooping forward with its piggish face " \
                            f"and prominent teeth,\nit prepares to satisfy its bloodlust by slaying any " \
                            f"humanoids that stand against it.."
        self.is_discovered = False

    name = "Orc"


class Ghoul(Monster):

    def __init__(self):
        super().__init__()
        self.level = 2
        self.experience_award = 200
        self.gold = self.level * 103 * round(random.uniform(1, 2))  # ghouls shouldn't have much gold
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(11, 12)
        self.dexterity = random.randint(12, 16)
        self.constitution = random.randint(12, 13)
        self.intelligence = random.randint(5, 10)
        self.wisdom = random.randint(7, 10)
        self.charisma = random.randint(1, 5)
        self.can_paralyze = True
        self.can_drain = False
        self.undead = True
        self.quantum_energy = False
        self.human_player_level = 0
        self.difficulty_class = 2
        self.proficiency_bonus = 1  # 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 2
        self.hit_dice = 6  # mm
        self.number_of_hd = 2  # mm
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = random.randint(20, 24) + self.constitution_modifier
        # self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier) + 1
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes with one claw.."
        self.attack_2 = 1
        self.attack_2_phrase = "It lunges and attacks with its rancid teeth!!"
        self.attack_3 = 2
        self.attack_3_phrase = "It strikes with both of its terrible claws!!"
        self.attack_4 = 2
        self.attack_4_phrase = "It rushes straight at you!!"
        self.attack_5 = 3
        self.attack_5_phrase = "It leaps upon you!!"
        self.introduction = "You have encountered a Ghoul, crouching and licking a skull. Noticing your approach,\n" \
                            "it drops the skull and rises to its feet, hissing through razor-sharp teeth and\n" \
                            "working its jagged claws. Driven by an insatiable hunger for humanoid flesh,\n " \
                            "its bulbous black eyes grow impossibly wide as it draws in its serpentine tongue. "
        self.is_discovered = False
        self.paralyze_phrase = "It lurches forward, grabbing your arm in its cold, sinewy and awful claws!"
    name = "Ghoul"


# For monster hit points..take hit dice and add (constitution modifier x number of hit dice).
# For example, if a monster has a Constitution of 12 (+1 modifier) and 2d8 Hit Dice, it has 2d8 + 2 Hit Points
# self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier)
'''def drain(self, monster_wisdom, monster_wisdom_modifier, human_player_level, human_player_wisdom,
              human_player_wisdom_modifier):
        drain_level = dice_roll(1, 20)  # need player_1 experience logic for proper drain??
        if drain_level > 17 and (monster_wisdom + monster_wisdom_modifier) > (
                human_player_wisdom + human_player_wisdom_modifier):
            # print("It drains a level!")
            level_drain = True
            return level_drain
        else:
            level_drain = False
            return level_drain'''
