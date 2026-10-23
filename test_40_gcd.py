import importlib

module = importlib.import_module("40_gcd")


def test_gcd_common_values():
    assert module.gcd(48, 18) == 6


def test_gcd_with_zero():
    assert module.gcd(7, 0) == 7


def test_gcd_negative_values():
    assert module.gcd(-24, 18) == 6
