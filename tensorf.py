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
    songList = []
    voiceList = []
    insList = []
    keyList = []
    for i in contents:
        try:
            q = re.findall('"([^"]*)"', i)[5]
            songList.append(q)
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
            print("HTML failed to parse.")


    return([insList, voiceList, keyList, songList])

result = programgen(contents)

#Printing the associated values with the songs yielded from music gen

def outputVal():
    print()
    print("Below are the associated values with your keyword")
    print("Song Names: " + str(result[3]))
    print("Instruments: " + str(result[0]))
    print("Ranges: " + str(result[1]))
    print("Keys: " + str(result[2]))


outputVal()


def getSongStats(songName: str):
    songVar = sp.search(q=songName, type="track", limit=3)['tracks']['items'][0]['id']
    songStat = sp.audio_analysis(songVar)
    songDic = {}
    timAvg = sum(songStat['segments'][0]['timbre']) / len(songStat['segments'][0]['timbre'])
    pitchAvg = sum(songStat['segments'][0]['pitches']) / len(songStat['segments'][0]['pitches'])
    songDic['timbre'] = timAvg
    songDic['pitch'] = pitchAvg
    songDic['duration'] = songStat['track']['duration']
    songDic['loudness'] = songStat['track']['loudness']
    songDic['tempo'] = songStat['track']['tempo']
    return songDic

songSum = []
finalSong = []
for i in result[3]:
    try:
        songSum.append(getSongStats(i))
    except:
        print("Unable to get song stats.")
print(songSum)

timbre, loudness, pitch, duration, tempo = 0,0,0,0,0

for i in songSum:
    timbre += i['timbre']
    loudness += i['pitch']
    pitch += i['pitch']
    duration += i['duration']
    tempo += i['tempo']

timbre = timbre/len(songSum)
loudness = loudness/len(songSum)
pitch = pitch/len(songSum)
duration = duration/len(songSum)
tempo = tempo/len(songSum)

print('total timbre for the song is: ' + str(timbre))
print('total loudness for the song is: ' + str(loudness))
print('total pitch for the song is: ' + str(pitch))
print('total duration for the song is: ' + str(duration))
print('total tempo for the song is: ' + str(tempo))



