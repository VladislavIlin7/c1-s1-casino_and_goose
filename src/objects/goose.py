from src.my_collections.player_collection import PlayerCollection
from src.objects.player import Player


class Goose:
    def __init__(self, name: str, honk_volume: int = 1):
        self.name: str = name
        self.honk_volume: int = honk_volume

    def honk(self) -> str:
        """Возвращает с какой громкостью гусь кричит"""
        return f"{self.name} HONK с громкостью {self.honk_volume})"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"{self.__class__.__name__}(name={self.name}, honk_volume={self.honk_volume})"


class WarGoose(Goose):
    def attack(self, player: Player) -> int:
        """
        Отнимаем у игрока часть денег
        :return: сколько отняли
        """
        damage: int = self.honk_volume * 10
        player.change_balance(-damage)
        return damage


class HonkGoose(Goose):
    def super_honk(self, players: PlayerCollection) -> str:
        """
        Гусь громко кричит и у всех игроков уменьшается баланс
        :return: текст сообщения (чтобы Casino его вывел)
        """
        loss = self.honk_volume
        for player in players:
            player.change_balance(-loss)

        return f"{self.name} очень громко закричал! Все игроки потеряли {loss}$!"
