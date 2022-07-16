import random
import time

from dice_roll_module import dice_roll


class Monster:

    def __init__(self):
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
        self.hit_dice = 0  # tiny d4, small d6, medium d8, large d10, huge d12, gargantuan d20
        self.number_of_hd = self.level
        self.human_player_level = 0
        self.difficulty_class = 0
        self.proficiency_bonus = 0
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

    def reduce_health(self, damage):
        self.hit_points -= damage
        return damage

    def check_dead(self):
        if self.hit_points > 0:
            return False
        else:
            return True

    def swing(self, name, level, dexterity, strength, weapon, player_level, player_hp, player_dexterity,
              player_armor_class):
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
            damage_to_opponent = round(damage_roll + self.strength_modifier + attack_bonus)
            if damage_to_opponent > 0:  # # at this point the player is the opponent!
                print(f"{attack_phrase}")
                time.sleep(1)
                print(f"{name} rolls {self.hit_dice} sided hit dice---> {damage_roll}")
                print(f"Strength modifier---> {self.strength_modifier}\nAttack bonus---> {attack_bonus}")
                print(f"It does {damage_to_opponent} points of damage!")
                time.sleep(3.5)
                return damage_to_opponent
            else:
                print(f"The {name} strikes, but you block the attack!")  # zero damage to player result
                time.sleep(2)
                return 0  # 0 points damage to player
        else:
            print(f"It missed..")
            time.sleep(2)
        return 0

    def paralyze(self, name, level, monster_wisdom, monster_wisdom_modifier, dexterity, strength, weapon,
                 human_player_level, human_player_hit_points,
                 human_player_dexterity, human_player_armor_class, human_player_wisdom,
                 human_player_wisdom_modifier):
        paralyze_chance = dice_roll(1, 20)
        if paralyze_chance == 20 or paralyze_chance > 17 and (monster_wisdom + monster_wisdom_modifier) >= (
                human_player_wisdom):
            print("You're paralyzed!!")
            time.sleep(1)
            print("As you stand, frozen and defenseless, it savagely gores you!")
            time.sleep(1)
            return True
            # damage_to_player = self.swing(name, level, dexterity, strength,
            #                              weapon,
            #                              human_player_level, human_player_hit_points, human_player_dexterity,
            #                              human_player_armor_class)
            # if damage_to_player > 0:

        else:
            print("You ignore its wiles and break free from its grip!")
            return False


class Kobold(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.experience_award = self.level * 25
        self.gold = self.level * 273 * round(random.uniform(1, 2))
        self.weapon_bonus = 0
        self.armor = 0
        self.shield = 0
        self.strength = random.randint(6, 8)
        self.dexterity = random.randint(14, 16)
        self.constitution = random.randint(8, 10)
        self.intelligence = random.randint(7, 8)
        self.wisdom = random.randint(7, 8)
        self.charisma = random.randint(7, 8)
        self.can_paralyze = False
        self.can_drain = False
        self.undead = False
        # self.human_player_level = human_player_level
        self.difficulty_class = 1
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.damage = 0
        self.challenge_rating = 1
        self.hit_dice = 4  # 12 for huge monster, 20 for gargantuan
        self.number_of_hd = self.level
        self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
        self.strength_modifier = round((self.strength - 10) / 2)
        self.constitution_modifier = round((self.constitution - 10) / 2)
        self.hit_points = self.level * (random.randint(5, 6)) + self.constitution_modifier
        # self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier) + 1
        self.dexterity_modifier = round((self.dexterity - 10) / 2)
        self.wisdom_modifier = round((self.wisdom - 10) / 2)
        self.armor_class = random.randint(11, 12)
        self.attack_1 = 0  # attack bonus
        self.attack_1_phrase = "It strikes at you with its dagger.."
        self.attack_2 = 1
        self.attack_2_phrase = "It thrusts forward and attacks with its jaws!"
        self.attack_3 = 2
        self.attack_3_phrase = "It raises its sling, in an attempt to bludgeon you!"
        self.attack_4 = 2
        self.attack_4_phrase = "With blinding speed, it kicks with its horrid claws.."
        self.attack_5 = 3
        self.attack_5_phrase = "It whips its tail!"

    name = "Kobold"

    class Ghoul(Monster):

        def __init__(self):
            super().__init__()
            self.level = 1
            self.experience_award = self.level * 90
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
            # self.human_player_level = human_player_level
            self.difficulty_class = 1
            self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
            self.damage = 0
            self.challenge_rating = 1
            self.hit_dice = 8  # 12 for huge monster, 20 for gargantuan
            self.number_of_hd = self.level
            self.proficiency_bonus = 1 + round(self.level / 4)  # 1 + (total level/4)Rounded up
            self.strength_modifier = round((self.strength - 10) / 2)
            self.constitution_modifier = round((self.constitution - 10) / 2)

            self.hit_points = self.level * (random.randint(8, 10)) + self.constitution_modifier
            # self.hit_points = dice_roll(self.number_of_hd, self.hit_dice) + (self.number_of_hd * self.constitution_modifier) + 1

            self.dexterity_modifier = round((self.dexterity - 10) / 2)
            self.wisdom_modifier = round((self.wisdom - 10) / 2)
            self.armor_class = random.randint(11, 12)
            self.attack_1 = 0  # attack bonus
            self.attack_1_phrase = "The Kobold strikes with one claw.."
            self.attack_2 = 1
            self.attack_2_phrase = "The Kobold lunges and attacks with its rancid teeth!!"
            self.attack_3 = 2
            self.attack_3_phrase = "The Kobold strikes with both of its terrible claws!!"
            self.attack_4 = 2
            self.attack_4_phrase = "The Kobold rushes straight at you!!"
            self.attack_5 = 3
            self.attack_5_phrase = "It leaps upon you!!"

        name = "Ghoul"

