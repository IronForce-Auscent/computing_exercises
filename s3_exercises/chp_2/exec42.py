"""
Write a program that will read a frequency from the user, and return the note name. If 
the frequency is within 1 Hz of a listed value, return the name of the note. Otherwise, return that the frequency 
does not corrospond to an existing note
"""

def frequency_to_note(frequency: float):
    notes_freq = {261.63: "C4", 293.66: "D4", 329.63: "E4", 349.23: "F4", 392.00: "G4", 440.00: "A4", 493.88: "B4"}
    found = 0
    for key, value in notes_freq.items():
        if frequency >= (key - 1) and frequency <= (key + 1):
            print(f"The note with frequency {frequency} is {value}")
            found = 1
        else:
            pass
    if found == 0:
        print(f"No notes with frequency {frequency} found in list")