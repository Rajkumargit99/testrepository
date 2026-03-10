
class Father:
    Father_business = "Own business"

    def __init__(self, f_name, initial):
        print("Welcome to family details")
        self.f_name = f_name
        self.f_initial = initial

    def father_name(self):
        print("Father name:", self.f_name)
        print("Family initial:", self.f_initial)

    def father_duty(cls):
        print("Father business:", cls.Father_business)

var1 = Father("Mallesh", "Kondagurla")
var1.father_name()
var1.father_duty()

class Mother:
    Mother_business = "Self business"

    def __init__(self, m_name, m_initial):
        self.mother_name = m_name
        self.mother_int = m_initial

    def mother_nam(self):
        print("Mother name:", self.mother_name)
        print("Mother initial:", self.mother_int)

    def mother_bus(cls):
        print("Mother business: ", cls.Mother_business)

var2 = Mother("Laxmi", "Same K")
var2.mother_nam()
var2.mother_bus()

class Son(Mother, Father):

    def __init__(self, nme, job, m_name, m_initial):
        super().__init__(m_name, m_initial)
        self.name = nme
        self.job = job

    def son_details(self):
        print("Son name: ", self.name)
        print("Son Job: ", self.job)

var3 = Son("Rajkumar", "SQE", "Laxmi", "KG")
var3.son_details()
var3.mother_nam()

class Son2(Father, Mother):

    def __init__(self, nme2, f_name, initial):
        super().__init__(f_name, initial)
        self.b_name = nme2

    def son2(self):
        print("Brother name: ", self.b_name)

var4 = Son2("King", "Mallesh", "Kondagurla")
var4.son2()
var4.father_name()