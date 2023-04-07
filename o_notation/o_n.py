"""
This program is a representation of how an O(n) time complexity program runs
"""
from utils.unit_tests import UnitTest

def find_item(arr: list, target) -> bool | int:
    """
    Find a target value in a list of any length

    Arguments:
    arr (list): the list that the program will search through
    target (any): the intended target

    Returns:
    index (int): the index of the target value
    """
    for value in arr:
        if value == target:
            return arr.index(value)
        else:
            pass

def test_find_item():
    test = UnitTest()
    sorted_int_list, unsorted_int_list = [i for i in range(1, 51)], [44, 13, 37, 22, 6, 49, 25, 19, 42, 1, 31, 9, 26, 20, 30, 16, 8, 12, 29, 11, 24, 46, 7, 38, 17, 41, 3, 33, 27, 50, 14, 10, 48, 5, 36, 47, 23, 21, 35, 2, 39, 40, 18, 45, 15, 32, 34, 28, 43]
    sorted_str_list, unsorted_str_list = ['apple', 'banana', 'cherry', 'date', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'peach', 'pear', 'pineapple'], ['cherry', 'apple', 'pineapple', 'kiwi', 'orange', 'banana', 'mango', 'grape', 'pear', 'date', 'peach', 'lemon']
    sorted_float_list, unsorted_float_list = [i * 0.5 for i in range(1, 51)], [44.5, 13.2, 37.1, 22.3, 6.7, 49.9, 25.4, 5.5, 19.8, 42.6, 1.0, 31.5, 9.6, 26.1, 20.7, 30.2, 16.4, 8.9, 12.3, 29.7, 11.1, 24.8, 46.2, 7.5, 38.9, 17.6, 41.3, 3.4, 33.7, 27.9, 50.0, 14.6, 10.8, 48.5, 5.1, 36.0, 47.3, 23.5, 21.2, 35.6, 2.3, 39.4, 40.1, 18.7, 45.9, 15.9, 32.8, 34.2, 28.5, 43.8]
    print(test.assert_equals(lambda: find_item(sorted_int_list, 25), 24))
    print(test.assert_equals(lambda: find_item(unsorted_int_list, 25), 6))
    print(test.assert_equals(lambda: find_item(sorted_str_list, "banana"), 1))
    print(test.assert_equals(lambda: find_item(unsorted_str_list, "banana"), 5))
    print(test.assert_equals(lambda: find_item(sorted_float_list, 5.5), 10))
    print(test.assert_equals(lambda: find_item(unsorted_float_list, 5.5), 7))