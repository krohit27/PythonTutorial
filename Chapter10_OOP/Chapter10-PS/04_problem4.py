#Add a static method in below problem , to greet the user with hello.


class calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod         #Here, We use static method because we don't want to use self.
    def Hello():
        print("Hello there !!")

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")


a = calculator(4)
a.Hello()
a.square()
a.cube()
a.squareroot()