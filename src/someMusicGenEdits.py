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
    if sentiment >= 50:#setPitchesToPitches/CMajor
        # Middle C Template: Note(value=0, octave=5, dur=0.25, volume=127)
        C = Note(0,5, duration)
        D = Note(2,5, duration)
        E = Note(4,5, duration)
        F = Note(5,5, duration)
        G = Note(7,5, duration)
        A = Note(9,5, duration)
        B = Note(11,5, duration)
        return NoteSeq([A, B, C, D, E, F, G])
    else:#setPitchesToA_minor
        A = Note(9,4, duration)
        B = Note(11,4,duration)
        C = Note(0,5,duration)
        D = Note(2,5,duration)
        E = Note(4,5,duration)
        F = Note(5,5,duration)
        Gs = Note(8,5,duration)
        return NoteSeq([A, B, C, D, E, F, Gs])
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
