import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_basic():
    assert module.most_frequent([1, 3, 2, 3, 3, 2]) == 3


def test_most_frequent_tie_uses_first_seen():
    assert module.most_frequent([2, 1, 2, 1]) == 2


def test_most_frequent_empty():
    assert module.most_frequent([]) is None
