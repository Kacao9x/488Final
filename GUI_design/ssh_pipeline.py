import subprocess, sys, numpy
import csv
import itertools
from PyQt4 import QtGui
import serial, time

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

################ DEFINE global variable ###########
BUFFER_SIZE = 10
buffer_ra = []  # global variable
buffer_distance = []

buffer_ra__1 = []       # temp var
buffer_distance_1 = []  # tmep var
line = 0
port='COM10'
baudrate = 115200
timeout = time.time() + 60/60
sample_rate = 44100
#############################3#####################


def __serial_config():
    print ("serial config ...")
    global port, baudrate, timeout
    try:
        ser = serial.Serial(port, baudrate, timeout)
    except serial.SerialException:
        print ("Serial connection failed")


def __scan_microphone():
    sample_len = sample_rate*5
    with serial.Serial(port, baudrate, timeout) as ser:

        row = ser.readline().rstrip()
        # distance = line[0], angle = line[1]
        if row:
            x,y = row.split(',')
            print row[0], row[1]
            buffer_distance_1.append(float(row[0]))
            buffer_ra__1.append(float(row[1]))

    ser.close()

def main():
    #__serial_config()
    app = QtGui.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

class Window(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
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

        self.__read_csv_file3("sample_data_for_kacao.csv")          # value stored in buffer1, buffer2
        #self.__scan_microphone()
        ra = self.__average_list3(buffer_ra)
        distance = self.__average_list3(buffer_distance)
        ra = ra/ 180.0 * 3.141593

        #ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        ax = self.figure.add_subplot(111, polar = True)
        ax.hold(False)                                              # discards the old graph
        ax.spines['polar'].set_visible(False)
        ax.set_ylim(0, 2.4)
        ax.set_yticks(numpy.arange(0, 2.4, 0.4))
        ax.scatter(ra, distance, c='r')                             # plot the first microphone


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
    main()
    __serial_config()
    while True:
        __scan_microphone()



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
# read the data directly from the ssh.
def _pipe_reading(cmd):
    print "Reading from ssh"
    for line in iter(PopenIter(cmd), ''):
        if (line > BUFFER_SIZE):
            break;
        buffer.append(line.rstrip())


"""
with open("test.txt", "wb") as output_file:
    csv_out = csv.writer(output_file, delimiter=',', dialect='excel-tab')
    csv_out.writerow("date","zenith","elevation","azimuth","conv_elevation")

    ser=serial.Serial(port=3, baudrate=9600, timeout=60)
    ser.open()
    for count in range(10):
        str = ser.readline().rstrip()
        csv_out.writerow(str.split(':'))
    ser.close()
"""