"""
Fixture :  fixture is a function that we want to execute before executing any test cases or with multiple scope.
to configure the pre-requisite on different levels.

function scope : This fixture will execute before and after execution of each test cases or test function.
class scope : This fixture will execute before and after execution of each test class.
module scope: This fixture will execute before and after execution of each test module or test suite file.
package scope:  This fixture will execute before and after execution of each test package.
session scope: This fixture will execute before and after execution of session of test execution.
"""
import pytest

@pytest.fixture(scope="function", autouse=True)
def fun_setup():
    print("\n--- Fun fixture initiated ---")
    yield
    print("\n--- Fun fixture completed ---")

@pytest.fixture(scope="class", autouse=True)
def cls_setup():
    print("\n--- Fun fixture initiated ---")
    yield
    print("\n--- Fun fixture completed ---")

@pytest.fixture(scope="module", autouse=True)
def mod_setup():
    print("\n--- Fun fixture initiated ---")
    yield
    print("\n--- Fun fixture completed ---")

@pytest.fixture(scope="package", autouse=True)
def pac_setup():
    print("\n--- Fun fixture initiated ---")
    yield
    print("\n--- Fun fixture completed ---")

@pytest.fixture(scope="session", autouse=True)
def ses_setup():
    print("\n--- Fun fixture initiated ---")
    yield
    print("\n--- Fun fixture completed ---")

class Test_math_oper:

    name = "Testing a logic of fixture"

    def test_addition(self, fun_setup):
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