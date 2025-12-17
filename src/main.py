import logging
import sys

from src.simulation import run_simulation


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    print('Введите сначала сколько шагов должна выполнить симуляция потом сид(если он не важен то введите None)')

    while sys.stdin:
        raw_steps = input("steps = ").strip()
        try:
            steps = int(raw_steps)
            if steps < 0:
                logging.info("steps не может быть отрицательным")
                continue
            break
        except ValueError:
            logging.info("steps должен быть целым числом")


    raw_seed = input("seed = ").strip()
    if raw_seed.lower() == "none" or raw_seed == "":
        seed = None
    else:
        try:
            seed = int(raw_seed)
        except ValueError:
            logging.info("seed должен быть целым неотрицательным числом или None, поэтому будет использован None")
            seed = None

    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    main()
