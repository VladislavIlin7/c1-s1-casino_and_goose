from src.objects.player import Player


def test_player():
    p = Player("Alex", 100)
    assert p.name == "Alex"
    assert p.balance == 100
    assert "Player(" in repr(p)

    p.change_balance(-30)
    assert p.balance == 70

    p.change_balance(10)
    assert p.balance == 80