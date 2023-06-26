import random

#Write a function to convert denary to binary number
def denary_to_bin(decimal):

    conversion_table = ['0', '1']
    binary = ''

    while decimal>0:
        remainder = decimal%2
        binary = conversion_table[remainder]+ binary
        decimal = decimal//2
    return binary
