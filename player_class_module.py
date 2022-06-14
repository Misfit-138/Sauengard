import random


class Player:

    def __init__(self, name, level, gold, sword, armor, shield, constitution, intelligence, wisdom, strength,
                 dexterity):
        self.name = name
        self.level = level
        self.gold = gold
        self.sword = sword
        self.armor = armor
        self.shield = shield
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity

    def navigate(self):
        print("The player is navigating")

    def swing(self, dexterity, strength, sword):
        player_roll20 = random.randint(1, 20)
        dexterity_modifier = round((dexterity - 10) / 2)
        monster_roll20 = random.randint(1, 20)
        player_roll12 = random.randint(1, 12)
        strength_modifier = round((strength - 10) / 2)
        damage_to_monster = round(player_roll12 + strength_modifier + sword)
        print(f"Player rolls 20 sided die---> {player_roll20}")
        print(f"Dexterity modifier {dexterity_modifier}")
        print(f"Monster rolls 20 sided die ---> {monster_roll20}")
        if player_roll20 + dexterity_modifier > monster_roll20:
            print(f"Player hits!")
            print(f"Player rolls 12 sided die---> {player_roll12}")
            print(f'Strength modifier---> {strength_modifier}')
            print (f"Player does {damage_to_monster} points of damage!")
        else:
            print(f"Player misses..")
            return


    def heals(self):
        print(f"{self.name} takes a restorative tincture")
