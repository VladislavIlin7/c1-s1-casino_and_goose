from src.models.player import Player


class PlayerCollection:
    def __init__(self):
        self._items: list[Player] = []