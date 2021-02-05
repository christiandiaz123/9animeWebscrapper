#! python3
import requests
from win10toast import ToastNotifier
import bs4
import datetime
def sendNotification(animename):
    try:
        toast = ToastNotifier()
        print("This ran")
        concatinationVar = (', '.join(animename))
        toast.show_toast("New episode(s) of " + concatinationVar +" is/are out", concatinationVar, duration=None, icon_path ="C:\\Users\\Christian\\Desktop\\CSC492PDFs\\WorldAnimesNetwork-favicon.ico")

    except:
        print("This ran too")
try:
    toast = ToastNotifier()
    res = requests.get('https://www12.9anime.ru/home')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    myList = soup.select('.anime-list  a[data-jtitle]')
    with open("myanimelist.txt", "r") as file_object:
        myAnimeList = file_object.read().split('\n')
    with open("alreadynotifiedanimelist.txt", "r") as file_object2:
        alreadyNotifiedList = file_object2.read().split('\n')[0:-1]
    with open("allAnimeList.txt", "r") as file_object4:
        allAnimeSet = set(file_object4.read().split('\n')[0:-1])
    finalAnimeSet = allAnimeSet.union(set([x.getText() for x in myList]))
    finalAnime =[]
    with open("alreadynotifiedanimelist.txt", "a") as file_object3:
        for myAnime in myAnimeList:
            if(myAnime.lower() in [anime.getText().lower() for anime in myList] and myAnime not in alreadyNotifiedList):
                finalAnime.append(myAnime)
                file_object3.write(myAnime+"\n")
    if(finalAnime != []):
        print(finalAnime)
        sendNotification(finalAnime)
    file_object5 = open("allAnimeList.txt", "w")
    for anime in finalAnimeSet:
        try:
            file_object5.write(anime+'\n')
        except:
            pass
except Exception as myExc:
    with open("log.txt", 'a') as log_object:
        log_object.write(str(myExc)+'\n'+ repr(datetime.datetime.today())+'\n\n')

