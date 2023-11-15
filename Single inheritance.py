#Single inheritance


class Wine:
    def __init__(self):
        self.brand = "RC"
    
    def m1(self):
        print("This is wine")

class TC(Wine):
    def __init__(self):
        super().__init__()  
        self.car_type = "full bottle"
    
    def m2(self):
        print("This is a wine and it is a full bottle")

c = TC()
c.m1()
c.m2()
