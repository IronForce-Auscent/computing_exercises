def even(word):  # Error 1
    count = 0  # Error 2
    for char in word:
        if char == '1': # Error 11 
            count += 1
    if count % 2 == 0:
        return ("Parity bit = {}".format(0))
    else:
        return ("Parity bit = {}".format(1))

def odd(word): # Error 3
    count = 0
    for char in word:
        if char == '1':
            count += 1  # Error 4
    # print(count)   - Error 10
    if count % 2 == 1: # Error 6 
        return ("Parity bit = {}".format(0)) 
    else:
        return ("Parity bit = {}".format(1))  # Error 5
    
print("Parity Bits") # Error 7 

parity = input("Choose between Even or Odd Parity.\n0 for Even, 1 for Odd : ")

print("Input the 7 bit binary word")
word = input("word: ") # Error 8 

if parity == '0':
    print(even(word)) # Error 9 
elif parity == '1':
    print(odd(word))