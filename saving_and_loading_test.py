# Step 1
import pickle
from player_class_module import Player
'''config_dictionary = {'remote_hostname': 'google.com', 'remote_port': 80}

# Step 2
with open('config.dictionary', 'wb') as player_save:
    # Step 3
    pickle.dump(config_dictionary, player_save)'''


'''class Player:

    def __init__(self):
        self.name = "Trett"


player_2 = Player()
with open('player.sav', 'wb') as player_save:
    pickle.dump(player_2, player_save)
'''
with open('player.sav', 'rb') as player_save:
    player_2 = pickle.load(player_save)

    # After config_dictionary is read from file
    print(player_2.name)
    print(f"                                                                     Name: {player_2.name}")
    print(f"                                                                     Level: {player_2.level}")
    print(f"                                                                     Experience: {player_2.experience}")
    print(f"                                                                     Gold: {player_2.gold}")
    print(f"                                                                     Weapon + {player_2.weapon}")
    print(f"                                                                     Armor Class {player_2.armor_class}")
    print(f"                                                                     Shield + {player_2.shield}")
    print(f"                                                                     Constitution {player_2.constitution}")
    print(f"                                                                     Intelligence: {player_2.intelligence}")
    print(f"                                                                     Wisdom: {player_2.wisdom}")
    print(f"                                                                     Strength: {player_2.strength}")
    print(f"                                                                     Dexterity: {player_2.dexterity}")
    print(f"                                                                     Charisma: {player_2.charisma}")
    print(f"                                                                     Hit points: {player_2.hit_points}/"
          f"{player_2.maximum_hit_points}")