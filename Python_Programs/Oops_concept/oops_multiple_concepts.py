
class Grandfather:

    Grandfather_address = "Kagaznagar"

    def __init__(self, name, initial):
        print("Welcome to family")
        self.G_name = name
        self.I_int = initial

    def G_father(self):
        print("Grand father name: ", self.G_name)
        print("Initial:", self.I_int)

    @classmethod
    def G_father_place(cls):
        print("Grand father place:", cls.Grandfather_address)

var = Grandfather("Subbaiah", "Kondagurla")
var.G_father()
var.G_father_place()

print("---------------------------------------------------------------")

class Father(Grandfather):
    def __init__(self, f_name, f_property, name, initial):
        super().__init__(name, initial)
        self.father_name = f_name
        self.father_property = f_property

    def show_grand_father_details(self):
        print("Grand Father Name :", self.father_name)
        print("Grand Father Property :", self.father_property)

obj = Father("Mallesh", "House", "Subbaiah", "Kondagurla")
obj.show_grand_father_details()
obj.G_father()
obj.G_father_place()

print("---------------------------------------------------------------")

class Son(Father):
    Son_place = "Hyderabad"

    def __init__(self, s_name, job, f_name, f_property, name, initial):
        super().__init__(f_name, f_property, name, initial)
        print("Welcome to Son Life")
        self.son_name = s_name
        self.j_job = job

    def son_details(self):
        print("Son name: ", self.son_name)
        print("Son Job: ", self.j_job)

    def son_address(cls):
        print("Son Address", cls.Son_place)

    def son_hobies(hi, hello):
        for i in range(1,10):
            a = 1
            print("ans: ", i*a)

sn = Son("Rajkumar", "SQE", "Mallesh", "House", "Subbaiah", "Kondagurla")
sn.son_details()
sn.son_address()
sn.son_hobies(2)
sn.show_grand_father_details()
sn.G_father()
sn.G_father_place()


