from math import inf

welcome_message = "Welcome to Simple Numbers\nNumbers please."

def user_input():
    numbers = input("Separate each number using spaces: ").split(" ")
    for num in numbers:
        if num.isnumeric():
            pass
        else:
            return user_input_error()
    return numbers

def user_input_error():
    numbers = input("Inputs must be integers: ").split(" ")
    for num in numbers:
        if num.isnumeric():
            pass
        else:
            user_input_error()
    return numbers

def get_average(nums: list):
    total = 0
    for num in nums:
        total += int(num)
    return total/len(nums)

def get_maximum(nums: list):
    largest = 0
    for num in nums:
        if int(num) > largest:
            largest = int(num)
    return largest

def get_minimum(nums: list):
    smallest = inf
    for num in nums:
        if int(num) < smallest:
            smallest = int(num)
    return smallest


def main():
    print(welcome_message)
    response = user_input()
    avg, maximum, minimum = get_average(response), get_maximum(response), get_minimum(response)
    print(f"Average: {avg}\nMaximum: {maximum}\nMinimum: {minimum}")
    return None


if __name__ == "__main__":
    main()