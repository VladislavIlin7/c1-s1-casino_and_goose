class Chip:
    def __init__(self, value: int):
        self.value: int = value

    def __add__(self, other: Chip) -> Chip:
        """
        Складываем две фишки и получаем новую с суммой номиналов

        :param other: фишка с каким-то номиналом
        :return: фишка с новым номиналом
        """
        return Chip(self.value + other.value)

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта"""
        return f"Chip({self.value}$)"
