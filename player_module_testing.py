import math
import random
import time
import os
from collections import Counter
import winsound
from dice_roll_module import dice_roll
from dungeons import *

# from typing_module import typing

'''Target
Identify your target to the table. 
Attack
Roll a d20. During an Attack roll, 1 always fails, and 20 always succeeds. 
Modify
Add your modifiers.  
Armor Class 
If the modified result is ≥ target’s Armor Class (AC) , the attack hits the target. 
Damage Roll Damage Dice and add modifiers. The target’s HP are reduced, factoring resistances and vulnerabilities. 
Spell Attack 
Many spells count as attacks. 
The caster rolls d20 + Spellcasting Ability Modifier + Proficiency Bonus to hit vs AC. PHB 205'''

# name0, level1, experience2, gold3, weapon_bonus4, armor5, shield6, constitution7,
# intelligence8, wisdom9, strength10, dexterity11, charisma12, hit_points13, maximum_hit_points14,
# 15is_paralyzed

'''Hit Dice: 1d10 per Fighter level
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st
In most cases, your AC will be equal to 10 + your DEX modifier + bonus from armor + bonus from magic items/effects.'''

rndm_aroma_lst = ['agarwood', 'angelica root', 'anise', 'basil', 'bergamot', 'calamodin', 'calamus', 'camphor',
                  'cardamom', 'cedar', 'camomile', 'cinnamon', 'citron', 'clary sage', 'clove', 'davana', 'eucalyptus',
                  'frankincense', 'galbanum', 'hemlock', 'jasmine', 'lavender', 'lemongrass', 'mugwort oil',
                  'pennyroyal', 'peppermint,' 'sage', 'sandalwood', 'sassafrass', 'garden mint', 'spikenard',
                  'spruce oil', 'star anise oil', 'tea tree oil', 'tarragon oil', 'tsuga', 'valerian',
                  'vanilla sweet grass', 'warionia', 'vetiver', 'wintergreen', 'yarrow oil']


def cls():
    os.system('cls')


def pause():
    os.system('pause')


def sleep(seconds):
    time.sleep(seconds)


class Weapon:

    def __init__(self):
        self.name = ""
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1

    def __repr__(self):
        return f"{self.name} - Damage Bonus: {self.damage_bonus}  To hit: {self.to_hit_bonus}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP"
    #       return self.name

    # def __str__(self):
    #    return f'{self.name} - Damage Bonus: {self.damage_bonus}  To hit: {self.to_hit_bonus}  Purchase Price: {self.buy_price} GP'


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 0
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 10
        self.minimum_level = 1


class BroadSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Broad Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = 1
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 1


class QuantumSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Sword"
        self.item_type = "Weapons"
        self.damage_bonus = 10  # 5
        self.to_hit_bonus = 5
        self.sell_price = 5000
        self.buy_price = 8000
        self.minimum_level = 5  # 3


short_sword = ShortSword()
broad_sword = BroadSword()
quantum_sword = QuantumSword()


class ShortAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Short Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 2
        self.to_hit_bonus = -1
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1


short_axe = ShortAxe()


class BattleAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Battle Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 3
        self.to_hit_bonus = 0
        self.sell_price = 5
        self.buy_price = 15
        self.minimum_level = 2


battle_axe = BattleAxe()


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Great Axe"
        self.item_type = "Weapons"
        self.damage_bonus = 4
        self.to_hit_bonus = 0
        self.sell_price = 15
        self.buy_price = 30
        self.minimum_level = 2


great_axe = GreatAxe()


class Armor:

    def __init__(self):
        self.name = ""
        self.item_type = "Armor"
        self.armor_bonus = 0
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - AC: {self.ac}  Armor bonus: {self.armor_bonus}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class PaddedArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Padded Armor"
        self.item_type = "Armor"
        self.ac = 10
        self.armor_bonus = 0
        self.sell_price = 1
        self.buy_price = 5
        self.minimum_level = 1


padded_armor = PaddedArmor()


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Leather Armor"
        self.item_type = "Armor"
        self.ac = 11
        self.armor_bonus = 0
        self.sell_price = 5
        self.buy_price = 10
        self.minimum_level = 1


leather_armor = LeatherArmor()


class StuddedLeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Studded Leather Armor"
        self.item_type = "Armor"
        self.ac = 12
        self.armor_bonus = 0
        self.sell_price = 30
        self.buy_price = 45
        self.minimum_level = 2


studded_leather_armor = StuddedLeatherArmor()


