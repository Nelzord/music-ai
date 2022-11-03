from music21 import note, stream

with open("contents.txt") as file:
    operationValues = [float(line.rstrip()) for line in file]

with open("song.txt") as file:
    songNote = [line.rstrip() for line in file]

def assignType(s: float) -> str:
    if s > 130:
        return 'whole'
    elif s > 110:
        return 'half'
    elif s > 100:
        return 'quarter'
    else:
        return 'eighth'


def assignOctave(s: float) -> int:
    return s//2

def assignDots(s : float) -> int:
    return s


def assignPitch(s : float) -> int:
    return s * 10


p = stream.Measure()

for i in songNote:
    if (i != ''):
        p.append(note.Note(step=i, type=assignType(operationValues[4]), octave=assignOctave(operationValues[0]),
                           pitch=assignPitch(operationValues[2]), dots=assignDots(operationValues[1])))

p.show('midi')
