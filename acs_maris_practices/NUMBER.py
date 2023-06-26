for count in range(10):
    number = int(input('Enter a positive integer: '))

    if number >= 1 and number <= 40:
        print(number, '- Low')
    elif number > 40 and number <= 70:
        print(number, '- Medium')
    elif number > 70 and number <= 100:
        print(number, '- High')
