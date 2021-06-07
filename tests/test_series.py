from math_series import __version__, series
from math_series.series import fibonacci,lucas,sum_series

# Tests for fibonacci

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_0():
    assert fibonacci(0) == 0


def test_fibonacci_1():
    assert fibonacci(1) == 1


def test_fibonacci_11():
    assert fibonacci(11) == 89


# Tests for lucas
def test_lucas_0():
    assert lucas(0) == 2


def test_lucas_1():
    assert lucas(1) == 1


def test_lucas_11():
    assert lucas(11) == 199




# Tests for sum_series
def test_sum_series_21():
    assert sum_series(21) == 10946


def test_sum_series_21_2_1():
    assert sum_series(21,2,1) == 24476

def test_sum_series_11_4_10():
    assert sum_series(11,4,10) == 1110
