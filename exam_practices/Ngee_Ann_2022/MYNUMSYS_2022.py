choice = input("Press B for conversion to Binary and D for conversion to Denary: ").upper() # Error 9
while choice not in ["B", "D"]:  # Error 1
    print("Wrong input.")
    choice = input("Press B for conversion to Binary and D for conversion to Denary: ").upper() # Error 10
    
print(choice)
if choice == "B":  # Error 11
    denary = int(input("Enter denary number: ")) # Error 3
    # denary = (denary) - Error 2 
    binary = ""
    while True: 
        r = denary%2
        binary += str(r)
        denary = denary//2 # Error 4 
        if denary == 0:
            break # Error 5

    print("The binary number is:", binary[::-1]) # Error 6

elif choice == "D": 
    denary = 0
    binary = input("Enter denary number: ")
    binary = binary[::-1]
    for n in range(len(binary)):  # Error 7 
        denary += int(binary[n])*(2**n) # Error 8 
    print("The denary number is:", denary) 