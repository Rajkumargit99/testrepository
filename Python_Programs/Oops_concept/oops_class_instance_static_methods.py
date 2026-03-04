
class Bike:
    bike_brand = "RoyalEnfield"

    def __init__(self, gt, hunter):
        print("Welcome to bike shop")
        # self.bike_name()
        self.gt = gt
        self.hunter = hunter

    #@isinstance()
    def bike_name1(self):
        print("bike name RE", self.gt)

    def bike_name2(self):
        print("bike name RE", self.hunter)

    @classmethod
    def bike_name3(cls):
        print("bike name Reborn", cls.bike_brand)

    @staticmethod
    def bike_name4(num):
        for i in range(1,51):
            i = i
        print("bike name bullet", i)

    def bike_name_all(self):
        print("Above all bikes are available")


var = Bike("RE GT 650", "Hunter 350")
var.bike_name1()
var.bike_name2()
var.bike_name3()
var.bike_name4(8)
var.bike_name_all()
print("-----------------------------------------------------")

