#Matt Jones, John Scott, Jon Mendez, Carson Quigley
#Music generator

from pyknon.genmidi import Midi
import pyknon.music
from pyknon.music import NoteSeq
from pyknon.music import Note
import random
import pygame


def genMusic(sentiment):
    key = genKey(sentiment)
    length = genLength(sentiment)
    notes = randomSeq(length, key, durations)
    tempo1 = genTempo(sentiment)
    midi = Midi(1, tempo=tempo1)
    midi.seq_notes(notes, track=0)
    midi.write("midi/audio.mid")

    pygame.init()
    pygame.mixer.music.load("midi/audio.mid")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)

durations = {
    "1"
    "2"
}

C_major = {
    'A',
    #'B',
    'C',
    'D',
    'E',
    #'F',
    'G'
}

A_minor = {
    'A',
    'B',
    #'C',
    'D',
    'E',
    'F',
    'G#'
}
def genKey(sentiment):
    if(sentiment == "happy"):
        return C_major
    else:
        return A_minor

def genTempo(sentiment):
    if(sentiment == "happy"):
        return 120
    else:
        return 30

def genLength(sentiment):
    if(sentiment == "happy"):
        return 90
    else:
        return 44

def randomSeq(n, pitches, durations, rests=True):
    # Add a rest to the set of pitches if desired.
    if rests:
        pitches.add('r')

    this_seq = ''
    for i in range(n):
        pitch = random.sample(pitches, 1)
        duration = random.sample(durations, 1)
        this_seq += pitch[0] + duration[0] + ' '

    return NoteSeq(this_seq)
