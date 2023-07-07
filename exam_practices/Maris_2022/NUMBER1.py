iteration = int(input("Enter the number of inputs: "))
highs = []

for count in range(iteration):
    number = int(input('Enter a positive integer: '))
    while number < 0 or number > 100:
        number = int(input("Enter a positive number between 0 and 100 inclusive: "))

    if number >= 1 and number <= 40:
        print(number, '- Low')
    elif number > 40 and number <= 70:
        print(number, '- Medium')
    elif number > 70 and number <= 100:
        highs.append(number)
        print(number, '- High')

print(f"Numbers classified as high: {highs}")