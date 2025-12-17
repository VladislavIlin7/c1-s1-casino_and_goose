from src.my_collections.player_collection import PlayerCollection
from src.objects.goose import Goose, WarGoose, HonkGoose
from src.objects.player import Player


def test_goose():
    g = Goose("Gus", honk_volume=2)
    s = g.honk()
    assert "Gus" in s
    assert "2" in s


def test_war_goose():
    p = Player("P", 100)
    wg = WarGoose("Rambo", honk_volume=5)

    msg = wg.attack(p)
    assert p.balance == 50
    assert "Rambo атакует P" in msg
    assert "50$" in msg


def test_super_honk_goose():
    pc = PlayerCollection()
    a = Player("A", 10)
    b = Player("B", 0)
    pc.add(a)
    pc.add(b)

    hg = HonkGoose("Screamer", honk_volume=3)
    msg = hg.super_honk(pc)

    assert a.balance == 7
    assert b.balance == -3
    assert "Screamer" in msg
    assert "3$" in msg
