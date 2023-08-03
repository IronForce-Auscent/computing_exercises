past_words = ["PopeyetheSailorm00n",
              "123qweasd",
              "Str0ngestpassw0rd"]
final = False

while final == False: 
    alpha_chk = False
    num_chk = False

    p1 = input("Enter new password: ") 
    while len(p1) < 8 or p1 in past_words:
        if len(p1) < 8:
            print("Please enter a password that has more than 8 characters: ")
        elif p1 in past_words:
            print("Pleas enter a new password that you have not used before: ")
        p1 = input("Enter new password: ")


    for i in p1:
        if i.isalpha():
            alpha_chk = True
        elif i.isdigit(): 
            num_chk = True
        elif not i.isalnum():
            alpha_chk = False
            num_chk = False
            break

    if alpha_chk == False or num_chk == False:
        print("Password has to be alphanumeric.")
            
    if (alpha_chk and num_chk):
        pwd_check = input("Please reenter your password: ")
        if pwd_check == p1:
            print("Password set.")
            final = True
        else:
            print("Passwords do not match")