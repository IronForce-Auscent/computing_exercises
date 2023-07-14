while True:
    print("Welcome to the string balancer")
    st1 = input('string 1: ')
    st2 = input('string 2: ')

    check = True

    for char in st2:
        if char not in st1:
            check = False

    if check == True:
        print("Strings are balanced")
    else:
        print("Strings are not balanced")

    if input("again? (y/n): ")!= 'y':
        break