"""
Write two functions, hex2int and int2hex, that convert between hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B,
C, D, E and F) and base 10 integers. The hex2int function is responsible for converting a string containing a single
hexadecimal digit to a base 10 integer, while the int2hex function is responsible for converting an integer between
0 and 15 to a single hexadecimal digit. Each function will take the value to convert as its only parameter and return
the converted value as the function’s only result. Ensure that the hex2int function works correctly for both
uppercase and lowercase letters. Your functions should end the program with a meaningful error message if an
invalid parameter is provided.
"""
hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
integer = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

def split(to_split, mode):
  if mode == "hex2int":
    return [to_split[i] for i in range(len(to_split))]
  elif mode == "int2hex":
    sliced_string = [to_split[i] for i in range(len(to_split))]
    result = []
    i = 0
    while i < (len(to_split) - 1):
      result.append(sliced_string[i] + sliced_string[i+1])
      i += 2
    return result

def exercise_98_hex2int(string):
  split_string = split(string, "hex2int")
  result = ""
  for char in split_string:
    result += integer[hexa.index(char.upper())]
  return result

def exercise_98_int2hex(string):
  split_string = split(string, "int2hex")
  result = ""
  for char in split_string:
    result += hexa[integer.index(char)]
  return result