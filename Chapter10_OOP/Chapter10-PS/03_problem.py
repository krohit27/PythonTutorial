#Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. 
#Does this change the class attribute?

class Demo:
    a = 4

x = Demo()
print(x.a)  #Prints the class attribute because instance attribute not present.

x.a = 5
print(x.a)  #Prints the instance attribute because instance attribute is present.

print(Demo.a) #Prints the class attribute