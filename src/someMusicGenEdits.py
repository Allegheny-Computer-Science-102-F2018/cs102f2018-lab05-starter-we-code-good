#Matt Jones, John Scott, Jon Mendez, Carson Quigley
#Fugue generator
#TODO: Make code that creates correct sized random melody, create code that transposes melody, create code that extends melody

#from IPython.display import Audio
#from midi2audio import FluidSynth
from pyknon.genmidi import Midi
import pyknon.music
from pyknon.music import NoteSeq
from pyknon.music import Note
import random

#Takes semantic analysis input
def generateNoteSet(sentiment, duration):
    if :#setPitchesToPitches/CMajor
        C = Note(0,5, duration)
        D = Note(2,5, duration)
        E =
        F =
        G =
        A =
        B =
        C =
        return NoteSeq([A, B, C, D, E, F, G])
    else#setPitchesToA_minor
        A = Note(9,5, duration)
        B = Note(11,5,duration)
        C = Note(12,5,duraiton)
        D =
        E =
        F =
        G =
        return NoteSeq([A, B, C, D, E, F, G])
    #return this as a parameter in genMidi()
def genLength(length):
    #if length == "short" return 16
    #elif length == "medium" return 8
    #else return  4
def genMusic(sentiment,length):
    duration = getLength(length)
    set = genNoteSet(sentiment, duration)
    #code to generate random sequence of notes given our key and duration goes here, ie.
    #seq = random(key) *Check syntax
    genMidi(sequence)

def genMidi(seq):
    #defaults: 1 track, 60bpm
    midi = Midi(1, tempo = 120)
    #midi.seq_notes(seq, track=0)
    midi.write("midi/test.mid")

    #FluidSynth().play_midi('midi/test.mid')

    #fs = FluidSynth()
    #fs.midi_to_audio('midi/test.mid', 'mp3/test.mp3')

    #Audio("mp3/test.mp3") this plays the mp3
genMusic()
