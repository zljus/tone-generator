# Zack James
# CS21
# This program generates random notes from certain musical modes

# Import libraries
import pyaudio
import numpy as np
import random

def main():
    # Welcome user and show modes
    print("Welcome to note generator!")
    print("This program generates random notes from a tonic of C.")
    print('''
    1 = Dorian
    2 = Ionian
    3 = Phrygian
    4 = Lydian
    5 = Mixolydian
    6 = Aeolian
    7 = Locrian
    ''',)

    # Set variable to return to / run once
    x = 1
    while x == 1:
        # User input that I'll pass to the function
        mode = input("Choose your mode and enter the corresponding number: ")
        # Implement exception handling for IOerrors
        try:
            # If statement for passing mode the function
            if mode == '1' or mode == '2' or mode == '3' or \
                    mode == '4' or mode == '5' or mode == '6' or mode == '7':
                x = 2
                # Call function
                notes_make(mode)
        # IO error try again
        except IOError:
            x = 1

def notes_make(modes):
    # Instantiate PyAudio
    p = pyaudio.PyAudio()

    # Define each note by its frequency in hertz
    C = 261.63
    Db = 277.18
    D = 293.66
    Eb = 311.13
    E = 329.63
    F = 349.23
    Gb = 369.99
    G = 392.00
    Ab = 415.30
    A = 440.00
    Bb = 466.16
    B = 493.88

    # Create sets containing notes in the 7 modes
    dorian = (C, D, Eb, F, G, A, Bb)
    ionian = (C, D,	E, F, G, A, B, C)
    phrygian = (C, Db, Eb, F, G, Ab, Bb, C)
    lydian = (C, D, E, Gb, G, A, B, C)
    mixolydian = (C, D, E, F, G, A, Bb, C)
    aeolian = (C, D, Eb, F, G, Ab, Bb, C)
    locrian = (C, Db, Eb,  F, Gb, Ab, Bb, C)

    # Set volume
    volume = 0.5
    # Set sampling frequency
    fs = 48000
    # Set duration of each note. 1 = 0.25 seconds
    duration = 0.35

    # Variable that allows the notes to be played, use paFloat32 as sample format
    play = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    # Long if/elif for which mode to freestyle in
    if modes == '1':
        # Iterate 64 times, very musical and intuitive
        for i in range(64):
            # Here is the protocol for making the samples
            # np.sin generates the sine waves for the values of C dorian notes using numpy
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(dorian) / fs)).astype(np.float32)
            # Play the note
            play.write(volume*rand_notes)
    # Repeat for the other modes
    elif modes == '2':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(ionian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)
    elif modes == '3':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(phrygian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)
    elif modes == '4':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(lydian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)
    elif modes == '5':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(mixolydian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)
    elif modes == '6':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(aeolian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)
    elif modes == '7':
        for i in range(64):
            rand_notes = (np.sin(2 * np.pi * np.arange(fs * duration) *
                                 random.choice(locrian) / fs)).astype(np.float32)
            play.write(volume*rand_notes)

    # Stop the stream and close
    play.stop_stream()
    play.close()

    # Terminate pyaudio
    p.terminate()

main()