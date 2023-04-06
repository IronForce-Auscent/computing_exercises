"""
In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.
"""
from math import floor

def exercise_25(seconds: int):
    days = floor(seconds / 86400)
    hours = floor((seconds - (days * 86400)) / 3600)
    minutes = floor((seconds - (days * 86400) - (hours * 3600)) / 60)
    seconds -= (days * 86400 + hours * 3600 + minutes * 60)
    return f"{days}:{hours}:{minutes}:{seconds}" 