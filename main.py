from music21 import note, stream

def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


def makenote(n):
    return note.Note(n)

f = readFile('happybirthday.txt')

notes = (f[0].split(" "))
notelist = []


for i in notes:
    notelist.append(makenote(str(i)))

p = stream.Part(stream.Measure(notelist))
p.show('midi')




#p = stream.Part(stream.Measure([result]))
#p.show('text')

