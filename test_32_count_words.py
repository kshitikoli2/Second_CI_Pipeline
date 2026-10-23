import importlib

module = importlib.import_module("32_count_words")


def test_count_words_sentence():
    assert module.count_words("Python is easy to learn") == 5


def test_count_words_extra_spaces():
    assert module.count_words("  hello   world  ") == 2


def test_count_words_empty():
    assert module.count_words("") == 0
