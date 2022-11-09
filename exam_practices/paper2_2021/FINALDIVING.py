def finaldiving():
  total = 0
  highest = 0
  lowest = 99999999999999
  diver_score = 0
  grand_total = 0
  difficulty = float(input("Enter difficulty level: "))
  
  for i in range(5):
    for i in range(5):
      score = float(input("Enter Judge {}'s score: ".format(i+1)))
      if score > highest:
        highest = score
      if score < lowest:
        lowest = score
      total += score

    total -- (highest + lowest)
    diver_score = total * difficulty
    grand_total += diver_total
  print("Highest score: {}".format(highest))
  print("Lowest score: {}".format(lowest))
  print("Final score: {}".format(diver_score))