class Player:
    def __init__(self, name: str, balance: int = 0):
        self.name: str = name
        self.balance: int = balance

    def change_balance(self, delta: int) -> None:
        """
        Изменяет баланс игрока

        :param delta: на сколько надо изменить баланс
        :return: None
        """
        self.balance += delta

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"Player({self.name}, balance={self.balance})"
