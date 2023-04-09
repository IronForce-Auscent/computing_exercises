"""
This program is a representation of how an O(n ^ 2) time complexity program runs
"""
from utils.unit_tests import UnitTest

def generate_matrix(x_axis: list, y_axis: list) -> list:
    """
    Generates a matrix containing values from 2 lists, along with the product of the numbers in the center

    Arguments:
    x_axis (list): the values on the x-axis of the matrix
    y_axis (list): the values on the y-axis of the matrix

    Returns:
    matrix (list): the final matrix
    """
    matrix = []
    for y_item in y_axis:
        new_row = []
        for x_item in x_axis:
            new_row.append(x_item * y_item)
        matrix.append(new_row)
    return matrix

def test_generate_matrix():
    test = UnitTest()
    test_case_1_a, test_case_1_b, expected_output_1 = [6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [[6, 7, 8, 9, 10], [12, 14, 16, 18, 20], [18, 21, 24, 27, 30], [24, 28, 32, 36, 40], [30, 35, 40, 45, 50]]
    test_case_2_a, test_case_2_b, expected_output_2 = [3, 5, 7, 9, 11, 13, 15], [2, 4, 6, 8, 10, 12, 14], [[6, 10, 14, 18, 22, 26, 30], [12, 20, 28, 36, 44, 52, 60], [18, 30, 42, 54, 66, 78, 90], [24, 40, 56, 72, 88, 104, 120], [30, 50, 70, 90, 110, 130, 150], [36, 60, 84, 108, 132, 156, 180], [42, 70, 98, 126, 154, 182, 210]]
    test_case_3_a, test_case_3_b, expected_output_3 = [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [[7, 14, 21, 28, 35, 42], [8, 16, 24, 32, 40, 48], [9, 18, 27, 36, 45, 54], [10, 20, 30, 40, 50, 60], [11, 22, 33, 44, 55, 66], [12, 24, 36, 48, 60, 72]]
    test_case_4_a, test_case_4_b, expected_output_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80], [9, 18, 27, 36, 45, 54, 63, 72, 81, 90], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]
    print(test.assert_equals(lambda: generate_matrix(test_case_1_a, test_case_1_b), expected_output_1))
    print(test.assert_equals(lambda: generate_matrix(test_case_2_a, test_case_2_b), expected_output_2))
    print(test.assert_equals(lambda: generate_matrix(test_case_3_a, test_case_3_b), expected_output_3))
    print(test.assert_equals(lambda: generate_matrix(test_case_4_a, test_case_4_b), expected_output_4))