"""
A particular retailer is having a 60 percent off sale on a variety of discontinued
products. The retailer would like to help its customers determine the reduced price
of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied. Write a program that
uses a loop to generate this table, showing the original price, the discount amount,
and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
that the discount amounts and the new prices are rounded to 2 decimal places when
they are displayed.
"""

from tabulate import tabulate

def exercise_62():
  original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
  discount_price = [str(a * 0.6) for a in original_price]
  new_price = [str(a * 0.4) for a in original_price]
  table = []
  for i in range(len(original_price)):
    table += [str(original_price[i]), discount_price[i], new_price[i]]
  header = ["Original Price", "Discount Amount", "Discounted Price"]
  print(tabulate(table, headers=header))


"""
for i in range(5):

"""