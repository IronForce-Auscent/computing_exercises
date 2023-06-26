def get_price(option):
    cake_list = ["A", "B", "C", "D","E","F","G","H"]
    price_list = [25, 22, 38, 35, 15, 40, 53, 20]
    position = cake_list.index(option)
    return price_list[position]

def get_input():
    choice = input("Enter the choice of cake: ")
    while True:
        if choice in ("A", "B", "C", "D","E","F","G","H"):
            return choice
        else:
            choice = input("Enter the uppercase letter between A to H only: ")

def get_order():
    total_cost = 0
    GST = 0.07
    while True:
        total_cost += get_price(get_input())
        more_order = input("More purchase? Y or N: ")
        if more_order == "Y":
            pass
        else:
            break
    print(f"""
    Subtotal   ${round(total_cost, 2)}
    GST        ${round(total_cost * GST, 2)}
    Total      ${round(total_cost * (1 + GST), 2)}

    Thank you!
    """)

get_order()