"""
This program is a representation of how an O(1) time complexity program runs
"""
from utils.unit_tests import UnitTest
from utils.generate_samples import generate_alphabet, generate_random_numbers

def list_search(to_search: list):
    """
    Returns the first entry in a non-empty list

    Arguments:
    to_search (list): a list with a non-zero length

    Returns: 
    result (Any): the first item (ie to_search[0]) in the given list
    """
    return to_search[0] if len(to_search) > 0 else "List is too short"

def test_list_search():
    # Code might take a while to execute when generating random numbers
    test = UnitTest()
    alphabet = generate_alphabet()['list-format']['uppercase']
    number_list = generate_random_numbers(1000000, 1, 1e10)
    print(test.assert_equals(lambda: list_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1))
    print(test.assert_equals(lambda: list_search(alphabet), 'A'))
    print(test.assert_equals(lambda: list_search(number_list), number_list[0]))