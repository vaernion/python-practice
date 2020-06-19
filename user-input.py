print(f"Multiply two numbers")


def inputFloat(text):
    while 1:
        try:
            num = float(input(text))
        except:
            print(f"Invalid input. Valid examples: -2, 4.33, 1e5")
        else:
            return num


a = inputFloat("First: ")
b = inputFloat("Second: ")

print(f"{a} * {b} = {a * b}")
