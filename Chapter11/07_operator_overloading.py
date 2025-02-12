#Operators in Python can be overloaded using dunder methods.

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):          ##dunder method
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)
