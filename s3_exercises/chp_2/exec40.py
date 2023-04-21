"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle
"""

def identify_triangles(length_1: float, length_2: float, length_3: float):
    if length_1 == length_2 == length_3:
        print("This is an equilateral triangle")
    elif ((length_1 == length_2) and length_3 != length_1) or ((length_2 == length_3) and length_1 != length_2) or ((length_3 == length_1) and length_2 != length_3):
        print("This is an isoceles triangle")
    else:
        print("This is a scalene triangle")