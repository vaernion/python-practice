class Person:
    "Class for sentient beings"

    isAlive = True

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def summary(self):
        return f"{self.name} is a {self.age} years old {self.species} that's {'alive' if self.isAlive else 'dead'}"

    def dies(self):
        self.isAlive = not self.isAlive


bob = Person("Bob", 200, "Hork-Bajir")
jim = Person("Jim", 111, "Andalite")
jim.age = 555
jim.dies()
jim.dies()  # reborn

print(bob.summary())
print(jim.summary())


class Subperson(Person):
    def isSub(self):
        return True

    def summary(self):
        return f"SUBPERSON: {super().summary()}"


nils = Subperson("nils", 1, "human")

print(nils.summary())
