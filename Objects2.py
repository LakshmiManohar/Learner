class Student:

    def __init__(self,Name,Grade):
        self.Name = Name
        self.Grade = Grade

Kate = Student('Kate',85)
Tom = Student('Tom',80)

print("Name: {0}, Grade: {1}".format(Kate.Name,Kate.Grade))
print("Name: {0}, Grade: {1}".format(Tom.Name,Tom.Grade))


