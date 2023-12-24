from scripts.openai_plugin import *


# Function to test addition function
def test_addition():
    result = addition(2, 2)
    assert result == 4


# Function to test subtraction function
def test_subtraction():
    result = subtraction(4, 2)
    assert result == 2


# Function to test multiplication function
def test_multiplication():
    result = multiplication(2, 3)
    assert result == 6


# Function to test division function
def test_division():
    result = division(4, 2)
    assert result == 2
