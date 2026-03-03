
class Bike:

    def __init__(self):
        print("Welcome to bike shop")
        self.bike_name1()

    def bike_name1(self):
        print("bike name RE")

    def bike_name2(self):
        print("bike name R15")

    def bike_name3(self):
        print("bike name ktm")

a = Bike()
a.bike_name1()
a.bike_name2()
a.bike_name3()
print("-----------------------------------------------------")

class Bike2:

    def __init__(self, mod1, mod2):
        print("Welcome to bike shop")
        self.bike_mod1 = mod1
        self.bike_mod2 = mod2

    def bike_name1(self):
        print("bike name RE", self.bike_mod1)

    def bike_name2(self):
        print("bike name R15", self.bike_mod2)

    def bike_name3(self):
        print("bike name ktm")

b = Bike2(2012, 2020)
b.bike_name1()
b.bike_name2()
b.bike_name3()
