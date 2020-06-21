import json
import os

import sw_person

dataFile = "file_basics_data.json"
backupFile = "file_basics_backup.json"
# dataBackup = [
#     {
#         "name": "Luke Skywalker",
#         "species": "Human",
#         "type": "Jedi",
#         "rank": "Grandmaster",
#     }
# ]


###########################
# initialize data from file
initialData = None

if os.path.isfile(dataFile):
    with open(dataFile, "r") as f:
        initialData = f.read()
        print("data read successful")

if not initialData:
    print("data empty or read failed, using backup", type(initialData), initialData)
    # initialData = json.dumps(dataBackup)
    if os.path.isfile(backupFile):
        with open(backupFile, "r") as f:
            initialData = f.read()
            print("backup read succesful")

data = json.loads(initialData)
print("loaded", type(data), len(data), "from", type(initialData), len(initialData))


####################
# do stuff with data


def dictInlist(key, value):
    # for e in data:
    # if e[key] == value:
    for e in [x for x in data if x[key] == value]:
        return e


dictInlist("name", "Luke Skywalker")["sabercolor"] = "green"

pToDict = lambda p: json.loads(p.toJson())
pObjList = []
pList = []


leia = sw_person.Person(
    "Leia Organa Solo", "Human", "Politician", "Chief of State", "Blue"
)
han = sw_person.Person("Han Solo", "Human", "Smuggler", "General")

pObjList.extend((leia, han))


for p in pObjList:
    if not dictInlist("name", p.name):
        pList.append(pToDict(p))

data.extend(pList)


###################
# save data to file
finalData = json.dumps(data, indent=2)
with open(dataFile, "w") as f:
    f.write(finalData)
    print("saved", type(finalData), len(finalData), "from", type(data), len(data))
