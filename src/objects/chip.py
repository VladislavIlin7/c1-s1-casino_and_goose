class Chip:
    def __init__(self, value: int):
        # if value <= 0:
        #     raise ValueError("Значение фишки должно быть положительным")
        self.value: int = value

    def __add__(self, other: Chip) -> Chip:
        """
        Складываем две фишки и получаем новую с суммой номиналов

        :param other: фишка с каким-то номиналом
        :return: фишка с новым номиналом
        """
        return Chip(self.value + other.value)

    def __repr__(self) -> str:
        return f"Chip({self.value}$)"