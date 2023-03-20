"""Using your solutions to Exercises 94 and 96, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise."""

from .exec96 import exercise_96 as check_password
from .exec94 import exercise_94 as generate_password

def exercise_97():
    password_generated = generate_password()
    print(password_generated)
    count = 0
    while check_password(password_generated) != "Strong password":
        password_generated = generate_password()
        count += 1
    
    res = f"Valid password generated after {count} tries: {password_generated}"
    return res