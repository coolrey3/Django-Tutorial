from bs4 import BeautifulSoup
from tkinter import *
import requests
import webbrowser

root = Tk()

class EventBrite:

    def __init__(self, master):
        self.cityName = ''

        self.master = master
        master.title("Eventbrite Scraper")
        master.geometry("500x580")

        self.mainTitle = Label(master, text="Eventbrite Scraper")
        self.mainTitle.pack()

        self.cityName = Entry(master, width=50)
        self.cityName.insert(END, 'Miami')
        self.cityName.pack(side="top")
        self.nameLabel = Label(master, text='Enter your City: ')
        self.nameLabel.pack(side="top")
        self.cityName.focus()
        self.searchButton = Button(root, text="Search", command=EventBrite.searchCity(self))
        self.searchButton.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    # def open_article(self, event):
    #     self.webbrowser.open(playerUrl)
    #
    #
    # def open_article(self, event):
    #     self.webbrowser.open(playerUrl)


    # def searchCity(self):
    #     self.city = self.cityName.get()
    #     self.cityUrl = site + self.city
        # self.webbrowser.open(playerUrl)

    # def greet(self):
    #     print("Greetings!")

site ='https://www.eventbrite.com/'
apiSite = ""
pageNumber=0
# getPage = apiSite + str(pageNumber)


# pcPlayer= "/profile/pc/"
source = requests.get(getPage).text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
article = soup.find('article' )
print("Latest Articles")
global news
global eventbox
news = []
eventbox = Listbox(root, height=30, width=150)
eventbox.pack(side ="bottom")
urlList = []

def eventsresults(event):
    global url
    global pageNumber
    global getPage
    global source
    global soup
    global onDouble


    for art in soup.find_all('article'):

        time = art.time.text
        headline = art.h2.text
        link = art.h2.a['href']
        url = site + link
        news =  time + " | " + headline
        eventbox.insert(END, news)
        urlList.append(url)


        def onDouble(event):
            widget = event.widget
            selection = widget.curselection()
            index = widget.nearest(event.y)
            i = index
            webbrowser.open(urlList[i])

    print("refreshed news results")
    pageNumber += 1
    getPage = apiSite + str(pageNumber)
    source = requests.get(getPage).text
    soup = BeautifulSoup(source, 'lxml')

    try:
        eventbox.bind("<Double-Button-1>", onDouble)
    except:
        pass

root.bind("<Return>", eventsresults)

#print(art.prettify())
title = soup.find("h2",class_="trn-article__title")
eventsresults("<RETURN>")

# my_gui = EventBrite(root)
# root.mainloop()
