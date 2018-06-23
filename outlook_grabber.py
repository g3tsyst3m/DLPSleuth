import win32com.client
import os,sys
import datetime

#clear email textfile
clear=open("email_data.txt","w")
clear.close()

month=str(sys.argv[2])
day=str(sys.argv[3])
year=str(sys.argv[4])

if month=="Jan":
    month=1    	
if month=="Feb":
    month=2    	
if month=="Mar":
    month=3    	
if month=="Apr":
    month=4    	
if month=="May":
    month=5    	
if month=="Jun":
    month=6    	
if month=="Jul":
    month=7    	
if month=="Aug":
    month=8    	
if month=="Sep":
    month=9    	
if month=="Oct":
    month=10    	
if month=="Nov":
    month=11   	
if month=="Dec":
    month=12    		

print (month,day,year)
#originaldatestring="[SentOn] > '3/8/2018 8:00 AM' AND [SentOn] < '3/8/2018 11:59 PM'"	
#originaldatestring="[SentOn] > '3/8/2018' AND [SentOn] < '3/9/2018'" 
dayplus1=int(day)+1
datestring="[SentOn] > '" +str(month) + "/" + str(day) + "/" + str(year) + "' AND " + "[SentOn] < '" + str(month) + "/" + str(dayplus1) + "/" + str(year) +"'"
print (datestring)	
#datestring=originaldatestring	

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
#messages = inbox.Items
messages = messages = inbox.Items.restrict(datestring)
count=1
ext="blank"

filename='email_data.txt'
f = open(filename,'a')

#f.write(str(month)+"-"+str(day)+"-"+str(year)+":\n")

for message in messages:
    print ("email #",count)
    thedate=message.LastModificationTime
    subject = message.subject.encode('ascii', 'ignore').decode('ascii')
    body_content = message.body
    #attachments = message.attachments
    body_content=body_content.encode('ascii', 'ignore').decode('ascii')
    print (thedate,subject,body_content)
    f.write("Date:%s Subject:%s Body_Content:\n %s \n" % (thedate, subject, body_content))
    

    count=count+1
f.close()