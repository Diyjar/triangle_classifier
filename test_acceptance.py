from triangle import classify_triangle
def test_criteria():
    # tests for acceptance criteria 1
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-3, 4, 5) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"

    #tests for acceptance criteria 2
    assert classify_triangle(6, 6, 6) == "Equilateral"
    assert classify_triangle(8, 8, 4) == "Isosceles"
    assert classify_triangle(7, 8, 9) == "Scalene"
    assert classify_triangle(6, 8, 10) == "Right Scalene"
    assert classify_triangle(2, 2, 2 * 2 ** 0.5) == "Right Isosceles"