# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designs\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 645)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.importBtn = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importBtn.sizePolicy().hasHeightForWidth())
        self.importBtn.setSizePolicy(sizePolicy)
        self.importBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.importBtn.setObjectName("importBtn")
        self.horizontalLayout_5.addWidget(self.importBtn)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.TopTW = QtWidgets.QTableWidget(self.frame)
        self.TopTW.setMaximumSize(QtCore.QSize(16777215, 300))
        self.TopTW.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TopTW.setObjectName("TopTW")
        self.TopTW.setColumnCount(3)
        self.TopTW.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TopTW.setItem(1, 2, item)
        self.verticalLayout_2.addWidget(self.TopTW)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EmailTW = QtWidgets.QTableWidget(self.frame_2)
        self.EmailTW.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.EmailTW.setObjectName("EmailTW")
        self.EmailTW.setColumnCount(2)
        self.EmailTW.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.EmailTW.setItem(1, 1, item)
        self.horizontalLayout.addWidget(self.EmailTW)
        self.NumberTW = QtWidgets.QTableWidget(self.frame_2)
        self.NumberTW.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.NumberTW.setObjectName("NumberTW")
        self.NumberTW.setColumnCount(2)
        self.NumberTW.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.NumberTW.setItem(1, 1, item)
        self.horizontalLayout.addWidget(self.NumberTW)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hostNameLbl = QtWidgets.QLabel(self.frame_4)
        self.hostNameLbl.setObjectName("hostNameLbl")
        self.horizontalLayout_3.addWidget(self.hostNameLbl, 0, QtCore.Qt.AlignLeft)
        self.developedMsgLbl = QtWidgets.QLabel(self.frame_4)
        self.developedMsgLbl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.developedMsgLbl.setOpenExternalLinks(False)
        self.developedMsgLbl.setObjectName("developedMsgLbl")
        self.horizontalLayout_3.addWidget(self.developedMsgLbl, 0, QtCore.Qt.AlignHCenter)
        self.IPLbl = QtWidgets.QLabel(self.frame_4)
        self.IPLbl.setObjectName("IPLbl")
        self.horizontalLayout_3.addWidget(self.IPLbl, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapper and Network Analyser"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Web Scrapper and Network Analyser</span></p></body></html>"))
        self.importBtn.setText(_translate("MainWindow", "  Import CSV containing list of URLs  "))
        item = self.TopTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL"))
        item = self.TopTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.TopTW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP"))
        __sortingEnabled = self.TopTW.isSortingEnabled()
        self.TopTW.setSortingEnabled(False)
        item = self.TopTW.item(0, 0)
        item.setText(_translate("MainWindow", "https://www.hybrique.com"))
        item = self.TopTW.item(0, 1)
        item.setText(_translate("MainWindow", "Hybrique | What is Hybrique"))
        item = self.TopTW.item(0, 2)
        item.setText(_translate("MainWindow", "186.56.45.92"))
        item = self.TopTW.item(1, 0)
        item.setText(_translate("MainWindow", "https://www.google.com"))
        item = self.TopTW.item(1, 1)
        item.setText(_translate("MainWindow", "Hybrique | Team"))
        item = self.TopTW.item(1, 2)
        item.setText(_translate("MainWindow", "181.56.45.12"))
        self.TopTW.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Scraped Emails</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Scraped Numbers</span></p></body></html>"))
        item = self.EmailTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL"))
        item = self.EmailTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        __sortingEnabled = self.EmailTW.isSortingEnabled()
        self.EmailTW.setSortingEnabled(False)
        item = self.EmailTW.item(0, 0)
        item.setText(_translate("MainWindow", "https://www.hybrique.com"))
        item = self.EmailTW.item(0, 1)
        item.setText(_translate("MainWindow", "admin@hybrique.com"))
        item = self.EmailTW.item(1, 0)
        item.setText(_translate("MainWindow", "https://www.hybrique.com"))
        item = self.EmailTW.item(1, 1)
        item.setText(_translate("MainWindow", "hybrique@gmail.com"))
        self.EmailTW.setSortingEnabled(__sortingEnabled)
        item = self.NumberTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "URL"))
        item = self.NumberTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number"))
        __sortingEnabled = self.NumberTW.isSortingEnabled()
        self.NumberTW.setSortingEnabled(False)
        item = self.NumberTW.item(0, 0)
        item.setText(_translate("MainWindow", "https://www.hybrique.com"))
        item = self.NumberTW.item(0, 1)
        item.setText(_translate("MainWindow", "62 266475562"))
        item = self.NumberTW.item(1, 0)
        item.setText(_translate("MainWindow", "https://www.hybrique.com"))
        item = self.NumberTW.item(1, 1)
        item.setText(_translate("MainWindow", "5974123144"))
        self.NumberTW.setSortingEnabled(__sortingEnabled)
        self.hostNameLbl.setText(_translate("MainWindow", "<html><head/><body><p>LAPTOP-8TC5UP6O</p></body></html>"))
        self.developedMsgLbl.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Developed with </span><span style=\" font-family:\'apple color emoji\',\'segoe ui emoji\',\'noto color emoji\',\'android emoji\',\'emojisymbols\',\'emojione mozilla\',\'twemoji mozilla\',\'segoe ui symbol\'; font-size:12pt; color:#000000;\">❤️  </span><span style=\" font-size:12pt;\">by Shreya and Tanusha</span></p></body></html>"))
        self.IPLbl.setText(_translate("MainWindow", "<html><head/><body><p>192.168.43.54</p></body></html>"))
