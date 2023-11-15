#combitnation of more than one type of inheritance


class Raju:
    def m1(self):
        print("I can run")

class Rani:
    def hobby(self):
        print("I can read")

class Child(Raju, Rani):
    pass

m = Raju()
f = Rani()
c = Child()

c.m1()
c.hobby()
