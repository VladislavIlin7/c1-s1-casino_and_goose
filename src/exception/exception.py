class PlayerAlreadyExistsException(Exception):
    def __init__(self, name: str):
        super().__init__(f"Игрок с именем '{name}' уже существует")


class GooseAlreadyExistsException(Exception):
    def __init__(self, name: str):
        super().__init__(f"Гусь с именем '{name}' уже существует")


class IndexOutOfRangeException(Exception):
    def __init__(self, index: int):
        super().__init__(f'Индекс "{index}" вне диапазона')


class PlayerNotFoundException(Exception):
    def __init__(self, player_name: str = None):
        super().__init__(f'Игрок "{player_name}" не найден')


class GooseNotFoundException(Exception):
    def __init__(self, player_name: str = None):
        super().__init__(f'Гусь "{player_name}" не найден')


class ZeroSlicesException(Exception):
    def __init__(self):
        super().__init__('Шаг среза не может быть равен нулю')


class NegativeArgumentException(Exception):
    def __init__(self):
        super().__init__('Количество шагов в симуляции не может быть < 0')
