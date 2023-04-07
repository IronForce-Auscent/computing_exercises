"""
This program is a representation of how an O(n log n) time complexity program runs
"""
from utils.unit_tests import UnitTest

def merge_sort(to_sort: list) -> list:
    if len(to_sort) > 1:
        mid_index = len(to_sort) // 2
        first_half = to_sort[:mid_index]
        second_half = to_sort[mid_index:]

        # sort each half recursively
        merge_sort(first_half)
        merge_sort(second_half)
        i = j = k = 0
        
        # Copy data over to temporary lists
        while i < len(first_half) and j < len(second_half):
            if first_half[i] <= second_half[j]:
                to_sort[k] = first_half[i]
                i += 1
            else:
                to_sort[k] = second_half[j]
                j += 1
        
        # Check for leftover elements
        while i < len(first_half):
            to_sort[k] = first_half[i]
            i += 1
            k += 1
        
        while j < len(second_half):
            to_sort[k] = second_half[j]
            j += 1
            k += 1
    return to_sort


def test_merge_sort():
    # Tests currently do not work, looking into possible fixes in the future
    test = UnitTest()
    unsorted_int_list, sorted_int_list = [49, 26, 41, 13, 5, 48, 37, 7, 24, 33, 46, 19, 39, 18, 10, 28, 11, 35, 16, 27, 47, 44, 17], [5, 7, 10, 11, 13, 16, 17, 18, 19, 24, 26, 27, 28, 33, 35, 37, 39, 41, 44, 46, 47, 48, 49]
    unsorted_float_list, sorted_float_list = [32.1, 44.9, 31.7, 47.2, 43.6, 27.8, 29.1, 39.3, 40.6, 47.8, 25.0, 29.2, 47.6, 46.7, 28.5, 31.3, 25.5, 48.1, 49.5, 33.8, 45.4], [25.0, 25.5, 27.8, 28.5, 29.1, 29.2, 31.3, 31.7, 32.1, 33.8, 39.3, 40.6, 43.6, 44.9, 45.4, 46.7, 47.2, 47.6, 47.8, 48.1, 49.5]
    unsorted_string_list, sorted_string_list = ['pear', 'banana', 'apple', 'kiwi', 'orange', 'mango', 'strawberry', 'papaya', 'pineapple', 'peach', 'grape', 'watermelon', 'blueberry', 'cherry', 'apricot'], ['apricot', 'apple', 'banana', 'blueberry', 'cherry', 'grape', 'kiwi', 'mango', 'orange', 'papaya', 'peach', 'pear', 'pineapple', 'strawberry', 'watermelon']
    print(test.assert_equals(lambda: merge_sort(unsorted_int_list), sorted_int_list))
    print(test.assert_equals(lambda: merge_sort(unsorted_float_list), sorted_float_list))
    print(test.assert_equals(lambda: merge_sort(unsorted_string_list), sorted_string_list))