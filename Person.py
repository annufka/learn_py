class Person():
    def __init__(self, memory=[]):
        self.memory = memory

    def know(self, person):
        if person not in self.memory:
            self.memory.append(person)
            person.memory.append(self)
        return self.memory

    def is_known(self, person):
        if person not in self.memory:
            return False
        return True

pete = Person()
kate = Person()
pete.know(kate)
print(kate.is_known(pete))
