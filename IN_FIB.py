n1 = 0
n2 = 1
sequence = []

nterms = 100
guess = int(input("Enter a positive integer: "))

for i in range(nterms):
    sequence.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

if guess in sequence:
    print("Your guess is in sequence")
else:
    print("Your guess is not within the sequence")