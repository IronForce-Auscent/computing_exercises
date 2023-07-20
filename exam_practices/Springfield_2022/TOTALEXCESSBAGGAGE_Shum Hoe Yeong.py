passenger_count = int(input("Enter the number of passengers: "))
total_weight, excess_cost = 0, 0

for _ in range(passenger_count):
    member_status = input("Are you a member of ABC Airline? (Y/N): ")
    weight = float(input("Enter the weight of baggage: "))

    while weight > 50:
        weight = float(input("Baggage exceeds maximum weight of 50kg, please enter the weight of another baggage: "))

    if weight > 30:
        excess_cost += (200 + (weight - 30) * 25) * 0.8 if member_status in ["Y", "y"] else (200 + (weight - 30) * 25)
    else:
        pass
    total_weight += weight
print(f"Total weight of baggage: {total_weight}\nTotal excess baggage cost: {excess_cost}")