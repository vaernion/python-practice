from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4


# simple dataclass example with immutable fields
@dataclass(frozen=True)
class Weapon:
    name: str
    power: int
    misc: str = None


vader_saber = Weapon("Vader's lightsaber", 10, "Red")
anakin_saber = Weapon("Anakin's lightsaber", 10, "Blue")
solo_blaster = Weapon("DL-44 blaster pistol", 4)

# more complex dataclass with field initializers
@dataclass()
class Person:
    name: str
    species: str
    occupation: str
    title: str
    # can't use union syntax with postponed evaluation: "Person" | None
    father: Optional["Person"]
    weapon: Weapon | None

    id: str = field(init=False, default_factory=uuid4)
    # easily searchable words for hypothetical internal use
    _search_string: str = field(init=False, repr=False)

    # can't access other fields during init
    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.species} {self.occupation}"


vader = Person("Darth Vader", "Human", "Sith", "Dark Lord", None, vader_saber)
luke = Person("Luke Skywalker", "Human", "Jedi", "Knight", vader, anakin_saber)
han = Person("Han Solo", "Human", "Smuggler", "Scoundrel", None, solo_blaster)

print(vader)
print(luke)
print(han)

print(vader.__dict__["name"])
