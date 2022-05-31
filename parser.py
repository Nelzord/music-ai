import requests
from bs4 import BeautifulSoup

#Generates a list of songs dependent on user input
def generator():
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

s = generator()



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

contents = (musicgen(s))
for i in contents:
    print(i)
