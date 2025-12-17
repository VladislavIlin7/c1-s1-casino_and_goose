from src.objects.player import Player


class PlayerCollection:
    def __init__(self):
        self._items: list[Player] = []

    def add(self, player: Player) -> None:
        """Добавляет игрока в коллекцию"""
        self._items.append(player)

    def remove(self, player: Player) -> None:
        """Удаляет игрока по объекту"""
        self._items.remove(player)

    def remove_by_name(self, name: str) -> None:
        """Удаляет игрока по имени"""
        for p in self._items:
            if p.name == name:
                self._items.remove(p)
                return
        raise ValueError(f"Игрок '{name}' не найден")

    def find_by_name(self, name: str) -> Player | None:
        """Возвращает игрока по имени или None"""
        for p in self._items:
            if p.name == name:
                return p
        return None

    def __len__(self) -> int:
        """Возвращает количество игроков"""
        return len(self._items)

    def __iter__(self):
        """Позволяет итерироваться по коллекции"""
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Player:
        """
        Поддержка индексов и срезов.
        index может быть int или slice.
        """
        return self._items[index]
