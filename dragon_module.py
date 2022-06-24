from monster_class_module import *


class Dragon(Monster):

    def breathe_fire(self, strength):
        print("The Dragon breathes fire!")
        fire_damage_to_player = strength + dice_roll(1, 20)
        print(f"It does {fire_damage_to_player} points of damage!")
        return fire_damage_to_player
