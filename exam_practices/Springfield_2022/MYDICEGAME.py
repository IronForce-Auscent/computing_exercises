import random   # Error 3

while True:   # Error 1   
  dice_list = []
  for i in range(2):  
    input("Player {}, press enter to roll the three dice".format(i+1))
    dice = [] # Error 8
    for j in range(3):
      dice.append(random.randint(0, 6)) # Error 9      
    dice_list.append(dice)  # Error 2     
    print("Player {}, dice = {}" .format(i+1,dice)) # Error 10      

  if max(dice_list[0]) > max(dice_list[1]):
    print("Player 1 wins!")
  elif max(dice_list[0]) == max(dice_list[1]): # Error 4      
    print("No winners!")
  else:   # Error 5   
    print("Player 2 wins!")

  play = input("Play again? (Y/N): ").upper()  # Error 7   
  if play == 'N':
    print("Thank you for playing, goodbye!")
    break  # Error 6