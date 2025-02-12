#Super method is used to access the methods of super class in the derived class

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()                         ##Super Class/Keyword
        print("Constructor of Manager")
    c = 3 

# x = Employee()
# print(x.a)

# x = Programmer()
# print(x.a, x.b)

x = Manager()
print(x.a, x.b, x.c)

