# client.py
import socket, ssl, os, re, sys, io
from pprint import pprint


#clear textfile
clear=open("mytext.txt","w")
clear.close()
chosendirectory=""
ccnchecked=sys.argv[2]
ssnchecked=sys.argv[3]
passwordschecked=sys.argv[4]
print(ssnchecked)
localdatafound=False
emaildatafound=False
browserdatafound=False

chosendirectory=str(sys.argv[1])
print (chosendirectory)

"""
##############
#beta stuff...
##############
try:
    svr_info="config\\hSvrConfig.ini"
    theconf = open(svr_info,'r')
    svrconfig=theconf.read()
    #print (svrconfig)
    #print (str(sys.argv))
    
    
except:
    print("server config doesn't exist or another unknown error occurred")
    sys.exit(0)

"""


f=open("mytext.txt", "a+")

mylist=[]
ext = (".txt", ".csv", ".pdf", ".xlsx", ".docx", ".doc", \
                        ".msg", ".ppt", ".xml", ".pptx")



print("Searching...please be patient")
for root, dirs, files in os.walk(chosendirectory, topdown=True):
   
    for name in files:
      
        if name.endswith(tuple(ext)):
            try:
                with open(os.path.join(root, name), "r") as auto:
                #auto=unidecode(str(auto))
                    print (auto) 
                    
                    for readthelines in auto:
						
                        if ssnchecked=="checked":
                            #SSN LOOKUP
                            ssnsearch=re.search(r'\d\d\d-\d\d-\d\d\d\d', readthelines) 
                            ssnsearch=re.search(r'\d\d\d\d\d\d\d\d\d', readthelines) 
                        else:
                            ssnsearch=False
						
                        if ccnchecked=="checked":
                            #CCN LOOKUP
                            #info on regex here: http://regexlib.com/Search.aspx?k=credit&c=-1&m=-1&ps=20
                            ccnsearch=re.search(r'^3(?:[47]\d([ -]?)\d{4}(?:\1\d{4}){2}|0[0-5]\d{11}|[68]\d{12})$|^4(?:\d\d\d)?([ -]?)\d{4}(?:\2\d{4}){2}$|^6011([ -]?)\d{4}(?:\3\d{4}){2}$|^5[1-5]\d\d([ -]?)\d{4}(?:\4\d{4}){2}$|^2014\d{11}$|^2149\d{11}$|^2131\d{11}$|^1800\d{11}$|^3\d{15}$', readthelines) 
                        else:
                            ccnsearch=False
							
                        if passwordschecked=="checked":
                            #PASSWORD LOOKUP
                            #info on regex here: http://regexlib.com/Search.aspx?k=password&c=-1&m=-1&ps=20
                            passwordssearch=re.search(r'(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,15})$', readthelines) 
                        else:
                            passwordssearch=False
							
                        if ccnsearch and ccnchecked=="checked" or ssnsearch and ssnchecked=="checked" or passwordssearch and passwordschecked=="checked":
                            fullpath=os.path.join(root, name)+" - " +"content of document: "+readthelines
                            mylist.append(fullpath.rstrip())
                            #mylist.append("document content: "+readthelines.rstrip()) #actual content of document
                            print(readthelines)
                            
            
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))		
            #except:
                #print ("hmm...an error occurred.  could either be a permissions related error or character encoding related error")		

for all in mylist:

    #print (all)
    f.write(all+"\n")
f.close()

print ("search complete!")

#server/client interaction
#----------------------------------------------------------------------------------------
#this is in extreme beta so this will remain commented out until further development changes are made
#
#
#
"""
filesize=os.path.getsize("mytext.txt")
print ("filesize: ", filesize)

if int(filesize) > 0:
    localdatafound=True
    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.readlines()


filesize2=os.path.getsize("browser_data.txt")
print ("filesize: ", filesize2)

if int(filesize2) > 0:
    browserdatafound=True
    g = open("browser_data.txt",'rb')
    browserdata = g.readlines()
	
filesize3=os.path.getsize("found_data.txt")
print ("filesize: ", filesize3)

if int(filesize3) > 0:
    emaildatafound=True
    h = open("found_data.txt",'rb')
    emaildata = h.readlines()

SVR_HOST = svrconfig

SVR_PORT = 8000

CA_CERT_PATH = 'certs\\sleuth.crt'

if __name__ == '__main__':

    sock = socket.socket()

    ssl_conn = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1, ca_certs=CA_CERT_PATH)

    svr_host = SVR_HOST

    svr_port = SVR_PORT
    try:
        ssl_conn.connect((svr_host, int(svr_port)))
    except:
        print("couldn't connect to server.  Is it running?")
		
        sys.exit(0)

    # get remote cert

    cert = ssl_conn.getpeercert()

    print("Checking server certificate")

    pprint(cert)

    if not cert or ssl.match_hostname(cert, svr_host):

        raise Exception("Invalid SSL cert for host %s. Check if this is a man-in-the-middle attack!" %svr_host )

    print("Server certificate OK.")

    #ssl_conn.write('GET / \n'.encode('utf-8'))
	
    if localdatafound:
        for lines in l:
            print (lines)
            ssl_conn.write(lines)
        f.close()

    if browserdatafound:
        for lines in browserdata:
            print (lines)
            ssl_conn.write(lines)
        g.close()
	
    if emaildatafound:
        for lines in emaildata:
            print (lines)
            ssl_conn.write(lines)
        h.close()
	
    print("Response received from server:")

    print(ssl_conn.read())

ssl_conn.close()
sock.close()

"""














