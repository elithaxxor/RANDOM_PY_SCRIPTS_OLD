class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim")
print(Person.number_of_people)

Person.number_of_people = 2
print(Person.number_of_people)
