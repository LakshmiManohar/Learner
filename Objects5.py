class Object5:
    def __init__(self,name):
        self.Name = name

    def displayname(self):
        return self.Name
    def printname(self):
        print(self.Name,"How are You ")
M1 = Object5("Mano")
print(M1.Name)
print(M1.displayname())
M1.printname()
