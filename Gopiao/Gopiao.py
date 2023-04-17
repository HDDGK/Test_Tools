# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoPiao.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from query_request import *
from get_station import *
def get_time():
    now=int(time.time())
    timeStruct=time.localtime(now)
    strTime=time.strftime("%Y-%m-%d",timeStruct)
    return strTime


def is_valid_data(str):
    try:
        time.strptime(str,"%Y-%m-%d")
        return True
    except:
        return False


def messageDialog(self,title,message):
    msg_box=QMessageBox(QMessageBox.Warning,title,message)
    msg_box.exec_()
def displayTable(self,train,info,data):
    self.model.clear()
    for row in range(train):
        for column in range(info):
            item=QStandardItem(data[row[column]])
            self.model.setItem(row,column,item)
    self.tableView.setModel(self.model)




class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 400)
        MainWindow.setMaximumSize(710, 400)
        MainWindow.setMinimumSize(710, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(690, 500, 256, 192))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 711, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 61, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_Find = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Find.setGeometry(QtCore.QRect(630, 20, 81, 31))
        self.pushButton_Find.setObjectName("pushButton_Find")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(60, 20, 131, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 20, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 20, 131, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, 120, 721, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.CheckBox_label = QtWidgets.QLabel(self.groupBox_2)
        self.CheckBox_label.setGeometry(QtCore.QRect(0, 20, 81, 41))
        self.CheckBox_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CheckBox_label.setAlignment(QtCore.Qt.AlignCenter)
        self.CheckBox_label.setObjectName("CheckBox_label")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(80, 30, 641, 20))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_T = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_T.setObjectName("checkBox_T")
        self.horizontalLayout_6.addWidget(self.checkBox_T)
        self.checkBox_GC = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_GC.setObjectName("checkBox_GC")
        self.horizontalLayout_6.addWidget(self.checkBox_GC)
        self.checkBox_K = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_K.setObjectName("checkBox_K")
        self.horizontalLayout_6.addWidget(self.checkBox_K)
        self.checkBox_D = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_D.setObjectName("checkBox_D")
        self.horizontalLayout_6.addWidget(self.checkBox_D)
        self.checkBox_Z = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.horizontalLayout_6.addWidget(self.checkBox_Z)

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 180, 711, 251))
        self.tableView.setObjectName("tableView")
        self.module=QStandardItemModel();
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车票查询"))
        self.label.setText(_translate("MainWindow", " 出 发 点 "))
        self.label_2.setText(_translate("MainWindow", " 目 的 地 "))
        self.label_3.setText(_translate("MainWindow", " 选 日 期  "))
        self.pushButton_Find.setText(_translate("MainWindow", "查询"))
        self.CheckBox_label.setText(_translate("MainWindow", "车次类型："))
        self.checkBox_T.setText(_translate("MainWindow", "T-特快"))
        self.checkBox_GC.setText(_translate("MainWindow", "GC-高铁"))
        self.checkBox_K.setText(_translate("MainWindow", "K-快速"))
        self.checkBox_D.setText(_translate("MainWindow", "D-动车"))
        self.checkBox_Z.setText(_translate("MainWindow", "Z-直达"))
        self.textEdit_3.setText(get_time())
        self.pushButton_Find.clicked.connect(self.on_click)
        self.checkBox_GC.stateChanged.connect(self.change_G)
    def on_click(self):
        get_from = self.textEdit.toPlainText()
        get_to = self.textEdit_2.toPlainText()
        get_data = self.textEdit_3.toPlainText
        if isStation() == True:
            self = eval(read())
            if get_from != "" and get_to != "" and get_data != "":
                if get_from in requests_stationName and is_valid_data(get_data):
                    inputYearDay = time.strptime(get_data, "%Y-%m-%d").tm_yday
                    yearToday = time.localtime(time.time()).tm_yday
                    time_Difference = inputYearDay - yearToday
                    if time_Difference >= 0 and time_Difference <= 28:
                        from_station = requests_stationName[get_from]
                        to_station = requests_stationName(get_to)
                        data = query(get_data, from_station, to_station)
                        if len(data) != 0:
                            self.displayTable(len(data), 16, data)
                        else:
                            self.messageDialog('警告', "没有返回网络数据")
                    else:
                        self.messageDialog('警告', "超出时间")
                else:
                    self.messageDialog('警告', "车站或者时间不对")
            else:
                self.messageDialog('警告', "需要填写车站")
        else:
            self.messageDialog('警告', "未下载车站查询文件")

    def change_G(self, state):
        if state == QtCore.Qt.Checked:
            g_vehicle()
            self.displayTable(len(type_data), 16, type_data)
        else:
            r_g_vehicle()
            self.displayTable(len(type_data), 16, type_data)


if __name__ == "__main__":
    import sys
    from get_station import *

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if isStation()==False:
        getStation()
        MainWindow.show()
    else:
        MainWindow.show()
    sys.exit(app.exec_())






URL_Go12306="https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
requests_cookie12306="https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-04-15&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=GCG&purpose_codes=ADULT"
requests_Go12306="https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-04-15&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=GCG&purpose_codes=ADULT"
requests_stationName="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9259"
'''
leftTicketDTO.train_date: 2023-04-15
leftTicketDTO.from_station: SZQ
leftTicketDTO.to_station: GCG
purpose_codes: ADULT
'''




