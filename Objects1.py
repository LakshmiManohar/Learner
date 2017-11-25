class Human:
    def __init__(self, n, o):
        self.Name = n
        self.Occupation = o

    def speak(self):
        print(self.Name," Speaks Hello How are you..!")

    def profession(self):
        if self.Occupation == 'Actor':
            print(self.Name, " Shoots films")
        elif self.Occupation == 'Sports':
            print(self.Name, "Plays Cricket")

Person1 = Human('Chiru','Actor')
Person2 = Human('Sachin','Sports')
Person1.speak()
Person1.profession()
Person2.speak()
Person2.profession()


