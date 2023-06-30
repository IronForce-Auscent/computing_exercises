word = input("Please enter your word: ")
word = word.lower()
begin_p = True if word[0] == "p" else False
end_h = True if word[-1] == "h" else False
contain_e = True if "e" in word else False
word_length = len(word)

if begin_p:
    print("Invalid. You entered a word that begins with 'p'.")
elif end_h:
    print("Invalid. You entered a word that ends with 'h'.") 
elif contain_e:
    print("Invalid. You entered a word that contains 'a'.")
else:   
    if not begin_p and not end_h and not contain_e: 
        if word_length < 4:
            print("The length of the word is short.") 
        elif word_length >= 4 and word_length <= 10:
            print("The length of the word is medium.") 
        else:
            print("The length of the word is long.") 