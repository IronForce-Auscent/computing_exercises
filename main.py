"""
Task:

Given a temperature (in Kelvins) and the temperature unit to convert to, write
a function that will return the converted temperature. Assume that all values provided are
valid

Formula References:
Kelvins to Celsius: K - 273.15
Kelvins to Fahrenheit: (K − 273.15) × 9/5 + 32

Challenge ID: 2c839e21375d637c
"""

def convert_temperature(temperature_kelvins, to_convert):
    # Your code here
    return False


# DO NOT EDIT
# Test cases to check if the function works as intended
def run_test():
    from utils.unit_tests import UnitTest
    CHALLENGE_ID = "2c839e21375d637c"
    test = UnitTest()

    test.describe("Basic Tests - Fahrenheit")
    print(test.assert_equals(lambda: convert_temperature(0, "F"), -459.67))
    print(test.assert_equals(lambda: convert_temperature(150, "F"), -189.67))
    print(test.assert_equals(lambda: convert_temperature(300, "F"), 80.33))
    print(test.assert_equals(lambda: convert_temperature(5000, "F"), 8540.33))
    print(test.assert_equals(lambda: convert_temperature(1e10, "F"), 17999999540.33))

    test.describe("Basic Tests - Celsius")
    print(test.assert_equals(lambda: convert_temperature(0, "C"), -273.15))
    print(test.assert_equals(lambda: convert_temperature(150, "C"), -123.15))
    print(test.assert_equals(lambda: convert_temperature(300, "C"), 26.85))
    print(test.assert_equals(lambda: convert_temperature(5000, "C"), 4726.85))    
    print(test.assert_equals(lambda: convert_temperature(1e10, "C"), 9999999726.85))

    test.describe("Random Tests")
    test.assert_equals_random(convert_temperature, CHALLENGE_ID)


if __name__ == "__main__":
    run_test()