import random
a,b,c,d = [5, 17, -8], [-13, 19], [6, -9, 10, 0], [-14, 7] # input().split(","), input().split(","),input().split(",").input().split(",")
while True:
  A,B,C,D = map(lambda p:int(random.choice(p)),(a,b,c,d))
  if 0 == A+B+C+D:
    print(A,B,C,D)
    break