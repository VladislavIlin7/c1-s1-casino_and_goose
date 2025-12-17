import logging
import sys

from src.simulation import run_simulation


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    run_simulation(steps=20, seed=52)


if __name__ == "__main__":
    main()

