"""
A sublist is a list that makes up part of a larger list. A sublist may be a list containing a single element, multiple
elements, or even no elements at all. For example, [1], [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3]
is also a sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because the elements 2 and 4 are not adjacent
in the longer list. The empty list is a sublist of any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of
itself, meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4]. In this exercise you will create a function, isSublist,
that determines whether or not one list is a sublist of another. Your function should take two lists, larger and smaller,
as its only parameters. It should return True if and only if smaller is a sublist of larger. Write a main program that
demonstrates your function.
"""

def exercise_125():
  smaller = []
  larger = []
  user_input = input("Enter an entry (sublist): ")
  while user_input != "0":
    user_input.replace(" ", "")
    if user_input != "":
      smaller.append(user_input)
    user_input = input("Enter another entry (sublist): ")
  user_input = input("Enter an entry (main list): ")
  while user_input != "0":
    user_input.replace(" ", "")
    if user_input != "":
      larger.append(user_input)
    user_input = input("Enter another entry (main list): ")
  print(smaller)
  print(larger)
  print(isSublist(smaller, larger))


def isSublist(smaller, larger):
  if smaller == []:
    return True
  for entry in smaller:
    if entry in larger and len(smaller) > 1:
      entry_index = larger.index(entry)
      current_index = smaller.index(entry)
      print(entry)
      print(entry_index)
      print(current_index)
      next_char = ""
      if current_index == 0:
        next_char = smaller[current_index + 1]
      else:
        next_char = smaller[current_index - 1]
      print(next_char)
      if (larger.index(next_char) - 1) != entry_index or (larger.index(next_char) + 1) != entry_index:
        return False
      else:
        return True  
    elif entry in larger and len(smaller) == 1:
      return True
    else:
      return False