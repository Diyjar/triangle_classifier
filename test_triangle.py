import math
from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"

def test_right_isosceles():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"

def test_invalid_negative_side():
    assert classify_triangle(-1, 2, 3) == "Invalid"

def test_invalid_zero_side():
    assert classify_triangle(0, 5, 6) == "Invalid"

def test_invalid_degenerate():
    assert classify_triangle(1, 2, 3) == "Invalid"

def test_invalid_inequality_failure():
    assert classify_triangle(1, 2, 4) == "Invalid"