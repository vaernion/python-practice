class TeamMember:
    "Basic team member class"

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Worker:
    "Worker class"

    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle


# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):
    "Team leader class"

    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)

    def summary(self):
        return "Name: {}, Pay: {}, Exp: {}".format(self.name, self.pay, self.exp)


class MegaTeamLeader(TeamLeader):
    "Super mega ultra"

    def __init__(self, name, uid, pay, jobtitle, exp, hyperbole):
        super().__init__(name, uid, pay, jobtitle, exp)
        self.hyperbole = hyperbole

    def boast(self):
        return f"{self.summary()} and they are {self.hyperbole}!"


TL = TeamLeader("Michael", 10001, 250000, "Scrum Master", 5)

bigTL = MegaTeamLeader("Abcdef", 10002, 1e10, "Scrum Grandmaster", 15, "godlike")

print(TL.summary())
print(bigTL.boast())

for k, v in bigTL.items():
    print(k, v)
