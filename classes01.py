class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)
        print(age) 

    def meow(self):
        return('meow')
    def bark(self):
        print('bark')
    def add_one(self, x):
        return x + 1


d = Dog('tim', 6)

print(d.add_one, 5)

d2 = Dog('YooOooooO', 5)
#dog('tim')
d.bark()
d.meow()
print(d.add_one(5))



#print(d.meow)
#print(type(d))
