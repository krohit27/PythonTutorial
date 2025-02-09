class Employee:
    language = "Py"    #This is Class attribute
    salary  = 525000  #This is Class attribute
    

Rohit = Employee()     #Object
Rohit.name = "Rohit Kalshetty"   #This is instance/Object attribute
print(Rohit.name, Rohit.language, Rohit.salary)

Rohan = Employee()     #Object
Rohan.name = "Rohan Babhale"     #This is instance/Object attribute
print(Rohan.name, Rohan.language, Rohan.salary)


# Here name is instance attribute and salary and language are class attributes as 
# they directly belong to the class