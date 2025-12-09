from src.collections.player_collection import PlayerCollection
from src.models.player import Player


class Goose:
    def __init__(self):
        self.name: str
        self.honk_volume: float

    def honk(self):
        pass


class WarGoose(Goose):
    def attack(self, player: Player) -> float:
        pass


class HonkGoose(Goose):
    def super_honk(self, players: PlayerCollection | list[Player]) -> None:
        pass