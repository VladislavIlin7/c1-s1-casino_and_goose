from src.collections.player_collection import PlayerCollection
from src.objects.player import Player


class Goose:
    def __init__(self, name: str, honk_volume: int = 1):
        self.name: str = name
        self.honk_volume: int = honk_volume

    def honk(self) -> str:
        return f"{self.name} HONK с громкостью {self.honk_volume})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, honk_volume={self.honk_volume})"


class WarGoose(Goose):
    def attack(self, player: Player) -> str:
        """
        Отнимаем у игрока часть денег

        :param player: Игрок
        :return: сколько украли $
        """
        damage: int = self.honk_volume * 10
        player.change_balance(-damage)
        return f"{self.name} атакует {player.name} и отнимает {damage}$!"


class HonkGoose(Goose):
    def super_honk(self, players: PlayerCollection) -> str:
        """
        Гусь громко кричит и у всех игроков уменьшается баланс

        :param players: все игроки
        :return: None
        """

        loss = self.honk_volume
        for player in players:
            player.change_balance(-loss)

        return f"{self.name} очень громко закричал! Все игроки потеряли {loss}$!"
