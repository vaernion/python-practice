listExample = [1, 5.16, True, "String", ("name", "Sei"), {"name": "Bob"}]

print(listExample[4][1])
print(listExample[5]["name"])

listCopy = listExample[4:] * 2
print(listCopy)

print(listCopy[3]["name"] is listExample[5]["name"])
