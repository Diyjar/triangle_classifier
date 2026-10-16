"""Triangle classifier."""

import math
from numbers import Real


def _is_side(x) -> bool:
    """A usable side is a finite real number greater than zero (bools excluded)."""
    return (
        isinstance(x, Real)
        and not isinstance(x, bool)
        and math.isfinite(x)
        and x > 0
    )


def is_valid_triangle(a, b, c) -> bool:
    """Return True if a, b, c can form a non-degenerate triangle."""
    if not all(_is_side(s) for s in (a, b, c)):
        return False
    x, y, z = sorted((a, b, c))
    # Strict inequality: x + y == z is a degenerate (flat) triangle.
    return x + y > z


def _is_right(a, b, c) -> bool:
    """Pythagorean check with a tolerance, since float sides rarely match exactly."""
    x, y, z = sorted((a, b, c))
    return math.isclose(x * x + y * y, z * z, rel_tol=1e-9)


def classify_triangle(a, b, c) -> str:
    """Return "Invalid", "Equilateral", "Isosceles" or "Scalene",
    prefixed with "Right " when the triangle has a right angle."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    if _is_right(a, b, c):
        return f"Right {kind}"
    return kind
