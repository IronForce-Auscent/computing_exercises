nric = input("Enter NRIC here: ")
allocated_alphabet = nric[-1]
allocated_dict = {0:'J', 1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}
count = 0

if nric != 0:
  for num in range(1, 8):
    count += int(nric[num])
  if nric[0] == 'T':
    count += 4

  identifier = count % 11
  if allocated_dict[identifier] == allocated_alphabet:
    print("You have entered a valid NRIC number!")
  else:
    print("You have entered an invalid NRIC number!")