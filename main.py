from s3_exercises.chp_5.exec125 import exercise_125 as exec125
from utils.unit_tests import UnitTest

def test_func():
    x = 0
    for i in range(1000000000):
        x += i
    return True

test = UnitTest()
res = test.assert_equals(lambda: test_func(), True)
print(res)


"""import random
a,b,c,d = [5, 17, -8], [-13, 19], [6, -9, 10, 0], [-14, 7] # input().split(","), input().split(","),input().split(",").input().split(",")
while True:
  A,B,C,D = map(lambda p:int(random.choice(p)),(a,b,c,d))
  if 0 == A+B+C+D:
    print(A,B,C,D)
    break"""