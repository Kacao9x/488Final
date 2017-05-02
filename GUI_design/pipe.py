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

#open csv file to read the data
def __read_csv_file(name =''):
    print "read the csv file"
    ra = []
    distance = []
    try:
        with open(name, 'rb') as csvfile:
            reading = csv.reader(csvfile, delimeter='')
            for row in reading:
                if(row >4000):
                    break;
                ra.append(row[0])
                distance.append(row[1])
    finally:
        csvfile.close()

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
