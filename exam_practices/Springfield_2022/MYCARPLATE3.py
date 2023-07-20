checksum_reference = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16,  "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}

def carplate(plate: str):
    checksum_string = plate[3:7]
    checksum, weight = checksum_reference[plate[2]], 4
    for num in checksum_string:
        checksum += (weight * int(num))
        weight -= 1
    return chr((checksum % 26) + 65)

def check_suffix(plate: str):
    suffix = plate[-1]
    correct_suffix = carplate(plate)
    if correct_suffix == suffix:
        return "Valid suffix"
    else:
        return f"Invalid checksum, correct checksum is {correct_suffix}"

def main():
    license_plate = input("Enter a car license plate: ")
    while len(license_plate) not in [7, 8]:
        license_plate = input("Invalid car license plate entered, please enter a valid license plate: ")
    if len(license_plate) == 7:
        print(carplate(license_plate))
    else:
        print(check_suffix(license_plate))

main()