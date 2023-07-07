def get_price(option):
    cake_list = ["A", "B", "C", "D","E","F","G","H"]
    price_list = [25, 22, 38, 35, 15, 40, 53, 20]
    position = cake_list.index(option)
    return price_list[position]

def get_input():
    choice = input("Enter the choice of cake: ")
    while True:
        if choice in ("A", "B", "C", "D","E","F","G","H"):
            print(choice); break
        else:
            choice = input("Enter the uppercase letter between A to H only: ")


get_input()