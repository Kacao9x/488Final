import subprocess, sys, numpy
import csv
import itertools
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

BUFFER_SIZE = 10
buffer_ra = []  # global variable
buffer_distance = []
line = 589



#Subprocess's call command with piped output and active shell
def Call(cmd):
    return subprocess.call(cmd, stdout=subprocess.PIPE,
                           shell=True)

#Subprocess's Popen command with piped output and active shell
def Popen(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            shell=True).communicate()[0].rstrip()

#Subprocess's Popen command for use in an iterator
def PopenIter(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            shell=True).stdout.readline

# example of reading text file
def __read_txt(name=''):
    columns=[]
    with open(name) as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            for (i, v) in enumerate(row):
                columns.append(v)
    print(columns)


def __average_list(numbers):
    #return float(sum(numbers)) / max(len(numbers), 1)
    return sum(numbers) / len(numbers)


def __read_csv_file2(name ='', line = int):
    print "read the csv file"
    del buffer_ra[:]
    del buffer_distance[:]
    loop_counter = 0
    try:
        with open(name, 'rb') as csvfile:
            reading = csv.reader(csvfile, dialect = 'excel', lineterminator ='\n', delimiter = ',')
            #next(reading)                               # skip the header
            for row in itertools.islice(reading, line, line + 10):
                if(loop_counter > 10):
                    break;
                try:                                    # insert number into the list + CONVERT data type
                    buffer_ra.append(float(row[1]))
                    buffer_distance.append(float(row[0]))
                    loop_counter += 1
                    line += 1
                except ValueError:
                    continue
    finally:
        csvfile.close()
    #print ra
    #print __average_list(ra)


# read the data directly from the ssh.
def _pipe_reading(cmd):
    print "Reading from ssh"
    for line in iter(PopenIter(cmd), ''):
        if (line > BUFFER_SIZE):
            break;
        buffer.append(line.rstrip())

class Window(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

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

    # update after 1 clicked
    def plot(self):
        global line
        print "plot", line, buffer_ra, buffer_distance

        self.__read_csv_file3("sample_data_for_kacao.csv")  # value stored in buffer1, buffer2

        ra = self.__average_list3(buffer_ra)
        distance = self.__average_list3(buffer_distance)
        ra = ra/ 180.0 * 3.141593

        #ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        ax = self.figure.add_subplot(111, polar = True)
        ax.hold(False)                                      # discards the old graph
        ax.set_ylim(0, 4.0)
        ax.set_yticks(numpy.arange(0, 4.0, 0.4))
        ax.scatter(ra, distance, c='r')                     # plot the first microphone

        self.canvas.draw()

    def __average_list3(self, numbers):
        # return float(sum(numbers)) / max(len(numbers), 1)
        return sum(numbers) / len(numbers)


    def __read_csv_file3(self, name=''):
        global line, BUFFER_SIZE
        print "Before read csv Line = ", line
        del buffer_ra[:]
        del buffer_distance[:]
        loop_counter = 0
        try:
            with open(name, 'rb') as csvfile:
                reading = csv.reader(csvfile, dialect='excel', lineterminator='\n', delimiter=',')
                # next(reading)                               # skip the header
                for row in itertools.islice(reading, line, line + BUFFER_SIZE):
                    if (loop_counter > BUFFER_SIZE):
                        break;
                    try:  # insert number into the list + CONVERT data type
                        buffer_ra.append(float(row[1]))
                        buffer_distance.append(float(row[0]))
                        loop_counter += 1
                        line += 1
                    except ValueError:
                        continue
        finally:
            csvfile.close()

        print "After all =", line
        print "\n"



# MAIN function
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())