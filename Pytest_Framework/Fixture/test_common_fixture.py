
class Test_math_oper2:

    name = "Testing a logic of fixture"

    def test_addition(self, setup):
        n1 = 2
        n2 = 4
        assert n1+n2 == 6

    def test_subtraction(self):
        n3 = 10
        n4 = 6
        assert n3-n4 == 4

    def test_multiplication(self):
        n5 = 3
        n6 = 5
        assert n5*n6 == 2

    def test_text(cls):
        print("test: ", cls.name)

    def test_greet(self):
        print("Good Morning")