# A class method is a method which is bound to the class and not the object of the class.

class Employee:
    a = 1 
    @classmethod           ##This decorator is used to create class method.
    def show(cls):
        print(f"The class attribute is {cls.a}")

x = Employee()
x.a = 50

x.show()

