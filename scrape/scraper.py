from Eventbrite import eventbrite
from tkinter import *
import webbrowser

root = Tk()

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
        webbrowser.open(self.apiSite)


    def searchCity(self):
        self.city = self.cityName.get()
        self.state = self.stateName.get()
        self.apiSite = f"https://www.eventbrite.com/d/{self.state}--{self.city}/ALL -events/"
        webbrowser.open(self.apiSite)



def onDouble(event):
    widget = event.widget
    selection = widget.curselection()
    index = widget.nearest(event.y)
    i = index
    webbrowser.open(urlList[i])


    eventbox = Listbox(root, height=30, width=150)
    eventbox.pack(side="bottom")
    try:
        eventbox.bind("<Double-Button-1>", onDouble)
    except:
        pass




    root.bind("<Return>", eventsresults)
    events = str(time) + " | " + str(event_name)

    eventbox.insert(END, events)

    eventsresults("<RETURN>")

    my_gui = EventBrite(root)
    root.mainloop()
    print(events)
