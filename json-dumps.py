import json

import class_basics

tim = class_basics.Person("Tim", 42, "Ork")
print(tim.summary())

timJson = json.dumps(tim.summary())
print(timJson)

timParsed = json.loads(timJson)
print(timParsed)


simple = {
    "abc": "abc def",
    "num": 123,
    "arr": [1, 2, 3],
    "dic": {"one": 1, "two": 2},
}

simpleJson = json.dumps(simple, indent=4,sort_keys=True)
print(simpleJson)
print(json.loads(simpleJson))
