class Animal:
    def __init__(self):
        print("Animal is created")

    def whoami(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog is created")

    def whoami(self):
        print("Dog")
    def bark(self):
        print("Woof")

d = Dog()
d.whoami()
d.eat()
d.bark()

