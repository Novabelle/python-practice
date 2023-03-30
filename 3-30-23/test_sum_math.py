import sum_math

def test_add_three():
    """Test add_three()."""
    assert sum_math.add_three(5) == 8
    assert sum_math.add_three(3) != 7
    assert sum_math.add_three(10) == 13