from math_series import __version__
from math_series.math_series import *


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_one():
    excepted = 3
    actual = fibonacci(4)
    assert actual == excepted

def test_fibonacci_tow():
    excepted = 8
    actual = fibonacci(6)
    assert actual == excepted

def test_fibonacci_three():
    excepted = 13
    actual = fibonacci(7)
    assert actual == excepted

def test_lucas_one():
    excepted = 4
    actual = lucas(3)
    assert actual == excepted     

def test_lucas_tow():
    excepted = 11
    actual = lucas(5)
    assert actual == excepted  

def test_lucas_three():
    excepted = 29
    actual = lucas(7)
    assert actual == excepted  


def test_sum_seriesone():
    excepted = 1
    actual = sum_series(2)
    assert actual == excepted

def test_sum_seriesone():
    excepted = 123
    actual = sum_series(10,2,1)
    assert actual == excepted

