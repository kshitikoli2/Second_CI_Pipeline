import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_right():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_full_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_empty_string():
    assert module.rotate_string("", 3) == ""
