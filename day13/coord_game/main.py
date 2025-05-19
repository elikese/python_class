from game import CoordGame

if __name__ == "__main__":
    game_options = {
        "map_size": 5,
        "player_start": (0, 0),
        "goal": (4, 4),
        "obstacles": [(1, 0), (2, 2), (3, 1)],
    }

    game = CoordGame(**game_options)
    game.run()
