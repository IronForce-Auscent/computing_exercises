"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should 
use one of the following two formulas to compute the BMI before displaying it. 
"""
from math import pow

def calculate_bmi(height: float, weight: float):
    return (weight / (pow(height, 2)))