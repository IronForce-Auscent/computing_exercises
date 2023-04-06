def calculate_gpe(mass, height, grav_acc): # Question 8
  return mass * height * grav_acc

def check_psi(psi_value):   # Question 9
  if psi_value >= 0 and psi_value <= 50:
    return "Good"
  elif psi_value >= 51 and psi_value <= 100:
    return "Moderate"
  elif psi_value >= 101 and psi_value <= 200:
    return "Unhealthy"
  elif psi_value >= 201 and psi_value <= 300:
    return "Very unhealthy"
  else: 
    return "Hazardous"

def identify_polygon(poly_sides): # Question 10
  sides_compare = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon"}
  return sides_compare[poly_sides]

def check_integers(integer): # Question 11
  sum = 0
  sum += integer
  if integer < 0:
    return "Negative"
  elif integer == 0:
     return "Zero"
  else:
    return "Positive"
  return sum

def simple_calculator(func, value1, value2):
  if func == 1:
    return value1 + value2
  elif func == 2:
    return value1 - value2
  elif func == 3:
    return value1 * value2
  elif func == 4:
    return value1 / value2
  else:
    return "Invalid function called"

def identify_polygon(poly_sides):
  sides_compare = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon"}
  if poly_sides >= 3 and poly_sides <= 8:
    return sides_compare[poly_sides]
  else:
    return "Unknown polygon sides"

def identify_integers(input_int):
  if input_int > 0:
    return "Positive"
  elif input_int < 0:
    return "Negative"
  else:
    return "Zero"

def calculate_operation(operation, first_int, second_int):
  if operation == 1:
    return first_int + second_int
  elif operation == 2:
    return first_int - second_int
  elif operation == 3:
    return first_int * second_int
  elif operation == 4:
    return first_int / second_int
  else:
    return "Invalid operation selected"