# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import socket, ssl, os, re, sys
import subprocess

from pprint import pprint
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import *
except:
    print("doesn't look like pyqt5 is installed.  installing now!  Please re-open DlpSleuth once it finishes installing.")
    os.system("pip3 install pyqt5")
from pathlib import Path
createfile=open("found_data.txt","w")
createfile.close()
selected="nope"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        #Form.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/deelight-Magnifying-Glass-transparent-square-300px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(123, 231, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 290, 161, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-color: rgb(10, 22, 255);")
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(490, 340, 121, 17))
        self.checkBox.setStyleSheet("background-color: rgb(6, 255, 68);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(600, 390, 361, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 651, 351))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 0, 201, 51))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 320, 61, 41))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("image: url(:/newPrefix/Folders-PNG-Image-41391.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 410, 511, 361))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 390, 261, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(490, 290, 121, 16))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(530, 410, 511, 361))
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(490, 310, 150, 20))
        self.checkBox_2.setStatusTip("")
        self.checkBox_2.setStyleSheet("background-color: rgb(6, 255, 68);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(360, 230, 71, 16))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(280, 250, 51, 20))
        self.checkBox_3.setStyleSheet("background-color: rgb(6, 255, 68);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(360, 250, 51, 20))
        self.checkBox_4.setStyleSheet("background-color: rgb(6, 255, 68);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(440, 250, 91, 20))
        self.checkBox_5.setStyleSheet("background-color: rgb(6, 255, 68);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_4.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.listWidget_2.raise_()
        self.checkBox_2.raise_()
        self.label_8.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
		
        """
        my_file = Path("config\\hSvrConfig.ini")
        if my_file.is_file():
            print("server config exists")
            svr_info="config\\hSvrConfig.ini"
            theconf = open(svr_info,'r')
            svrconfig=theconf.read()
            self.textEdit_2.setText(svrconfig)
            self.textEdit_2.setReadOnly(True)
            theconf.close()
            print (svrconfig)
        else:
            print("server config does NOT exist.  creating now")
            text, okPressed = QInputDialog.getText(Form, "Get text","Please enter the DLPSleuth Server IP:", QLineEdit.Normal, "")
            filename='config\\hSvrConfig.ini'
            f = open(filename,'w')
            f.write(text)
            f.close()
            svr_info="config\\hSvrConfig.ini"
            theconf = open(svr_info,'r')
            svrconfig=theconf.read()
            self.textEdit_2.setText(svrconfig)
            self.textEdit_2.setReadOnly(True)
            theconf.close()
            #print(text)
        """

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DLPSleuth"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Click on the folder to begin</span></p></body></html>"))
        self.checkBox.setToolTip(_translate("Form", "pulls from outlook inbox"))
        self.checkBox.setText(_translate("Form", "Scan Email Inbox"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">File Search Results (click to open in explorer):</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/man-308611_640.png\"/></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/dlpsleuth.png\"/></p></body></html>"))
        #self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">DLPSleuth Server IP:</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Email and Browser Results:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Optional Components</span></p></body></html>"))
        self.checkBox_2.setToolTip(_translate("Form", "chrome browser only for now"))
        self.checkBox_2.setText(_translate("Form", "Scan Browser Data"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Data Type:</span></p></body></html>"))
        self.checkBox_3.setText(_translate("Form", "SSN"))
        self.checkBox_4.setText(_translate("Form", "CCN"))
        self.checkBox_5.setText(_translate("Form", "PASSWORDS"))
        
        self.pushButton.clicked.connect(self.addInputTextToListbox)
        self.checkBox.clicked.connect(self.checkbox)
        
        
        #!IMPORTANT! don't remove these when updating the .ui file
        ui.listWidget.itemClicked.connect(self.emailexplorer)
        ui.listWidget_2.itemClicked.connect(self.fileexplorer)
		
        #for i in range(self.listWidget_2.count()):
        #    if self.listWidget_2.item(i): #check if item still exists
        #        if "" in self.listWidget_2.item(i).text():
        #            self.listWidget_2.takeItem(i)
		
        
		
    def emailexplorer(self, item):
        print (str(item.text()))
    def fileexplorer(self, item):
        try:
            
            print (str(item.text()))
            ourpath=str(item.text())
            ourpath_corrected=ourpath.split(" - content")
            ourpath_corrected=ourpath_corrected[0]
            ourpath_corrected=ourpath_corrected.replace("/","\\")
            print ("ourpath corrected: "+ourpath_corrected)
            if not "\\" in ourpath_corrected:
                print ("I think you are trying to open data instead of the file that owns the data.  try again") 
                
                return
            #ourpath_corrected='"' + ourpath_corrected + '"'
            #print (ourpath_corrected)
            #os.system(ourpath_corrected)
			
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Please choose an option below:")
            msgBox.setText('What would you like to do with this document?')
            msgBox.addButton(QPushButton('Open document'), QMessageBox.YesRole)
            msgBox.addButton(QPushButton('Open document location'), QMessageBox.NoRole)
            msgBox.addButton(QPushButton('Delete document'), QMessageBox.RejectRole)
            selection = msgBox.exec_()
			
            separator=ourpath_corrected.split('\\')
            file_location=[]
            for x in separator[:-1]:
                file_location.append(x)
            filedirectory='\\'.join(file_location)
            #filedirectory = filedirectory.lstrip('"')
            filedirectory=filedirectory+'"'
            #print ("path = ",filedirectory)
			
            if selection==0:
                print("opening document: "+ourpath_corrected)
                subprocess.call(ourpath_corrected, shell=True)
            if selection==1:
                print ("openining document location now")
                subprocess.Popen('explorer '+filedirectory)
				
            if selection==2:
                #print ("delete it")
                subprocess.call("del /F /Q "+'"'+ourpath_corrected+'"', shell=True)
                #for item in self.listWidget_2.selectedItems():
                #    self.listWidget_2.takeItem(self.listWidget_2.row(item)) 
                #print (separator[-1])
                separator=separator[-1]
                separator=separator.split(" - content")
                separator=separator[0]
                print ("separator: "+separator)
                #itemsTextList =  [str(self.listWidget_2.item(i).text()) for i in range(self.listWidget_2.count())]
                listItems = self.listWidget_2.selectedItems()
                if not listItems: return        
                for item in listItems:
                    self.listWidget_2.takeItem(self.listWidget_2.row(item))
	   
                #tracker=[]
                #counter=0
                #addtocounter=False
                #print("counter= "+str(counter))
                #print(itemsTextList)
                
                #for j in itemsTextList:
                #    print (j)     
                #    if separator in j:
                #        itemsTextList.remove(j)
                #        self.listWidget_2.takeItem(counter)
                #print (itemsTextList)
                #rowcounter=1
                #for remover in itemsTextList:
                    #if "f.txt" in remover:
                        #print (self.listWidget_2.item(rowcounter).text())
                        #self.listWidget_2.takeItem(rowcounter)
                        #print (rowcounter)
                    #rowcounter=rowcounter+1
                print("document: "+ourpath_corrected+" has been deleted successfully!")
				
          
                
			
            
        except Exception as e:
            #print ("hmmm...there seems to be an error.  possibly an encoding issue with this document")
            print (e)
            			
    def checkbox(self):
        if self.checkBox.isChecked():
            #print("email selected\n")
            selected="selected"
            return selected
        else:
            #print("email NOT selected\n")
            selected="nope"	
    def browserpasswords(self):
        if self.checkBox_2.isChecked():
            return True
        else:
            donothing="true"
    def CCN_checked(self):
        if self.checkBox_4.isChecked():
            return True
        else:
            donothing="true"
    def SSN_checked(self):
        if self.checkBox_3.isChecked():
            return True
        else:
            donothing="true"
    def Passwords_checked(self):
        if self.checkBox_5.isChecked():
            return True
        else:
            donothing="true"
    def addInputTextToListbox(self):
        selected=self.checkbox()
        #allow user to select the root directory
        chosendirectory = QFileDialog.getExistingDirectory(
        Form,
        "Select a scan directory (subfolders will be included in the scan)",
        "/",
        QFileDialog.ShowDirsOnly
        )
        if not chosendirectory:
            print ("didn't select a directory...defaulting to %USERPROFILE% ")
            chosendirectory="%USERPROFILE%"
        print(chosendirectory)
        print("Initiating a scan!")
        self.scanmachine('"'+chosendirectory+'"', selected)
        results=open("mytext.txt","r", encoding = "ISO-8859-1")
        for eachline in results.readlines():
            self.listWidget_2.addItem(eachline.rstrip())
        
        

    def scanmachine(self, chosendirectory, selected):
        
        if selected == "selected":
            #calendar for inbox scans
            print ("Opening a new popup window...")
            d = QDialog()
            #d.setGeometry(150,150,150,150)
            cal = QtWidgets.QCalendarWidget(d)
            cal.setGridVisible(True)
            cal.setGeometry(0,0,350,290)
            #cal.move(150, 0)
            date = cal.selectedDate()
            cal.clicked[QtCore.QDate].connect(self.scanEmail)

            d.setWindowTitle("Choose a day then click the 'X'")
            #d.setWindowModality(Qt.ApplicationModal)
            d.exec_()
            
            #cal = QtWidgets.QCalendarWidget(Form)
            #cal.setGeometry(50,50,150,150)
            #cal.clicked[QtCore.QDate].connect(self.showDate)
        
            #self.lbl.setText(date.toString())
        if self.browserpasswords():
            os.system("chrome_decrypt.py")
            fi = open("browser_data.txt",'r')
            filesize=os.path.getsize("browser_data.txt")
            print ("filesize: ", filesize)

            if int(filesize) > 0:
                for eachline in fi.readlines():
                    self.listWidget.addItem(eachline)
            else:
                print ("no browser data discovered")
                self.listWidget.addItem("no browser data discovered")
            fi.close()
        if self.CCN_checked():
            ccnchecked="checked"
        else: 
            ccnchecked="!ccn"
			
        if self.Passwords_checked():
            passwordschecked="checked"
        else: 
            passwordschecked="!pass"
			
        if self.SSN_checked():
            ssnchecked="checked"
        else: 
            ssnchecked="!ssn"
        
        os.system("sleuthclient.py %s %s %s %s" % (chosendirectory, ccnchecked, ssnchecked, passwordschecked))
        #subprocess.Popen("py sleuthclient.py " + chosendirectory).wait()
        
	
    def scanEmail(self, date):
        ourdate=date.toString()
        emailheader=""
        os.system("py outlook_grabber.py %s" % ourdate)
        clear2=open("found_data.txt","w")
        clear2.close()
        #Popen("python outlook_grabber.py " + ourdate, shell=True).wait()
        filename='email_data.txt'
        founddata='found_data.txt'
        f = open(filename,'r')
        g = open(founddata,'a+')
        #firstline=f.readline()
        for eachline in f.readlines():
            
            if "Date:" in eachline:	
                emailheader=eachline        
            
			
            if self.SSN_checked():
                #SSN LOOKUP
                found1=re.search(r'\d\d\d-\d\d-\d\d\d\d', eachline) 
                found1=re.search(r'\d\d\d\d\d\d\d\d\d', eachline) 
            else:
                found1=False			
            if self.CCN_checked():
                #CCN LOOKUP
                #info on regex here: http://regexlib.com/Search.aspx?k=credit&c=-1&m=-1&ps=20
                found2=re.search(r'^3(?:[47]\d([ -]?)\d{4}(?:\1\d{4}){2}|0[0-5]\d{11}|[68]\d{12})$|^4(?:\d\d\d)?([ -]?)\d{4}(?:\2\d{4}){2}$|^6011([ -]?)\d{4}(?:\3\d{4}){2}$|^5[1-5]\d\d([ -]?)\d{4}(?:\4\d{4}){2}$|^2014\d{11}$|^2149\d{11}$|^2131\d{11}$|^1800\d{11}$|^3\d{15}$', eachline) 
            else:
                found2=False				
            if self.Passwords_checked():
                #PASSWORD LOOKUP
                #info on regex here: http://regexlib.com/Search.aspx?k=password&c=-1&m=-1&ps=20
                found3=re.search(r'(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,15})$', eachline) 
                
            else:
                found3=False
			
            #if found1 or found2 or found3:
                #g.write(firstline)
                #self.listWidget.addItem(firstline)
            if found1:
                self.listWidget.addItem(emailheader)
                self.listWidget.addItem("Potential SSN: " + eachline)
                g.write(eachline+"\n")
            if found2:
                self.listWidget.addItem(emailheader)
                self.listWidget.addItem("Potential CCN: " + eachline)
                g.write(eachline+"\n")
            if found3:
                self.listWidget.addItem(emailheader)
                self.listWidget.addItem("Potential Password: "+eachline)
                g.write(eachline+"\n")
        f.close()
        g.close()
        filesize=os.path.getsize("found_data.txt")
        print ("filesize: ", filesize)

        if filesize <= 0:
            print ("no sensitive data discovered in email(s) searched!")
            self.listWidget.addItem("no sensitive data discovered in email(s) searched!")
            #filename='found_data.txt'
            #f = open(filename,'w')
            #f.write("no sensitive data discovered!")
            #f.close()
            
		
		
		
		

		
import main_rc

def redoClicked():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Info")
    msg_box.setText('Thanks for trying out DLPSleuth!  I have much to add to this project as time permits, so consider this laying the foundation for things to come.\nIt is my aim to make this DLP client as simple and out-of-the-box ready as possible\nThe following file extensions are searched by default: txt,csv,pdf,xlsx,docx,doc,msg,ppt,xml,pptx \
	\nIf you have questions or suggestions please feel free to shoot me an email at: musicmancorley@gmail.com or create an issue request on GitHub \
	\nDonations are of course always welcome @ paypal.me/BriarIDS :) \
	')
    msg_box.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    vbox = QVBoxLayout()
    
    menu_bar = QMenuBar()
    file_menu = menu_bar.addMenu('File')
    edit_menu = menu_bar.addMenu('Help')
    exit_action = QAction('Exit', Form)
    exit_action.triggered.connect(exit)
    file_menu.addAction(exit_action)
    redo_action = QAction('Info', Form)
    redo_action.triggered.connect(redoClicked)
    edit_menu.addAction(redo_action)
	
    Form.setLayout(vbox)
    vbox.addWidget(menu_bar)
	
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

