"""
Write a program that reads the name of a note from the user and display the note's frequency. Your
program should support all of the notes listed above.

Once it is working properly for the provided notes, add support for all the notes from C0 to C8. Try to avoid using if...else statements
as it is tedious, and instead exploit the relationship between notes in adjacent octaves
"""

def identify_note_frequency(note: str):
    notes_frequency = {'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88}
    if note in notes_frequency.keys():
        print(f"The frequency of {note} is {notes_frequency[note]}")
    else:
        if note[0] != "C":
            print("uhh...")
        else:
            c4_freq, current_octave, note_freq = 261.63, int(note[1]), 261.63
            note_freq = c4_freq / (2 ** (4 - current_octave))
            print(f"The frequency of {note} is {note_freq}")


identify_note_frequency("C4")
identify_note_frequency("E4")
identify_note_frequency("C1")
identify_note_frequency("C8")