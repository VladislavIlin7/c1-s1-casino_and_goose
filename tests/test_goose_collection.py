import pytest
from src.exception.exception import (
    GooseAlreadyExistsException,
    GooseNotFoundException,
    IndexOutOfRangeException,
)
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

    with pytest.raises(GooseNotFoundException):
        gc.remove_by_name("X")


def test_goose_already_exists():
    gc = GooseCollection()
    g1 = Goose("G1", 1)
    gc.add(g1)

    with pytest.raises(GooseAlreadyExistsException):
        gc.add(Goose("G1", 2))



def test_goose_not_found_remove():
    gc = GooseCollection()
    g1 = Goose("G1", 1)
    g2 = Goose("G2", 2)
    gc.add(g1)

    with pytest.raises(GooseNotFoundException):
        gc.remove(g2)


def test_goose_index_out_of_range():
    gc = GooseCollection()
    g1 = Goose("G1", 1)
    gc.add(g1)

    with pytest.raises(IndexOutOfRangeException):
        gc.get_by_index(10)

    with pytest.raises(IndexOutOfRangeException):
        gc.get_by_index(-1)


def test_goose_getitem_index_out_of_range():
    gc = GooseCollection()
    g1 = Goose("G1", 1)
    gc.add(g1)

    with pytest.raises(IndexOutOfRangeException):
        _ = gc[10]

    with pytest.raises(IndexOutOfRangeException):
        _ = gc[-1]
