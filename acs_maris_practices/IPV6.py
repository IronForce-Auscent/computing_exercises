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

def denary_to_hex(number):
    conversion_table, hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], ""
    while number > 0:
        remainder = number % 16
        hex = conversion_table[remainder] + hex
        number = number // 16
    return hex

def randomnumber(start, end):
    return random.randint(start, end)

def createIPv4():
    return f"{randomnumber(0, 255)}.{randomnumber(0, 255)}.{randomnumber(0, 255)}.{randomnumber(0, 255)}"

def storeIPv4(n):
    ip_addresses = []
    for i in range(n):
        ip_addresses.append(createIPv4())
    return ip_addresses

def createIPv6():
    return f"{denary_to_hex(randomnumber(0, 65535))}.{denary_to_hex(randomnumber(0, 65535))}.{denary_to_hex(randomnumber(0, 65535))}.{denary_to_hex(randomnumber(0, 65535))}.{denary_to_hex(randomnumber(0, 65535))}.{denary_to_hex(randomnumber(0, 65535))}"
