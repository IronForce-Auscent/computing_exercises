n1 = 0
n2 = 1
sequence = []

nterms = int(input("Enter the number of terms you want to output: "))
while nterms < 1:
    nterms = int(input("Please enter a positive number: "))

for i in range(nterms):
    sequence.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth