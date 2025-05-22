from game import CoordGame
from map import Map
from player import Player


if __name__ == "__main__":
    map_options = {
        "size": 5,
        "goal": (4, 4),
        "obstacles": [(1, 0), (2, 2), (3, 1)],
    }
    player_options = {
        "start_position": (0, 0),
    }

    map_instance = Map(**map_options)
    player_instance = Player(**player_options)
    game = CoordGame(map_instance, player_instance)
    game.run()
