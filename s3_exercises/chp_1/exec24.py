"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration
"""

def exercise_24(days: int, hours: int, minutes: int, seconds: int):
    return (days * 86400) + (hours * 3600) + (minutes * 60) + seconds