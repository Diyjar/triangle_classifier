## How To Run Tests

1. Install Python 3, then from the project folder run 'python -m pip install -r requirements.txt'
2. Run all tests: 'python -m pytest -v'

## Equivalence Classes and Boundaries

| Class | Example Input | Expected Response |
|---|---|---|---|
| All sides equal | (3, 3, 3) | Equilateral |
| All sides different | (4, 5, 6) | Scalene |
| Exactly two sides equal | (5, 5, 3) | Isosceles |
| Right, integer sides | (3, 4, 5) | Right Scalene |
| Right, non-integer sides | (1, 1, √2) | Right Isosceles |
| Non-positive side | (0, 5, 6) | Invalid |
| Triangle inequality fails | (1, 2, 4) | Invalid |
| Degenerate boundary (a + b = c) | (1, 2, 3) | Invalid |
| Degenerate decimal | (0.1, 0.2, 0.3) | Invalid |

Boundaries: a side of exactly 0 (Invalid) versus any positive length; a + b = c, including float sums that are only off by rounding such as 0.1 + 0.2 vs 0.3 (Invalid), versus a + b clearly greater than c (valid); and a² + b² = c², which is compared with `math.isclose` because floating-point values like √2 can't be stored exactly.

## Why an Equilateral Triangle Can't Be Right

Every angle in an equilateral triangle is 60°, so none can be 90°. Algebraically, s² + s² = s² only holds when s = 0, which is not a valid side.

## Co-Pilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| test_equilateral | Yes | Kept | All sides are equal |
| test_isosceles | Yes | Kept | 2 sides are equal |
| test_scalene | Yes | Kept | 3 sides different lengths |
| test_right_scalene | Yes | Kept | 3 different lengths with right angle |
| test_right_isosceles| Yes | Kept | 2 sides equal with 1 right angle |
| test_invalid_negative_side | Yes | Kept | 1 side was negative |
| test_invalid_zero_side | Yes | Kept | 1 side contained a zero |
| test_invalid_inequality_failure | No | | 2 lengths together weren't longer then 1 side |
| test_invalid_degenerate | Yes | Edited | Only tested integers, missing float rounding. |

## Acceptance Criteria

1. Input given when asked length of sides are checked to ensure they are not zeros, negative, or a size which cannot produce a triangle, if they are, will return an "Invalid" message without crashing.

2. Input which isn't invalid, will return either "Equilateral", "Isosceles", or "Scalene" based on spec table, unless input forms right triangle, which will produce either "Right Isosceles" or "Right Scalene" based on spec table.

## AI-Use Disclosure

| Tool | What I used it for | What I verified |
|---|---|---|
| Claude | Building triangle.py | Ensured that both methods were written to spec, caught and fixed a bug in degenerate check|
| GitHub Co-pilot | Drafting test_triangle.py | Drafted tests cases for each spec, reviewed all cases against spec table and edited test_invalid_degenerate |
| Claude | Writing README sections "How To Test" and "Why An equilateral Triangle Can't Be Right" | Ensured that testing steps worked, as well as equilateral triangle explanation was accurate. |