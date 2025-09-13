# test_app.py
import pytest

from app import add_numbers  # assuming your main function is in app.py


def test_add_positive_numbers():
    assert add_numbers(5, 7) == 12

def test_add_negative_numbers():
    assert add_numbers(-3, -6) == -9

def test_add_mixed_numbers():
    assert add_numbers(-4, 10) == 6

def test_add_with_zero():
    assert add_numbers(0, 9) == 9
    assert add_numbers(8, 0) == 8
