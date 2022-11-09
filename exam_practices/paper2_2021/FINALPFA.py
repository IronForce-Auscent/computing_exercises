flag = True  
while flag:
    total = 0 # Error 2
    sit_up = int(input("Enter the number of sit_ups: "))
    pull_up = int(input("Enter the number of pull_ups: "))
    run = float(input("Enter the timing for 2 km run: ")) # Error 1  

    if sit_up == 0:
      flag = False  # Error 13 
      break

    if 33 <= sit_up <= 36:  
        print("You have achieved a 'C' grade for Sit-ups!")
        total +=3
    elif 37 <= sit_up <= 40:   # Error 8
        print("You have achieved a 'B' grade for Sit-ups!")
        total +=4
    elif sit_up > 40:
        print("You have achieved a 'A' grade for Sit-ups!")
        total +=5

    if pull_up == 5: # Error 2   
        print("You have achieved a 'C' grade for Pull-ups!")
        total +=3
    elif 6 <= pull_up < 7: # Error 3   
        print("You have achieved a 'B' grade for Pull-ups!")
        total +=4
    elif pull_up > 7:
        print("You have achieved a 'A' grade for Pull-ups!")
        total +=5   # Error 12

    if 11 <= run < 12:
        print("You have achieved a 'C' grade for 2 km run!")
        total +=3
    elif 10 <= run < 11:
        print("You have achieved a 'B' grade for 2 km run!")
        total +=4
    elif run < 10:
        print("You have achieved a 'A' grade for 2 km run!")
        total +=5
    print("You have a total score of {}".format(total)) # Error 4   
    
    if total > 13 and run < 10:
        print("You have achieved Gold award")
    elif total > 11 and run < 11: 
        print("You have achieved Silver award")
    elif total > 9 or run < 12: 
        print("You have achieved Bronze award")
    else: # Error 7   
        print("You did not achieve any award")
