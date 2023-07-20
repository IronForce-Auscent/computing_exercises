member_status = input("Are you a member of ABC Airline? (Y/N): ")
weight = float(input("Enter the weight of baggage: "))

while weight > 50:
    weight = float(input("Baggage exceeds maximum weight of 50kg, please enter the weight of another baggage: "))

if weight >= 20 and weight <= 30:
    cost = (weight - 20) * 20
elif weight > 30:
    cost = (200 + (weight - 30) * 25) * 0.8 if member_status == "Y" else (200 + (weight - 30) * 25)
else:
    cost = 0
print(f"The excess baggage cost is ${cost}\nThank you for being a member of ABC Airline")