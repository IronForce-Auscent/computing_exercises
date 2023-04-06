from utils import generate_samples

import datetime

class UnitTest():
    """
    Mimics the unit test library used by Codewars

    Functions:
    assert_equals: runs a given function, then checks if the result obtains is the same as the expected result or not, as well as the runtime (in milliseconds)
    """
    def __init__(self):
        self.upper_alphabet = generate_samples.generate_alphabet()['list-format']['uppercase']
        self.lower_alphabet = generate_samples.generate_alphabet()['list-format']['uppercase']
    
    def assert_equals(self, code_to_test: function, expected_result) -> str:
        """
        Checks if the result of a function is the same as the expected result, and returns the runtime (in millseconds)

        Arguments:
        code_to_test (func): The function that is being tested, code must have at least 1 "return" function to return the result from the code
        expected_result (Any): The expected result from the code

        Returns:
        res (str): Returns 1 of 3 possible results
            - Exception/error has occured: "Returned error x"
            - Test failed, no errors: "Expected (result x), got (result y) instead with runtime of x ms"
            - Test passed: "Test passed with runtime of x ms
        """
        test_res, res = "", ""
        try:
            start_time = datetime.datetime.now()
            test_res = code_to_test()
        except Exception as e:
            res = f"Returned error {e}"
        else:
            end_time = datetime.datetime.now()
            delta = end_time - start_time
            if test_res == expected_result:
                res = f"Test passed with runtime of {delta.total_seconds() * 1000} ms"
            else:
                res = f"Expected \'{expected_result}\', got \'{test_res}\' instead with runtime of {delta.total_seconds() * 1000} ms"
        return res