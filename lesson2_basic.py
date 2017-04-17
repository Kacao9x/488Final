import sys
from PyQt4 import QtGui, Qtcore
import pyqtgraph
import numpy as np
import time

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__
        self.setGeometry(50,50,500,300)
        self.setWindowTitle()
        self.setWindowIcon(QtGui.QIcon('xxx.png'))

    def home(self):
        btn = Qtn.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()

    def set_frequency(self):
        spin1 = Qtn.QSpinText("Frequency", freq_spin_1)
        spin2 = Qtn.QSpinText("Amplifier", amp_spin_2)
        spin3 = Qtn.QSpinText("Frequency", amp_spin_3)
        spin4 = Qtn.QSpinText("Amplifier", amp_spin_4)

    def QT_draph(self):

frg
    def update(self):
        t1 = time.clock()
        points = 100        #number of data points
        X=np.arance(points)

    def close_application(self):
        print("Closing the application")
        sys.exit()
