"""
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.

Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
"""

def calculate_heating_cost(mass, change):
    HEAT_CAPACITY, JOULES_KW = 4.186, 2.777e-7
    energy = mass * change * HEAT_CAPACITY
    kwh = energy * JOULES_KW
    cost = kwh * 8.9
    print(f'Energy required: {energy}')
    print(f'Total cost: {cost}')