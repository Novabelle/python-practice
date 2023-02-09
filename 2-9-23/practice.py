
# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"



# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    """if a is even answer returns True. If a is odd answer returns False"""
    # To check if a is even divide by 2 if even return True
    if a % 2 == 0:
        return True
    elif a % 2 !=0:
        return False


def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True



# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    """returns the ones didget of the number"""
    # Cast num to a string
    working_string = str(num)
    result = working_string[-1:]
    return int(result)

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2




# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    ...

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'


