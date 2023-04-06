import worksheet_12, random

def generate_values(min, max, cycles):
  generated = [random.randint(min, max) for i in range(cycles)]
  return generated

# Question 8
"""
sample_mass = [random.randint(0, 50) for i in range(10)]
sample_height = [random.randint(0, 50) for i in range(10)]
gpe_results = []
for i in range(10):
  gpe_results.append(worksheet_12.calculate_gpe(sample_mass[i], sample_height[i], 9.8))

print(gpe_results)
"""

# Question 9
"""
sample_psi = generate_values(0, 350, 10)
psi_results = []
for i in range(len(sample_psi)):
  psi_results.append(worksheet_12.check_psi(sample_psi[i]))

print(psi_results)
"""

# Question 10
"""
sample_sides = generate_values(0, 9, 10)
polygon_results = []
for i in range(len(sample_sides)):
  polygon_results.append(worksheet_12.identify_polygon(sample_sides[i]))

print(sample_sides)
print(polygon_results)
"""

# Question 11
"""
sample_int = generate_values(-100, 100, 20)
positive = 0
negative = 0
zero = 0
for i in range(len(sample_int)):
  result = worksheet_12.identify_integers(sample_int[i])
  if result == "Positive":
    positive += 1
  elif result == "Negative":
    negative += 1
  else:
    zero += 1
print(sample_int)
print(positive, negative, zero)
"""

# Question 12

display = "*************************\n1. +\n2. -\n3. *\n4. /\n*************************"
print(display)
operator = int(input("Key in the number for operator (1 to 4): "))
first_int = int(input("Enter your first integer? "))
second_int = int(input("Enter your second integer? "))
print(worksheet_12.calculate_operation(operator, first_int, second_int))

# Automated test, kinda...
"""
sample_operators = generate_values(0, 5, 10)
sample_firstint = generate_values(0, 10, 10)
sample_second_int = generate_values(0, 10, 10)
results = []
for i in range(10):
  results.append(worksheet_12.calculate_operation(sample_operators[i], sample_firstint[i], sample_second_int[i]))

print(sample_operators)
print(sample_firstint)
print(sample_second_int)
print(results)
"""