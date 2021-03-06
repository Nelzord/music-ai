from music21 import note, stream

a1 = note.Note('E')
a2 = note.Note('D')
a3 = note.Note('C')
a4 = note.Note('D')
a5 = note.Note('E')
a6 = note.Note('E')
a7 = note.Note('E')
a8 = note.Note('D')
a9 = note.Note('D')
b1 = note.Note('D')
b2 = note.Note('E')
b3 = note.Note('G')
b4 = note.Note('G')
b5 = note.Note('E')
b6 = note.Note('D')
b7 = note.Note('C')
b8 = note.Note('D')
b9 = note.Note('E')
c1 = note.Note('E')
c2 = note.Note('E')
c3 = note.Note('E')
c4 = note.Note('D')
c5 = note.Note('D')
c6 = note.Note('E')
c7 = note.Note('D')
c8 = note.Note('C')

p = stream.Part(stream.Measure([a1, a2, a3, a4, a5, a6, a7, a8, a9, b1, b2, b3, b4, b5, b6, b7 , b8,
                                b9, c1, c2, c3, c4, c5, c6, c7, c8]))
p.show('midi')
p.show('text')