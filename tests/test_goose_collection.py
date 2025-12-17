import pytest
from src.my_collections.goose_collection import GooseCollection
from src.objects.goose import Goose


def test_geese():
    gc = GooseCollection()
    assert len(gc) == 0

    g1 = Goose("G1", 1)
    g2 = Goose("G2", 2)
    gc.add(g1)
    gc.add(g2)

    assert len(gc) == 2
    assert gc[0].name == "G1"
    assert [g.name for g in gc] == ["G1", "G2"]


def test_geese_remove_by_name():
    gc = GooseCollection()
    g = Goose("X", 1)
    gc.add(g)

    gc.remove_by_name("X")
    assert len(gc) == 0

    with pytest.raises(ValueError):
        gc.remove_by_name("X")
