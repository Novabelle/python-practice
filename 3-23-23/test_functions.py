from functions import add_one, add_two, times_three, divide_by_seven


def test_add_one():
    assert add_one(3) == 4
    assert add_one(4) == 5
    assert add_one(5) == 6
    assert add_one(6) != 8


def test_add_two():
    assert add_two(3) == 5
    assert add_two(4) == 6
    assert add_two(5) == 7


def test_times_three():
    """multiply by three"""
    assert times_three(3) == 9
    assert times_three(4) == 12
    assert times_three(5) == 15

def test_divide_by_seven():
    """divide by seven"""
    assert divide_by_seven(7) == 1
    assert divide_by_seven(14) == 2
    assert divide_by_seven(21) == 3