    if monster.can_drain:
        level_drain = monster.drain(monster.wisdom, monster.wisdom_modifier,
                                    player_1.level, player_1.wisdom,
                                    player_1.wisdom_modifier)
        if level_drain:  # try to offload this logic
            print("It drains a level!\nYou go down a level!!")
            player_1.level -= 1
            player_1.experience *= .50
            if player_1.level < 1:
                print(f"You have died from drainage!!!!!")
                in_proximity_to_monster = False
                in_dungeon = False
                in_town = False
                break

        else:
            print(f"You have {player_1.hit_points} out of a maximum "
                  f"{player_1.maximum_hit_points} hit points, and"
                  f" {player_1.experience} experience. "
                  f"You are level {player_1.level}")
            continue
