"""
This program is a representation of how an O(log n) time complexity program runs
"""
from math import floor
from utils.unit_tests import UnitTest

def binary_search(arr: list, target, min = 0, max = 0) -> int | bool:
    """
    Given a sorted list arr and an integer target, return the index of the target value

    Arguments:
    arr (list): a sorted/unsorted list
    target (Any): the intended target value

    Returns: 
    average (int): the index of the target in the array
    """
    arr.sort()
    if min == 0:
        min = 0
    if max == 0:
        max = len(arr)

    average = floor((min + max) / 2)
    if min > max:
        return False
    
    if arr[average] == target:
        return average
    elif target < arr[average]:
        max = average - 1
    elif target > arr[average]:
        min = average + 1
    else:
        pass
    return binary_search(arr, target, min, max)

def test_binary_search():
    test = UnitTest()
    sorted_list_1, sorted_list_2, sorted_list_3 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140]
    sorted_list_4, unsorted_test_1 = ["apple", "banana", "cherry", "lemon", "orange", "peach", "pear"], ["banana", "apple", "orange", "peach", "lemon", "pear", "cherry"]
    print(test.assert_equals(lambda: binary_search(sorted_list_1, 8), sorted_list_1.index(8)))
    print(test.assert_equals(lambda: binary_search(sorted_list_2, 29), sorted_list_2.index(29)))
    print(test.assert_equals(lambda: binary_search(sorted_list_3, 126), sorted_list_3.index(126)))
    print(test.assert_equals(lambda: binary_search(sorted_list_4, "banana"), 1))
    print(test.assert_equals(lambda: binary_search(unsorted_test_1, "apple"), 1)) # Will throw an error (Maximum recursion depth exceeded)