"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
"""

def bread_cost_calculator(num_loaves: int) -> float:
    DISCOUNT = .6
    original_cost = num_loaves * 3.49
    discount = num_loaves * DISCOUNT
    discounted_cost = original_cost - discount
    return [original_cost, discount, discounted_cost]