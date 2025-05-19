from game import Game

if __name__ == "__main__":
    game = Game(
        size=5,
        player_pos=(0, 0),
        goal=(4, 4),
        enemy_data=[
            ((1, 0), 30, 10),
            ((2, 2), 40, 15),
            ((3, 3), 25, 20),
        ],
        max_moves=30,
    )
    game.run()
