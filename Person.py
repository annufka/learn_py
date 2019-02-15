class Person():
    def __init__(self, name, age, memory=[]):
        self.name = name
        self.age = age
        self.memory = memory

    def know(self, person):
        if person not in self.memory:
            self.memory.append(person)
        return self.memory

    def is_known(self, person):
        if person not in self.memory:
            return False
        return True

pete = Person('Pete', 23)
kate = Person('Kate', 19)
pete.know(kate)
print(kate.is_known(pete))
