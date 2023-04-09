"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
"""
from math import floor

def calculate_change(cents: int):
    PENNY, NICKEL, DIME, QUARTER, LOONIE, TOONIE = 1, 5, 10, 25, 100, 200
    to_toonie = floor(cents / TOONIE)
    to_loonie = floor((cents - (to_toonie * TOONIE)) / LOONIE)
    to_quarter = floor((cents - (to_toonie * TOONIE) - (to_loonie * LOONIE)) / QUARTER)
    to_dime = floor((cents - (to_toonie * TOONIE) - (to_loonie * LOONIE) - (to_quarter * QUARTER)) / DIME)
    to_nickel = floor((cents - (to_toonie * TOONIE) - (to_loonie * LOONIE) - (to_quarter * QUARTER) - (to_dime * DIME)) / NICKEL)
    to_penny = floor((cents - (to_toonie * TOONIE) - (to_loonie * LOONIE) - (to_quarter * QUARTER) - (to_dime * DIME) - (to_nickel * NICKEL)))
    print(f"Converting {cents} cents: {to_toonie} toonies, {to_loonie} loonies, {to_quarter} quarters, {to_dime} dimes, {to_nickel} nickels and {to_penny} pennies")