letter = ['J','K','Q','A','2','3','4','5','6','7','8','9']
suit = ['D','C','H','S']
import random 
total1 = 0 
total2 = 0
def deal():
  deal = []
  for i in range (52):
    num= random.choice(letter)
    pattern= random.choice(suit)
    total = num + pattern 
    deal.append(total)
  return deal 

print(deal())
card_point = { 'J': 0,'K': 0,'Q': 0,'A': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0}

"""
def points():
  p1 = []
  p2 = []
  player1 = deal()
  number1 = player1[0:26]
  p1.append(number1)
  for card in p1:
    for c in card:
      if c in card_point:
        card_point[c] += 1

  
      
  print(card_point)
        #,J,Q,one,two,three,four,five,six,seven,eight,nine,ten)
    
  player2 = deal()
  number2 = player2[0:26]
  p2.append(number2)

    
"""