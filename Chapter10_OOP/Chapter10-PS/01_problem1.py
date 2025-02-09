# Create a class Programmer for storing information of few Programmers working at microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
Rohit = Programmer("ROHIT", 35000, 415523)
print(Rohit.name, Rohit.salary, Rohit.pin, Rohit.company)

Rohan = Programmer("ROHAN", 45000, 411045)
print(Rohan.name, Rohan.salary, Rohan.pin, Rohan.company)



