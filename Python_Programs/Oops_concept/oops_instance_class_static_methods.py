"""
class:  class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
constructor: constructor initialize the memory for the object, when ever we create object of the class
             ->  constructor will be call automatically, when we can create object of the class.


There are 2 types of constructor
1).  default constructor :
  def __init__(self)
     pass


2)  Parametrize constructor: when we pass parameter to the constructor then it is called parametrize constructor.
  def __init__(self, param1, param2):
     pass

########## Variables ###########
1). instance variable :  when we define any variable with self  then it is called instance variable
2). class variable:  when we define any variable on class level, then it is called class variable

"""

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

