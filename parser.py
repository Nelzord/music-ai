import requests
from bs4 import BeautifulSoup

#Generates a list of songs dependent on user input
def generator():
    try:
        search = input("Input a word to create a song: ")
        url = 'https://www.lyrics.com/lyrics/' + search
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = (soup.find_all('b'))

        songList = []
        for i in (range (len (results))):
            if i % 2 == 0:
                s = ""
                s += results[i].text
            else:
                s += " by "
                s += results[i].text
                songList.append(s)
                s = ""
        return (songList)
    except:
        print("Please try another word, there are not enough song occurences.")

s = generator()


#Using the list of generated song, musicgen finds the associated sheet music with the corresponding songs
def musicgen(x):
    lister = []
    for i in range(len(x)):
        search = x[i]
        url = 'https://www.musicnotes.com/search/go?w=' + search
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup)
        results = (soup.find_all('td'))
        loc = results[30]
        lister.append(str(loc).splitlines()[1])
    return(lister)


#Takes contents of music generator, returning instruments, keys, and majors
contents = (musicgen(s))
def programgen(contents):
    voiceList = []
    insList = []
    keyList = []
    for i in contents:
        try:
            print(i)
            q = i.index("Voice")
            voice = i[q+8:q+14]
            voiceList.append(voice.strip(""))
            q = i.index("instruments")
            instrument = i[q+11:q+26]
            insList.append(instrument.strip(""))
            q = i.index("key")
            key = i[q+4:q+13]
            keyList.append(key.strip(""))
        except:
            print("an error has occurred")


    return([insList, voiceList, keyList])

result = programgen(contents)

#Printing the associated values with the songs yielded from music gen

def outputVal():
    print()
    print("Below are the associated values with your keyword")
    print("Instruments: " + str(result[0]))
    print("Ranges: " + str(result[1]))
    print("Keys: " + str(result[2]))


outputVal()





