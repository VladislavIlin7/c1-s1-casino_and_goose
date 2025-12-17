from src.exception.exception import (
    IndexOutOfRangeException,
    PlayerAlreadyExistsException,
    PlayerNotFoundException, ZeroSlicesException,
)
from src.objects.player import Player


class PlayerCollection:
    def __init__(self):
        self._items: list[Player] = []

    def add(self, player: Player) -> None:
        """Добавляет игрока в коллекцию"""
        for p in self._items:
            if p.name == player.name:
                raise PlayerAlreadyExistsException(player.name)
        self._items.append(player)

    def remove(self, player: Player) -> None:
        """Удаляет игрока по объекту"""
        if player not in self._items:
            raise PlayerNotFoundException(player.name)
        self._items.remove(player)

    def remove_by_name(self, name: str) -> None:
        """Удаляет игрока по имени"""
        for p in self._items:
            if p.name == name:
                self._items.remove(p)
                return
        raise PlayerNotFoundException(name)

    def find_by_name(self, name: str) -> Player | None:
        """Возвращает игрока по имени или None"""
        for p in self._items:
            if p.name == name:
                return p
        return None

    def get_by_index(self, n: int) -> Player:
        """Возвращает игрока по индексу"""
        if n < 0 or n >= len(self._items):
            raise IndexOutOfRangeException(n)
        return self._items[n]

    def __len__(self) -> int:
        """Возвращает количество игроков"""
        return len(self._items)

    def __iter__(self):
        """Позволяет итерироваться по коллекции"""
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Player | list[Player]:
        """
        Поддержка индексов и срезов
        index может быть int или slice
        """
        if isinstance(index, int):
            if index < 0 or index >= len(self._items):
                raise IndexOutOfRangeException(index)

            return self._items[index]

        if index.step == 0:
            raise ZeroSlicesException()
        return self._items[index]

    def __repr__(self):
        """Возвращает строковое представление объекта"""
        return f'PlayerCollection({self._items})'