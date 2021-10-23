from collections import abc
import requests
from bs4 import BeautifulSoup
#using beautifulsoup to get the content in html format
import plyer
#player is used for notifications
def datacollected():
    def notification(title,message):
        plyer.notification.notify(
        title=title,
        message = message,
        #app_icon='corona.ico',
        timeout=20  #we will keep notification for 20 seconds
        )

    url="https://www.worldometers.info/coronavirus/"
    res= requests.get(url)#req made to url
    #output= response 200,which means all our data has been fetched succesfully
    soup=BeautifulSoup(res.content, 'html.parser')
    ##print (soup.prettify)

    #now we will scrp the data
    #from inspecting element of the page from which we want to scrap the data we conclude that in which 'element' our data is there.
    #here pour element is 'tbody'
    tbody=soup.find('tbody')
    abc=tbody.find_all('tr')

    countrynotification= cntdata.get()
    # we will keep world as by deafault when no country is entered
    if(countrynotification==""):
        countrynotification="world"

    #creating list variables with the column names same as on the website
    serial_number,countries,total_cases,new_cases,total_deaths,new_deaths,total_recovered,active_cases,serious_critical,total_cases_per_mn,deaths_per_mn,total_tests,tests_per_mn,population=[],[],[],[],[],[],[],[],[],[],[],[],[],[]

    #header is used to name the columns in the downlaod file
    header=['serial_number','countries','total_cases','new_cases','total_deaths','new_deaths','total_recovered','active_cases','serious_critical','total_cases_per_mn','deaths_per_mn','total_tests','tests_per_mn','population']
    for i in abc:
        id=i.find_all('td')
        ##print(id[1].text) #id 1 is for country names all the names will be printed
        if(id[1].text.strip().lower()==countrynotification):
            totalcases1=int(id[2].text.strip().replace(',',""))
            totaldeaths=id[4].text.strip()
            newcases=id[3].text.strip()
            newdeaths=id[5].text.strip()
            notification("CORONA RECENT UPDATES OF {} ".format(countrynotification),"Total Cases : {}\nTotal Deaths:{}\nNew Cases : {}\nNew Deaths :{}".format(totalcases1,totaldeaths,newcases,newdeaths))
        #'.text' will give only the data we want nothing else, in this case it will op country names
        
        serial_number.append(id[0].text.strip())
        countries.append(id[1].text.strip())
        total_cases.append(id[2].text.strip().replace(',',""))#beacuse we want to remove commas in number
        new_cases.append(id[3].text.strip())
        total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious_critical.append(id[8].text.strip())
        total_cases_per_mn.append(id[9].text.strip())
        deaths_per_mn.append(id[10].text.strip())
        total_tests.append(id[11].text.strip())
        tests_per_mn.append(id[12].text.strip())
        population.append(id[13].text.strip())

    #we will use here pandas to create our data frame and use zip function so that we can store all our data together

    df= pd.DataFrame(list(zip(serial_number,countries,total_cases,new_cases,total_deaths,new_deaths,total_recovered,active_cases,serious_critical,total_cases_per_mn,deaths_per_mn,total_tests,tests_per_mn,population)),columns=header)

    #now we will use sort function and here wewill sort acc to total cases in the world
    #which country has more cases
    sorts=df.sort_values('total_cases',ascending=False)
    for a in flist:
        if(a=='html'):
            path2='{}/coronadata.html'.format(path)
            sorts.to_html(r'{}'.format(path2))
            #used r to read our mentioned path

        if(a=='json'):
            path2='{}/coronadata.json'.format(path)
            sorts.to_json(r'{}'.format(path2))
        
        if(a=='csv'):
            path2='{}/coronadata.csv'.format(path)
            sorts.to_csv(r'{}'.format(path2))


        #creating mesaage box
        if(len(flist)!=0):
            messagebox.showinfo("notification","Corona record is saved {}".format(path2),parent=coro)

def downloaddata():
    #now if any dialog is not clicked
    global path
    if(len(flist)!=0):
        path=filedialog.askdirectory()
    else:
        pass
    datacollected()
    flist.clear() #after we finsih our downloading it should come back to its normal state from downloading state
    Inhtml.configure(state='normal')
    Injson.configure(state='normal')
    Inexcel.configure(state='normal')


def inhtmldownload():
    flist.append('html')
    Inhtml.configure(state="disabled")


def injsondownload():
    flist.append('json')
    Injson.configure(state="disabled")

def inexceldownload():
    flist.append('csv')
    Inexcel.configure(state="disabled")

   
   


import pandas as  pd
from tkinter import *
from tkinter import messagebox,filedialog
coro=Tk()
coro.title('COVID-19 Information')
#Python Tkinter 'title' refers to the name provided to the window. 
#It appears on the top of the window 
#& mostly found on the top left or center of the screen.

coro.geometry("800x500+200+100")
#geometry method is used to set the dimensions of the Tkinter window 
#and is used to set the position of the main window on the user’s desktop.
#800x500 is the size of the  tkinter window
#this window will shift 200 on x axis and 100 on y axis

coro.configure(bg='#046173')
#configure method is used to donfigure the properties of widget

#coro.iconbitmap('D:\DOWNLOADS\PROGRAMS\covid_notifier&data_collection\corona.ico')#download only ico files
#Iconbitmap is used to set an icon of a window or a frame to bitmap. 
# the bitmap image should be an icon type with .ico as its extension.
flist=[]
path=""



####Labels
#Here is the simple syntax to create this widget −
#w = Label ( master, option, ... )
mainlabel=Label(coro,text="COVID-19 Live Tracker",font=("new roman",30,"italic bold"),bg="#05897A",width=33,
                fg="black", bd=5)
#master − This represents the parent window.
#options − Here is the list of most commonly used options for this widget. 
#These options can be used as key-value pairs separated by commas.

mainlabel.place(x=0,y=0)
#This geometry manager organizes widgets by placing them in a specific position in the parent widget.

label1=Label(coro,text="Country Name",font=("arial",20,"italic bold"),bg="#046173")
label1.place(x=15,y=100)


label2=Label(coro,text="Download file in",font=("arial",20,"italic bold"),bg="#046173")
label2.place(x=15,y=200)

cntdata= StringVar()#creating string variable

#The Entry widget is used to accept single-line(input) text strings from a user.
entry1=Entry(coro,textvariable=cntdata,font=("arial",20,"italic bold"),relief=RIDGE,bd=2,width=32)
entry1.place(x=280,y=100)

#### Buttons
Inhtml=Button(coro, text='Html', bg="#2DAE9A", font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#05945B", activeforeground="white", bd=5,width=5,command=inhtmldownload)
Inhtml.place(x=300,y=200)

Injson=Button(coro, text='json', bg="#2DAE9A", font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#05945B", activeforeground="white", bd=5,width=5,command=injsondownload)
Injson.place(x=300,y=260)

Inexcel=Button(coro, text='Excel', bg="#2DAE9A", font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#05945B", activeforeground="white", bd=5,width=5,command=inexceldownload)
Inexcel.place(x=300,y=320)

Submit=Button(coro, text='Submit', bg="#CB054A", font=("arial",15,"italic bold"),relief=RIDGE,activebackground="#7B0549", activeforeground="white", bd=5,width=25,command=downloaddata )
Submit.place(x=450,y=260)

coro.mainloop()
