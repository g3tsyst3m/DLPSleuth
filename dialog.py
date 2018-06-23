import sys
from PyQt5.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Set window size.
w.resize(320, 240)

# Set window title
w.setWindowTitle("DLPSleuth")

# Get filename using QFileDialog
chosendirectory = QFileDialog.getExistingDirectory(
    w,
    "Select a scan directory (subfolders will be included in the scan)",
    "/",
    QFileDialog.ShowDirsOnly
    )

print (chosendirectory)

# print file contents
#with open(filename, 'r') as f:
#    print(f.read())

# Show window

#myListWidget = QListWidget()
#for word in ['cat', 'dog', 'bird']:
#    list_item = QListWidgetItem(word, myListWidget)

#def print_info():
#    print myListWidget.currentItem().text()


#myListWidget.currentItemChanged.connect(print_info)
#myListWidget.show()
w.show()

sys.exit(a.exec_())
