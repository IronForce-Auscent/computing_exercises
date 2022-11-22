import generate


user_input = int(input("Select a number from 1 to 9 inclusive: "))
column = int(input("Input number of columns: "))
if user_input == 1: # Completed
  generate.generate_1(column)
elif user_input == 2: # Completed
  generate.generate_2(column)
elif user_input == 3: # Completed
  generate.generate_3(column)
elif user_input == 4: 
  generate.generate_4(column)
elif user_input == 5: # Completed
  generate.generate_5(column)
elif user_input == 6: # Completed
  generate.generate_6(column)
elif user_input == 7:
  generate.generate_7(column)
elif user_input == 8:
  generate.generate_8(column)
elif user_input == 9:
  generate.generate_9(column)
