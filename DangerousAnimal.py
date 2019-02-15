class Animal():
    def __init__(self, name, agressive):
        self.name = name
        self.agressive = agressive

    def attack_human(self, person):
        if self.agressive == True and person.agressive == True or self.agressive == False and person.agressive == False:
            return "Атака бесполезна"
        if self.agressive == False and person.agressive == True:
            return "слабое животное"
        if self.agressive == True and person.agressive == False:
            return "царь зверей"

class Human(Animal):
    def __init__(self, name, agressive):
        super(Human, self).__init__(name, agressive)

    def is_dangerous(self, animal):
        if animal.agressive == True:
            return "Это опасное животное"
        return "Это безопасное животное, не бойся"

hercules = Human('Геракл', True)
prometeus = Human('Прометей', False)

hydra = Animal('Гидра', True)
hawk = Animal('Ястреб', True)
lamb = Animal('Овца', False)
print('\nПолучение людьми опыта общения с животными:\n ')
print(hydra.attack_human(hercules))
print(hawk.attack_human(hercules))
print(lamb.attack_human(hercules))

print(hydra.attack_human(prometeus))
print(hawk.attack_human(prometeus))
print(lamb.attack_human(prometeus))

print('\nПолучение людьми опыта общения с другими людьми:\n ')
print(hercules.attack_human(prometeus))

print('\nПроверка накопленного людьми опыта общения с животными:\n ')
print('Опасна ли {} для {}? : {}'.format(hydra.name, hercules.name, hercules.is_dangerous(hydra)))
print('Опасен ли {} для {}? : {}'.format(hawk.name, hercules.name, hercules.is_dangerous(hawk)))
print('Опасна ли {} для {}? : {}'.format(lamb.name, hercules.name, hercules.is_dangerous(lamb)))


