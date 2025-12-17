import logging

from src.objects.goose import Goose

logger = logging.getLogger(__name__)

class GooseCollection:
    def __init__(self):
        self._items: list[Goose] = []

    def add(self, goose: Goose) -> None:
        """Добавить гуся"""
        self._items.append(goose)

    def remove(self, goose: Goose) -> None:
        """Удалить гуся по объекту"""
        self._items.remove(goose)

    def remove_by_name(self, name: str) -> None:
        """Удалить гуся по имени"""
        for g in self._items:
            if g.name == name:
                self._items.remove(g)
                return
        logger.info(f"Гусь '{name}' не найден")
        return

    def get_by_index(self, n: int) -> Goose | None:
        if n < 0 or n >= len(self._items):
            return None
        return self._items[n]

    def __len__(self):
        """Количество гусей"""
        return len(self._items)

    def __iter__(self):
        """Итерация по гусям"""
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Goose:
        """
        Поддержка индексов и срезов
        index может быть int или slice
        """
        return self._items[index]

    def __repr__(self):
        return f"GooseCollection({self._items})"
