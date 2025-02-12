#Inheritance is a way of creating new class from an existing class.
# Syntax: 

# class Employee:     #Base class
#     code

# class Programmer(Employee):  # Derived or child class
#     code
          


class Employee:              #Base Class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} the salary is {self.salary}")

class Programmer(Employee):    #Derived or child class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)

        