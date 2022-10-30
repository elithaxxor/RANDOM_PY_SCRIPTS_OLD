class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #def show(self):
##################################
### Inheretance ###
class Cat(Pet): ####### USING INHERTANCE AND ADDING OCLOR TO CAT
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print('meow')
    def show(self):
        print(f'my name is {self.name} , I am {self.age} years old and am {self.color} .')
class Dog(Pet):
    def speak (self):
        print('wooof')

p = Pet('jackson', 34)
print(type(Pet))
#p.show()

c = Cat('Frank', 22, 'RED')
c.show() ## passes back to main class
c.speak()
