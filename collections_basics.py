person = {"name": "Luke", "class": "Jedi", "skill": 10}
person2 = {"name": "Leia", "class": "Politician", "skill": 9}

personList = [person, person2]
print(type(personList), personList)

for i, v in enumerate(personList):
    print(i, v["name"])

personTuple = (person, person2)
print(type(personTuple), personTuple)

setExample = {"table", "notebook", "IDE", "headphones", "podcasts", "table"}
print(type(setExample), setExample)

# del person["class"]
person["profession"] = person.pop("class")

print(type(person), person)

for k, v in person.items():
    print(k, v)
