import random

class Network():
    def denary_to_bin(self, decimal):
        conversion_table = ['0', '1']
        binary = ''

        while decimal>0:
            remainder = decimal%2
            binary = conversion_table[remainder]+ binary
            decimal = decimal//2
        return binary

    def denary_to_hex(self, number):
        conversion_table, hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'], ""
        while number > 0:
            remainder = number % 16
            hex = conversion_table[remainder] + hex
            number = number // 16
        return hex

    def randomnumber(self, start, end):   
        return random.randint(start, end)

    def createIPv4(self):   
        return f"{self.randomnumber(0, 255)}.{self.randomnumber(0, 255)}.{self.randomnumber(0, 255)}.{self.randomnumber(0, 255)}"

    def storeIPv4(self, n):
        return [self.createIPv4() for _ in range(n)]

    def createIPv6(self):
        return f"{self.denary_to_hex(self.randomnumber(0, 65535))}.{self.denary_to_hex(self.randomnumber(0, 65535))}.{self.denary_to_hex(self.randomnumber(0, 65535))}.{self.denary_to_hex(self.randomnumber(0, 65535))}.{self.denary_to_hex(self.randomnumber(0, 65535))}.{self.denary_to_hex(self.randomnumber(0, 65535))}"

    def createMAC(self):
        return f"{self.denary_to_hex(self.randomnumber(0, 255))}:{self.denary_to_hex(self.randomnumber(0, 255))}:{self.denary_to_hex(self.randomnumber(0, 255))}:{self.denary_to_hex(self.randomnumber(0, 255))}:{self.denary_to_hex(self.randomnumber(0, 255))}:{self.denary_to_hex(self.randomnumber(0, 255))}"
    
    def network(self):
        print("Option 1: Create an IPv4 address\nOption 2: Create an IPv6 address\nOption 3: Create a MAC address")
        option = int(input("Please select options 1/2/3: "))
        while option not in (1, 2, 3):
            option = int(input("Re-enter options 1/2/3: "))
        print(self.createIPv4() if option == 1 else self.createIPv6() if option == 2 else self.createMAC())

network = Network()
network.network()
ip_addresses = network.storeIPv4(10)
print(ip_addresses)