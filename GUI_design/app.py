# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_app.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import csv
import random

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as pyplot
import numpy

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
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(750, 340, 251, 61))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label9_input = QtGui.QLabel(self.centralwidget)
        self.label9_input.setGeometry(QtCore.QRect(750, 310, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label9_input.setFont(font)
        self.label9_input.setObjectName(_fromUtf8("label9_input"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(750, 410, 256, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label10_output = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label10_output.setFont(font)
        self.label10_output.setObjectName(_fromUtf8("label10_output"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.splitter)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.PORT_groupbox_1 = QtGui.QGroupBox(self.centralwidget)
        self.PORT_groupbox_1.setGeometry(QtCore.QRect(190, 50, 262, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PORT_groupbox_1.setFont(font)
        self.PORT_groupbox_1.setObjectName(_fromUtf8("PORT_groupbox_1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.PORT_groupbox_1)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label1_com = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1_com.setFont(font)
        self.label1_com.setObjectName(_fromUtf8("label1_com"))
        self.gridLayout_4.addWidget(self.label1_com, 0, 0, 1, 1)
        self.label2_baud = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2_baud.setFont(font)
        self.label2_baud.setObjectName(_fromUtf8("label2_baud"))
        self.gridLayout_4.addWidget(self.label2_baud, 1, 0, 1, 2)
        self.lineEdit_baud = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_baud.setFont(font)
        self.lineEdit_baud.setObjectName(_fromUtf8("lineEdit_baud"))
        self.gridLayout_4.addWidget(self.lineEdit_baud, 1, 2, 1, 1)
        self.label3_filename = QtGui.QLabel(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3_filename.setFont(font)
        self.label3_filename.setObjectName(_fromUtf8("label3_filename"))
        self.gridLayout_4.addWidget(self.label3_filename, 2, 0, 1, 1)
        self.lineEdit_filename = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_filename.setFont(font)
        self.lineEdit_filename.setObjectName(_fromUtf8("lineEdit_filename"))
        self.gridLayout_4.addWidget(self.lineEdit_filename, 2, 2, 1, 1)
        self.lineEdit_com = QtGui.QLineEdit(self.PORT_groupbox_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_com.setFont(font)
        self.lineEdit_com.setObjectName(_fromUtf8("lineEdit_com"))
        self.gridLayout_4.addWidget(self.lineEdit_com, 0, 2, 1, 1)
        self.label3_filename.raise_()
        self.lineEdit_filename.raise_()
        self.lineEdit_baud.raise_()
        self.label1_com.raise_()
        self.lineEdit_com.raise_()
        self.label2_baud.raise_()
        self.virtualsound_groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.virtualsound_groupBox_2.setGeometry(QtCore.QRect(680, 40, 391, 261))
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
        self.label4_sound1 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label4_sound1.setFont(font)
        self.label4_sound1.setFrameShape(QtGui.QFrame.Box)
        self.label4_sound1.setObjectName(_fromUtf8("label4_sound1"))
        self.gridLayout_3.addWidget(self.label4_sound1, 0, 0, 1, 1)
        self.label5_sound2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label5_sound2.setFont(font)
        self.label5_sound2.setFrameShape(QtGui.QFrame.Box)
        self.label5_sound2.setObjectName(_fromUtf8("label5_sound2"))
        self.gridLayout_3.addWidget(self.label5_sound2, 0, 2, 1, 1)
        self.amp_dial = QtGui.QDial(self.layoutWidget)
        self.amp_dial.setObjectName(_fromUtf8("amp_dial"))
        self.gridLayout_3.addWidget(self.amp_dial, 1, 0, 1, 1)
        self.button1_generate = QtGui.QPushButton(self.layoutWidget)
        self.button1_generate.setObjectName(_fromUtf8("button1_generate"))
        self.gridLayout_3.addWidget(self.button1_generate, 1, 1, 1, 1)
        self.amp_dial_2 = QtGui.QDial(self.layoutWidget)
        self.amp_dial_2.setObjectName(_fromUtf8("amp_dial_2"))
        self.gridLayout_3.addWidget(self.amp_dial_2, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.freq_slider_2 = QtGui.QSlider(self.layoutWidget)
        self.freq_slider_2.setMaximum(20000)
        self.freq_slider_2.setSingleStep(10)
        self.freq_slider_2.setSliderPosition(0)
        self.freq_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.freq_slider_2.setTickInterval(3)
        self.freq_slider_2.setObjectName(_fromUtf8("freq_slider_2"))
        self.gridLayout_5.addWidget(self.freq_slider_2, 0, 2, 3, 1)
        self.time_progress = QtGui.QProgressBar(self.layoutWidget)
        self.time_progress.setProperty("value", 24)
        self.time_progress.setObjectName(_fromUtf8("time_progress"))
        self.gridLayout_5.addWidget(self.time_progress, 1, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.amp_spin_1 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_spin_1.setFont(font)
        self.amp_spin_1.setMaximum(20000)
        self.amp_spin_1.setSingleStep(10)
        self.amp_spin_1.setObjectName(_fromUtf8("amp_spin_1"))
        self.gridLayout_2.addWidget(self.amp_spin_1, 1, 0, 1, 1)
        self.freq_spin_1 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.freq_spin_1.setFont(font)
        self.freq_spin_1.setMaximum(20000)
        self.freq_spin_1.setSingleStep(10)
        self.freq_spin_1.setObjectName(_fromUtf8("freq_spin_1"))
        self.gridLayout_2.addWidget(self.freq_spin_1, 0, 0, 1, 1)
        self.freq_spin_2 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.freq_spin_2.setFont(font)
        self.freq_spin_2.setMaximum(20000)
        self.freq_spin_2.setSingleStep(10)
        self.freq_spin_2.setObjectName(_fromUtf8("freq_spin_2"))
        self.gridLayout_2.addWidget(self.freq_spin_2, 0, 2, 1, 1)
        self.label7_amp = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label7_amp.setFont(font)
        self.label7_amp.setObjectName(_fromUtf8("label7_amp"))
        self.gridLayout_2.addWidget(self.label7_amp, 1, 1, 1, 1)
        self.amp_spin_2 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amp_spin_2.setFont(font)
        self.amp_spin_2.setMaximum(20000)
        self.amp_spin_2.setSingleStep(10)
        self.amp_spin_2.setObjectName(_fromUtf8("amp_spin_2"))
        self.gridLayout_2.addWidget(self.amp_spin_2, 1, 2, 1, 1)
        self.dur_spin_1 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dur_spin_1.setFont(font)
        self.dur_spin_1.setMaximum(20000)
        self.dur_spin_1.setSingleStep(10)
        self.dur_spin_1.setObjectName(_fromUtf8("dur_spin_1"))
        self.gridLayout_2.addWidget(self.dur_spin_1, 2, 0, 1, 1)
        self.label8_duration = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label8_duration.setFont(font)
        self.label8_duration.setObjectName(_fromUtf8("label8_duration"))
        self.gridLayout_2.addWidget(self.label8_duration, 2, 1, 1, 1)
        self.dur_spin_2 = QtGui.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dur_spin_2.setFont(font)
        self.dur_spin_2.setMaximum(20000)
        self.dur_spin_2.setSingleStep(10)
        self.dur_spin_2.setObjectName(_fromUtf8("dur_spin_2"))
        self.gridLayout_2.addWidget(self.dur_spin_2, 2, 2, 1, 1)
        self.label6_freq = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label6_freq.setFont(font)
        self.label6_freq.setObjectName(_fromUtf8("label6_freq"))
        self.gridLayout_2.addWidget(self.label6_freq, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        ### Matplot here
        self.matplotlibwidget = MatplotlibWidget(self.centralwidget)
        self.matplotlibwidget.setGeometry(QtCore.QRect(130, 210, 521, 401))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        #self.canvas = FigureCanvas(self.figure)
        self.matplotlibwidget.draw()        # required to update the windows



        self.Button2_Plot = QtGui.QPushButton(self.centralwidget)
        self.Button2_Plot.setGeometry(QtCore.QRect(350, 620, 75, 23))
        self.Button2_Plot.setObjectName(_fromUtf8("Button2_Plot"))
        self.Button2_Plot.clicked.connect(self.plot)

        ############

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
        self.menuSetting.addAction(self.actionTerminal)
        self.menuSetting.addAction(self.actionGraph)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
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
        self.label9_input.setText(_translate("MainWindow", "Input Textbox", None))
        self.label10_output.setText(_translate("MainWindow", "Output Textbox", None))
        self.PORT_groupbox_1.setTitle(_translate("MainWindow", "COM configuration", None))
        self.label1_com.setText(_translate("MainWindow", "COM", None))
        self.label2_baud.setText(_translate("MainWindow", "BAUD", None))
        self.label3_filename.setText(_translate("MainWindow", "Filename", None))
        self.virtualsound_groupBox_2.setTitle(_translate("MainWindow", "Virtual Sound Control Panel", None))
        self.label4_sound1.setText(_translate("MainWindow", "Sound 1", None))
        self.label5_sound2.setText(_translate("MainWindow", "Sound 2", None))
        self.button1_generate.setText(_translate("MainWindow", "GENERATE", None))
        self.label7_amp.setText(_translate("MainWindow", "Amplitude", None))
        self.label8_duration.setText(_translate("MainWindow", "Duration (ms)", None))
        self.label6_freq.setText(_translate("MainWindow", "Frequency (Hz)", None))
        self.Button2_Plot.setText(_translate("MainWindow", "Plot", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph", None))

    def plot(self):
        #populate the ra
        #ra =

        # plot a polar graph here
        ra = [random.randint(-50,100) for i in range(6)]
        #ra = [45, 40, 90, -75, 80.2, 106.7]            # angle  --> change to buffer_angle[4000]
        ra = [x / 180.0 * 3.141593 for x in ra]             # convert angle to radian

        dec = [1.01, 6.05, 5.6, 4.02, 9.1, 7.85]            # distance --> change to buffer_distance[4000]

        fig = pyplot.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        ax.set_ylim(0, 10)
        ax.set_yticks(numpy.arange(0, 10, 2))
        ax.scatter(ra, dec, c='r')                          # plot the first microphone

        pyplot.show()
        #pyplot.draw()

    # open csv file to read the data
    def __read_csv_file(name=''):
        print "read the csv file"
        ra = []
        distance = []
        try:
            with open(name, 'rb') as csvfile:
                reading = csv.reader(csvfile, delimeter='')
                for row in reading:
                    if (row > 4000):
                        break;
                    ra.append(row[0])
                    distance.append(row[1])
        finally:
            csvfile.close()
        return ra


class MatplotlibWidget(QtGui.QWidget):
    def __init__(self):
        super
from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

