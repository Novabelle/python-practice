THE_STUPID_CONSTANT = "the stupid phrase"

def herpdederp_result(number):
    """
    returns the herpdederp result
    """
    if number % 3 == 0 and number % 5 == 0:
        return "HerpDeDerp"
    elif number % 3 == 0: 
        return "Herp"
    elif number % 5 == 0:
        return "Derp"
    else:
        return number

def main():
    for i in range(35):
        print(i, herpdederp_result(i))

# main()

if __name__ == "__main__":
    main()