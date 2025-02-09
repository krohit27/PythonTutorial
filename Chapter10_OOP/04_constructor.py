class Employee:
    language = "Python"
    salary = 750000

    def __init__(self, name, language, salary):    # dunder method which is automatically called OR constructor
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating a constructor")

    
Rohit = Employee("ROHIT", "Python", 750000)
print(Rohit.name, Rohit.language, Rohit.salary)


        
