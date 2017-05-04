# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simple_app.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1154, 710)
        self.centralwidget = QtGui.QWidget(MainWindow)	
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		
        self.matplotlibwidget = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget.setGeometry(QtCore.QRect(290, 140, 521, 401))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))

		self.Button2_Plot = QtGui.QPushButton(self.centralwidget)
        self.Button2_Plot.setGeometry(QtCore.QRect(510, 560, 75, 23))
        self.Button2_Plot.setObjectName(_fromUtf8("Button2_Plot"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionTerminal = QtGui.QAction(MainWindow)
        self.actionTerminal.setObjectName(_fromUtf8("actionTerminal"))
        self.actionGraph = QtGui.QAction(MainWindow)
        self.actionGraph.setObjectName(_fromUtf8("actionGraph"))
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Button2_Plot, QtCore.SIGNAL(_fromUtf8("clicked()")), self.matplotlibwidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Button2_Plot.setText(_translate("MainWindow", "Plot", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph", None))

from matplotlibwidget import MatplotlibWidget
