#single class to multiple class

class Amithab:
    def __init__(self):
        print("This is an Amithab class.")

class AbhishkOne(Amithab):
    def m1(self):
        print("This is an AbhishkOne class.")

class AbhishkTwo(Amithab):
    def m2(self):
        print("This is an AbhishkTwo class.")

abhishk_one_instance = AbhishkOne()
abhishk_one_instance.m1()

abhishk_two_instance = AbhishkTwo()
abhishk_two_instance.m2()
