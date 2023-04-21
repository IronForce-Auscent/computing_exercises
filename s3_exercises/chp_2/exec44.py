"""
Write a program that reads a month and day from the user. If the month and day match
one of the holidays listed then your program should display the holiday's name. Otherwise
your program should indicate that the entered month and day do not corrospond to a fixed-date 
holiday
"""

def date_to_holiday(date: str):
    holidays = {"January 1": "New Year\'s Day", "July 1": "Canada Day", "December 25": "Christmas Day"}
    if date in holidays.keys():
        print(holidays[date])
    else:
        print("Inputted date does not corrospond to a fixed-date holiday")