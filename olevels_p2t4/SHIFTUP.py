def shiftup(char):
  if char == 'z':
    return 'a'
  elif char == 'a':
    return 'z'
  elif char.islower():
    return chr(ord(char) - 1)
  else:
    return char