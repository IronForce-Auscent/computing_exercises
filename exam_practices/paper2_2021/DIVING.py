# <------------ ORIGINAL SOURCE FILE -------------->

total = 0
difficulty = float(input("Enter difficulty level: "))

for i in range(5):
  score = float(input("Enter Judge {}'s score: ".format(i+1)))
  total += score

diver_score = total * difficulty
print("Diver score: {}".format(diver_score))
