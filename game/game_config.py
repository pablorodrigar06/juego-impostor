from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class GameConfig:
    def __init__(self, number_of_players: int, rounds: int, difficulty: Difficulty):
        self.number_of_players = number_of_players
        self.rounds = rounds
        self.difficulty = difficulty

    def validate(self):
        if self.number_of_players < 3:
            raise ValueError("Debe haber al menos 3 jugadores.")

        if self.rounds <= 0:
            raise ValueError("Debe haber al menos una ronda.")

        if not isinstance(self.difficulty, Difficulty):
            raise ValueError("Dificultad inválida.")