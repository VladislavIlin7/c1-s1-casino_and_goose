from src.models.goose import Goose


class GooseCollection:
    def __init__(self):
        self._items: list[Goose] = []

    def __len__(self):
        """Количество гусей"""
        return len(self._items)

    def __iter__(self):
        """Итерация по гусям"""
        return iter(self._items)

    def __getitem__(self, index):
        """Доступ по индексу и срезу"""
        return self._items[index]

    def __repr__(self):
        return f"GooseCollection({self._items})"

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
        raise ValueError(f"Гусь '{name}' не найден")

    def get_random(self):
        """Вернуть случайного гуся"""
        if not self._items:
            return None
        import random
        return random.choice(self._items)
