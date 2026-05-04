from dataclasses import dataclass


@dataclass
class Player:
    name: str
    is_impostor: bool = False
    score: int = 0
    vote: str | None = None

    def reset_for_round(self) -> None:
        self.is_impostor = False
        self.vote = None