#Multiple inheritance :

class Grandparent:
    def m1(self):
        self.grandfather = "shakr"
        print("Grandparent class")

class Parent(Grandparent):
    def m2(self):
        self.father = "veru"
        print("Parent class")

class Child(Parent): 
    def m3(self):
        self.child = "nari"

    def display(self):
        print("My grandfather's name:", self.grandfather)
        print("My father's name:", self.father)
        print("My name:", self.child)

c = Child()
c.m1()
c.m2()
c.m3()
c.display()
