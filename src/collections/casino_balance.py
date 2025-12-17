class CasinoBalance:
    def __init__(self):
        self._balances: dict[str, int] = {}

    def update_balance(self, name: str, delta: int):
        """Метод для изменения баланса"""
        if name not in self._balances:
            raise KeyError(f"Игрок '{name}' не найден в CasinoBalance")

        new_balance = self._balances[name] + delta
        self[name] = new_balance

    def add_player(self, name: str, balance: int):
        """Добавление игрока"""
        self[name] = balance

    def remove_player(self, name: str):
        """Удалить игрока"""
        if name not in self._balances:
            raise KeyError(f"Игрок '{name}' не найден")
        print(f"Игрок '{name}' удалён")
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
            print(f"Добавлен игрок '{name}' с балансом {new_balance}$")
        else:
            print(f"{name}: {old}$ -> {new_balance}$")

    def __repr__(self):
        return f"CasinoBalance({self._balances}$)"
