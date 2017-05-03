import subprocess, sys, os, time
import csv

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


#open csv file to read the data
def __read_csv_file(name ='', loop_counter = int):
    print "read the csv file"
    ra = []
    distance = []
    try:
        with open(name, 'rb') as csvfile:
            reading = csv.reader(csvfile, dialect = 'excel', lineterminator ='\n', delimiter = ',')
            next(reading)                               # skip the header
            for (i, row) in enumerate(reading):
                if(i > 10):
                    break;
                try:                                    # insert number into the list + CONVERT data type
                    ra.append(float(row[0]))
                    distance.append(float(row[1]))
                except ValueError:
                    continue
    finally:
        csvfile.close()
    print ra
    print __average_list(ra)
    print distance


def __average_list(numbers):
    #return float(sum(numbers)) / max(len(numbers), 1)
    return sum(numbers) / len(numbers)


# read the data directly from the ssh.
def _pipe_reading(cmd):
    print "Reading from ssh"
    for line in iter(PopenIter(cmd), ''):
        if (line > 4000):
            break;
        buffer.append(line.rstrip())



# global variable
buffer = []         #global variable
cmd =''             #cmd
__read_csv_file("sample_data_for_kacao.csv", 15)

