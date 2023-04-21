"""
Write a program that reads the denomination of a banknote from the user, then
display the name of the individual that appears on the banknote of the entered amount.
An appropriate error message should be displayed if no such note exists

Assume that all values are in USD (banknotes being checked belong to the US)
"""

def identify_individual(denomination: int):
    individuals = {1: "George Washington", 2: "Thomas Jefferson", 5: "Abraham Lincoln", 10: "Alexander Hamilton", 20: "Andrew Jackson", 50: "Ulysses S. Grant", 100: "Benjamin Franklin"}
    if denomination in individuals.keys():
        print(f"The individual on the note with the ${denomination} denomination is {individuals[denomination]}")
    else:
        print(f"No such note exists")