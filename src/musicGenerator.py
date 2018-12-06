#Matt Jones, John Scott, Jon Mendez, Carson Quigley
#Fugue generator
#TODO: Make code that creates correct sized random melody, create code that transposes melody, create code that extends melody

#from IPython.display import Audio
#from midi2audio import FluidSynth
from pyknon.genmidi import Midi
import pyknon.music
from pyknon.music import NoteSeq
import random
import pygame


#Takes semantic analysis input
#def majorMinor():
    #if :
    #else

#def genRandom():


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

sentiment = input("Was it happy or sad?\n")
key = genKey(sentiment)
length = genLength(sentiment)
notes = randomSeq(length, key, durations)
tempo1 = genTempo(sentiment)
midi = Midi(1, tempo=tempo1)
midi.seq_notes(notes, track=0)
midi.write("midi/a_minor6.mid")

pygame.init()
pygame.mixer.music.load("midi/a_minor6.mid")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)
