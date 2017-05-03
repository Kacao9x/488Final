# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_app.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random
import numpy
import matplotlib.pyplot as pyplot

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
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        #Form the layout for Tab
        self.tabWidget.setGeometry(QtCore.QRect(50, 250, 531, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()

        #########################################################################################
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        #layout = QtGui.QVBoxLayout(self.tab1_polar_plot)

        # Plotting the live data from the microphone here.
        #self.matplotlibwidget = MatplotlibWidget(self.tab, None, "488 Audio Tracking")
        self.matplotlibwidget = MatplotlibWidget(self.tab)
        self.matplotlibwidget.setObjectName(_fromUtf8("plot_polar"))
        self.verticalLayout_3.addWidget(self.matplotlibwidget)
        self.tabWidget.addTab(self.tab, _fromUtf8("Mapping"))





        # Graphic View: do the mapping sound here
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = PlotWidget(self.tab_2)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

##########################################################################################

        # Label: Input Textbox
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(640, 360, 251, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 330, 111, 21))


        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(640, 430, 256, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_5 = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.splitter)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.PORT_groupbox_1 = QtGui.QGroupBox(self.centralwidget)
        self.PORT_groupbox_1.setGeometry(QtCore.QRect(80, 20, 262, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PORT_groupbox_1.setFont(font)
        self.PORT_groupbox_1.setObjectName(_fromUtf8("PORT_groupbox_1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.PORT_groupbox_1)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit_2 = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_4.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_10.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.virtualsound_groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.virtualsound_groupBox_2.setGeometry(QtCore.QRect(590, 20, 391, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.virtualsound_groupBox_2.setFont(font)
        self.virtualsound_groupBox_2.setObjectName(_fromUtf8("virtualsound_groupBox_2"))
        self.layoutWidget = QtGui.QWidget(self.virtualsound_groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 211))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.freq_slider_1 = QtGui.QSlider(self.layoutWidget)
        self.freq_slider_1.setMaximum(20000)
        self.freq_slider_1.setSingleStep(10)
        self.freq_slider_1.setSliderPosition(0)
        self.freq_slider_1.setOrientation(QtCore.Qt.Vertical)
        self.freq_slider_1.setTickInterval(3)
        self.freq_slider_1.setObjectName(_fromUtf8("freq_slider_1"))
        self.gridLayout_5.addWidget(self.freq_slider_1, 0, 0, 3, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtGui.QFrame.Box)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtGui.QFrame.Box)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)
        self.amp_dial = QtGui.QDial(self.layoutWidget)
        self.amp_dial.setObjectName(_fromUtf8("amp_dial"))
        self.gridLayout_3.addWidget(self.amp_dial, 1, 0, 1, 1)

        # Generate button
        self.generate_button = QtGui.QPushButton(self.layoutWidget)
        self.generate_button.setObjectName(_fromUtf8("generate_button"))
        self.gridLayout_3.addWidget(self.generate_button, 1, 1, 1, 1)

        # Volume dial 1
        self.amp_dial_2 = QtGui.QDial(self.layoutWidget)
        self.amp_dial_2.setObjectName(_fromUtf8("amp_dial_2"))
        self.gridLayout_3.addWidget(self.amp_dial_2, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        # Freq slider 2
        self.freq_slider_2 = QtGui.QSlider(self.layoutWidget)
        self.freq_slider_2.setMaximum(20000)
        self.freq_slider_2.setSingleStep(10)
        self.freq_slider_2.setSliderPosition(0)
        self.freq_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.freq_slider_2.setTickInterval(3)
        self.freq_slider_2.setObjectName(_fromUtf8("freq_slider_2"))
        self.gridLayout_5.addWidget(self.freq_slider_2, 0, 2, 3, 1)

        # Time progress percent % bar
        self.time_progress = QtGui.QProgressBar(self.layoutWidget)
        self.time_progress.setProperty("value", 24)
        self.time_progress.setObjectName(_fromUtf8("time_progress"))
        self.gridLayout_5.addWidget(self.time_progress, 1, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        # Amp spinner 1: volume input 1
        self.amp_spin_1 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_spin_1.setFont(font)
        self.amp_spin_1.setMaximum(20000)
        self.amp_spin_1.setSingleStep(10)
        self.amp_spin_1.setObjectName(_fromUtf8("amp_spin_1"))
        self.gridLayout_2.addWidget(self.amp_spin_1, 1, 0, 1, 1)

        # Freq spinner input 1
        self.freq_spin_1 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.freq_spin_1.setFont(font)
        self.freq_spin_1.setMaximum(20000)
        self.freq_spin_1.setSingleStep(10)
        self.freq_spin_1.setObjectName(_fromUtf8("freq_spin_1"))
        self.gridLayout_2.addWidget(self.freq_spin_1, 0, 0, 1, 1)

        # Freq spinner input 2
        self.freq_spin_2 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.freq_spin_2.setFont(font)
        self.freq_spin_2.setMaximum(20000)
        self.freq_spin_2.setSingleStep(10)
        self.freq_spin_2.setObjectName(_fromUtf8("freq_spin_2"))
        self.gridLayout_2.addWidget(self.freq_spin_2, 0, 2, 1, 1)

        # Label 4: amplitude
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        # Amp spinner 2: volume input 2
        self.amp_spin_2 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_spin_2.setFont(font)
        self.amp_spin_2.setMaximum(20000)
        self.amp_spin_2.setSingleStep(10)
        self.amp_spin_2.setObjectName(_fromUtf8("amp_spin_2"))
        self.gridLayout_2.addWidget(self.amp_spin_2, 1, 2, 1, 1)
        self.dur_spin_1 = QtGui.QSpinBox(self.layoutWidget)

        # Duration spinner 1: time duration input 1
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dur_spin_1.setFont(font)
        self.dur_spin_1.setMaximum(20000)
        self.dur_spin_1.setSingleStep(10)
        self.dur_spin_1.setObjectName(_fromUtf8("dur_spin_1"))
        self.gridLayout_2.addWidget(self.dur_spin_1, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)

        # Label Amplitude
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.dur_spin_2 = QtGui.QSpinBox(self.layoutWidget)

        # Duration spinner 2: time duration input 2
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dur_spin_2.setFont(font)
        self.dur_spin_2.setMaximum(20000)
        self.dur_spin_2.setSingleStep(10)
        self.dur_spin_2.setObjectName(_fromUtf8("dur_spin_2"))
        self.gridLayout_2.addWidget(self.dur_spin_2, 2, 2, 1, 1)

        # Frequency spinner label
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.textEdit.raise_()
        self.label_6.raise_()
        self.splitter.raise_()
        self.PORT_groupbox_1.raise_()
        self.virtualsound_groupBox_2.raise_()
        self.tabWidget.raise_()

        # Menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))                                                              # menu File
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))                                                        # Menu Setting
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.dockWidget_3.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
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

        # Add event handling for the menu bar here
        self.menuFile.addAction(self.actionOpen)                                                                        #Menu bar: open file
        self.menuFile.addAction(self.actionSave)                                                                        #Menu bar: save to
        self.menuFile.addAction(self.actionSave_as)                                                                     #Menu bar: save as
        self.menuFile.addAction(self.actionQuit)                                                                        #Menu bar: Quit
        self.menuSetting.addAction(self.actionTerminal)                                                                 #Menu bar: terminal
        self.menuSetting.addAction(self.actionGraph)                                                                    #Menu bar: Graph
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        # establish the connection betwween button and field text
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.freq_spin_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.freq_slider_2.setValue)
        QtCore.QObject.connect(self.freq_slider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.freq_spin_2.setValue)
        QtCore.QObject.connect(self.amp_dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.amp_spin_1.setValue)
        QtCore.QObject.connect(self.amp_spin_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.amp_dial_2.setValue)
        QtCore.QObject.connect(self.amp_dial_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.amp_spin_2.setValue)
        QtCore.QObject.connect(self.amp_spin_1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.amp_dial.setValue)
        QtCore.QObject.connect(self.freq_spin_1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.freq_slider_1.setValue)
        QtCore.QObject.connect(self.freq_slider_1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.freq_spin_1.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.label_6.setText(_translate("MainWindow", "Input Textbox", None))
        self.label_5.setText(_translate("MainWindow", "Output Textbox", None))
        self.PORT_groupbox_1.setTitle(_translate("MainWindow", "COM configuration", None))
        self.label.setText(_translate("MainWindow", "COM", None))
        self.label_2.setText(_translate("MainWindow", "BAUD", None))
        self.label_10.setText(_translate("MainWindow", "Filename", None))
        self.virtualsound_groupBox_2.setTitle(_translate("MainWindow", "Virtual Sound Control Panel", None))
        self.label_7.setText(_translate("MainWindow", "Sound 1", None))
        self.label_8.setText(_translate("MainWindow", "Sound 2", None))
        self.generate_button.setText(_translate("MainWindow", "GENERATE", None))
        self.label_4.setText(_translate("MainWindow", "Amplitude", None))
        self.label_9.setText(_translate("MainWindow", "Duration (ms)", None))
        self.label_3.setText(_translate("MainWindow", "Frequency (Hz)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph", None))

def plot_data(self):

    # a figure instance to plot on
    self.figure = plt.figure()

    # this is the Canvas Widget that displays the `figure`
    # it takes the `figure` instance as a parameter to __init__
    self.canvas = FigureCanvas(self.figure)

    # this is the Navigation widget
    # it takes the Canvas widget and a parent
    self.toolbar = NavigationToolbar(self.canvas, self)

    # Just some button connected to `plot` method
    self.button = QtGui.QPushButton('Plot')
    self.button.clicked.connect(self.plot)

    # set the layout
    layout = QtGui.QVBoxLayout()
    layout.addWidget(self.toolbar)
    layout.addWidget(self.canvas)
    layout.addWidget(self.button)
    self.setLayout(layout)


def plot(self):
    ''' plot some random stuff '''
    # random data
    data = [random.random() for i in range(10)]

    # create an axis
    ax = self.figure.add_subplot(111)

    # discards the old graph
    ax.hold(False)

    # plot data
    ax.plot(data, '*-')

    # refresh canvas
    self.canvas.draw()

"""
    def file_save(self):
        name = QtGui.QFiledialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlaintext()
        file.write(text)
"""

from matplotlibwidget import MatplotlibWidget
from pyqtgraph import PlotWidget


import numpy
import matplotlib.pyplot as pyplot

class plot_polar(object):
    def plot_data(self):
        ra = [45, 40, 90, -75, 80.2, 102.63]  # angle  --> change to buffer_angle[4000]
        ra = [x / 180.0 * 3.141593 for x in ra]  # convert angle to radian

        dec = [1.01, 6.05, 5.6, 4.02, 9.1, 7.85]  # distance --> change to buffer_distance[4000]

        fig = pyplot.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        ax.set_ylim(0, 10)
        ax.set_yticks(numpy.arange(0, 10, 2))
        ax.scatter(ra, dec, c='r')  # plot the first microphone

        # ax.scatter(rb, dec, c = 'b')                   # plot the second microphone
        # ax.scatter(rh, dec, c = 'g')                   # plot the human voice

        pyplot.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #plot = plot_polar()
    #plot.plot_data()


    plot = plot_polar()
    plot.plot_data()
    sys.exit(app.exec_())

