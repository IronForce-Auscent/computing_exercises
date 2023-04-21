"""
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

def sound_levels(decibal_level: int):
    sounds_dict = {130: 'Jackhammer', 106: 'Gas lawnmower', 70: 'Alarm clock', 40: 'Quiet room'}
    if decibal_level in sounds_dict:
        print(sounds_dict[decibal_level])
    else:
        # list comprehension + keys() function + lambda 
        res = sounds_dict[min(sounds_dict.keys(), key = lambda key: abs(key - decibal_level))]
        print(f"Closest to \'{res}\'")