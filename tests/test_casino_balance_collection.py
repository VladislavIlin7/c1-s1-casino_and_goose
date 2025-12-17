import pytest
from src.exception.exception import (
    PlayerAlreadyExistsException,
    PlayerNotFoundException,
)
from src.my_collections.casino_balance import CasinoBalance


def test_balance():
    b = CasinoBalance()
    assert len(b) == 0
    b.add_player("Alex", 10)
    assert len(b) == 1
    assert b["Alex"] == 10
    b.update_balance("Alex", 5)
    assert b["Alex"] == 15
    b["Alex"] = 7
    assert b["Alex"] == 7
    assert list(b) == ["Alex"]


def test_balance_remove():
    b = CasinoBalance()
    b.add_player("Alex", 10)
    b.remove_player("Alex")

    assert len(b) == 0


def test_balance_errors():
    b = CasinoBalance()
    b.add_player("Alex", 10)

    with pytest.raises(PlayerAlreadyExistsException):
        b.add_player("Alex", 20)


def test_balance_player_not_found_remove():
    b = CasinoBalance()

    with pytest.raises(PlayerNotFoundException):
        b.remove_player("Oleg")


def test_balance_player_not_found_getitem():
    b = CasinoBalance()

    with pytest.raises(PlayerNotFoundException):
        _ = b["NonExistent"]
