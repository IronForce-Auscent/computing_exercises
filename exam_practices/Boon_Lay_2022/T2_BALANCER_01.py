while True:
    print("Welcome to the string balancer")
    st1 = input('string 1: ')
    print(len(st1))
    st2 = input('string 2: ')
    print(len(st2))

    check = True
    for char in st2:
        if char not in st1:
            check = False
    if check == True:
        print("Strings are balanced")
    else:
        print("Strings are not balanced")
    print("String 1 is longer") if len(st1) > len(st2) else print("String 2 is longer")
    
    if input("Again? (Y/N): ") not in ["Y", "y"]:
        break