from bs4 import BeautifulSoup
from tkinter import *
import requests
import webbrowser


class EventBrite:

    def __init__(self, master):
        self.cityName = ''

        self.master = master
        master.title("Eventbrite Scraper")
        master.geometry("500x580")

        # self.mainTitle = Label(master, text="Eventbrite Scraper")
        # self.mainTitle.pack()
        self.nameLabel = Label(master, text='Enter your City: ')
        self.nameLabel.pack(side="top")

        self.cityName = Entry(master, width=10)
        self.cityName.insert(END, 'Miami')
        self.cityLabel = Label(root, text = 'City:')
        self.cityLabel.pack(side = 'left')
        self.cityName.pack(side="left")

        self.stateName = Entry(master, width=10)
        self.stateName.insert(END, 'FL')
        self.stateLabel = Label(root, text = 'State:')
        self.stateLabel.pack(side = 'left')

        self.stateName.pack(side="left")

        self.cityName.focus()
        self.searchButton = Button(root, text="Search", command=lambda:EventBrite.searchCity(self))
        self.searchButton.pack()
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()



    def open_article(self, event):
        webbrowser.open(apiSite)


    def searchCity(self):
        self.city = self.cityName.get()
        self.state = self.stateName.get()
        self.apiSite = f"https://www.eventbrite.com/d/{self.state}--{self.city}/ALL -events/"
        webbrowser.open(self.apiSite)


def eventsresults(event):
    global url
    global pageNumber
    global getPage
    global source
    global soup

    for art in soup.find('ul', {"class": "search-main-content__events-list"}):

        time = art.find('div',{"class":"eds-media-card-content__sub-content"}).text
        print(time)
        # print(art)
        event_name = art.div.h3.text
        print(event_name)
        link = art.a['href']
        url = site + link
        print(url)
        events = str(time) + " | " + str(event_name)
        eventbox.insert(END, events)
        urlList.append(link)


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


root = Tk()

state = 'fl'
city = 'miami'
pageNumber=0
page_link = f'/?page={pageNumber}'
site = 'https://www.eventbrite.com/'
apiSite = f"https://www.eventbrite.com/d/{state}--{city}/all-events/"

getPage = apiSite
source = requests.get(getPage).text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
article = soup.find('li')
print(article)
news = []
eventbox = Listbox(root, height=30, width=150)
eventbox.pack(side="bottom")
urlList = []

city_description = ''

root.bind("<Return>", eventsresults)

#print(art.prettify())
title = soup.find("h2",class_="trn-article__title")
eventsresults("<RETURN>")

print(apiSite)
my_gui = EventBrite(root)
root.mainloop()
