filler = 'x'
display = ""

def generate_1(column):
  """
  x----
  xx---
  xxx--
  xxxx-
  xxxxx
  """
  for i in range(column):
    print(filler * (i + 1))

def generate_2(column):
  """
  ----x
  ---xx
  --xxx
  -xxxx
  xxxxx
  """
  for i in range(column):
    print((" " * (column - i)) + (filler * (i + 1)))

def generate_3(column):
  """
  ----x----
  ---xxx---
  --xxxxx--
  -xxxxxxx-
  xxxxxxxxx
  """
  global display
  for i in range(column):
    display = ""
    display += (" " * (column - i))
    display += (filler * ((2 * (i + 1) - 1)))
    display += (" " * (column - i))
    print(display)

def generate_4(column):
  """
  ----x----
  ---x-x---
  --x-x-x--
  -x-x-x-x-
  x-x-x-x-x
  -x-x-x-x-
  --x-x-x--
  ---x-x---
  ----x----
  """
  global display
  for i in range(1, (column + 1)):
    display = ""
    display += (" " * (column - i))
    if i != (column):
      display += ((filler + " ") * i)
      display += " "
    else:
      display += ((filler + " ") * (i - 1))
      display += filler
      display += (" " * (column - i))
    print(display)
    
  for i in range((column - 1), 0, -1):
    display = ""
    display += (" " * (column - i))
    display += ((filler + " ") * i)
    display += (" " * (column - (i + 1)))
    print(display)
    
def generate_5(column):
  """
  xxxxx
  xxxx-
  xxx--
  xx---
  x----
  """
  for i in range(column, 0, -1):
    display = ""
    display += (filler * i)
    print(display)

def generate_6(column):
  """
  xxxxx
  -xxxx
  --xxx
  ---xx
  ----x
  """
  for i in range(column):
    display = ""
    display += (" " * i)
    display += (filler * (column - i))
    print(display)

def generate_7(column):
  """
  ----x
  ---xx
  --x-x
  -x--x
  xxxxx
  """
  display = ""
  display += ((" " * (column - 1)) + (filler * 1))
  print(display)
  display = ((" " * (column - 2)) + (filler * 2))
  print(display)
  for i in range(1, column - 2):
    display = ""
    display += (" " * (column - (i + 2)))
    display += filler
    display += (" " * i)
    display += filler
    print(display)

  display = (filler * column)
  print(display)
    
def generate_8(column):
  """
  x----
  xx---
  x-x--
  x--x-
  xxxxx
  """
  print(filler + (" " * (column - 1)))
  print((filler * 2) + (" " * (column - 2)))
  for i in range(1, (column - 2)):
    display = ""
    display += filler
    display += (" " * i)
    display += filler
    display += (" " * (column - (i + 2)))
    print(display)
  print(filler * column)
  
def generate_9(column):
  """
  1 space:
  xxx
  x-x
  xxx
  2 spaces:
  xxxx
  x--x
  x--x
  xxxx
  3 spaces:
  xxxxx
  x---x
  x---x
  x---x
  xxxxx
  """
  display = ""
  display += (filler * (column + 2))
  for i in range(column):
    display += "\n"
    display += filler
    display += (" " * column)
    display += filler
  display += "\n"
  display += (filler * (column + 2))
  print(display)