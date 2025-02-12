#Multilevel Inheritance: when a child class becomes a parent for another child class.

class Employee:              #Parent Class
    a = 1

class Programmer(Employee):  #Child 1
    b = 2

class Manager(Programmer):   #Child 2
    c = 3 

x = Employee()
print(x.a)

x = Programmer()
print(x.a, x.b)

x = Manager()
print(x.a, x.b, x.c)

