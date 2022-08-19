from player_module_old import *

found_item = short_axe


def found_item_calculation(self, found_item):
    if found_item.item_type_to_sell == 'Weapons':
        if self.wielded_weapon.damage_bonus < self.level:
            found_item.damage_bonus = (self.level + 1)
            if found_item.name == self.wielded_weapon.name:
                print(
                    f"Quantum wierdness fills the air...\nYour {self.wielded_weapon} is enhanced to + {found_item.damage_bonus}!")
                self.wielded_weapon.damage_bonus = found_item.damage_bonus
                pause()
                return
            else:
                print(
                    f"You are currently wielding a {self.wielded_weapon}. Damage bonus: {self.wielded_weapon.damage_bonus}")
                print(f"The {found_item}'s damage bonus is {found_item.damage_bonus}.")
            while True:
                replace_weapon = input(f"Do you wish to wield it instead? y/n: ").lower()
                if replace_weapon == 'y':
                    self.wielded_weapon = found_item
                    print(f"You are now wielding the {found_item}")
                    return
                elif replace_weapon == 'n':
                    return
                elif replace_weapon not in ("y", "n"):
                    continue
    else:
        return


while True:
    replace_weapon = input(f"Do you wish to wield it instead? y/n: ").lower()
    if replace_weapon == 'y':
        wielded_weapon = found_item
        print(f"You are now wielding the {found_item}")
        break
    elif replace_weapon == 'n':
        print("This should stop")
        break
    elif replace_weapon not in ("y", "n"):
        continue
