class Employee:
    language = "Python"
    salary = 550000

    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

Rohit = Employee()
    
#Rohit.language = "Javascript"  #This is instance attribute

Rohit.greet()
Rohit.getInfo()
# Employee.getInfo(Rohit)
