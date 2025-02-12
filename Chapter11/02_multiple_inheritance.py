
#Multiple Inheritance - When child class inherits from more than one parent class

class Employee:              #Parent Class
    name = "ROHIT"
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:                 #Parent Class
    language = "Python"
    def printLanguage(self):
        print(f"The name of the Scripting language is {self.language}")


class Programmer(Employee, Coder):    ##Multiple Inheritance or Child Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} he is good with {self.language} language")

a = Employee()
b = Programmer()
a.show()
b.printLanguage()
b.showLanguage()

# print(a.company, b.company)