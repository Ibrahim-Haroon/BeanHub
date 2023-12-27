

def inputRED(string: str = "ARE YOU SURE YOU WANT TO DUMP AND CREATE A NEW TABLE (YES/NO) ") -> str:
    print("\033[91m", end="")
    user_input = input(string)
    print("\033[0m", end="")

    return user_input
