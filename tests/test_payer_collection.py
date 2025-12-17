import pytest
from src.exception.exception import (
    IndexOutOfRangeException,
    PlayerAlreadyExistsException,
    PlayerNotFoundException,
)
from src.my_collections.player_collection import PlayerCollection
from src.objects.player import Player


def test_players():
    pc = PlayerCollection()
    assert len(pc) == 0

    a = Player("A", 10)
    b = Player("B", 20)
    c = Player("C", 30)

    pc.add(a)
    pc.add(b)
    pc.add(c)

    assert len(pc) == 3
    assert pc[0].name == "A"
    assert [p.name for p in pc[1:]] == ["B", "C"]
    assert [p.name for p in pc] == ["A", "B", "C"]


def test_players_find_remove():
    pc = PlayerCollection()
    x = Player("X", 1)
    pc.add(x)

    assert pc.find_by_name("X") is x
    assert pc.find_by_name("NO") is None

    pc.remove_by_name("X")
    assert len(pc) == 0

    with pytest.raises(PlayerNotFoundException):
        pc.remove_by_name("X")


def test_player_already_exists():
    pc = PlayerCollection()
    a = Player("A", 10)
    pc.add(a)

    with pytest.raises(PlayerAlreadyExistsException):
        pc.add(Player("A", 20))


def test_player_not_found_remove():
    pc = PlayerCollection()
    a = Player("A", 10)
    b = Player("B", 20)
    pc.add(a)

    with pytest.raises(PlayerNotFoundException):
        pc.remove(b)


def test_player_index_out_of_range():
    pc = PlayerCollection()
    a = Player("A", 10)
    pc.add(a)

    with pytest.raises(IndexOutOfRangeException):
        pc.get_by_index(1)

    with pytest.raises(IndexOutOfRangeException):
        pc.get_by_index(-1)


def test_player_getitem_index_out_of_range():
    pc = PlayerCollection()
    a = Player("A", 10)
    pc.add(a)

    with pytest.raises(IndexOutOfRangeException):
        _ = pc[1]

    with pytest.raises(IndexOutOfRangeException):
        _ = pc[-5]
