import random
class Player:

    def __init__(self,name,constitution,intelligence,wisdom,strength,dexterity):
        self.name = name
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.strength = strength
        self.dexterity = dexterity

    def navigate(self):
        print("The player is navigating")

    def swing(self, dexterity, strength):
        player_roll20 = random.randint(1,20)
        print(f"Player rolls {player_roll20}")
        dexterity_modifier = (dexterity - 10) / 2
        print(f"Dexterity modifier {dexterity_modifier}")
        monster_roll20 = random.randint(1,20)
        print(f"Monster rolls {monster_roll20}")
        if player_roll20 + dexterity_modifier > monster_roll20:
            player_roll12 = random.randint(1,12)
            strength_modifier = (strength - 10) / 2
            damage_to_monster = player_roll12 + strength_modifier
            print (f"Player hits for {dexterity_modifier} points of damage!")
        else:
            print(f"Player misses..")


    def heals(self):
        print(f"{self.name} takes a restorative tincture")

