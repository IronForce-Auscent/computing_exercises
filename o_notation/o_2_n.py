"""
This program is a representation of how an O(2 ^ n) time complexity program runs
"""

def inverted_fibonacci(start_num: int) -> int:
    if start_num <= 1:
        return start_num
    return inverted_fibonacci(start_num - 1) + inverted_fibonacci(start_num - 2)

def test_inverted_fibonacci():
    from utils.unit_tests import UnitTest
    test = UnitTest()
    # Just to be clear, I have no idea whether these vallues are actually correct :P
    # Dont try this with a value of 60 or higher btw, your computer will probably shit itself
    print(test.assert_equals(lambda: inverted_fibonacci(10), 55))
    print(test.assert_equals(lambda: inverted_fibonacci(15), 610))
    print(test.assert_equals(lambda: inverted_fibonacci(20), 6765))
    print(test.assert_equals(lambda: inverted_fibonacci(25), 75025))
    print(test.assert_equals(lambda: inverted_fibonacci(30), 832040))
    print(test.assert_equals(lambda: inverted_fibonacci(35), 9227465))