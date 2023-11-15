#multilevel inheritance 

class Grandma:
    def __init__(self):
        self.m = 32
        print("This is grandma constructor")

    def m1(self):
        self.n = 34

class Mother(Grandma):
    def m2(self):
        self.o = 60

class Child(Mother):
    def sum(self):
        print(self.m + self.n + self.o)

o = Child()
o.m1()
o.m2()
o.sum()
