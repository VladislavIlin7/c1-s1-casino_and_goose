from src.objects.chip import Chip


def test_chip():
    c = Chip(10)
    assert c.value == 10
    assert repr(c) == "Chip(10$)"

    c2 = Chip(5)
    c3 = c + c2
    assert isinstance(c3, Chip)
    assert c3.value == 15
    assert repr(c3) == "Chip(15$)"
