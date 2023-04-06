"""
Many recipe books still use cups, tablespoons and teaspoons to describe the volumes of ingredients used when
cooking or baking. While such recipes are easy enough to follow if you have the appropriate measuring cups and
spoons, they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended
family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when
quadrupled. However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup. Write a
function that expresses an imperial volume using the largest units possible. The function will take the number of
units as its first parameter, and the unit of measure (cup, tablespoon or teaspoon) as its second parameter. Return
a string
representing the measure using the largest possible units as the function’s only result.
For example, if the function is provided with parameters representing 59 teaspoons then it should return the string
“1 cup, 3 tablespoons, 2 teaspoons”.
Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons.
"""
import math

def exercise_102(unit, measure):
  output = {"teaspoon": 0, "tablespoon": 0, "cup": 0}
  result = ""
  if measure == "teaspoon" or measure == "teaspoons":
    output["cup"] = math.floor(unit / 48)
    output["tablespoon"] = math.floor((unit - (output["cup"] * 48)) / 3)
    output["teaspoon"] = unit - (output["tablespoon"] * 3) - (output["cup"] * 48)
  elif measure == "tablespoon" or measure == "tablespoons":
    output["cup"] = math.floor(unit / 16)
    output["tablespoon"] = math.floor((unit - output["cup"] * 16))
  else:
    return False

  result = str(output["cup"]) + " cups " + str(output["tablespoon"]) + " tablespoons " + str(output["teaspoon"]) + " teaspoons"
  return result