import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_basic():
    assert module.first_non_repeating("swiss") == "w"


def test_first_non_repeating_first_character():
    assert module.first_non_repeating("abcdef") == "a"


def test_first_non_repeating_none():
    assert module.first_non_repeating("aabb") is None
