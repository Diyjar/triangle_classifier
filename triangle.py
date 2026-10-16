"""Triangle classifier."""

import math


def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    x, y, z = sorted((a, b, c))
    return x + y > z  # strict: x + y == z is degenerate


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"
    x, y, z = sorted((a, b, c))
    if math.isclose(x * x + y * y, z * z, rel_tol=1e-9):
        return "Right " + kind
    return kind