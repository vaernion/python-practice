def inputFloat(text):
    while 1:
        try:
            num = float(input(text))
        except:
            print("Invalid input. Valid examples: -2, 4.33, 1e5")
        else:
            return num


def inputInt(text):
    while 1:
        try:
            num = int(input(text))
        except:
            print("Invalid input. Valid examples: 3, -1")
        else:
            return num


summary = ""
result = 1

print("Multiply X factors")

x = inputInt("How many factors? ")
while x < 1:
    x = inputInt("Input a positive integer ")

for i in range(x):
    factor = inputFloat(f"{i + 1}: ")
    summary += str(factor) if i + 1 == x else f"{factor} * "
    result *= factor
else:
    summary += f" = {result}"

print(summary)
