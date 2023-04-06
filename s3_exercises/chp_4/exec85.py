"""
Words like first, second and third are referred to as ordinal numbers. In this exercise, you will write a function that
takes an integer as its only parameter and returns a string containing the appropriate English ordinal number as
its only result. Your function must handle the integers between 1 and 12 (inclusive). It should return an empty
string if a value outside of this range is provided as a parameter. Include a main program that demonstrates your
function by displaying each integer from 1 to 12 and its ordinal number. Your main program should only run when
your file has not been imported into another program.
"""

int_string = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12}
def exercise_85(ord_num):
  x = lambda ord_num: int_string[ord_num] if (ord_num in int_string) else " "
  return x(ord_num)

"""
from s3_exercises.exec85 import exercise_85 as exec85

ordinal = input("Enter an ordinal number: ")
print(exec85(ordinal))
"""