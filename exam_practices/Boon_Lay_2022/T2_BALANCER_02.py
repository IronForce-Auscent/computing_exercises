while True:
    print("Welcome to the string balancer")
    strings = []
    strings.append(input("string 1: "))
    strings.append(input("string 2: "))
    print(len(strings[0]))
    print(len(strings[1]))

    check = True
    for char in strings[1]:
        if char not in strings[0]:  
            check = False
    if check == True:
        print("Strings are balanced")
    else:
        print("Strings are not balanced")
    print("String 1 is longer") if len(strings[1]) > len(strings[0]) else print("String 2 is longer")
    
    if input("Again? (Y/N): ") not in ["Y", "y"]:
        break