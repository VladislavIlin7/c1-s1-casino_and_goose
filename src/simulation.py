import logging
import random

from src.exception.exception import NegativeArgumentException
from src.objects.casino import Casino
from src.objects.goose import WarGoose, HonkGoose, Goose

logger = logging.getLogger(__name__)


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """Запускает симуляцию казино"""
    if steps < 0:
        raise NegativeArgumentException()

    if seed is not None:
        random.seed(seed)

    casino = Casino()

    casino.register_player("Alex", initial_balance=150)
    casino.register_player("Ali", initial_balance=80)
    casino.register_player("Subo", initial_balance=120)

    casino.register_goose(Goose("Гусар", honk_volume=2))
    casino.register_goose(WarGoose("Рэмбо", honk_volume=5))
    casino.register_goose(HonkGoose("Крикун", honk_volume=3))

    logger.info("=== Симуляция запущена ===")
    for step in range(steps):
        logger.info("")
        logger.info(f"Шаг {step + 1}")
        casino.simulate_step()
    logger.info("Симуляция окончена")
