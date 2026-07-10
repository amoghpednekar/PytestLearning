import pytest;
from calc_app import add, subtract, multiply

# This is before parameterization, we are writing individual test cases for each function
def test_add_positive_numbers():
    assert add(2, 3) == 5
    print(f"Addition of 2 and 3 is {add(2, 3)}")

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    print(f"Addition of -1 and -1 is {add(-1, -1)}")

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-1, 1) == -1

def test_multiply_zero():
    assert multiply(0, 0) == 0

#after adding parameterization, we can write a single test function for each operation and use different sets of input values to test the function. This makes the code more concise and easier to maintain.
#parametrize decorator is used to define the input values and expected output for the test function. The test function takes the input values as parameters and asserts that the output of the function being tested matches the expected output.
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2)
])
def test_addition(a, b, expected):
    assert add(a, b) == expected
    print(f"Addition of {a} and {b} is {add(a, b)}")

#parametrize with ids is used to provide a custom name for each test case. This makes it easier to identify which test case failed when running the tests.
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, -1),
    (0, 0, 0),
    (-1, -1, 0)
], ids=["positive numbers", "zero", "negative numbers"])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
    print(f"Subtraction of {a} and {b} is {subtract(a, b)}")

#parametrize with pytest.params used to define a set of input values and expected output for the test function. The test function takes the input values as parameters and asserts that the output of the function being tested matches the expected output.
@pytest.mark.parametrize("a, b, expected",[
    pytest.param(2,4, 8, id = "positive numbers"),
    pytest.param(0,0,0, id= "zero"),
    pytest.param(2,-6,-12,id ="negative numbers")
])
def test_multiply_param(a,b,expected):
    assert multiply(a,b) == expected
    print(f"Multiplication of {a} and {b} is {multiply(a,b)}")