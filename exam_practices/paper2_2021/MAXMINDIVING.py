
def minmaxdiving():
  total = 0
  highest = 0
  lowest = 99999999999999
  difficulty = float(input("Enter difficulty level: "))

  for i in range(5):
    score = float(input("Enter Judge {}'s score: ".format(i+1)))
    if score > highest:
      highest = score
    if score < lowest:
      lowest = score
    total += score

  diver_score = total * difficulty
  print("Diver score: {}".format(diver_score))
  print("Highest score: {}".format(highest))
  print("Lowest score: {}".format(lowest))