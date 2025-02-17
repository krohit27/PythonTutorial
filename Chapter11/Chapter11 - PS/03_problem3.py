#Write a method 'salaryAfterIncrement' method with a @property decorator with a setter 
#which changes the value of increment based on the salary.

class Employee:
    salary = 300
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1 ) * 100


a = Employee()

a.salaryAfterIncrement = 390
print(a.increment)