class ScaleMail(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Scale Mail"
        self.item_type = "Armor"
        self.ac = 14
        self.armor_bonus = 0
        self.sell_price = 300
        self.buy_price = 400
        self.minimum_level = 4


scale_mail = ScaleMail()


class HalfPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Half Plate Armor"
        self.item_type = "Armor"
        self.ac = 16
        self.armor_bonus = 0
        self.sell_price = 550
        self.buy_price = 750
        self.minimum_level = 6


half_plate = HalfPlate()


class FullPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Full Plate Armor"
        self.item_type = "Armor"
        self.ac = 18
        self.armor_bonus = 0
        self.sell_price = 1000
        self.buy_price = 1500
        self.minimum_level = 10


full_plate = FullPlate()


class Shield:

    def __init__(self):
        self.name = ""
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name

        # def __str__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class NoShield(Shield):  # default
    def __init__(self):
        super().__init__()
        self.name = "No Shield"
        self.item_type = "Shields"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1


no_shield = NoShield()


class Buckler(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Buckler"
        self.item_type = "Shields"
        self.ac = 1
        self.sell_price = 5
        self.buy_price = 50
        self.minimum_level = 1  # 2


buckler = Buckler()


class KiteShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Kite Shield"
        self.item_type = "Shields"
        self.ac = 2
        self.sell_price = 50
        self.buy_price = 100
        self.minimum_level = 5


kite_shield = KiteShield()


class QuantumTowerShield(Shield):
    def __init__(self):
        super().__init__()
        self.name = "Quantum Tower Shield"
        self.item_type = "Shields"
        self.ac = 3
        self.sell_price = 375
        self.buy_price = 700
        self.minimum_level = 7


quantum_tower_shield = QuantumTowerShield()


class Boots:

    def __init__(self):
        self.name = ""
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name

        # def __str__(self):
        return f'{self.name} - AC: {self.ac}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class LeatherBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Leather Boots"
        self.item_type = "Boots"
        self.ac = 0
        self.sell_price = 1
        self.buy_price = 1
        self.minimum_level = 1


leather_boots = LeatherBoots()


class ElvenBoots(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Elven Boots"
        self.item_type = "Boots"
        self.ac = 1
        self.sell_price = 30
        self.buy_price = 50
        self.minimum_level = 1


elven_boots = ElvenBoots()


class AncestralFootsteps(Boots):
    def __init__(self):
        super().__init__()
        self.name = "Ancestral Footsteps"
        self.item_type = "Boots"
        self.ac = 2
        self.sell_price = 300
        self.buy_price = 500
        self.minimum_level = 5


ancestral_footsteps = AncestralFootsteps()


class Cloak:

    def __init__(self):
        self.name = ""
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 0
        self.buy_price = 0
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name

        # def __str__(self):
        return f'{self.name} - Stealth: {self.stealth}  Minimum level: {self.minimum_level}  Purchase Price: {self.buy_price} GP'


class CanvasCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Canvas Cloak"
        self.item_type = "Cloaks"
        self.stealth = 0
        self.sell_price = 1
        self.buy_price = 0
        self.minimum_level = 1


canvas_cloak = CanvasCloak()


class ElvenCloak(Cloak):
    def __init__(self):
        super().__init__()
        self.name = "Elven Cloak"
        self.item_type = "Cloaks"
        self.stealth = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1


elven_cloak = ElvenCloak()


class Healing:
    def __init__(self):
        self.name = ""
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 0
        self.sell_price = 0
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


class Elixir:
    def __init__(self):
        self.name = "Elixir"
        self.item_type = "Elixirs"
        self.uses = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1

    def __repr__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


elixir = Elixir()


class HealingPotion(Healing):
    def __init__(self):
        super().__init__()
        self.name = "Potion of Healing"
        self.item_type = "Healing"
        self.heal_points = 0
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1


healing_potion = HealingPotion()


class StrengthPotion:
    def __init__(self):
        self.name = "Potion of Strength"
        self.item_type = "Potions of Strength"
        self.duration = 5
        self.buy_price = 50
        self.sell_price = 20
        self.minimum_level = 1

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


strength_potion = StrengthPotion()


class Regeneration:

    def __init__(self):
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1

    def __repr__(self):
        return self.name


class DefaultRingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "No Ring"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1


default_ring_of_regeneration = DefaultRingOfRegeneration()


class RingOfRegeneration(Regeneration):
    def __init__(self):
        super().__init__()
        self.name = "Ring of Regeneration"
        self.item_type = "Rings of Regeneration"
        self.regenerate = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1


ring_of_regeneration = RingOfRegeneration()


class Protection:

    def __init__(self):
        self.name = ""
        self.item_type = "Rings"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1

    def __repr__(self):
        return self.name


class DefaultRingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "No Ring"
        self.item_type = "Rings of Protection"
        self.protect = 0
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1


default_ring_of_protection = DefaultRingOfProtection()


class RingOfProtection(Protection):
    def __init__(self):
        super().__init__()
        self.name = "Ring Of Protection"
        self.item_type = "Rings of Protection"
        self.protect = 1
        self.sell_price = 10000
        self.buy_price = 10000
        self.minimum_level = 1


ring_of_protection = RingOfProtection()


class TownPortalImplements:

    def __init__(self):
        self.name = "Scroll of Town Portal"
        self.item_type = "Town Portal Implements"
        self.protect = 1
        self.sell_price = 25
        self.buy_price = 50
        self.minimum_level = 1
        self.uses = 1

    def __repr__(self):
        #        return self.name
        # def __str__(self):
        return f'{self.name} - Purchase Price: {self.buy_price} GP'


scroll_of_town_portal = TownPortalImplements()


class Player:

    def __init__(self, name):  # level, experience, gold, weapon_bonus, armor_bonus, shield, armor_class, strength,
        # dexterity,
        #  constitution, intelligence, wisdom, charisma, hit_points, maximum_hit_points, is_paralyzed, boots,
        #  cloak, weapon_name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.gold = 500000
        self.wielded_weapon = short_sword
        # self.weapon_bonus = self.wielded_weapon.damage_bonus  # self.weapon_bonus no longer used
        self.armor = padded_armor
        self.shield = no_shield
        self.boots = leather_boots
        self.armor_bonus = self.armor.armor_bonus + self.shield.ac + self.boots.ac
        self.strength = 15  # random.randint(14, 16)
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity = 14  # random.randint(13, 15)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution = 13  # random.randint(12, 14)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence = 12  # random.randint(11, 13)
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom = 10  # random.randint(9, 11)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma = 8  # random.randint(7, 9)
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)
        self.hit_dice = 10  # Hit Dice: 1d10 per Fighter level
        self.proficiency_bonus = 2  # 1 + math.ceil(self.level / 4)  # 1 + (total level/4)Rounded up
        self.maximum_hit_points = 10 + self.constitution_modifier
        self.hit_points = self.maximum_hit_points  # Hit Points at 1st Level: 10 + your Constitution modifier
        self.is_paralyzed = False
        self.cloak = canvas_cloak
        self.ring_of_prot = default_ring_of_protection
        self.ring_of_reg = default_ring_of_regeneration
        self.two_handed = False
        self.extra_attack = 0
        self.armor_class = self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac + self.dexterity_modifier
        self.stealth = self.cloak.stealth
        self.town_portals = 1
        self.elixirs = 2
        self.potions_of_healing = 1
        self.potions_of_strength = 1
        self.potion_of_strength_effect = False
        self.potion_of_strength_uses = 0
        self.poisoned = False
        self.poisoned_turns = 0
        self.necrotic = False
        self.necrotic_turns = 0
        self.dot_multiplier = 1
        self.current_dungeon_level = 1
        self.dungeon_key = 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        self.position = 0
        self.x = 0
        self.y = 0
        self.coordinates = (self.x, self.y)
        self.previous_x = 0
        self.previous_y = 0
        self.pack = {

            'Armor': [],
            'Shields': [],
            'Boots': [],
            'Weapons': [],
            'Cloaks': [],
            'Rings of Regeneration': [],
            'Rings of Protection': []
            # 'Town Portal Implements': []  # [scroll_of_town_portal]

        }

    def regenerate(self):
        if self.hit_points < self.maximum_hit_points and self.ring_of_reg.regenerate > 0:
            regeneration = self.ring_of_reg.regenerate
            self.hit_points = self.hit_points + regeneration
            if self.hit_points > self.maximum_hit_points:
                self.hit_points = self.maximum_hit_points
            print(f"You regenerate + {regeneration}")  # remove after testing
            sleep(1)
            return

    def hud(self):
        os.system('cls')
        print(f"                                                                     Name: {self.name}")
        print(f"                                                                     Level: {self.level}")
        print(f"                                                                     Experience: {self.experience}")
        print(f"                                                                     Gold: {self.gold}")
        print(
            f"                                                                     Weapon: {self.wielded_weapon.name} + {self.wielded_weapon.damage_bonus}")
        print(
            f"                                                                     To hit bonus: + {self.wielded_weapon.to_hit_bonus}")
        print(
            f"                                                                     Armor: {self.armor.name} (AC: {self.armor.ac})")

        print(
            f"                                                                     Shield: {self.shield.name} (AC: {self.shield.ac})")
        print(
            f"                                                                     Boots: {self.boots.name} (AC: {self.boots.ac})")
        print(
            f"                                                                     Your Armor Class: {self.armor_class}")
        print(
            f"                                                                     Strength: {self.strength} (Modifier: {self.strength_modifier})")
        print(
            f"                                                                     Dexterity: {self.dexterity} (Modifier: {self.dexterity_modifier})")
        print(
            f"                                                                     Constitution: {self.constitution} (Modifier: {self.constitution_modifier})")
        print(
            f"                                                                     Intelligence: {self.intelligence} (Modifier: {self.intelligence_modifier})")
        print(
            f"                                                                     Wisdom: {self.wisdom} (Modifier: {self.wisdom_modifier})")

        print(
            f"                                                                     Charisma: {self.charisma} (Modifier: {self.charisma_modifier})")
        print(f"                                                                     Hit points: {self.hit_points}/"
              f"{self.maximum_hit_points}")

        print(
            f"                                                                     Cloak: {self.cloak.name} (Stealth: {self.stealth})")
        if self.potions_of_strength > 0:
            number_of_potions_of_strength = self.potions_of_strength
            print(
                f"                                                                     Strength Potions: {number_of_potions_of_strength}")
        if self.potion_of_strength_effect:
            print(
                f"                                                                     (GIANT STRENGTH EFFECT)")
            print(
                f"                                                                     Strength Potion uses: ({self.potion_of_strength_uses}/5)")
        if self.poisoned:
            print(
                f"                                                                     (POISONED)")
            print(
                f"                                                                     Poison clarifying: ({self.poisoned_turns}/5)")
        if self.necrotic:
            print(
                f"                                                                     (NECROTIC)")
            print(
                f"                                                                     Necrotic clarifying: ({self.necrotic_turns}/5)")
        if self.potions_of_healing > 0:
            number_of_potions_of_healing = self.potions_of_healing  # len(self.pack['Healing'])
            print(
                f"                                                                     Healing Potions: {number_of_potions_of_healing}")
        if self.elixirs > 0:
            number_of_elixirs = self.elixirs  # len(self.pack['Healing'])
            print(
                f"                                                                     Elixirs: {number_of_elixirs}")
        if self.town_portals > 0:
            number_of_portal_scrolls = self.town_portals  # len(self.pack['Town Portal Implements'])
            print(
                f"                                                                     Town Portal Scrolls: {number_of_portal_scrolls}")
        if self.ring_of_reg.name != default_ring_of_regeneration.name:
            print(
                f"                                                                     Ring of Reg: +{self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != default_ring_of_protection.name:
            print(
                f"                                                                     Ring of Prot: +{self.ring_of_prot.protect}")

        return

    # CALCULATION

    def calculate_stealth(self):
        self.stealth += self.cloak.stealth

    def calculate_armor_class(self):
        self.armor_class = self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac + self.dexterity_modifier
        return

    def calculate_poison(self):
        # self.dungeon_description()
        if self.poisoned:
            if self.poisoned_turns > 4:
                self.poisoned = False
                self.poisoned_turns = 0
                print(f"The poison leaves your body..")
                pause()
            else:
                self.poisoned = True
                self.poisoned_turns += 1
                poison_damage = (1 * self.dot_multiplier)
                self.hit_points -= poison_damage
                print(f"*POISON DAMAGE: {poison_damage}*")
                sleep(1.5)
        return self.poisoned

    def calculate_necrotic_dot(self):
        # self.dungeon_description()
        if self.necrotic:
            if self.necrotic_turns > 4:
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The necrotic plague leaves your body..")
                pause()
            else:
                self.necrotic = True
                self.necrotic_turns += 1
                necrotic_damage = (1 * self.dot_multiplier)
                self.hit_points -= necrotic_damage
                print(f"*NECROTIC DAMAGE: {necrotic_damage}*")
                sleep(1.5)
        return self.necrotic

    def calculate_potion_of_strength(self):
        if self.potion_of_strength_effect:
            if self.potion_of_strength_uses > 4:
                self.potion_of_strength_effect = False
                self.potion_of_strength_uses = 0
                print(f"The potion's effects wear off....the giant strength leaves your body..")
                pause()
            else:
                self.potion_of_strength_effect = True
                self.potion_of_strength_uses += 1
        return self.potion_of_strength_effect

    def calculate_modifiers(self):
        self.strength_modifier = math.floor((self.strength - 10) / 2)
        self.dexterity_modifier = math.floor((self.dexterity - 10) / 2)
        self.constitution_modifier = math.floor((self.constitution - 10) / 2)
        self.intelligence_modifier = math.floor((self.intelligence - 10) / 2)
        self.wisdom_modifier = math.floor((self.wisdom - 10) / 2)
        self.charisma_modifier = math.floor((self.charisma - 10) / 2)

    def calculate_proficiency_bonus(self):
        if self.level <= 4:
            self.proficiency_bonus = 2
        if self.level > 4 < 9:
            self.proficiency_bonus = 3
        if self.level > 8 < 13:
            self.proficiency_bonus = 4
        if self.level > 12 < 17:
            self.proficiency_bonus = 5
        if self.level > 16:
            self.proficiency_bonus = 6
        return

    def calculate_current_level(self):
        if self.experience < 300:
            self.level = 1
        if self.experience >= 300 < 900:
            self.level = 2
        if self.experience >= 900 < 2700:
            self.level = 3
        if self.experience >= 2700 < 6500:
            self.level = 4
        if self.experience >= 6500 < 14000:
            self.level = 5
        if self.experience >= 14000 < 23000:
            self.level = 6
        if self.experience >= 23000 < 34000:
            self.level = 7
        if self.experience >= 34000 < 48000:
            self.level = 8
        if self.experience >= 48000 < 64000:
            self.level = 9
        if self.experience >= 64000 < 85000:
            self.level = 10
        if self.experience >= 85000 < 100000:
            self.level = 11
        if self.experience >= 100000 < 120000:
            self.level = 12
        if self.experience >= 120000 < 140000:
            self.level = 13
        if self.experience >= 140000 < 165000:
            self.level = 14
        if self.experience >= 165000 < 195000:
            self.level = 15
        if self.experience >= 195000 < 225000:
            self.level = 16
        if self.experience >= 225000 < 265000:
            self.level = 17
        if self.experience >= 265000 < 305000:
            self.level = 18
        if self.experience >= 305000 < 355000:
            self.level = 19
        if self.experience >= 355000:
            self.level = 20
        return

    # LEVEL AND EXPERIENCE
    def asi(self):
        # Ability Score Improvement at levels 4, 8, 12, 16, and 19.
        # Fighters gain additional ASIs at the 6th and 14th levels
        # so, 4, 6, 8, 12, 14, 16, 19

        # Define list of attributes you are allowed to change
        # ability_dict_subset_too = {1: "strength", 2: "dexterity", 3: "constitution", 4: "intelligence", 5: "wisdom",
        #                           6: "charisma"}
        if self.strength < 20 or self.dexterity < 20 or self.constitution < 20 or self.intelligence < 20 or self.wisdom < 20 or self.charisma < 20:
            os.system('cls')
            print(f"         *Ability Score Improvement*")
            print()
            print(
                f"You may choose to improve a single ability score, such as strength, \n"
                f"and increase it by 2 points.\n"
                f"\n"
                f"                     *OR*\n"
                f"\n"
                f"You may choose to improve two ability scores, such as charisma and constitution, by 1 point each.\n"
                f"\n"
                f"NOTES: \n"
                f"Ability *modifiers* improve with each ascending even-numbered score, therefore, if unsure,\n"
                f"it is generally recommended to apply 1 point to odd-numbered ability scores and apply \n"
                f"2 points to even-numbered scores.\n"
                f"\n"
                f"    *The maximum score for any ability is 20*"
                f"\n")
            pause()

            while True:
                self.hud()
                tries = 0
                points = 2
                while True:
                    self.hud()
                    # print(f"Ability Score Improvement for level {self.level}")

                    if tries > 1:
                        print(f"You savor the empowering abilities you have gained..\n"
                              f"And yet, the dungeon horde grows more powerful with you!")
                        return

                    ability_dict = self.__dict__  # create variable as actual copy of player dict attribute

                    ability_lst = []
                    # the working dict and 'for' loop just takes the place of many 'if:' statements
                    working_dict = {'strength': self.strength, 'dexterity': self.dexterity,
                                    'constitution': self.constitution, 'intelligence': self.intelligence,
                                    'wisdom': self.wisdom, 'charisma': self.charisma}
                    # add all abilities < 20 in working dict to ability list
                    for key, value in working_dict.items():
                        if value < 20:
                            ability_lst.append(key)

                    # this code should be reachable if stats are maxed out, and player level_up calls it
                    if not len(ability_lst):  # if ability list is empty, all stats at 20; no more improvements allowed
                        print(f"All of your abilities are at the maximum level!")
                        # pause()
                        return
                    print(f"Ability Score Improvement for level {self.level}")
                    print(f"Points to distribute: {points}")
                    # create a subset ability dictionary from the ability list by indexing, and then print out
                    ability_dict_subset_too = {}
                    for ability in ability_lst:
                        if len(ability_lst):
                            ability_dict_subset_too[ability_lst.index(ability)] = ability
                    for key, value in ability_dict_subset_too.items():
                        print(key + 1, ':', value.capitalize())  # add 1 to key since indexing begins at 0
                    try:
                        ability_index = int(input(f"Enter the ability to improve.\n"
                                                  f"(THIS IS PERMANENT!) : "))
                        #
                        ability_index -= 1  # indexing begins at zero...
                        ability_to_improve = (ability_dict_subset_too[ability_index])
                        old_score = ability_dict[ability_to_improve]
                        ability_dict[ability_to_improve] += 1
                        print(
                            f"Your {ability_to_improve} has been increased from {old_score} "
                            f"to {ability_dict[ability_to_improve]}!")
                        self.calculate_modifiers()
                        tries += 1
                        points -= 1
                        pause()
                        continue
                    except (ValueError, KeyError):
                        print("Invalid entry..")
                        sleep(1)
                        continue
        else:
            print(f"All abilities at maximum!")  # remove after testing
            return

    # def increase_experience(self, exp_award):
    #   self.experience += exp_award  # this should be redundant now
    #    return

    def level_up(self, exp_award, monster_gold):
        # *****************
        self.gold += monster_gold
        before_level = self.level
        before_proficiency_bonus = self.proficiency_bonus
        self.experience += exp_award
        self.calculate_current_level()
        self.calculate_proficiency_bonus()
        after_proficiency_bonus = self.proficiency_bonus
        after_level = self.level
        if after_level > before_level:
            print(f"You snarf {monster_gold} gold pieces and gain {exp_award} experience points.")
            sleep(2)
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\SOUNDS\\GONG\\gong.wav', winsound.SND_ASYNC)
            print(f"You went up a level!!")
            sleep(2)
            print(f"You are now level {self.level}.")
            sleep(2)
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\creepy_dungeon_theme.wav',
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
            self.calculate_proficiency_bonus()  # according to DnD 5e
            gain_hit_points = dice_roll(1, self.hit_dice) + self.constitution_modifier
            if gain_hit_points < 1:
                gain_hit_points = 1
            self.hit_points += gain_hit_points  # you heal and gain max hp (previous HP + Hit Die roll + CON modifier)
            self.maximum_hit_points += gain_hit_points
            print(f"You heal, and gain {gain_hit_points} maximum hit points")
            sleep(2)
            # Ability Score Improvement at levels 4, 8, 12, 16, and 19.
            # Fighters gain additional ASIs at the 6th and 14th levels
            # so, 4, 6, 8, 12, 14, 16, 19
            if self.level == 4 or self.level == 6 or self.level == 8 or self.level == 12 \
                    or self.level == 14 or self.level == 16 or self.level == 19:
                self.asi()  # Ability Score Improvement calls calculate modifiers, so
            self.calculate_modifiers()  # you may want to remove this call to calculate modifiers
            if self.level == 5:
                print(
                    "You gain the Extra Attack skill!!")  # this works automatically in battle loop if level > 4, but change this to be a boolean attribute
                sleep(2)
            if after_proficiency_bonus > before_proficiency_bonus:
                print(f"Your proficiency bonus increases from {before_proficiency_bonus} to {after_proficiency_bonus}!")
                sleep(2)
            # self.ring_of_reg  ADD RING LOGIC...UP WITH EACH LEVEL ?
            self.hud()
        else:
            print(f"You snarf {monster_gold} gold pieces and gain {exp_award} experience points")
            sleep(2)
            self.hud()

    # BATTLE AND PROXIMITY TO MONSTER OCCURRENCES

    def monster_likes_you(self, monster_name, monster_intel):
        if dice_roll(1, 20) > 17 and monster_intel > 8 and self.charisma > 10:
            print(f"The {monster_name} likes you!")
            sleep(1)
            gift_item = dice_roll(1, 3)
            if gift_item == 1:
                self.armor.ac += 1
                self.calculate_armor_class()
                # self.armor_class = self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac + self.dexterity_modifier
                print(f"He enhances your armor to AC {self.armor.ac}!")
                pause()
                return True
            if gift_item == 2:
                if self.shield.name != no_shield.name:
                    self.shield.ac += 1
                    self.calculate_armor_class()
                    # self.armor_class = self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac + self.dexterity_modifier
                    print(f"He enhances your shield to AC {self.shield.ac}!")
                else:
                    self.shield = buckler
                    print(f"He gives you a {self.shield.name}!")
                    self.calculate_armor_class()
                pause()
                return True
            if gift_item == 3:
                self.wielded_weapon.damage_bonus += 1
                # *****ADD LOGIC TO APPEND PREFIX TO WEAPON NAME, LIKE, 'ENHANCED', ETC *******************************
                print(f"He enhances your weapon damage bonus to + {self.wielded_weapon.damage_bonus}!")
                pause()
                return True

        else:
            return False

    def quick_move(self, monster_name):
        self.hud()
        quick_move_roll = dice_roll(1, 20)  # - self.stealth
        # player_initiative_roll = dice_roll(1, 20)
        if quick_move_roll == 20:
            print(f"The {monster_name} makes a quick move...")
            sleep(1.5)
            # pack inventory logic:
            available_item_types_to_steal = []
            for i in self.pack.keys():  # gather all available
                if len(self.pack[i]) > 0:  # item types to steal based on player's current item TYPES and put them
                    available_item_types_to_steal.append(i)  # in available_item_types_to_steal = []
                    # **** REMARKED FOLLOWING LINE AND DROPPED IT DOWN TO if len(available_item_types_to_steal) > 0:
                    # **** TO ADDRESS REFERENCED BEFORE ASSIGNMENT WARNING ****
                    # item_type = random.choice(available_item_types_to_steal)  # Get an item *TYPE* you want to "steal"
            if len(available_item_types_to_steal) > 0:
                item_type = random.choice(available_item_types_to_steal)  # Get random item *TYPE* you want to "steal"
                if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type"
                    # pop random item from that item type. -1 because indexes start at 0
                    stolen_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                    print(f"He steals a {stolen_item.name}")  # from your {item_type}")
                    pause()
                    return True  # True means monster gets away clean

            # Belt inventory is handled differently. This is clunky but should work.
            # belt inventory logic:
            elif self.potions_of_strength > 0 or self.potions_of_healing > 0 or self.town_portals > 0 or self.elixirs > 0:
                item_string = ""
                # Define list of attributes you are allowed to change
                self_dict = self.__dict__  # create variable as actual copy of player dict attribute
                stealing_lst = []
                # the working dict and 'for' loop just takes the place of many 'if:' statements
                working_dict = {'potions_of_strength': self.potions_of_strength,
                                'potions_of_healing': self.potions_of_healing,
                                'town_portals': self.town_portals, 'elixirs': self.elixirs}

                # add all items > 0 in working dict to stealing list
                for key, value in working_dict.items():
                    if value > 0:
                        stealing_lst.append(key)
                random_stolen_item = random.choice(stealing_lst)
                # I am proud of this next bit of code :)
                grammar_dict = {'potions_of_strength': 'potion of strength',
                                'potions_of_healing': 'potion of healing',
                                'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir'}
                for key, value in grammar_dict.items():
                    if random_stolen_item == key:
                        item_string = value
                print(f"It steals a {item_string} right off of your belt!")
                self_dict[random_stolen_item] -= 1
                pause()
                return True  # True means monster gets away clean
            else:
                print("You have nothing he wants to steal!")
                pause()
                # sleep(2)
                return True  # Changing this to False means your inventory is empty and monster sticks around to fight
        else:
            return False  # False here means monster failed check, and he sticks around to fight; invisible to player

    def damage_while_paralyzed(self, monster_number_of_hd, monster_hit_dice):
        paralyze_damage = dice_roll(monster_number_of_hd, monster_hit_dice)
        self.reduce_health(paralyze_damage)
        print(f"You suffer {paralyze_damage} hit points!!")
        pause()

    def reduce_health(self, damage):
        self.hit_points -= damage
        return  # damage

    def check_dead(self):
        # I am proud of this code...it was very difficult for me and took many hours
        if self.hit_points > 0:
            return False
        else:
            # return True
            self.hud()
            if self.necrotic:
                necrotic = "necrotic,"
            else:
                necrotic = ""
                # print(f"NECROTIC")
            if self.poisoned:
                poisoned = "poisoned,"
            else:
                poisoned = ""
            print(f"You are {necrotic} {poisoned} unconscious and moribund!")
            sleep(1)
            print(f"Death saving throw!")
            sleep(1)
            successes = 0
            fails = 0
            attempt = 0
            while successes < 3 or fails < 3:
                if successes == 3:
                    print(f"You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False
                if fails >= 3:
                    print(f"Death saving throw failed!")
                    sleep(1)
                    return True
                death_save = dice_roll(1, 20)
                attempt += 1
                print(f"Attempt {attempt}: {death_save}")
                sleep(1)
                if death_save == 20:
                    print(f"20 Roll! You are revived!")
                    sleep(1)
                    self.hit_points = 1
                    return False
                if death_save > 9:
                    successes += 1
                    print(f"{successes} Successful saves..")
                    sleep(1)
                if 10 > death_save > 1:
                    fails += 1
                    print(f"{fails} Failed saves..")
                    sleep(1)
                if death_save == 1:
                    fails += 2
                    print(f"Rolling a 1 adds 2 failed saves. ")
                    print(f"{fails} Failed saves..")
                    sleep(1)
            return True  # player IS dead

    def poison_attack(self, monster_name, monster_dot_multiplier):
        challenge_rating = self.constitution
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {monster_name} hisses in evil glee..")
        print(f"Attack roll---> {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You dodge!")
            sleep(1)
            print(f"And you perceive it was attempting to poison you!")
            pause()
            self.hud()
            return False
        else:
            print(f"Your Constitution: {self.constitution}\nYour Constitution Modifier: {self.constitution_modifier}\n")
            if roll_d20 == 20 or roll_d20 >= challenge_rating:  # self.constitution + self.constitution_modifier:
                # return True
                # self.hud()
                self.dot_multiplier = monster_dot_multiplier
                rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                         "An unnerving frailty spreads throughout your body...",
                                         "Pain and tenderness courses through your body.."
                                         ]
                poisoned_phrase = random.choice(rndm_poisoned_phrases)
                print(f"{poisoned_phrase}")
                sleep(1.5)
                print(f"You have been poisoned!")
                self.poisoned = True
                self.poisoned_turns = 0
                # self.calculate_poison()
                pause()
                # self.dungeon_description()
                # self.hud()
                return self.poisoned
            else:
                print(f"You swiftly dodge its poison attack!")
                sleep(1)
                pause()
                self.hud()
                return False

    def necrotic_attack(self, monster_name, monster_dot_multiplier):
        challenge_rating = self.constitution + self.constitution_modifier
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"The {monster_name} harnesses its innate understanding of quantum natures..")
        print(f"Attack roll---> {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You dodge the deadly necrotic attack!")
            sleep(1)
            pause()
            self.hud()
            return False
        else:
            print(f"Your Constitution: {self.constitution}\nYour Constitution Modifier: {self.constitution_modifier}\n")
            if roll_d20 == 20 or roll_d20 >= challenge_rating:  # self.constitution + self.constitution_modifier:
                self.dot_multiplier = monster_dot_multiplier
                # self.hud()
                rndm_necrotic_phrases = ["You feel morbid dread and withering overcoming you..",
                                         "An unnerving pain, planted like a seed, germinates within you...",
                                         "Agony creeps into your very veins..."
                                         ]
                necrotic_phrase = random.choice(rndm_necrotic_phrases)
                print(f"{necrotic_phrase}")
                sleep(1.5)
                print(f"Necrotic forces ravage through your body!")
                self.necrotic = True
                self.necrotic_turns = 0
                pause()
                self.hud()
                return self.necrotic
            else:
                print(f"You swiftly dodge its death-dealing necrotic attack!")
                sleep(1)
                pause()
                self.hud()
                return False

    def swing(self, monster_name, monster_armor_class):
        # add evade logic
        strength_bonus = 1
        if self.potion_of_strength_effect:
            strength_bonus = 1.5  # round(self.strength * .5)
        self.hud()
        roll_d20 = dice_roll(1, 20)  # attack roll
        print(f"You strike at the {monster_name}..")
        print(f"Attack roll---> {roll_d20}")
        sleep(1)
        if roll_d20 == 1:
            print("You missed.")
            print(f"You rolled a 1. 1 means failure..")
            pause()
            self.hud()
            return 0
        if roll_d20 == 20:
            critical_bonus = 2
            hit_statement = "CRITICAL HIT!!"

        else:
            critical_bonus = 1
            hit_statement = "You hit!"
        print(f"Dexterity modifier {self.dexterity_modifier}\nProficiency bonus {self.proficiency_bonus}\n"
              f"Weapon to hit bonus {self.wielded_weapon.to_hit_bonus}")
        print(f"Monster armor class {monster_armor_class}")
        if roll_d20 == 20 or roll_d20 + self.proficiency_bonus + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus >= monster_armor_class:
            damage_roll = dice_roll((self.level * critical_bonus), self.hit_dice)

            damage_to_opponent = math.ceil(
                (damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus) * strength_bonus)
            if damage_to_opponent > 0:
                print(hit_statement)
                sleep(1)
                print(
                    f"{self.level * critical_bonus}d{self.hit_dice} roll ---> {damage_roll} + weapon bonus "
                    f"({self.wielded_weapon.damage_bonus}) + "
                    f"Strength modifier ({self.strength_modifier}) * Strength Bonus ({strength_bonus}) = {damage_to_opponent} (rounded)")
                print(f"You do {damage_to_opponent} points of damage!")
                pause()
                self.hud()
                return damage_to_opponent
            else:
                print(f"It blocks!")  # zero damage result
                sleep(1)
                return 0
        elif self.level > 4:
            print("You missed..")
            sleep(2)
            print("Extra Attack Skill chance to hit!")
            sleep(2)
            roll_d20 = dice_roll(1, 20)
            if roll_d20 == 20 or roll_d20 + self.proficiency_bonus + self.dexterity_modifier + self.wielded_weapon.to_hit_bonus >= monster_armor_class:
                damage_roll = dice_roll(self.level, self.hit_dice)
                damage_to_opponent = math.ceil(
                    damage_roll + self.strength_modifier + self.wielded_weapon.damage_bonus) + 1
                print(f"You manage to attack for {damage_to_opponent} points of damage!")
                sleep(2)
                self.hud()
                return damage_to_opponent
            else:
                print("You miss again.")
                sleep(1)
                return 0
        else:
            print(f"You missed...")
            pause()
            self.hud()
            return 0

    def evade(self, monster_name, monster_dexterity):
        print(f"You attempt an evasive maneuver..")
        sleep(1)
        evade_success = dice_roll(1, 20)
        if evade_success + self.dexterity_modifier + self.stealth >= monster_dexterity or evade_success == 20:
            print(f"You successfully evade the {monster_name}!")
            pause()
            return True
        else:
            print(f"The {monster_name} swiftly blocks your escape!")
            time.sleep(.5)
            print(f"You are rooted to the spot. You must stand your ground!")
            time.sleep(1)
            self.hud()
            print(f"You raise your {self.wielded_weapon.name}..")
            time.sleep(1.5)
            return  # False

    # INVENTORY AND ITEMS

    def chemist_main(self):

        while True:
            self.hud()
            rndm_aroma = random.choice(rndm_aroma_lst)
            print(f"Jahns, the Fieldenberg quantum chemist is here, busying himself at the crucible.\n"
                  f"Mortars and pestles litter the counter and the smell of {rndm_aroma} fills the air...")
            if self.hit_points < self.maximum_hit_points:
                print("The aura fills your nostrils and lungs...healing you to full strength!")
                self.hit_points = self.maximum_hit_points
                pause()
                self.hud()
            print(f"Your gold: {self.gold} GP")
            chemist_choice = input(
                "(P)urchase items, (S)ell quantum items, Display your (I)nventory, or (E)xit the chemist: ").lower()
            if chemist_choice not in ('p', 's', 'i', 'e'):
                continue
            elif chemist_choice == 'p':
                self.buy_chemist_items()
                continue
            elif chemist_choice == 's':
                self.sell_chemist_items()
                continue
            elif chemist_choice == 'i':
                self.inventory()
                continue
            elif chemist_choice == 'e':
                return
            else:
                continue

    def sell_chemist_items(self):

        while True:
            self.hud()
            if self.potions_of_healing == 0 and self.town_portals == 0 and self.potions_of_strength == 0:
                print(f"You have no quantum items to sell..")
                pause()
                return
            print(f"You currently carry the following quantum items:")
            print(f"1: Potions of Healing - Quantity: {self.potions_of_healing}")
            print(f"2: Scrolls of Town Portal - Quantity: {self.town_portals}")
            print(f"3: Potions of Strength - Quantity: {self.potions_of_strength}")
            print(f"4: Clarifying Elixirs - Quantity: {self.elixirs}")
            print(f"Your gold: {self.gold} GP")
            sell_or_not = input(f"(S)ell items or go (B)ack: ").lower()
            if sell_or_not == 'b':
                return
            elif sell_or_not == 's':
                type_to_sell = input(f"Enter the category of item you wish to sell: ")

                if type_to_sell == '1':
                    your_item = "potions"
                    if self.potions_of_healing < 1:
                        print(f"You don't have any {your_item}..")
                        sleep(1)
                        continue

                elif type_to_sell == '2':
                    your_item = "scrolls of town portal"
                    if self.town_portals < 1:
                        print(f"You don't have any {your_item}..")
                        sleep(1)
                        continue
                elif type_to_sell == '3':
                    your_item = "potions of strength"
                    if self.potions_of_strength < 1:
                        print(f"You don't have any {your_item}..")
                        sleep(1)
                        continue
                elif type_to_sell == '4':
                    your_item = "clarifying elixirs"
                    if self.elixirs < 1:
                        print(f"You don't have any {your_item}..")
                        sleep(1)
                        continue
                else:
                    print(f"Invalid..")
                    continue

                try:
                    number_of_items_to_sell = int(input(f"Enter number of {your_item} to sell: "))
                    if type_to_sell == '1' and number_of_items_to_sell > 0:
                        if self.potions_of_healing >= number_of_items_to_sell:
                            self.potions_of_healing -= number_of_items_to_sell
                            gold_recieved = (healing_potion.sell_price * number_of_items_to_sell)
                            self.gold += gold_recieved
                            print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                            pause()
                            continue
                        else:
                            print(f"Invalid.")
                            sleep(1)
                            continue
                    elif type_to_sell == '2' and number_of_items_to_sell > 0:
                        if self.town_portals >= number_of_items_to_sell:
                            self.town_portals -= number_of_items_to_sell
                            gold_recieved = (scroll_of_town_portal.sell_price * number_of_items_to_sell)
                            self.gold += gold_recieved
                            print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                            pause()
                            continue
                        else:
                            print(f"Invalid.")
                            sleep(1)
                            continue
                    elif type_to_sell == '3' and number_of_items_to_sell > 0:
                        if self.potions_of_strength >= number_of_items_to_sell:
                            self.potions_of_strength -= number_of_items_to_sell
                            gold_recieved = (strength_potion.sell_price * number_of_items_to_sell)
                            self.gold += gold_recieved
                            print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                            pause()
                            continue
                        else:
                            print(f"Invalid.")
                            sleep(1)
                            continue
                    elif type_to_sell == '4' and number_of_items_to_sell > 0:
                        if self.elixirs >= number_of_items_to_sell:
                            self.elixirs -= number_of_items_to_sell
                            gold_recieved = (elixir.sell_price * number_of_items_to_sell)
                            self.gold += gold_recieved
                            print(f"You sell {number_of_items_to_sell} {your_item} for {gold_recieved} GP.")
                            pause()
                            continue
                        else:
                            print(f"Invalid.")
                            sleep(1)
                            continue
                    else:
                        print(f"Invalid entry..")
                except ValueError:
                    print("Invalid input")
                    continue

    def buy_chemist_items(self):

        chemist_dict = {
            'Healing': [healing_potion],
            'Potions of Strength': [strength_potion],
            'Town Portal Implements': [scroll_of_town_portal],
            'Elixirs': [elixir]
        }
        while True:
            self.hud()
            print(f"Jahns has items for sale in the following categories:")
            # create a list of item types:
            item_type_lst = list(chemist_dict.keys())
            # create a dictionary from list of item types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Display your (I)nventory, (P)ick item type, or go (B)ack: ").lower()
            if buy_or_exit not in ('i', 'p', 'b'):
                self.hud()
                continue
            elif buy_or_exit == 'i':
                self.inventory()
                continue
            elif buy_or_exit == 'b':
                return
                # break
            elif buy_or_exit == 'p':
                try:
                    item_type_index_to_buy = int(input(f"Enter the category of the item to buy by number: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    chemist_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (chemist_dict[item_type_to_buy]):
                        item_dict[item] = (chemist_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Display your (I)nventory, (P)ick item by number, or go (B)ack: ").lower()
                    if buy_or_exit not in ('i', 'p', 'b'):
                        self.hud()
                        continue
                    elif buy_or_exit == 'i':
                        self.inventory()
                        continue
                    elif buy_or_exit == 'b':
                        break
                    elif buy_or_exit == 'p':
                        try:
                            item_index_to_buy = int(
                                input(f"Enter the number of the item you wish to consider for purchase: "))
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (chemist_dict[item_type_to_buy])[item_index_to_buy]
                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        # confirm_purchase = input(f"Purchase {sale_item.name} for {sale_item.buy_price} GP (y/n)? ")
                        # if confirm_purchase == 'y':

                        try:
                            number_of_items = int(input(f"How many would you like to buy: "))
                        except ValueError:
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        if number_of_items > 0:
                            purchase_price = sale_item.buy_price * number_of_items
                            if self.gold >= purchase_price:
                                if self.level >= sale_item.minimum_level:
                                    self.gold -= purchase_price
                                    # replace these if statements with dictionary in future
                                    if sale_item.name == 'Scroll of Town Portal':
                                        self.town_portals += number_of_items
                                    elif sale_item.name == 'Potion of Strength':
                                        self.potions_of_strength += number_of_items
                                    elif sale_item.name == 'Potion of Healing':
                                        self.potions_of_healing += number_of_items
                                    elif sale_item.name == 'Elixir':
                                        self.elixirs += number_of_items
                                    self.hud()
                                    print(f"You buy {number_of_items} {sale_item.name}s")
                                    # (self.pack[sale_item.item_type]).append(sale_item)
                                    self.item_type_inventory(sale_item.item_type)
                                    pause()
                                    continue
                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            print(f"Zero..")
                            continue

    def item_management_sub_menu(self):
        while True:
            self.hud()
            item_to_manage = input(
                f"Manage (W)eapons, (A)rmor, (S)hields, (B)oots, (C)loaks, View your (I)nventory, or (E)xit: ")
            if item_to_manage == 'w':
                self.item_management('Weapons', self.wielded_weapon)
                # self.weapon_management()
                continue

            elif item_to_manage == 'a':
                self.item_management('Armor', self.armor)
                continue

            elif item_to_manage == 's':
                self.item_management('Shields', self.shield)
                continue
            elif item_to_manage == 'b':
                self.item_management('Boots', self.boots)
                continue
            elif item_to_manage == 'c':
                self.item_management('Cloaks', self.cloak)
                continue
            elif item_to_manage == 'i':
                self.inventory()
                continue
            elif item_to_manage == 'e':
                return
            else:
                continue

    def blacksmith_main(self):

        while True:
            # you can make this into a dictionary, with each value being a function
            # something like
            # if blacksmith_choice in blacksmith_main_dict:
            #   blacksmith_function = (blacksmith_main_dict[blacksmith_choice])
            #   blacksmith_function()
            # elif blacksmith_choice == 'e':
            #   return
            self.hud()
            print(f"Lucino, the Fieldenberg blacksmith is here, hammering at his anvil.\n"
                  f"He notices you, grumbles, and continues hammering...")
            print(f"Your gold: {self.gold} GP")
            blacksmith_choice = input(
                "(P)urchase items, (L)iquidate items, (M)anage your inventory items, View (I)nventory, or (E)xit the blacksmith: ").lower()
            if blacksmith_choice == 'p':
                self.buy_blacksmith_items()
                continue
            elif blacksmith_choice == 'l':
                self.sell_blacksmith_items()
                continue
            elif blacksmith_choice == 'm':
                self.item_management_sub_menu()
            elif blacksmith_choice == 'i':
                self.inventory()
                continue
            elif blacksmith_choice == 'e':
                return
            else:
                continue

    def buy_blacksmith_items(self):

        blacksmith_dict = {
            'Weapons': [short_axe, broad_sword, quantum_sword, battle_axe, great_axe],
            'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
            'Shields': [buckler, kite_shield, quantum_tower_shield],
            'Boots': [elven_boots, ancestral_footsteps],
            'Cloaks': [elven_cloak]
        }
        while True:
            self.hud()
            print(f"Armory for sale:")
            # create a list of blacksmith item types:
            item_type_lst = list(blacksmith_dict.keys())
            # create a dictionary from list of blacksmith items types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            buy_or_exit = input("Display your (I)nventory, (P)ick item type, or go (B)ack: ").lower()
            if buy_or_exit not in ('i', 'p', 'b'):
                self.hud()
                continue
            elif buy_or_exit == 'i':
                self.inventory()
                continue
            elif buy_or_exit == 'b':
                return
            elif buy_or_exit == 'p':
                try:
                    item_type_index_to_buy = int(input(f"Enter the number of the category of the item to buy: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
                while True:
                    self.hud()
                    print(f"{item_type_to_buy} for sale:")
                    item_dict = {}
                    blacksmith_dict[item_type_to_buy].sort(key=lambda x: x.buy_price)
                    for item in (blacksmith_dict[item_type_to_buy]):
                        item_dict[item] = (blacksmith_dict[item_type_to_buy]).index(item)
                    for key, value in item_dict.items():
                        print(value + 1, ':', key)
                    print(f"Your gold: {self.gold} GP")
                    buy_or_exit = input("Display your (I)nventory, (P)ick item by number, or go (B)ack: ").lower()
                    if buy_or_exit not in ('i', 'p', 'b'):
                        self.hud()
                        continue
                    elif buy_or_exit == 'i':
                        self.inventory()
                        continue
                    elif buy_or_exit == 'b':
                        break
                    elif buy_or_exit == 'p':
                        try:
                            item_index_to_buy = int(
                                input(f"Enter the number of the item you wish to consider for purchase: "))
                            item_index_to_buy -= 1  # again, indexing starts at 0 and is awkward
                            sale_item = (blacksmith_dict[item_type_to_buy])[item_index_to_buy]
                        except (IndexError, ValueError):
                            print("Invalid entry..")
                            sleep(1)
                            continue
                        confirm_purchase = input(f"Purchase {sale_item.name} for {sale_item.buy_price} GP (y/n)? ")
                        if confirm_purchase == 'y':
                            if self.gold >= sale_item.buy_price:
                                if self.level >= sale_item.minimum_level:
                                    if not self.duplicate_item(sale_item.item_type, sale_item):
                                        self.hud()
                                        print(f"You buy the {sale_item.name}")
                                        self.gold -= sale_item.buy_price
                                        (self.pack[sale_item.item_type]).append(sale_item)
                                        self.item_type_inventory(sale_item.item_type)
                                        pause()
                                        continue
                                    else:
                                        print(f"You already have a {sale_item.name}")
                                        pause()
                                        continue
                                else:
                                    print(f"Minimum requirements not met.")
                                    pause()
                                    continue
                            else:
                                print("You do not have enough gold.")
                                pause()
                                continue
                        else:
                            continue

    def item_management(self, item_type, current_item):
        self.hud()
        if len(self.pack[item_type]) > 0:
            print(f"Your current {item_type} inventory:")
            (self.pack[item_type]).sort(key=lambda x: x.buy_price)
            item_mgmt_dict = {}
            for item in (self.pack[item_type]):
                item_mgmt_dict[item] = (self.pack[item_type]).index(item)
            for key, value in item_mgmt_dict.items():
                print(value + 1, ':', key)  # value is index. indexing starts at zero, so add 1
            print()
        else:
            print(f"You have nothing in your {item_type} inventory..")
            pause()
            return
        old_item = current_item
        print(f"You are currently using: ")
        if item_type == 'Weapons':
            print(f"{self.wielded_weapon}, Sell Price: {self.wielded_weapon.sell_price} GP")

        elif item_type == 'Armor':
            print(f"{self.armor}, Sell Price: {self.armor.sell_price} GP")

        elif item_type == 'Shields':
            if self.shield.name != 'No Shield':
                print(f"{self.shield}, Sell Price: {self.shield.sell_price} GP")
            else:
                print(f"{self.shield.name}")
        elif item_type == 'Boots':
            print(f"{self.boots}, Sell Price: {self.boots.sell_price} GP")

        elif item_type == 'Cloaks':
            print(f"{self.cloak}, Sell Price: {self.cloak.sell_price} GP")
        swap_or_exit = input(f"(S)wap item, or go (B)ack: ").lower()
        if swap_or_exit == "b":
            return
        elif swap_or_exit == "s":
            try:
                new_item_index = int(input(f"Enter the number of the item from your inventory that you wish to use: "))
                new_item_index -= 1  # again, indexing starts at 0 so add 1
                if item_type == 'Weapons':
                    new_weapon = (self.pack[item_type])[new_item_index]  # SYNTAX FOR INDEX
                    print(f"{new_weapon}")
                    self.wielded_weapon = new_weapon
                elif item_type == 'Armor':
                    new_armor = (self.pack[item_type])[new_item_index]
                    print(f"{new_armor}")
                    self.armor = new_armor
                elif item_type == 'Shields':
                    new_shield = (self.pack[item_type])[new_item_index]
                    print(f"{new_shield}")
                    self.shield = new_shield
                elif item_type == 'Boots':
                    new_boots = (self.pack[item_type])[new_item_index]
                    print(f"{new_boots}")
                    self.boots = new_boots
                elif item_type == 'Cloaks':
                    new_cloak = (self.pack[item_type])[new_item_index]
                    print(f"{new_cloak}")
                    self.cloak = new_cloak
                # CALCULATE STEALTH AND ARMOR CLASS. NOTICE INDENT
                self.calculate_stealth()
                self.calculate_armor_class()
            except (IndexError, ValueError):
                print("Invalid entry..")
                sleep(1)
                return
            print(f"You are now using the {(self.pack[item_type])[new_item_index]}.")
            if old_item.name != 'No Shield':
                print(f"You place the {old_item.name} in your inventory.")
                (self.pack[item_type]).pop(new_item_index)  # INDEX SYNTAX
                (self.pack[item_type]).append(old_item)  # old_weapon represents an object, not an index
                # (self.pack[item_type]).sort(key=lambda x: x.buy_price)
                pause()
            else:
                print(f"You are well equipped.")
                pause()

    def sell_blacksmith_items(self):

        while True:
            cls()
            # self.hud()
            print(f"You have items eligible to sell in the following categories:")
            non_empty_item_type_lst = []
            # make a list of non-empty inventory item keys from player's inventory
            for key in self.pack:
                if len(self.pack[key]) > 0:
                    non_empty_item_type_lst.append(key)
            if len(non_empty_item_type_lst) < 1:
                print(f"Your inventory is empty")
                pause()
                return
            else:
                # print(non_empty_item_type_lst)  # remove after testing
                # make a dictionary from the non_empty item type list. index, and print
                item_type_dict = {}
                for item_type in self.pack:
                    if len(self.pack[
                               item_type]) and item_type != 'Rings of Protection' and item_type != 'Rings of Regeneration':
                        item_type_dict[item_type] = non_empty_item_type_lst.index(item_type)
                for key, value in item_type_dict.items():
                    print(value + 1, ':', key)

                try:
                    print(f"Your gold: {self.gold} GP")
                    sell_or_exit = input("(S)ell, (L)iquidate entire armory, or go (B)ack: ").lower()
                    if sell_or_exit not in ('s', 'l', 'b'):
                        cls()
                        # self.hud()
                        continue
                    if sell_or_exit == 'l':
                        self.sell_everything()
                        return
                    if sell_or_exit == 'b':
                        break
                    item_type_index_to_sell = int(input(f"Enter the number of the category of the item to sell: "))
                    item_type_to_sell = non_empty_item_type_lst[item_type_index_to_sell - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue
            while True:
                cls()
                # self.hud()
                persistent_item_type = item_type_to_sell
                print(f"Your {item_type_to_sell} inventory eligible for sale:")
                # self.item_type_inventory(item_type_to_sell)
                sell_all = []
                mgmt_dict = {}
                for item in (self.pack[item_type_to_sell]):
                    mgmt_dict[item] = (self.pack[item_type_to_sell]).index(item)
                for key, value in mgmt_dict.items():
                    print(value + 1, ':', key.name, '- Sell price:', key.sell_price, 'GP')
                    sell_all.append(key.sell_price)
                gold_for_all_items = sum(sell_all)
                if not len(sell_all):
                    # if gold_for_all_items == 0:
                    print(f"You have no {item_type_to_sell} to sell.")
                    pause()
                    break
                else:
                    print(f"Total sell price for all {item_type_to_sell}: {gold_for_all_items} GP")
                print(f"Your gold: {self.gold} GP")
                sell_or_exit = input(
                    f"Show entire (I)nventory, (S)ell an item, Sell (A)ll {item_type_to_sell} or go (B)ack: ").lower()
                if sell_or_exit not in ('i', 's', 'a', 'b'):
                    cls()
                    # self.hud()
                    continue
                elif sell_or_exit == 'a':

                    while True:
                        yes_or_no = input(f"Sell all {item_type_to_sell} for {gold_for_all_items} GP? ").lower()
                        if yes_or_no not in ('y', 'n'):
                            continue
                        elif yes_or_no == 'y':
                            print(f"You sell all of your {item_type_to_sell} for {gold_for_all_items} GP.")
                            self.gold += gold_for_all_items
                            (self.pack[item_type_to_sell]).clear()
                            pause()
                            break
                        elif yes_or_no == 'n':
                            break
                elif sell_or_exit == 'i':
                    self.inventory()
                    continue
                elif sell_or_exit == 'b':
                    break
                elif sell_or_exit == 's':

                    try:

                        item_index_to_sell = int(input(f"Enter the number of the item you wish to sell: "))
                        item_index_to_sell -= 1  # again, indexing starts at 0 and is awkward
                        sold_item = (self.pack[item_type_to_sell])[item_index_to_sell]
                    except (IndexError, ValueError):
                        print("Invalid entry..")
                        sleep(1)
                        continue
                    # sold_item = (self.pack[item_type_to_sell])[item_index_to_sell]
                    confirm_sale = input(f"Sell the {sold_item.name} for {sold_item.sell_price} GP (y/n)? ")
                    if confirm_sale == 'y':
                        # print(f"You sell the {(self.pack[item_type_to_sell])[item_index_to_sell]} for {sold_item.sell_price} GP")
                        print(f"You sell the {sold_item.name} for {sold_item.sell_price} GP")
                        self.gold += sold_item.sell_price
                        (self.pack[item_type_to_sell]).pop(item_index_to_sell)
                        print(f"Your gold: {self.gold} GP")
                        pause()
                        cls()
                        # self.hud()
                        if len(self.pack[item_type_to_sell]) > 0:
                            self.item_type_inventory(item_type_to_sell)
                            print(f"Your gold: {self.gold} GP")
                            sell_again = input(
                                f"(S)ell more {persistent_item_type} (B)ack to main market menu or (E)xit to town: ")
                            if sell_again == 's':
                                continue
                            elif sell_again == 'b':
                                break
                            else:
                                # if sell_again not in ('y', 'n'):
                                return
                        else:
                            # print(f"Your gold: {self.gold} GP")
                            print(f"Your {persistent_item_type} inventory is now empty.")
                            pause()
                            break
                    else:
                        continue

    def sell_everything(self):
        # this code took me many hours to come up with
        liquidate_lst = []
        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']
        mgmt_dict = {}
        for each_category in item_type_lst:
            if len(self.pack[each_category]):
                for item in (self.pack[each_category]):
                    mgmt_dict[item] = (self.pack[each_category]).index(item)
        for key, value in mgmt_dict.items():
            print(key.name, '- Sell price:', key.sell_price, 'GP')
            liquidate_lst.append(key.sell_price)
            # (self.pack[each_category]).clear()
        total = sum(liquidate_lst)
        print(f"Total: {total}")
        confirm_liquidate = input(f"Sell everything for {total} GP? ")
        if confirm_liquidate == 'y':
            for each_category in item_type_lst:
                (self.pack[each_category]).clear()
            print(f"You sell your entire armory inventory for {total} GP.")
            self.gold += total
            pause()
            return
        else:
            return

    def use_scroll_of_town_portal(self):
        if self.town_portals < 1:
            # if not self.duplicate_item(scroll_of_town_portal.item_type, scroll_of_town_portal): # scroll_of_town_portal not in self.pack['Town Portal Implements']:
            print(f"You have no scrolls!")
            time.sleep(2)
            return False
        else:
            self.hud()
            # (self.pack['Town Portal Implements'].remove(scroll_of_town_portal))
            self.town_portals -= 1
            print(f"The quantum portal appears before you; a seemingly impossible gateway between distant places..")
            time.sleep(2)
            # winsound.PlaySound(None, winsound.SND_ASYNC)
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\town_theme.wav',
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
            return True

    def poison(self):
        self.hud()
        self.dot_multiplier = self.dungeon.level
        rndm_poisoned_phrases = ["You feel a disturbing weakness overcoming you..",
                                 "An unnerving frailty spreads throughout your body...",
                                 "Pain and tenderness courses through your body.."
                                 ]
        poisoned_phrase = random.choice(rndm_poisoned_phrases)
        print(f"{poisoned_phrase}")
        sleep(1.5)
        print(f"You have been poisoned!")
        self.poisoned = True
        self.poisoned_turns = 0
        # self.calculate_poison()
        pause()
        # self.dungeon_description()
        self.hud()
        return self.poisoned

    def drink_potion_of_strength(self):
        self.hud()
        rndm_drinking_phrases = [
            "Tilting it to your lips, you empty the vial and the strength of giants surges through you!",
            "Retrieving the vial from your belt, you pop the cork and down the sweet liquid...\n"
            "Great power courses through your body!",
            "No sooner is the tincture running down your throat, than does the great\n "
            "and overwhelming strength fill your body! You feel invincible!"

        ]
        drink_phrase = random.choice(rndm_drinking_phrases)
        if self.potions_of_strength > 0:
            print(f"{drink_phrase}")
            self.potion_of_strength_effect = True
            self.potions_of_strength -= 1
            self.potion_of_strength_uses = 0
            pause()
            return self.potion_of_strength_effect
        else:
            print(f"You have no potions!")
            pause()
            return False

    def drink_elixir(self):
        if self.elixirs > 0:
            self.hud()
            if not self.poisoned and not self.necrotic:
                print(f"Your flesh is not corrupted!")
                sleep(1)
                return
            else:
                print(f"You retrieve the emerald vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.elixirs -= 1
                self.hud()
                print(f"You feel a cleansing of the flesh..")
                sleep(1)
                self.poisoned = False
                self.poisoned_turns = 0
                self.necrotic = False
                self.necrotic_turns = 0
                print(f"The foul corruption leaves your body..")
                pause()
                return

    def drink_healing_potion(self):
        self.hud()
        if self.potions_of_healing > 0:
            # if healing_potion in self.pack['Healing']:
            if self.hit_points >= self.maximum_hit_points:
                print(f"You are already at maximum health!")
                sleep(1)
                return
            else:
                print(f"You retrieve the vial from your belt and eagerly drain its contents into your mouth...")
                sleep(2)
                self.potions_of_healing -= 1
                self.hit_points = self.hit_points + math.ceil(self.maximum_hit_points * .75)
                if self.hit_points > self.maximum_hit_points:
                    self.hit_points = self.maximum_hit_points
                self.hud()
                print(f"Your vitality increases.")
                sleep(1)

                # print(f"You now have {self.hit_points} hit points.")
                # (pack[sub_item_type]).remove(sub_item)
                pause()
                return
        else:
            print("You have no potions!")
            pause()
            return

    def duplicate_item(self, item_type, possible_duplicate):
        duplicate_item_name_lst = []
        inv_dict = Counter(item for item in self.pack[item_type])
        # print(inv_dict)  # for testing
        for key, value in inv_dict.items():
            duplicate_item_name_lst.append(key.name)
        # print(duplicate_item_name_lst)  # for testing
        if possible_duplicate.name in duplicate_item_name_lst or \
                possible_duplicate.name == self.wielded_weapon.name or \
                possible_duplicate.name == self.armor.name or \
                possible_duplicate.name == self.shield.name or \
                possible_duplicate.name == self.boots.name:
            return True
        else:
            return False

    def item_type_inventory(self, item_type):  # list items in inventory by type
        if item_type != 'Town Portal Implements' and item_type != 'Elixirs' \
                and item_type != 'Potions of Strength' and item_type != 'Healing':
            print(f"Your {item_type}:")
            self.pack[item_type].sort(key=lambda x: x.name)
            stuff_dict = Counter(item.name for item in self.pack[item_type])
            for key, value in stuff_dict.items():
                # print(key, ':    ', value, sep='')
                if value > 1:
                    print(value, ' ', key, 's', sep='')
                    # print(key, 's', ':    ', value, sep='')
                else:
                    print(value, ' ', key, sep='')
            number_of_items = len(self.pack[item_type])
            # print(f"You now have {number_of_items} items in your {item_type} inventory.")
            if number_of_items:
                return True
            else:
                # print(f"You currently have no {item_type} in your inventory.")
                return False
        elif item_type == 'Town Portal Implements':
            if self.town_portals > 0:
                print(f"You have {self.town_portals} Scrolls of Town Portal")
                return True
            else:
                print(f"You have no scrolls of town portal.")
                return False
        elif item_type == 'Potions of Strength':
            if self.potions_of_strength > 0:
                print(f"You have {self.potions_of_strength} Potions of Strength")
                return True
            else:
                print(f"You have no Potions of Strength.")
                return False
        elif item_type == 'Healing':
            if self.potions_of_healing > 0:
                print(f"You have {self.potions_of_healing} Potions of Healing")
                return True
            else:
                print(f"You have no potions of healing.")
                return False
        elif item_type == 'Elixirs':
            if self.elixirs > 0:
                print(f"You have {self.elixirs} Clarifying Quantum Elixirs")
                return True
            else:
                print(f"You have no Elixirs.")
                return False

    def inventory(self):
        self.hud()

        print(
            f"You are wielding: \nA {self.wielded_weapon.name}. Damage bonus: {self.wielded_weapon.damage_bonus}. To hit: {self.wielded_weapon.to_hit_bonus}.")
        if self.shield.name != 'No Shield':
            print(f"A {self.shield.name}. Armor class: {self.shield.ac}")
        print(
            f"You are wearing:\n{self.armor.name}. Armor class: {self.armor.ac}. Armor bonus: {self.armor.armor_bonus}")
        print(f"{self.cloak.name}. Stealth: {self.cloak.stealth}")
        if self.ring_of_reg.name != 'No Ring':
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate}")
        if self.ring_of_prot.name != 'No Ring':
            print(f"A Ring of Protection + {self.ring_of_prot.protect} ")
        if self.town_portals or self.potions_of_healing or self.potions_of_strength > 0:
            print(f"On your belt, you are carrying:")
            print(f"{self.potions_of_strength} Potions of Strength")
            print(f"{self.potions_of_healing} Potions of Healing")
            print(f"{self.town_portals} Town Portal Scrolls")
            print(f"{self.elixirs} Clarifying Elixirs")
        item_type_lst = ['Weapons', 'Armor', 'Shields', 'Boots', 'Cloaks']

        print(f"Your dungeoneer's pack contains:")
        current_items = []
        for each_item in item_type_lst:
            is_item_on_list = len(self.pack[each_item])
            # is_item_on_list = self.item_type_inventory(each_item)  # item_type_inv function returns True or False
            # print(is_item_on_list)  # True or False for testing
            if is_item_on_list > 0:
                current_items.append(each_item)
                self.item_type_inventory(each_item)  # call the item_type_inventory for each item in inv.
                # print(current_items)  # for testing
        if not len(current_items):
            print(f"Nothing but cobwebs..")
            pause()
            return False  # need this False for when called from..?
        else:
            pause()
            return

    def found_weapon_substitution(self, found_item):
        if self.wielded_weapon.damage_bonus < (self.level * 2):
            # found_item.damage_bonus = self.level
            if found_item.name == self.wielded_weapon.name:
                print(
                    f"Quantum wierdness fills the air...\nYour {self.wielded_weapon.name} is enhanced to + {found_item.damage_bonus + 1}!")
                self.wielded_weapon.damage_bonus = found_item.damage_bonus + 1
                pause()
                return
            else:
                print(
                    f"You have found a {found_item.name}. Damage bonus: {found_item.damage_bonus}. To hit bonus: {found_item.to_hit_bonus}.")
                print(
                    f"You are currently wielding a {self.wielded_weapon.name}. Damage bonus: {self.wielded_weapon.damage_bonus}. To hit bonus: {self.wielded_weapon.to_hit_bonus}.")
            while True:
                replace_weapon = input(f"Do you wish to wield the {found_item.name} instead? y/n: ").lower()
                if replace_weapon == 'y':
                    old_weapon = self.wielded_weapon
                    self.wielded_weapon = found_item
                    print(f"You are now wielding the {found_item.name}")
                    print(
                        f"Damage bonus: {self.wielded_weapon.damage_bonus}. To hit: {self.wielded_weapon.to_hit_bonus}")
                    if not self.duplicate_item(old_weapon.item_type,
                                               old_weapon):  # old_weapon not in self.pack['Weapons']:
                        (self.pack[found_item.item_type]).append(old_weapon)
                        print(f"You place the {old_weapon.name} upon your back..")

                    else:
                        print(f"You drop the {old_weapon.name}.")
                    pause()
                    return
                elif replace_weapon == 'n':
                    print(f"You don't wield the {found_item.name}.")
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} on your back.")

                    else:
                        print(f"You can't carry any more weapons of this type. You leave the {found_item.name}")
                    pause()
                    return False
                elif replace_weapon not in ("y", "n"):
                    continue
        else:
            print(f"Wielded_weapon.damage_bonus already >= self.level * 2!!!")  # remove after testing
            pause()
            return

    def found_armor_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if self.armor.ac < found_item.ac:
            if found_item.name == 'Full Plate Armor' and found_item.name == self.armor.name:
                found_item.ac += 1
                print(
                    f"Quantum wierdness fills the air...\nYour {self.armor.name} is enhanced to armor class {found_item.ac}!")
                self.armor.ac = found_item.ac
                self.calculate_armor_class()
                pause()
                return
            else:
                print(f"You have found {found_item.name}!! Armor Class: {found_item.ac}")
                print(f"Your current {self.armor.name} Armor Class: {self.armor.ac}")
                # USE THIS NEXT BLOCK OF CODE FOR WEARING ARMOR AT THE BLACKSMITH:
            while True:
                replace_armor = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_armor == 'y':
                    old_armor = self.armor
                    self.armor = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(found_item.item_type, old_armor):
                        (self.pack[found_item.item_type]).append(old_armor)
                        print(f"You place the {old_armor.name} upon your back..")
                    else:
                        print(f"You drop your {old_armor.name}.")
                    pause()
                    return
                elif replace_armor == 'n':
                    print(f"You don't wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type, found_item):
                        # if found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} on your back.")

                    else:
                        print(f"You can't carry any more {found_item.name}. You leave it.")  # can't carry any more
                    pause()
                    return
                elif replace_armor not in ("y", "n"):
                    continue
        else:
            print(f"Worn armor >= found item...")  # remove after testing
            pause()  # remove after testing
            return

    def found_shield_substitution(self, sub_item):
        if self.shield.ac < sub_item.ac:
            if sub_item.name == 'Quantum Tower Shield' and sub_item.name == self.shield.name:
                sub_item.ac += 1
                print(
                    f"Quantum wierdness fills the air...\nYour {self.shield.name} is enhanced to armor class {sub_item.ac}!")
                self.shield.ac = sub_item.ac
                self.calculate_armor_class()
                # self.armor_class = self.armor.ac + self.armor.armor_bonus + self.shield.ac + self.boots.ac + self.dexterity_modifier
                pause()
                return
            else:
                print(f"You have found a {sub_item.name}!! Armor Class: {sub_item.ac}")
                if self.shield.name == 'No Shield':
                    print(f"You currently hold no shield in your off hand.")
                else:
                    print(f"Your current {self.shield.name} Armor Class: {self.shield.ac}")
            while True:
                replace_shield = input(f"Do you wish to wield the {sub_item.name} instead? y/n: ").lower()
                if replace_shield == 'y':
                    old_shield = self.shield
                    self.shield = sub_item
                    print(f"You are now wielding the {sub_item.name}")
                    self.calculate_armor_class()
                    if old_shield.name == 'No Shield':
                        pause()
                        return
                    elif not self.duplicate_item(old_shield.item_type,
                                                 old_shield):  # old_shield not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(old_shield)
                        print(f"You place the {old_shield.name} on your back..")
                    else:
                        print(f"You drop your {old_shield.name}.")
                    pause()
                    return
                elif replace_shield == 'n':
                    print(f"You don't wield the {sub_item.name}.")
                    if not self.duplicate_item(sub_item.item_type,
                                               sub_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[sub_item.item_type]).append(sub_item)
                        print(f"You place the {sub_item.name} on your back.")

                    else:
                        print(f"You can't carry any more {sub_item.name}s. You leave it.")  # can't carry any more
                    pause()
                    return
                elif replace_shield not in ("y", "n"):
                    continue
        else:
            print(f"Wielded shield >= found item...")  # remove after testing
            pause()
            return

    def found_boots_substitution(self, found_item):
        # ADD armor_bonus FOR FOUND PLATE ARMOR AFTER PLAYER REACHES CERTAIN LEVEL?
        if self.boots.ac < found_item.ac:
            if found_item.name == 'Elven Boots' and found_item.name == self.boots.name:  # make this the most elite item
                found_item.ac += 1
                print(
                    f"Quantum wierdness fills the air...\nYour {self.boots.name} are enhanced to armor class {found_item.ac}!")
                self.boots.ac = found_item.ac
                self.calculate_armor_class()
                pause()
                return
            else:
                print(f"You have found a pair of {found_item.name}!! Armor Class: {found_item.ac}")
                print(f"Your current {self.boots.name} Armor Class: {self.boots.ac}")

            while True:
                replace_boots = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_boots == 'y':
                    old_boots = self.boots
                    self.boots = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_armor_class()
                    if not self.duplicate_item(old_boots.item_type,
                                               old_boots):  # old_boots not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_boots)
                        print(f"You place the {old_boots.name} in your dungeoneer's pack..")

                    else:
                        print(f"You drop your {old_boots.name}.")
                    pause()
                    return
                elif replace_boots == 'n':
                    print(f"You don't wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} in your dungeoneer's pack.")

                    else:
                        print(f"You can't carry any more {found_item.name}. You leave them.")  # can't carry any more
                    pause()
                    return
                elif replace_boots not in ("y", "n"):
                    continue
        else:
            print(f"Worn boots >= found item...")  # remove after testing
            pause()
            return

    def found_cloak_substitution(self, found_item):

        if self.cloak.stealth < math.ceil(self.dexterity * .25):
            if found_item.name == self.cloak.name:
                found_item.stealth += 1
                print(
                    f"Quantum wierdness fills the air...\nYour {self.cloak.name} is enhanced to stealth + {found_item.stealth}!")
                self.cloak.stealth = found_item.stealth
                self.calculate_stealth()
                pause()
                return
            else:
                print(f"You have found a {found_item.name}!! Stealth: {found_item.stealth}")
                print(f"Your current {self.cloak.name} Stealth: {self.cloak.stealth}")
            while True:
                replace_cloak = input(f"Do you wish to wear the {found_item.name} instead? y/n: ").lower()
                if replace_cloak == 'y':
                    old_cloak = self.cloak
                    self.cloak = found_item
                    print(f"You are now wearing the {found_item.name}")
                    self.calculate_stealth()
                    if not self.duplicate_item(old_cloak.item_type,
                                               old_cloak):  # old_cloak not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(old_cloak)
                        print(f"You place the {old_cloak.name} in your dungeoneer's pack..")
                    else:
                        print(f"You drop your {old_cloak.name}.")
                    pause()
                    return
                elif replace_cloak == 'n':
                    print(f"You don't wear the {found_item.name}.")  # remove after testing
                    if not self.duplicate_item(found_item.item_type,
                                               found_item):  # found_item not in self.pack[found_item.item_type]:
                        (self.pack[found_item.item_type]).append(found_item)
                        print(f"You place the {found_item.name} into your dungeoneer's pack.")
                    else:
                        print(f"You can't carry any more {found_item.name}s. You leave it.")  # can't carry any more
                    pause()
                    return
                elif replace_cloak not in ("y", "n"):
                    continue
        else:
            print(f"Stealth already >= .25 * dex...")  # remove after testing
            pause()
            return

    def found_ring_of_reg_substitution(self, found_item):

        if self.ring_of_reg.name == default_ring_of_regeneration.name:  # self.ring_of_reg.regenerate == 0:
            # self.ring_of_regeneration and default class object has 0 regenerate
            self.ring_of_reg = found_item
            print(f"Quantum wierdness fills the air...")
            print(f"A Ring of Regeneration + {self.ring_of_reg.regenerate} appears on your finger!")
            sleep(1)
            print(f"It becomes permanently affixed..fused to your flesh and bone!")
            self.regenerate()  # this is fair. this could save you from poison or necrosis
            pause()
            return
        elif self.ring_of_reg.regenerate < math.ceil(self.maximum_hit_points * .17):
            # old_ring = self.ring_of_reg
            self.ring_of_reg.regenerate = (self.ring_of_reg.regenerate + 1)
            print(f"Quantum wierdness fills the air...")
            print(f"Your {ring_of_regeneration.name} is enhanced to + {self.ring_of_reg.regenerate} !")
            pause()
            return

        else:
            print("Ring of reg already equal to or more than 17% of max hit points")  # remove after testing
            pause()
            return

    def found_ring_of_prot_substitution(self, found_item):

        if self.ring_of_prot.name == default_ring_of_protection.name:  # default ring is transparent placeholder
            self.ring_of_prot = found_item
            # (self.pack[found_item.item_type]).append(found_item) you can't sell rings. new rule
            print(f"Quantum wierdness fills the air...")
            print(f"A Ring of Protection + {self.ring_of_prot.protect} appears on your finger!")
            sleep(1)
            print(f"Tunneling through realities, it permanently fuses to flesh and bone!")
            pause()
            return
        elif self.ring_of_prot.protect < math.ceil(self.wisdom * .33):
            self.ring_of_prot.protect += 1
            print(f"Quantum wierdness fills the air...")
            print(f"Your {ring_of_protection.name} is enhanced to + {self.ring_of_prot.protect} !")
            pause()
            return
        else:
            print("Ring of prot already equal to or more than 33% of wisdom")  # remove after testing
            pause()
            return

    def loot(self):
        # place armor first here; otherwise it will mess up the order of operations below
        loot_dict = {
            'Armor': [leather_armor, studded_leather_armor, scale_mail, half_plate, full_plate],
            'Shields': [buckler, kite_shield, quantum_tower_shield],
            'Boots': [elven_boots, ancestral_footsteps],
            'Cloaks': [elven_cloak],
            'Weapons': [short_axe, broad_sword, quantum_sword, battle_axe, great_axe],
            'Elixirs': [elixir],
            'Healing': [healing_potion],
            'Rings of Regeneration': [ring_of_regeneration],
            'Rings of Protection': [ring_of_protection],
            'Town Portal Implements': [scroll_of_town_portal],
            'Potions of Strength': [strength_potion]
        }

        while True:
            # ****** NOTICE THE DIFFERENCE BETWEEN found_item and found_item.item_type !! ************************
            loot_roll = dice_roll(1, 20)
            self.hud()
            print(f"Loot roll ---> {loot_roll}")
            pause()
            if loot_roll > 9:
                key = random.choice(list(loot_dict.keys()))  # this code should negate item key type list
                rndm_item_index = random.randrange(len(loot_dict[key]))
                found_item = loot_dict[key][rndm_item_index]
                print(found_item)  # REMOVE AFTER TESTING *****************************************************
                if self.level >= found_item.minimum_level:
                    if found_item.item_type == 'Armor':
                        self.found_armor_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Shields':
                        self.found_shield_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Cloaks':
                        self.found_cloak_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Weapons':
                        self.found_weapon_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Regeneration':
                        self.found_ring_of_reg_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Rings of Protection':
                        self.found_ring_of_prot_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Boots':
                        self.found_boots_substitution(found_item)
                        continue
                    elif found_item.item_type == 'Town Portal Implements':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.town_portals += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Healing':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_healing += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Potions of Strength':
                        print(f"You see a {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.potions_of_strength += 1
                        pause()
                        continue
                    elif found_item.item_type == 'Elixirs':
                        print(f"You see an {found_item.name} !")
                        sleep(.5)
                        print(f"You snarf it..")
                        self.elixirs += 1
                        pause()
                        continue
                    '''                    else:
                        print(f"You already have a {found_item.name} of equal or greater value.."
                              f"(remove this statement after testing.)")  # remove after tesing
                        pause()  # remove this pause after testing
                        continue'''
                else:
                    print(f"Minimum requirements not met for {found_item.name}.")  # remove after testing
                    pause()  # remove after testing
                    continue
            else:
                return self.dungeon_description()

    def increase_random_ability(self):
        # I was unable to come up with this code on my own.
        # Thanks to Angus Nicolson from Stack Overflow!
        # By editing player.__dict__ directly,
        # or a variable which you derived from it (ability_dict in the code below),
        # you can edit your object's attributes.
        # create a dictionary from self.__dict__
        # Note: Editing ability_dict_subset will not change the object's attributes,
        # because it was made from a dict comprehension.
        # You need to edit self.__dict__ or ability_dict.
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ability_dict_subset = {k: v for k, v in ability_dict.items() if k in attributes}
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Choose random attribute name
        random_attribute = random.choice(list(ability_dict_subset.keys()))
        print(f"Weird Quantum forces surge through your body..")
        sleep(1.5)
        print(f"You have gained unnatural {random_attribute}!")
        ability_dict[random_attribute] += 1
        pause()

    def increase_lowest_ability(self):
        ability_dict = self.__dict__
        # Define list of attributes you are allowed to change
        attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        ability_dict_subset = {key: value for key, value in ability_dict.items() if key in attributes}
        # Find the minimum attribute name
        min_attribute = min(ability_dict_subset, key=ability_dict_subset.get)
        print()  # remove after testing
        print(f"Weird sensations surge through your body..")
        sleep(1.5)
        print(f"You have gained {min_attribute}!")
        # Add one to min attribute
        ability_dict[min_attribute] += 1
        pause()

    def throne_event(self):
        rndm_throne_descriptions = ['There is a magnificent, gem-encrusted throne of gold here. Throughout its\n'
                                    'shimmering surface are countless runes and symbols.',
                                    'In the center of the room stands a majestic throne encrusted with many\n'
                                    'gems and jewels, all laid in gold. Ancient runes cover its glimmering surface.',
                                    'A great, golden throne, replete with many gems and inscribed with countless '
                                    'runes stands here.']
        rndm_throne_description = random.choice(rndm_throne_descriptions)
        print(f"{rndm_throne_description}")
        sit = input(f"Do you wish to sit? ")
        if sit == 'y':
            print(f"You sit on the throne...")
            self.regenerate()  # testing
            return "King Boss"
        else:
            winsound.PlaySound('C:\\Program Files\\Telengard\\MEDIA\\MUSIC\\creepy_dungeon_theme.wav',
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
            print("You don't sit...wonder what may have happened.")
            return

    def heal_event(self):
        heal = ((3 * self.dungeon.level) + 1)  # math right out of telengard!
        self.hit_points += heal
        print(f"You feel vitality bubbling up within you...")
        sleep(1.5)
        if self.poisoned or self.necrotic:
            print(f"Your flesh no longer crawls with agony..")
            sleep(1)
            self.poisoned = False
            self.poisoned_turns = 0
            self.necrotic = False
            self.necrotic_turns = 0
            print(f"The foul corruption leaves your body..")
            sleep(1)
        if self.hit_points < self.maximum_hit_points:
            print(f"You feel refreshing strength return.")
            sleep(1)
        else:
            print(f"Your hit points have been unnaturally raised to {self.hit_points}!")
            sleep(1)
            print(f"You wonder how long this advantage will last..")
            sleep(1)
        pause()
        return

    def lose_items(self):
        available_item_types_to_lose = []
        for i in self.pack.keys():  # gather all available
            if len(self.pack[i]) > 0:  # item types to lose based on player's current item TYPES and put them
                available_item_types_to_lose.append(i)  # in available_item_types_to_lose = []
        if len(available_item_types_to_lose) > 0:
            item_type = random.choice(available_item_types_to_lose)  # Get random item *TYPE* you want to "steal"
            if len(self.pack[item_type]) > 0:  # If the player has an item of type "item_type"
                # pop random item from that item type. -1 because indexes start at 0
                lost_item = (self.pack[item_type].pop(random.randint(0, len(self.pack[item_type]) - 1)))
                print(f"Your load feels lighter..")
                sleep(1)
                print(f"The {lost_item.name} from your dungeoneer's pack is gone!")  # from your {item_type}")
                pause()
                return
        elif self.potions_of_strength > 0 or self.potions_of_healing > 0 or self.town_portals > 0 or self.elixirs > 0:
            item_string = ""
            # Define list of attributes you are allowed to change
            self_dict = self.__dict__  # create variable as actual copy of player dict attribute
            stealing_lst = []
            # the working dict and 'for' loop just takes the place of many 'if:' statements
            working_dict = {'potions_of_strength': self.potions_of_strength,
                            'potions_of_healing': self.potions_of_healing,
                            'town_portals': self.town_portals, 'elixirs': self.elixirs}
            # add all items > 0 in working dict to stealing list
            for key, value in working_dict.items():
                if value > 0:
                    stealing_lst.append(key)
            random_stolen_item = random.choice(stealing_lst)
            # I am proud of this next bit of code :)
            grammar_dict = {'potions_of_strength': 'potion of strength',
                            'potions_of_healing': 'potion of healing',
                            'town_portals': 'scroll of town portal', 'elixirs': 'clarifying elixir'}
            for key, value in grammar_dict.items():
                if random_stolen_item == key:
                    item_string = value
            print(f"Your load feels lighter...")
            sleep(1)
            print(f"A {item_string} has disappeared from your belt!")
            self_dict[random_stolen_item] -= 1
            pause()
            return
        else:
            print("Nothing happens...")
            pause()
            # sleep(2)
            return

    def fountain_event(self):
        # WHITE GREEN CLEAR RED BLACK
        # telengard has these 5 random events:
        # heal 3 * dungeon level + 1 hit points
        # poison 3 * dungeon level + 1 hit points
        # drunk
        # lose items
        # increase num of spells Magic power SURGES through your body
        water_colors = ['white', 'green', 'crystal clear', 'red', 'black']
        water_color = random.choice(water_colors)
        print(f"A fountain with flowing {water_color} water is here.")
        sleep(1)
        print(f"The tranquil sound eases your mind.")
        sleep(1)
        drink = input(f"Do you wish to drink? ")
        if drink == 'y':
            rndm_occurrence_lst = [self.poison, self.increase_random_ability, self.teleporter_event,
                                   self.increase_lowest_ability,
                                   self.lose_items,
                                   self.heal_event]
            rndm_occurrence = random.choice(rndm_occurrence_lst)
            rndm_occurrence()
        else:
            #print("You don't drink...wonder what may have happened.")
            return

    def teleporter_event(self):
        print(f"Zzzzzzap....You've been teleported.....")
        self.dungeon_key += 1  # this will become random.randint(1, deepest dungeon level) in future
        self.dungeon = dungeon_dict[self.dungeon_key]
        # self.x = random.randint(1, 18)
        # self.y = random.randint(1, 18)
        (self.x, self.y) = self.dungeon.teleporter_landing
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = self.dungeon.grid[self.y][self.x]
        # self.regenerate()  # testing
        # self.position = 0
        pause()
        self.hud()
        return

    def pit_event(self):
        print(f"The ground here is very unsteady..")
        sleep(1.5)
        print(f"You see a pit..")
        sleep(1.5)
        pit_challenge_rating = 10
        pit_outcome = dice_roll(1, 20)
        if (pit_outcome + self.dexterity_modifier + self.intelligence_modifier) > pit_challenge_rating:
            descend_or_not = input(f"Do you wish to descend (y/n)?: ")
            if descend_or_not == 'y':
                print(f"Carefully and craftily, you repel down the slick, treacherous pit walls.")
                self.dungeon_key += 1
                self.dungeon = dungeon_dict[self.dungeon_key]
                (self.x, self.y) = self.dungeon.pit_landing
                self.previous_x = self.x
                self.previous_y = self.y
                self.position = self.dungeon.grid[self.y][self.x]
                pause()
                return
            else:
                return
        else:
            print(f"The ground beneath your feet collapse! You fall in!")
            damage = dice_roll(1, (3 * self.dungeon.level))  # dice_roll(1, self.dungeon.level)
            self.hit_points -= damage
            sleep(1)
            print(f"You suffer {damage} hit points..")
            pause()
            # falling into pits lands you on the next dungeon level at the dungeon.pit_landing coordinates
            self.dungeon_key += 1
            self.dungeon = dungeon_dict[self.dungeon_key]
            (self.x, self.y) = self.dungeon.pit_landing
            self.previous_x = self.x
            self.previous_y = self.y
            self.position = self.dungeon.grid[self.y][self.x]
            return

    def staircase_description(self):
        # this is a description of the spiral staircase, if player navigates to it *after* the map is initialized
        # it is not an 'event', since it is not really interactive.
        # this function is called from the description function
        print(f"This is the spiral staircase entrance to {self.dungeon.name}.")
        if self.dungeon.level > 1:
            previous_place = f"dungeon level {self.dungeon.level - 1}"
        else:
            previous_place = f"the town of Fieldenberg"
        print(f"The stairs lead up to {previous_place}. However, there is no returning;\n"
              f"The door is locked and barricaded. You must continue onward!")

    def event_logic(self):
        # interactive events, items etc.
        # the event dictionary *key* is the dungeon tuple corresponding to
        # dungeon x y coordinates of an event or item e.g. (2, 3)
        # the event dictionary *value* is the corresponding player function
        # if the player's coordinates exist as a key in event_dict,
        # the dictionary value is given the variable 'event_function'
        # finally, the proper function is called and any
        # function values are returned to the main program
        # using 'return event_function()'
        self.coordinates = (self.x, self.y)
        event_dict = {self.dungeon.throne: self.throne_event,
                      self.dungeon.fountain: self.fountain_event,
                      self.dungeon.teleporter: self.teleporter_event,
                      self.dungeon.pit: self.pit_event

                      }
        if self.coordinates in event_dict:
            event_function = (event_dict[self.coordinates])
            return event_function()

        # NAVIGATION

    def dungeon_description(self):
        self.hud()
        north_south = ""
        east_west = ""
        if self.x > 9:
            east_west = "eastern"
        elif self.x < 10:
            east_west = "western"
        if self.y > 9:
            north_south = "South"
        elif self.y < 10:
            north_south = "North"
        # print(self.coordinates)  # remove after testing
        # print(f"(Dungeon level {self.dungeon.level} {self.dungeon.name}) {self.coordinates}")
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
        # ^ <> v dungeon exit in the indicated direction!
        description_dict = {
            ".": f"You are in a rather wide open area of {self.dungeon.name}. There are exits in each direction...",
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
            "T": f"You are in a chamber of {self.dungeon.name} that seems to have been re-purposed as a sort of throne room."
        }
        # if self.position == 0:  # integer representing starting position
        #    print(self.dungeon.intro)
        # self.hud()
        # return

        if self.position == "*":  # string representing walls
            print("You can't go that way...")
            self.x = self.previous_x
            self.y = self.previous_y
            self.coordinates = (self.x, self.y)
            self.position = self.dungeon.grid[self.y][self.x]
            # sleep(1.5)
            # return
        if self.coordinates == self.dungeon.staircase:
            self.staircase_description()
        if self.position in description_dict:
            description = (description_dict[self.position])
            # return description
            print(description)
            # return
            # ^ <> v dungeon EXIT in the indicated direction!

        elif self.position == ">" or self.position == "<" or self.position == "^" or self.position == "v":
            print(f"You feel a draft... ")
            sleep(1.25)
            if self.position == ">":
                print("You see the dungeon exit to the East!")
                # return
            elif self.position == "<":
                print("You see the dungeon exit to the West!")
                # return
            elif self.position == "^":
                print("You see the dungeon exit to the North!")
                # return
            elif self.position == "v":
                print("You see the dungeon exit to the South!")
                # return
        self.coordinates = (self.x, self.y)
        print(
            f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}, {north_south}{east_west} region) Coordinates: {self.coordinates}")
        return

    def display_map(self, maps):
        # self.hud()
        cls()
        print("You look at the map..")
        print(f"Position key: {self.position}")  # remove after testing
        self.coordinates = (self.x, self.y)

        if self.position == 0:
            print(self.dungeon.intro)
        print(f"(Dungeon level {self.dungeon.level} - {self.dungeon.name}) Coordintes: {self.coordinates}")
        if self.position != 0 and self.coordinates != self.dungeon.staircase:
            self.dungeon.player_grid[self.y][self.x] = "X"
        for element in range(0, 20):
            print(*maps[element])
        # replace the X with a dot so that it doesn't leave a trail:
        if self.position != 0 and self.coordinates != self.dungeon.staircase:
            self.dungeon.player_grid[self.y][self.x] = "."
        self.position = self.dungeon.grid[self.y][self.x]
        print(f"S = Staircase X = your position E = Exit")
        # place the following line in the main file to leave a trail of x's throughout the map to see where you've been.
        # player_1.dungeon.player_grid[player_1.y][player_1.x] = "x"

    def next_dungeon(self):
        # dungeon dictionary in dungeons.py
        print(
            "You found the exit...\nYou begin to descend the stairs, deeper into the dungeon...\nYet, you sense you are not alone!")
        self.dungeon_key += 1
        self.dungeon = dungeon_dict[self.dungeon_key]
        (self.x, self.y) = self.dungeon.start  # simplified with tuple by adding 'start' attribute to dungeon class
        # self.x = self.dungeon.starting_x
        # self.y = self.dungeon.starting_y
        # self.coordinates will be set after first move..otherwise the intro will be printed, followed by the
        # staircase description, which is awkward
        self.previous_x = self.x
        self.previous_y = self.y
        self.position = 0
        pause()
        return


'''
In most cases, your AC will be equal to 10 + your DEX modifier + bonus from armor + bonus from magic items/effects.

Fighter
As a Fighter, you gain the following Class Features.

Hit Points
Hit Dice: 1d10 per Fighter level
Hit Points at 1st Level: 10 + your Constitution modifier
Hit Points at Higher Levels: 1d10 (or 6) + your Constitution modifier per Fighter level after 1st

Starting Proficiencies
You are proficient with the following items, in addition to any Proficiencies provided by your race or Background.

Armor: Light Armor, Medium Armor, Heavy Armor, Shields
Weapons: simple Weapons, martial Weapons
Tools: none
Saving Throws: Strength, Constitution
Skills: Choose two Skills from Acrobatics, Animal Handling, Athletics, History, 
Insight, Intimidation, Perception, and Survival

Starting Equipment
You start with the following items, plus anything provided by your Background.

• (a) Chain Mail or (b) Leather Armor, Longbow, and 20 Arrows
• (a) a martial weapon and a Shield or (b) two martial Weapons
• (a) a Light Crossbow and 20 bolts or (b) two handaxes
• (a) a Dungeoneer's Pack or (b) an Explorer's Pack

Table: The Fighter
Level	Proficiency Bonus	Bonus Features
1st	+2	Fighting Style, Second Wind
2nd	+2	Action Surge (one use)
3rd	+2	Martial Archetype
4th	+2	Ability Score Improvement
5th	+3	Extra Attack
6th	+3	Ability Score Improvement
7th	+3	Martial Archetype feature
8th	+3	Ability Score Improvement
9th	+4	Indomitable (one use)
10th	+4	Martial Archetype feature
11th	+4	Extra Attack (2)
12th	+4	Ability Score Improvement
13th	+5	Indomitable (two uses)
14th	+5	Ability Score Improvement
15th	+5	Martial Archetype feature
16th	+5	Ability Score Improvement
17th	+6	Action Surge (two uses), Indomitable (three uses)
18th	+6	Martial Archetype feature
19th	+6	Ability Score Improvement
20th	+6	Extra Attack (3)
Fighting Style
You adopt a particular style of Fighting as your specialty. Choose a Fighting style from the list of optional features.
 You can't take the same Fighting Style option more than once, even if you get to choose again.
Archery
You gain a +2 bonus to Attack rolls you make with ranged Weapons.

Defense
While you are wearing armor, you gain a +1 bonus to AC.

Dueling
When you are wielding a melee weapon in one hand and no other Weapons, 
you gain a +2 bonus to Damage Rolls with that weapon.

Great Weapon Fighting
When you roll a 1 or 2 on a damage die for an Attack you make with a melee weapon that you are wielding with two hands,
 you can Reroll the die and must use the new roll, even if the new roll is a 1 or a 2. 
 The weapon must have the Two-Handed or Versatile property for you to gain this benefit.

Protection
When a creature you can see attacks a target other than you that is within 5 feet of you,

you can use your Reaction to impose disadvantage on the Attack roll. You must be wielding a Shield.

Two-Weapon Fighting
When you engage in two-weapon Fighting, you can add your ability modifier to the damage of the second Attack.

Second Wind
You have a limited well of stamina that you can draw on to protect yourself from harm. On Your Turn, 
you can use a bonus Action to regain Hit Points equal to 1d10 + your Fighter level.

Once you use this feature, you must finish a short or Long Rest before you can use it again.

Action Surge
Starting at 2nd Level, you can push yourself beyond your normal limits for a moment. On Your Turn, 
you can take one additional Action on top of your regular Action and a possible bonus Action.

Once you use this feature, you must finish a short or Long Rest before you can use it again. Starting at 17th level, 
you can use it twice before a rest, but only once on the same turn.

Martial Archetype
At 3rd Level, you choose an archetype that you strive to emulate in your Combat styles and Techniques, 
such as Champion. The archetype you choose grants you features at 3rd Level 
and again at 7th, 10th, 15th, and 18th level.

Ability Score Improvement
When you reach 4th Level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, 
you can increase one ability score of your choice by 2, or you can increase two Ability Scores of your choice by 1. 
As normal, you can’t increase an ability score above 20 using this feature.

Extra Attack
Beginning at 5th Level, you can Attack twice, instead of once, whenever you take the Attack Action on Your Turn.

The number of attacks increases to three when you reach 11th level in this class 
and to four when you reach 20th level in this class.

Indomitable
Beginning at 9th level, you can Reroll a saving throw that you fail.
 If you do so, you must use the new roll, and you can't use this feature again until you finish a Long Rest.

You can use this feature twice between long rests starting at 13th level 
and three times between long rests starting at 17th level.

Martial Archetypes
Different fighters choose different approaches to perfecting their Fighting Prowess. 
The Martial Archetype you choose to emulate reflects your approach.

Champion
The archetypal Champion focuses on the Development of raw physical power honed to deadly perfection.
 Those who model themselves on this archetype combine rigorous Training with physical excellence 
 to deal devastating blows.

Improved Critical
Beginning when you choose this archetype at 3rd Level, your weapon attacks score a critical hit on a roll of 19 or 20.

Remarkable Athlete
Starting at 7th level, you can add half your Proficiency bonus (round up) to any Strength, 
Dexterity, or Constitution check you make that doesn’t already use your Proficiency bonus.

In addition, when you make a running Long Jump, the distance you can cover increases 
by a number of feet equal to your Strength modifier.

Additional Fighting Style
At 10th level, you can choose a second option from the Fighting Style class feature.

Superior Critical
Starting at 15th level, your weapon attacks score a critical hit on a roll of 18–20.

Survivor
At 18th level, you attain the pinnacle of resilience in battle. 
At the start of each of your turns, you regain Hit Points equal to 5 + your Constitution modifier,
 if you have no more than half of your Hit Points left.

You don’t gain this benefit if you have 0 Hit Points.
Attributes
Hit Die
d10
Starting Gold
5d4 x 10
Subclass Name
Martial Archetype
Suggested Abilities
Strength or Dexterity, Constitution or Intelligence
Experience Points	Level	Proficiency Bonus
0	                1	    +2
300	                2	    +2
900	                3	    +2
2,700	            4	    +2
6,500	            5	    +3
14,000	            6	    +3
23,000	            7	    +3
34,000	            8	    +3
48,000	            9	    +4
64,000	            10	    +4
85,000	            11	    +4
100,000	            12	    +4
120,000	            13	    +5
140,000	            14	    +5
165,000	            15	    +5
195,000	            16	    +5
225,000	            17	    +6
265,000	            18	    +6
305,000	            19	    +6
355,000	            20	    +6
'''
# removed code:
'''
item_type_key_lst = ['Weapons', 'Healing', 'Armor', 'Shields', 'Boots', 'Cloaks',
                             'Rings of Regeneration',
                             'Rings of Protection', 'Town Portal Implements']

if len(self.pack):
                stolen_item = random.choice(self.pack[random.choice(item_type_key_lst)])
                self.pack.pop(stolen_item)
                # stolen_item = random.choice(self.pack)
                print(f"He steals your {stolen_item}!")

                item_type_key_lst = ['Weapons', 'Healing', 'Armor', 'Shields', 'Boots', 'Cloaks',
                             'Rings of Regeneration',
                             'Rings of Protection', 'Town Portal Implements']
        # found_item = random.choice(loot_dict[random.choice(item_type_key_lst)])



                '''
'''   def inventory_old(self):
       while True:
           if len(self.pack):
               self.hud()
               print("Your pack contains:")
               print("Item                       Quantity")
               print()
               self.pack.sort(key=lambda x: x.damage_bonus)
               stuff_dict = Counter(item.name for item in self.pack)
               for key, value in stuff_dict.items():
                   print(key, 's', ':    ', value, sep='')
                   # print(value, ':', key)
               print()
           else:
               print("Your pack is empty")
           print(f"Your current wielded weapon: "
                 f"{self.wielded_weapon}\n"
                 f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                 f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
           if not len(self.pack):
               return
           inventory_choice = input(f"(S)ubstitute wielded weapon or (E)xit: ").lower()
           if inventory_choice not in ('s', 'e'):
               continue
           if inventory_choice == 'e':
               return
           if inventory_choice == 's':
               self.hud()
               # stuff = Counter(item.name for item in self.pack)
               # items = [item for item in self.pack if item.item_type == "weapon"]
               self.pack.sort(key=lambda x: x.damage_bonus)
               # stuff = Counter(item.name for item in items)
               stuff = {}
               for item in self.pack:
                   # if getattr(item, item.item_type) == "weapon":
                   stuff[item] = self.pack.index(item)
               for key, value in stuff.items():
                   print(value, ':', key)
               old_weapon = self.wielded_weapon
               print(f"Your current wielded weapon: "
                     f"{self.wielded_weapon}\n"
                     f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
                     f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
               try:
                   new_weapon = int(input(f"Enter the number of the weapon from your pack you wish to wield: "))
                   # try:
                   self.wielded_weapon = self.pack[new_weapon]
               except (IndexError, ValueError):
                   print("Invalid entry..")
                   sleep(1)
                   break
               print(f"You remove the {self.pack[new_weapon]} from your pack and are now wielding it.\n"
                     f"You place the {old_weapon} in your pack.")
               self.pack.pop(new_weapon)
               self.pack.append(old_weapon)
               self.pack.sort(key=lambda x: x.damage_bonus)
               sleep(1)
               if not len(self.pack):
                   print("Your pack is now empty.")
                   sleep(1)
                   return
           else:
               print("Your pack is empty..see if this statement is ever seen")
               return'''
'''elif found_item.item_type != 'Armor' and found_item.item_type != 'Shields' and found_item.item_type != 'Cloaks' and found_item.item_type != 'Rings of Protection' and found_item.item_type != 'Rings of Regeneration' and found_item.item_type != 'Weapons' and found_item.item_type != 'Healing' and found_item.item_type != 'Town Portal Implements' and found_item not in \

                            self.pack[
                                found_item.item_type]: '''
'''if sale_item_key == 'i':
        self.hud()
        inventory_from_blacksmith = self.item_type_inventory('Weapons')
        if not inventory_from_blacksmith:
            print(f"Your weapons inventory is empty")
        os.system('pause')
        self.hud()
        continue'''
''' old blacksmith code
print("The following items are for sale:")
            print(f"Item             Level Requirement          Price")
            print(f"1 Shortsword             {short_sword.minimum_level}                    {short_sword.buy_price}   ")
            print(f"2 Broad Sword            {broad_sword.minimum_level}                    {broad_sword.buy_price}   ")
            print(
                f"3 Quantum Sword          {quantum_sword.minimum_level}                    {quantum_sword.buy_price}")
            print(f"You have {self.gold} gold pieces.")
            #sale_item_key = input("Enter item number to buy, (M)anage Wielded Weapons or (E)xit the blacksmith: ").lower()
            #if sale_item_key not in ('1', '2', '3', 'e', 'm'):'''
'''old blacksmith buy items code
sale_item = (sale_items_dict[sale_item_key])
            if self.gold >= sale_item.sell_price and sale_item not in (
                    self.pack[
                        'Weapons']) and sale_item != self.wielded_weapon and self.level >= sale_item.minimum_level:
                self.hud()
                print(f"You buy a {sale_item}")
                self.gold -= sale_item.buy_price
                (self.pack[sale_item.item_type]).append(sale_item)
                number_of_items = len(self.pack[sale_item.item_type])
                print(f"You now have {number_of_items} items in your {sale_item.item_type} inventory:")
                (self.pack[sale_item.item_type]).sort(key=lambda x: x.name)
                stuff_dict = Counter(item.name for item in self.pack[sale_item.item_type])
                for key, value in stuff_dict.items():
                    print(key)
                    # print(key, 's', ':    ', value, sep='')
                pause()
                continue
            elif self.gold < sale_item.sell_price:
                print(f"You do not have enough gold")
                sleep(1)
                self.hud()
                continue
            elif self.level < sale_item.minimum_level:
                print(f"The minimum level requirement is {sale_item.minimum_level}. You are level {self.level}")
                sleep(1)
                self.hud()
                continue
            else:
                print(f"You already have a {sale_item}")
                sleep(1)
                self.hud()
                continue'''
'''sale_items_dict = {'1': short_sword,
                           '2': broad_sword,
                           '3': quantum_sword
                           }'''
'''    def weapon_management(self):
    self.hud()
    if len(self.pack['Weapons']) > 0:
        print(f"Your current weapon inventory:")
        print(f"(Sorted by highest damage bonus)")
        (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus, reverse=True)
        weapon_mgmt_dict = {}
        for item in (self.pack['Weapons']):
            weapon_mgmt_dict[item] = (self.pack['Weapons']).index(item)
        for key, value in weapon_mgmt_dict.items():
            print(value + 1, ':', key)  # value is index. indexing starts at zero, so add 1
        print()

    else:
        print(f"You have nothing in your weapons inventory..")
        pause()
        return
    old_weapon = self.wielded_weapon
    print(f"Your current wielded weapon: "
          f"{self.wielded_weapon}\n"
          f"Damage bonus: {self.wielded_weapon.damage_bonus}\n"
          f"To hit bonus: {self.wielded_weapon.to_hit_bonus}\n")
    wield_or_exit = input(f"(S)wap wielded weapon, or go (B)ack: ").lower()
    if wield_or_exit == "b":
        return
    elif wield_or_exit == "s":
        try:
            new_weapon_index = int(input(f"Enter the number of the weapon you wish to wield: "))
            new_weapon_index -= 1  # again, indexing starts at 0 and is awkward
            self.wielded_weapon = (self.pack['Weapons'])[new_weapon_index]  # SYNTAX FOR INDEX
            # self.wielded_weapon = self.pack['Weapons']new_weapon  # find syntax...on the right track
        except (IndexError, ValueError):
            print("Invalid entry..")
            sleep(1)
            return
        print(f"You remove the {(self.pack['Weapons'])[new_weapon_index]} from your back and are now wielding it.\n"
              f"You place the {old_weapon} on your back.")

        (self.pack['Weapons']).pop(new_weapon_index)  # INDEX SYNTAX
        (self.pack['Weapons']).append(old_weapon)  # old_weapon represents an object, not an index
        (self.pack['Weapons']).sort(key=lambda x: x.damage_bonus)
        # self.pack.append(old_weapon)  # for the old list inventory method
        pause()'''
'''    def print_weapon_stats(self, weapon):
        print(f"{weapon.name}:")
        print(f"Damage bonus: {weapon.damage_bonus}")
        print(f"To hit: {weapon.to_hit_bonus}")
        print(f"Sell price: {weapon.sell_price}")
        print(f"Minimum level requirement: {weapon.minimum_level}")

    def print_armor_stats(self, armor):  # should be deprecated
        print(f"{armor.name}:")
        print(f"AC: {armor.ac}")
        print(f"Sell Price: {armor.sell_price}")
        print(f"Minimum level requirement: {armor.minimum_level}")

    def print_shield_stats(self, shield):  # should be deprecated
        print(f"{shield.name}:")
        print(f"AC: {shield.ac}")
        print(f"Sell Price: {shield.sell_price}")
        print(f"Minimum level requirement: {shield.minimum_level}")

    def print_boots_stats(self, boots):  # should be deprecated
        print(f"{boots.name}:")
        print(f"AC: {boots.ac}")
        print(f"Sell Price: {boots.sell_price}")
        print(f"Minimum level requirement: {boots.minimum_level}")'''
'''    def alternate_sell_chemist_items(self):  # redo this and make default if possible
        chemist_sell_dict = {
            'Healing': [healing_potion],
            'Town Portal Implements': [scroll_of_town_portal],
        }
        while True:
            # create a list of item types:
            item_type_lst = list(chemist_sell_dict.keys())
            # create a dictionary from list of item types, print out, add 1 to indexing
            item_type_dict = {}
            for item_type in item_type_lst:
                item_type_dict[item_type] = item_type_lst.index(item_type)
            for key, value in item_type_dict.items():
                print(value + 1, ':', key)
            print(f"Your gold: {self.gold} GP")
            sell = input("Display your (I)nventory, (P)ick item type, or go (B)ack: ").lower()
            if sell not in ('i', 'p', 'b'):
                self.hud()
                continue
            elif sell == 'i':
                self.inventory()
                continue
            elif sell == 'b':
                return
                # break
            elif sell == 'p':
                try:
                    item_type_index_to_buy = int(input(f"Enter the category of the item to sell by number: "))
                    item_type_to_buy = item_type_lst[item_type_index_to_buy - 1]
                except (IndexError, ValueError):
                    print("Invalid entry..")
                    sleep(1)
                    continue'''
'''            elif self.potions_of_healing > 0 and self.town_portals > 0:
                potion_or_scroll = dice_roll(1, 20)
                if potion_or_scroll > 10:
                    print(f"He steals a potion of healing.")
                    self.potions_of_healing -= 1
                    pause()
                    return True
                else:
                    print(f"He steals a scroll of town portal.")
                    self.town_portals -= 1
                    pause()
                    return True
            # if player has one or the other, potions are stolen first,
            elif self.potions_of_healing > 0:
                print(f"He steals a potion of healing.")
                self.potions_of_healing -= 1
                pause()
                return True
            elif self.town_portals > 0:
                print(f"He steals a scroll of town portal.")
                self.town_portals -= 1
                pause()
                return True'''
'''quantum_item_list = [self.potions_of_healing, self.town_portals]
            for quantum_item in quantum_item_list:
                if quantum_item < 1:
                    quantum_item_list.remove(quantum_item)
            print(quantum_item_list)
            if len(quantum_item_list):
                stolen_item = random.choice(quantum_item_list)
                if stolen_item == self.potions_of_healing:
                    print(f"He steals a potion of healing.")
                    quantum_item_list.remove(self.potions_of_healing)
                    self.potions_of_healing -= 1

                    pause()
                    return True
                elif stolen_item == self.town_portals:
                    print(f"He steals a scroll of town portal.")
                    quantum_item_list.remove(self.town_portals)
                    self.town_portals -= 1

                    pause()
                    return True'''
'''#elif self.position == ".":
#    print(f"You are in a rather wide open area of {self.dungeon.name}. There are exits in each direction...")

#    return
# DEAD ENDs - Only 1 exit!
# 1 exit to the north
        elif self.position == "1":
            print("You are at a dead end. Exit is to the north...")
            # sleep(1.5)
            return
        # 2 exit to the south
        elif self.position == "2":
            print("You are at a dead end. Exit is to the south...")
            # sleep(1.5)
            return
        # 3 exit to the east
        elif self.position == "3":
            print("You are at a dead end. Exit is to the east...")
            # sleep(1.5)
            return
        # 4 exit to the west
        elif self.position == "4":
            print("You are at a dead end. Exit is to the west...")
            # sleep(1.5)
            return
        # STRAIGHT HALLWAYs:

        # 5 exits north and south
        elif self.position == "5":
            print("You are in a corridor. Exits are to the North and South...")
            # sleep(1.5)
            return
        # 6 exits east and west
        elif self.position == "6":
            print("You are in a corridor. Exits are to the East and West...")
            # sleep(1.5)
            return
        # CORNERS:
        # 7 exits to the south and east UPPER LEFT
        elif self.position == "7":
            print(f"You are in a corner. Exits are to the South and East.")
            return
            # 8 exits to the north and east LOWER LEFT
        elif self.position == "8":
            print(f"You are in a corner. Exits are to the North and East.")
            return
            # 9 exits to the south and west UPPER RIGHT
        elif self.position == "9":
            print(f"You are in a corner. Exits are to the South and West.")
            return
            # "-" exits to the north and west LOWER RIGHT
        elif self.position == "-":
            print(f"You are in a corner. Exits are to the North and West.")
            return

        # WALLS:
        # |  exits to the south. east and west  NORTH WALL
        elif self.position == "|":
            print(f"You are against a wall to the North. Exits are to the South, East and West.")
            return
            # / exits to the north, east and west SOUTH WALL
        elif self.position == "/":
            print(f"You are against a wall to the South. Exits are to the North, East and West.")
            return
            # ( exits to the north, south and east WEST WALL
        elif self.position == "(":
            print(f"You are against a wall to the West. Exits are to the North, South and East.")
            return
            # ) exits to the north, south and west EAST WALL
        elif self.position == ")":
            print(f"You are against a wall to the East. Exits are to the North, South and West.")
            return'''
'''            elif sale_item_key == 'w':
                self.item_management('Weapons', self.wielded_weapon)
                # self.weapon_management()
                continue
            elif sale_item_key == 'a':
                self.item_management('Armor', self.armor)
                continue
            elif sale_item_key == 's':
                self.item_management('Shields', self.shield)
                continue
            elif sale_item_key == 'b':
                self.item_management('Boots', self.boots)
                continue
            elif sale_item_key == 'c':
                self.item_management('Cloaks', self.cloak)
                continue'''
'''                    if self.strength < 19:
                        ability_lst.append('strength')
                    if self.dexterity < 19:
                        ability_lst.append('dexterity')
                    if self.constitution < 19:
                        ability_lst.append('constitution')
                    if self.intelligence < 19:
                        ability_lst.append('intelligence')
                    if self.wisdom < 19:
                        ability_lst.append('wisdom')
                    if self.charisma < 19:
                        ability_lst.append('charisma')'''
'''                        if self.strength < 20:
                            ability_lst.append('strength')
                        if self.dexterity < 20:
                            ability_lst.append('dexterity')
                        if self.constitution < 20:
                            ability_lst.append('constitution')
                        if self.intelligence < 20:
                            ability_lst.append('intelligence')
                        if self.wisdom < 20:
                            ability_lst.append('wisdom')
                        if self.charisma < 20:
                            ability_lst.append('charisma')'''
'''print(f"You may choose:\n1. Improve 1 ability by 2 points\nor\n"
                      f"2. Improve 2 abilities by 1 point ")
                one_or_two = input(f"Your choice (1 / 2): ")
                if one_or_two not in ('1', '2'):
                    continue
                elif one_or_two == '1':
                    self.hud()
                    ability_dict = self.__dict__  # create variable as actual copy of player dict attribute
                    # create ability list
                    ability_lst = []
                    # create a working dictionary for all abilities
                    working_dict = {'strength': self.strength, 'dexterity': self.dexterity,
                                    'constitution': self.constitution, 'intelligence': self.intelligence,
                                    'wisdom': self.wisdom, 'charisma': self.charisma}
                    for key, value in working_dict.items():
                        if value < 19:
                            ability_lst.append(key)
                    # add all keys for values less than 19 to the ability list
                    if not len(ability_lst):  # if list is empty, no more improvements allowed
                        print(f"You cannot improve any of your abilities by 2. "
                              f"You can max out a 19 score with option 2.")
                        pause()
                        continue
                    # create a subset ability dictionary from ability list by indexing, and then print out
                    # this dictionary is the resulting abilities with indexed keys corresponding to each
                    ability_dict_subset_too = {}
                    for ability in ability_lst:
                        if len(ability_lst):
                            ability_dict_subset_too[ability_lst.index(ability)] = ability
                            # ability_dict_subset_too[ability] = ability_lst.index(ability)  # <-reverses key and value!
                    for key, value in ability_dict_subset_too.items():
                        print(key + 1, ':', value.capitalize())  # add one because indexing starts at zero
                    try:
                        one_ability = int(
                            input(f"Enter the number of the ability you wish to improve by 2 points. "
                                  f"(NOTE: This is permanent!): "))
                        one_ability -= 1  # subtract one because indexing starts at 0
                        ability_to_improve = (ability_dict_subset_too[one_ability])
                        old_score = ability_dict[ability_to_improve]
                        ability_dict[ability_to_improve] += 2
                        print(f"Your {ability_to_improve} has been increased from "
                              f"{old_score} to {ability_dict[ability_to_improve]}!")
                        print(f"The dungeon horde also grows in power...")
                        self.calculate_modifiers()
                        # pause()
                        return
                    except(ValueError, KeyError):
                        print("Invalid entry..")
                        sleep(1)
                        continue'''
''' def necrotic_dot(self, dot_multiplier):
        self.dot_multiplier = dot_multiplier
        self.hud()
        rndm_necrotic_phrases = ["You feel absolute dread and withering overcoming you..",
                                 "An unnerving pain, planted like a seed, germinates within you...",
                                 "Agony creeps into your very veins..."
                                 ]
        necrotic_phrase = random.choice(rndm_necrotic_phrases)
        print(f"{necrotic_phrase}")
        sleep(1.5)
        print(f"Necrotic forces ravage through your body!")
        self.necrotic = True
        self.necrotic_turns = 0

        pause()

        self.hud()
        return self.necrotic'''
'''            elif self.potions_of_healing > 0 and self.potions_of_strength > 0 and self.town_portals > 0 and self.elixirs > 0:
                potion_or_scroll = dice_roll(1, 4)
                if potion_or_scroll == 1:
                    print(f"He steals a potion of healing.")
                    self.potions_of_healing -= 1
                    pause()
                    return True
                elif potion_or_scroll == 2 and self.potions_of_strength > 0:
                    print(f"He steals a potion of strength.")
                    self.potions_of_strength -= 1
                    pause()
                    return True
                elif potion_or_scroll == 3 and self.town_portals > 0:
                    print(f"He steals a scroll of town portal.")
                    self.town_portals -= 1
                    pause()
                    return True
                elif potion_or_scroll == 4 and self.town_portals > 0:
                    print(f"He steals a clarifying elixir.")
                    self.elixirs -= 1
                    pause()
                    return True
            # if player has one or the other- make this into lists and dictionaries in the future!

            elif self.potions_of_healing > 0:
                print(f"He steals a potion of healing.")
                self.potions_of_healing -= 1
                pause()
                return True
            elif self.potions_of_strength > 0:
                print(f"He steals a potion of strength.")
                self.potions_of_strength -= 1
                pause()
                return True
            elif self.elixirs > 0:
                print(f"He steals a clarifying elixir.")
                self.elixirs -= 1
                pause()
                return True
            elif self.town_portals > 0:
                print(f"He steals a scroll of town portal.")
                self.town_portals -= 1
                pause()
                return True
'''
