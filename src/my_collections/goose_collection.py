import logging

from src.exception.exception import (
    GooseAlreadyExistsException,
    GooseNotFoundException,
    IndexOutOfRangeException, ZeroSlicesException,
)
from src.objects.goose import Goose

logger = logging.getLogger(__name__)

class GooseCollection:
    def __init__(self):
        self._items: list[Goose] = []

    def add(self, goose: Goose) -> None:
        """Добавить гуся"""
        for g in self._items:
            if g.name == goose.name:
                raise GooseAlreadyExistsException(goose.name)
        self._items.append(goose)

    def remove(self, goose: Goose) -> None:
        """Удалить гуся по объекту"""
        if goose not in self._items:
            raise GooseNotFoundException(goose.name)
        self._items.remove(goose)

    def remove_by_name(self, name: str) -> None:
        """Удалить гуся по имени"""
        for g in self._items:
            if g.name == name:
                self._items.remove(g)
                return
        raise GooseNotFoundException(name)

    def get_by_index(self, index: int) -> Goose:
        """Возвращает гуся по индексу"""
        if index < 0 or index >= len(self._items):
            raise IndexOutOfRangeException(index)
        return self._items[index]

    def __len__(self):
        """Количество гусей"""
        return len(self._items)

    def __iter__(self):
        """Итерация по гусям"""
        return iter(self._items)

    def __getitem__(self, index: int | slice) -> Goose | list[Goose]:
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
        return f"GooseCollection({self._items})"
