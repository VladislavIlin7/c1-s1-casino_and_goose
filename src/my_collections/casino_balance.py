import logging

logger = logging.getLogger(__name__)


class CasinoBalance:
    def __init__(self):
        self._balances: dict[str, int] = {}

    def update_balance(self, name: str, delta: int):
        """Метод для изменения баланса"""
        if name not in self._balances:
            self.add_player(name, delta)
            return

        new_balance = self._balances[name] + delta
        self[name] = new_balance

    def add_player(self, name: str, balance: int):
        """Добавление игрока"""
        if name in self._balances:
            return logger.info("Игрок с этим именем существует")
        self[name] = balance
        return None

    def remove_player(self, name: str):
        """Удалить игрока"""
        if name not in self._balances:
            logger.info(f"Игрок '{name}' не найден")
            return
        logger.info(f"Игрок '{name}' удалён")
        del self._balances[name]

    def __len__(self):
        """Сколько игроков хранится"""
        return len(self._balances)

    def __iter__(self):
        """Итерация по именам игроков"""
        return iter(self._balances)

    def __getitem__(self, name: str) -> int:
        """Получение баланса по имени"""
        return self._balances[name]

    def __setitem__(self, name: str, new_balance: int) -> None:
        """Изменение баланса"""
        old = self._balances.get(name, None)
        self._balances[name] = new_balance

        if old is None:
            logger.info(f"Добавлен игрок '{name}' с балансом {new_balance}$")
        else:
            logger.info(f"{name}: {old}$ -> {new_balance}$")

    def __repr__(self):
        return f"CasinoBalance({self._balances}$)"
