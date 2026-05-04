import random

from game.game_config import GameConfig
from game.player import Player
from game.round import Round
from game.word_manager import WordManager

class GameManager:
    def __init__(
        self,
        players: list[Player],
        config: GameConfig,
        word_manager: WordManager | None = None,
    ) -> None:
        config.validate()
        if len(players) != config.number_of_players:
            raise ValueError("La cantidad de jugadores no coincide con la configuracion.")

        self.players = players
        self.config = config
        self.word_manager = word_manager or WordManager()
        self.current_round: Round | None = None
        self.round_history: list[Round] = []

    def start_round(self) -> Round:
        round_number = len(self.round_history) + 1
        if round_number > self.config.rounds:
            raise ValueError("Ya se jugaron todas las rondas.")

        for player in self.players:
            player.reset_for_round()

        impostor = random.choice(self.players)
        impostor.is_impostor = True
        word = self.word_manager.get_word(self.config.difficulty)

        self.current_round = Round(
            number=round_number,
            word=word,
            impostor=impostor,
            players=self.players,
        )

        if self.current_round is None:
            raise Exception("Error: no se creó la ronda correctamente")

        return self.current_round

    def finish_round(self) -> dict[str, object]:
        if self.current_round is None:
            raise ValueError("No hay una ronda activa.")

        round_result = {
            "round": self.current_round.number,
            "word": self.current_round.word,
            "impostor": self.current_round.impostor.name,
            "found": self.current_round.impostor_was_found(),
            "most_voted": None,
        }

        most_voted = self.current_round.most_voted_player()
        if most_voted:
            round_result["most_voted"] = most_voted.name

        if round_result["found"]:
            for player in self.players:
                if not player.is_impostor:
                    player.score += 1
        else:
            self.current_round.impostor.score += 2

        self.round_history.append(self.current_round)
        self.current_round = None
        return round_result

    def game_is_over(self) -> bool:
        return len(self.round_history) >= self.config.rounds

    def scoreboard(self) -> list[tuple[str, int]]:
        return sorted(
            ((player.name, player.score) for player in self.players),
            key=lambda item: item[1],
            reverse=True,
        )