import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QMainWindow, QTabWidget, QWidget, QListView


def QString(param):
    pass


class tabdemo(QMainWindow):
   def __init__(self):
        super(tabdemo, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1,"Form View")
        self.tabs.addTab(self.tab2,"Matrix View")
        self.tab1UI()
        self.tab2UI()
        self.setWindowTitle("tab demo")

   def tab1UI(self):
        l1 = QListView()
        l2 = QListView()
        model = QStringListModel()        
        model.setStringList(QString("Item 1;Item 2;Item 3;Item 4").split(";"))    
        l1.setModel(model)
        l2.setModel(model)
        hbox = QHBoxLayout()
        hbox.addWidget(l1)
        hbox.addStretch()
        hbox.addWidget(l2) 
        self.tab1.setLayout(hbox)

   def tab2UI(self):
        vbox = QVBoxLayout()
        tbl1 = QTableWidget()
        tbl1.setRowCount(5)
        tbl1.setColumnCount(5)
        vbox.addWidget(tbl1)
        tbl1.setItem(0, 0, QTableWidgetItem("1")) # row, col
        self.tab2.setLayout(vbox)

def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
