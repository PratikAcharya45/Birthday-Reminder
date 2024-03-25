from strmonth import find_str_month
import os
os.system("cls")
try:
    f_name,l_name=list(map(str,input("Enter the space separated full name of the person : ").split(" ")))
    month,day=list(map(str,input("Enter space separated numeric month and day : ").split(" ")))
except:
    print("Entered data was not as the provided prompt.")

#Validating Name
f_name,l_name=f_name.title(),l_name.title()

# Validating Month
if(int(month)<10):
    if (month[0]!="0"):
        month="0"+month
month=find_str_month(month)

#Validating Day
if(int(day)<10):
    if (day[0]!="0"):
        day="0"+day

#Appending in file    
with open("dates.txt","a") as f:
    f.write(f"\n{f_name}_{l_name} = {month} {day}")

os.system("cls")
print("Done")
