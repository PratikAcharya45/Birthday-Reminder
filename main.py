import time
import os
from strmonth import find_str_month
from notifypy import Notify

notification=Notify()

def wish(name,date):
    notification.application_name="𝓩𝓸𝓻𝓾𝓼"
    notification.title="Birthday Reminder"
    # notification.message=date
    text=f"Today is {name}'s birthday."
    notification.message=text+"\n"+date
    notification.audio="audio.wav"
    notification.icon="cake.png"
    notification.send()
    return text
date=time.strftime("%Y-%m-%d") #Importing today's date
year,month,day=date.split("-")

month=find_str_month(month) #Changing int month to str month
l=str()
with open("dates.txt","r") as f:
    lines=f.readlines() #Reading the lines of info.txt
    for line in lines:
        name,bdate=line.split("=") #Splitting name and birthdate in the txt file
        bdate=bdate.strip() #removing spaces and new lines in birthdate
        bmonth,bday=bdate.split(" ") #splitting month and day of birthday
        if(bmonth==month and bday==day): 
            l=wish(name,date)
    
os.system("cls")
print(l)
