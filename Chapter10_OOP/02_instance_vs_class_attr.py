class Employee:
    language = "Python"  #Class attribute
    salary = 550000


Rohit = Employee()
Rohit.language = "Javascript"   #This is an instance attribute
print(Rohit.language, Rohit.salary)


#NOTE - Instance attribute take preference over class attributes during assignment and retrieval