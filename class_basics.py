class Person:
    "Class for sentient beings"
    isSentient = True

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.isAlive = True

    def summary(self):
        return f"{self.name} is a {self.age} years old {self.species} that's {'alive' if self.isAlive else 'dead'}"

    def dies(self):
        self.isAlive = not self.isAlive

    @staticmethod
    def test():
        print(Person.isSentient)


class Subperson(Person):
    def isSub(self):
        return True

    def summary(self):
        return f"SUBPERSON: {super().summary()}"


def main():
    bob = Person("Bob", 200, "Hork-Bajir")
    jim = Person("Jim", 111, "Andalite")
    jim.age = 555
    jim.dies()
    # jim.dies()  # reborn

    print(bob.summary())
    print(jim.summary())
    Person.test()

    nils = Subperson("nils", 1, "human")

    print(nils.summary())


if __name__ == "__main__":
    main()
