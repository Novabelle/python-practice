# Numbers divisable by 3 return "Herp"
# Numbers divisable by 5 return "Derp"
# Numbers divisable by both return "HerpDeDerp"


# Define a function "herpdederp_result()"
# Funtion accepts aurgument "number"
# Use keyword "def"
#Use keyword "return"


# def herpdederp_result(number):
#     """
#     returns the herpdederp result
#     """
#     # If numbe is evenly divisable by 3
#     if number % 3 == 0 and number % 5 != 0: 
#         return "Herp"
#     elif number % 5 == 0 and number % 3 != 0:
#         return "Derp"
#     elif number % 3 == 0 and number % 5 == 0:
#         return "HerpDeDerp"
#     else:
#         return number


def herpdederp_result(number):
    """
    returns the herpdederp result
    """
    # If numbe is evenly divisable by 3
    if number % 3 == 0 and number % 5 == 0:
        return "HerpDeDerp"
    elif number % 3 == 0: 
        return "Herp"
    elif number % 5 == 0:
        return "Derp"
    else:
        return number
    # return "everything else"

# print(herpdederp_result)
# PS C:\Users\SethHanslik\Programming\python-practice\2-2-23> python .\herpdederp.py
# <function herpdederp_result at 0x00000260A5490540>
#  "Function" means: herpdederp_result is a function


# print(3, herpdederp_result(3))
# print(5, herpdederp_result(5))
# print(9, herpdederp_result(9))
# print(10, herpdederp_result(10))
# print(11, herpdederp_result(11))
# print(15, herpdederp_result(15))
# print(18, herpdederp_result(18))


if __name__ == "__main__":
    for i in range(35):
        print(i, herpdederp_result(i))
# This is a "for loop"

# To run the test:
# pytest herpdederp.py
def test_herpdederp_result():
    assert herpdederp_result(5) == "Derp"
    assert herpdederp_result(6) == "Herp"
    assert herpdederp_result(7) == 7