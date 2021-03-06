# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_design_files\loadingProgress.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayLoadingProgress(object):
    def setupUi(self, DisplayLoadingProgress):
        DisplayLoadingProgress.setObjectName("DisplayLoadingProgress")
        DisplayLoadingProgress.resize(355, 138)
        DisplayLoadingProgress.setStyleSheet("QProgressBar {\n"
"    border-style: solid;\n"
"    border-color: grey;\n"
"    border-radius: 7px;\n"
"    border-width: 2px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 2px;\n"
"    background-color: #de7c09;\n"
"    margin: 3px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(DisplayLoadingProgress)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(DisplayLoadingProgress)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logoFrame = QtWidgets.QFrame(self.frame)
        self.logoFrame.setAutoFillBackground(False)
        self.logoFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logoFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoFrame.setObjectName("logoFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.logoFrame)
        self.verticalLayout_3.setContentsMargins(30, 20, 30, 24)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.logoFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadingText = QtWidgets.QLabel(self.frame_2)
        self.loadingText.setObjectName("loadingText")
        self.verticalLayout.addWidget(self.loadingText, 0, QtCore.Qt.AlignHCenter)
        self.loadingProgressText = QtWidgets.QLabel(self.frame_2)
        self.loadingProgressText.setObjectName("loadingProgressText")
        self.verticalLayout.addWidget(self.loadingProgressText, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.loadingProgressBar = QtWidgets.QProgressBar(self.logoFrame)
        self.loadingProgressBar.setStyleSheet("")
        self.loadingProgressBar.setMaximum(100)
        self.loadingProgressBar.setProperty("value", 24)
        self.loadingProgressBar.setTextVisible(False)
        self.loadingProgressBar.setInvertedAppearance(False)
        self.loadingProgressBar.setObjectName("loadingProgressBar")
        self.verticalLayout_3.addWidget(self.loadingProgressBar)
        self.verticalLayout_2.addWidget(self.logoFrame)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(DisplayLoadingProgress)
        QtCore.QMetaObject.connectSlotsByName(DisplayLoadingProgress)

    def retranslateUi(self, DisplayLoadingProgress):
        _translate = QtCore.QCoreApplication.translate
        DisplayLoadingProgress.setWindowTitle(_translate("DisplayLoadingProgress", "TaskName"))
        self.loadingText.setText(_translate("DisplayLoadingProgress", "<html><head/><body><p><span style=\" font-size:12pt;\">Fetching Data</span></p></body></html>"))
        self.loadingProgressText.setText(_translate("DisplayLoadingProgress", "<html><head/><body><p><span style=\" font-size:10pt;\">24%</span></p></body></html>"))
        