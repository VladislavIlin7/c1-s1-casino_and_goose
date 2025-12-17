from src.objects.casino import Casino
from src.objects.goose import Goose, WarGoose, HonkGoose


def test_register_player():
    c = Casino()
    p = c.register_player("Alex", 150)

    assert p.name == "Alex"
    assert p.balance == 150
    assert len(c.players) == 1
    assert c.balance["Alex"] == 150


def test_register_goose():
    c = Casino()
    g = c.register_goose(Goose("Gusar", 2))

    assert g.name == "Gusar"
    assert len(c.geese) == 1


def test_player_bet_changes_balance():
    c = Casino()
    c.register_player("Alex", 100)

    before = c.players[0].balance
    c.event_player_bet()
    after = c.players[0].balance

    assert after != before
    assert after <= before


def test_player_win_changes_balance():
    c = Casino()
    c.register_player("Alex", 100)

    before = c.players[0].balance
    c.event_player_win()
    after = c.players[0].balance

    assert after != before
    assert after >= before


def test_goose_attack_changes_balance():
    c = Casino()
    c.register_player("Alex", 100)
    c.register_goose(WarGoose("Rambo", 5))

    before = c.players[0].balance
    c.event_goose_attack()
    after = c.players[0].balance

    assert after == before - 50


def test_goose_super_honk_changes_all_balances():
    c = Casino()
    c.register_player("Alex", 10)
    c.register_player("Ali", 0)
    c.register_goose(HonkGoose("Screamer", 3))

    before = [p.balance for p in c.players]
    c.event_goose_super_honk()
    after = [p.balance for p in c.players]

    assert after == [x - 3 for x in before]


def test_steal_changes_balance():
    c = Casino()
    c.register_player("Alex", 100)
    c.register_goose(Goose("Gusar", 2))

    before = c.players[0].balance
    c.event_steal()
    after = c.players[0].balance

    assert after != before
    assert after <= before


def test_simulate_step_runs():
    c = Casino()
    c.register_player("Alex", 100)
    c.register_player("Ali", 80)
    c.register_goose(Goose("Gusar", 2))
    c.register_goose(WarGoose("Rambo", 5))
    c.register_goose(HonkGoose("Screamer", 3))

    c.simulate_step()
