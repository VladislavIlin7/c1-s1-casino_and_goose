import pytest

from src.exception.exception import NegativeArgumentException
from src.simulation import run_simulation


def test_simulation_runs():
    run_simulation()

def test_simulation_many_steps():
    run_simulation(100)

def test_simulation_seed():
    run_simulation(10, seed=42)

def test_negative_steps():
    with pytest.raises(NegativeArgumentException):
        run_simulation(-10)
