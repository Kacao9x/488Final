import sys, numpy
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random
# https://sukhbinder.wordpress.com/2013/12/16/simple-pyqt-and-matplotlib-example-with-zoompan/

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()

        # Just some button
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button1 = QtGui.QPushButton('Zoom')
        self.button1.clicked.connect(self.zoom)

        self.button2 = QtGui.QPushButton('Pan')
        self.button2.clicked.connect(self.pan)

        self.button3 = QtGui.QPushButton('Home')
        self.button3.clicked.connect(self.home)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)

    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def pan(self):
        self.toolbar.pan()

    def plot(self):
        ''' DO NOT CHANGE. Original sample '''
        #data = [random.random() for i in range(25)]
        #ax = self.figure.add_subplot(111)      # create an axis
        #ax.hold(False)                         # discards the old graph
        #ax.plot(data, '*-')                    # plot data
        #self.canvas.draw()                     # refresh canvas



        ra = [45, 40, 90, -75, 80.2, 102.63]        # angle  --> change to buffer_angle[4000]
        ra = [x / 180.0 * 3.141593 for x in ra]     # convert angle to radian
        dec = [1.01, 6.05, 5.6, 4.02, 9.1, 7.85]    # distance --> change to buffer_distance[4000]

        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

        ax.set_ylim(0, 10)
        ax.set_yticks(numpy.arange(0, 10, 2))
        ax.scatter(ra, dec, c='r')                  # plot the first microphone

        self.canvas.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()

    sys.exit(app.exec_())