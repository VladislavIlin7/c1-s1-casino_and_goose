import pytest
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

    with pytest.raises(ValueError):
        pc.remove_by_name("X")