from tennis_game import TennisGame


def main():
    game = TennisGame("Serena Williams", "Venus Williams")

    print(game.get_score())

    game.won_point("player1")
    print(game.get_score())

    game.won_point("player1")
    print(game.get_score())

    game.won_point("player2")
    print(game.get_score())

    game.won_point("player1")
    print(game.get_score())

    game.won_point("player2")
    print(game.get_score())

    game.won_point("player2")
    print(game.get_score())

    game.won_point("player2")
    print(game.get_score())

    game.won_point("player2")
    print(game.get_score())




if __name__ == "__main__":
    main()
