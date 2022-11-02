from music21 import note, stream

with open("contents.txt") as file:
    operationValues = [float(line.rstrip()) for line in file]

with open("song.txt") as file:
    songNote = [line.rstrip() for line in file]

def assignType(s: float) -> str:
    if s > 120:
        return 'eighth'
    elif s > 70:
        return 'half'
    elif s > 50:
        return 'whole'

def assignOctave(s: float) -> int:
    if s > 18:
        return 3
    elif s > 8:
        return 2
    else:
        return 1

def assignDots(s : float) -> int:
    return s//10


def assignPitch(s : float) -> int:
    return int(s * 10)


p = stream.Measure()

for i in songNote:
    if (i != ''):
        p.append(note.Note(step=i, type=assignType(operationValues[4]), octave=assignType(operationValues[0]),
                           pitch=assignPitch(operationValues[2]), dots=assignDots(operationValues[1])))

p.show('midi')
p.show('text')
