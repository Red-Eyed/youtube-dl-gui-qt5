# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_qt-designer-beta.ui'
#
# Created: Thu Jan 15 03:38:31 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(622, 388)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.DownloadTab = QtGui.QWidget()
        self.DownloadTab.setObjectName(_fromUtf8("DownloadTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.DownloadTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.DownloadTab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(24, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.BatchAdd = QtGui.QPushButton(self.groupBox)
        self.BatchAdd.setObjectName(_fromUtf8("BatchAdd"))
        self.horizontalLayout_3.addWidget(self.BatchAdd)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(33, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.browse_btn = QtGui.QPushButton(self.groupBox)
        self.browse_btn.setObjectName(_fromUtf8("browse_btn"))
        self.horizontalLayout_2.addWidget(self.browse_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox_2 = QtGui.QGroupBox(self.DownloadTab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ConvertCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.ConvertCheckBox.setObjectName(_fromUtf8("ConvertCheckBox"))
        self.horizontalLayout_4.addWidget(self.ConvertCheckBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.ConvertComboBox = QtGui.QComboBox(self.groupBox_2)
        self.ConvertComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.ConvertComboBox.setObjectName(_fromUtf8("ConvertComboBox"))
        self.ConvertComboBox.addItem(_fromUtf8(""))
        self.ConvertComboBox.addItem(_fromUtf8(""))
        self.ConvertComboBox.addItem(_fromUtf8(""))
        self.ConvertComboBox.addItem(_fromUtf8(""))
        self.ConvertComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.ConvertComboBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.DeleteFileCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.DeleteFileCheckBox.setChecked(True)
        self.DeleteFileCheckBox.setObjectName(_fromUtf8("DeleteFileCheckBox"))
        self.verticalLayout_9.addWidget(self.DeleteFileCheckBox)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.download_btn = QtGui.QPushButton(self.DownloadTab)
        self.download_btn.setStyleSheet(_fromUtf8(""))
        self.download_btn.setDefault(True)
        self.download_btn.setFlat(False)
        self.download_btn.setObjectName(_fromUtf8("download_btn"))
        self.verticalLayout_4.addWidget(self.download_btn)
        self.tabWidget.addTab(self.DownloadTab, _fromUtf8(""))
        self.ActivityTab = QtGui.QWidget()
        self.ActivityTab.setObjectName(_fromUtf8("ActivityTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.ActivityTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tableWidget = QtGui.QTableWidget(self.ActivityTab)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(_fromUtf8("QTableWidget\n"
"{\n"
"    outline: 0;\n"
"}"))
        self.tableWidget.setFrameShape(QtGui.QFrame.VLine)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.ActivityTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionLicense = QtGui.QAction(MainWindow)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionLicense)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.download_btn.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Enter url and download location", None))
        self.label_2.setText(_translate("MainWindow", "Video URL:", None))
        self.BatchAdd.setText(_translate("MainWindow", "Batch Add", None))
        self.label_3.setText(_translate("MainWindow", "Save To:", None))
        self.browse_btn.setText(_translate("MainWindow", "Browse", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Convert", None))
        self.ConvertCheckBox.setText(_translate("MainWindow", "Convert After Download", None))
        self.ConvertComboBox.setItemText(0, _translate("MainWindow", "mp4", None))
        self.ConvertComboBox.setItemText(1, _translate("MainWindow", "flv", None))
        self.ConvertComboBox.setItemText(2, _translate("MainWindow", "ogg", None))
        self.ConvertComboBox.setItemText(3, _translate("MainWindow", "webm", None))
        self.ConvertComboBox.setItemText(4, _translate("MainWindow", "mkv", None))
        self.DeleteFileCheckBox.setText(_translate("MainWindow", "Delete Original File", None))
        self.download_btn.setText(_translate("MainWindow", "Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DownloadTab), _translate("MainWindow", "Download", None))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Video/Song", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ETA", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Speed", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ActivityTab), _translate("MainWindow", "Activity", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionLicense.setText(_translate("MainWindow", "License", None))

import resource_rc
