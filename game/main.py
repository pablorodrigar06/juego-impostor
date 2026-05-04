from game.game_config import GameConfig, Difficulty
from game.player import Player
from game.game_manager import GameManager

def main():
    players = [
        Player("Jugador 1"),
        Player("Jugador 2"),
        Player("Jugador 3"),
        Player("Jugador 4"),
    ]

    config = GameConfig(
        number_of_players=4,
        rounds=3,
        difficulty=Difficulty.EASY
    )

    game = GameManager(players, config)

    while not game.game_is_over():
        current_round = game.start_round()

        print(f"\n--- RONDA {current_round.number} ---")

        # Mostrar palabra de forma individual
        for player in players:
            input(f"\n{player.name}, pulsa ENTER para ver tu palabra...")
            print(current_round.word_for_player(player))
            input("Pulsa ENTER para continuar...")
            print("\n" * 50)

        # Votación
        for player in players:
            vote = input(f"{player.name}, ¿quién es el impostor?: ")
            current_round.vote(player, vote)

        result = game.finish_round()

        print("\nResultado:")
        print(result)

    print("\n🏆 PUNTUACIONES:")
    for name, score in game.scoreboard():
        print(f"{name}: {score}")


if __name__ == "__main__":
    main()