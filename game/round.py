from dataclasses import dataclass, field

from game.player import Player


@dataclass
class Round:
    number: int
    word: str
    impostor: Player
    players: list[Player]
    descriptions: dict[str, str] = field(default_factory=dict)

    def word_for_player(self, player: Player) -> str:
        if player.is_impostor:
            return "IMPOSTOR"
        return self.word.upper()

    def add_description(self, player: Player, description: str) -> None:
        self.descriptions[player.name] = description

    def vote(self, voter: Player, suspect_name: str) -> None:
        if suspect_name not in {player.name for player in self.players}:
            raise ValueError("Ese jugador no existe.")
        voter.vote = suspect_name

    def most_voted_player(self) -> Player | None:
        counts: dict[str, int] = {}
        for player in self.players:
            if player.vote:
                counts[player.vote] = counts.get(player.vote, 0) + 1

        if not counts:
            return None

        max_votes = max(counts.values())
        winners = [name for name, total in counts.items() if total == max_votes]
        if len(winners) > 1:
            return None

        winner_name = winners[0]
        return next(player for player in self.players if player.name == winner_name)

    def impostor_was_found(self) -> bool:
        selected = self.most_voted_player()
        return selected is not None and selected.name == self.impostor.name

