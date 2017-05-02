import subprocess, sys, os, time
import csv
from threading import Thread

def main():
    Call("mkdir -p " + test_dir + "/lists")
    Call("echo 0 > /proc/sys/kernel/dmesg_restrict")
    Call("dmesg -c > /dev/null")

    global MODEL
    MODEL = Popen("hugo show | awk 'NR==4 {print$3}'")
    FillJBODList()                                                          # create /fill the JBOD list sg1 -- sg16
    DriveSync(JBOD_list, "all")                                             # power on specified drives in each JBOD
    FillDevList()                                                           # create/fill device list for the whole system
    CheckDrive(len(JBOD_list)*tray_size)                                    # check if any drive failed expected == tray * slot ??
    LogDump(test_dir + "/Pre-Test-Logs")                                    # save the PreTest Logs
    PowerOffAll()                                                           # power down all drives
    #all drive off

    __create_csv_title('runtime.csv')                                       # create a template to acquire data
    for loop in num_loops:
        for slot in slot_list:
            DriveSync(JBOD_list, slot)                                      # Power 1 slot every tray
            FillActiveDevList(len(JBOD_list))                               # Get active lsblk
            serial_list = get_serial_number()                               # Get serial number of active device

            Call("lsblk | awk '{print$1}' > " 
                + test_dir 
                + "/lists/BeforeFWDownload.txt")                            # Device list before download
            
            prep_out = PrepFIO(loop,slot)                                   # create FIO command
    
            t1 = Thread(target=RunFIO, args=(prep_out[0],))                 # run a command
            t2 = Thread(target=FW_Download, args=(0, loop, slot, serial_list))  # Download new FW
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            print "cycle: %d concurrent task completed" % loop
            time.sleep(2)

            CheckFIO(prep_out[1])
            CheckDrive(len(JBOD_list))                                      # count how many ON drive
            PowerOffActive()                                                # Power off active device
    
    LogDump(test_dir + "/Post-Test-Logs")
    CheckSmart()
    Call("dmesg -c > " + test_dir + "/dmesg.txt")
    return

# FW Download: downgrade upgrade the drive's fw from the given list of fw
# @tool: index associated to the tool list.
# @fw : a pair of 2 fw: current fw and the targeting fw to download
# return
def FW_Download(tool=int, loop=int, slot=int, serial_list=[]):
    for fw in FW_to_down:
        if tool == 0:                                                       # using hugo to download fw if tool = 0
            print "Downloading from %s to %s" %(fw[0][4:8], fw[1][4:8])+ " with hugo"
            # Popen("hugo u -m " + MODEL
            #     + " -f " + fw[1])                                         # download fw based on MODEL
            for serial in serial_list:
                start_time = time.time()
                Call("hugo u -s " + serial
                     + " -f " + fw[1])                                      # download fw based on serial
                RUN_TIME = time.time() - start_time
                print "Cycle: " + str(loop)
                print "The download runtime is %.2f sec" % (RUN_TIME)
                __create_test_log('runtime.csv', loop, slot, serial, RUN_TIME, fw)
                CheckDownload(loop, slot, fw)
            CheckFirmware(fw[1][4:8])                                       # Check hugo for current fw for all drive
        """
    	elif tool == 1:                                                               # using other tool to download fw
    		pass
        """
        
    return


# Check Download
# compare the number of dev list before and after download
def CheckDownload(loop,slot, fw):
    disklist = ("/lists/AfterFWDownload"
                + "_" + str(loop) 
                + "_" + str(slot)
                + "_" + fw[0].split('.')[0] 
                + "_" + fw[1].split('.')[0])
    Call("lsblk | awk '{print$1}' > " 
        + test_dir
        + disklist + ".txt")
    if Popen("diff -q "
                     + test_dir
                     + "/lists/BeforeFWDownload.txt "
                     + test_dir + disklist + ".txt") != "":
        sys.exit("One or more drives didn't show up...")
    else:
        print "no error in download checking."
    return


#Fills the global jbod list
def FillJBODList():
    global JBOD_list
    JBOD_list = []
    jbod_list_cmd = ("sg_map -i | grep facebook | awk '{print$1}' " +
                     "| sed 's/.*v\///'")
    for line in iter(PopenIter(jbod_list_cmd), ''):
        JBOD_list.append(line.rstrip())                                         #Populates the jbod list
    print "     number of jbods: ", len(JBOD_list)
    print "     jbod list: ", JBOD_list

#Fills the global device list
def FillDevList():
    global DEV_list
    DEV_list = []
    grep = len(JBOD_list) * len(slot_list) -1                                   #Number of devices to search for
    dev_list_cmd = ("lsblk | grep -w -A " + str(grep) +
                    " sdb | awk '{print$1}'")
    for line in iter(PopenIter(dev_list_cmd), ''):
        DEV_list.append(line.rstrip())                                          #Populate device list
    print "     number of devices: ", len(DEV_list)
    #print "     device list: ", DEV_list

# print out the active device list
def FillActiveDevList(length):
    global ACTIVE_dev_list
    ACTIVE_dev_list = DEV_list[0:length]                                        #Accurate list of connected devices
    print "     number of active devices: ", len(ACTIVE_dev_list)
    #print "     active_dev_list: ", active_dev_list

#Checks lsblk for number of connected drives
def CheckDrive(expected):
    print "Checking for Drives"
    found = int(Popen("lsblk -o model | grep -c " + check_model))               #Number of drives showing in lsblk
    print "     found:    ", found
    print "     expected: ", expected
    if found != expected:
        sys.exit("Failed drive check")                                          #If drives went missing between now and the sync, something is wrong with the system
    else:
        print "Found expected number of drives"

#Checks hugo for the current firmware on all drives
def CheckFirmware(expected):
    print "Checking current firmware"
    ###########TEMP FIX############
    if len(sys.argv) > 3:
            expected = expected.replace("FB", "GN")
    ###########TEMP FIX############
    for line in iter(PopenIter("hugo show | grep " + MODEL +
                               " | awk '{print$9}'"), ''):
        #Send to file?
        if line.rstrip() != expected:
            sys.exit("Failed firmware check")
    print "Found correct firmware on all drives"

# Checks the SMART health of drives in the device list, sets fault LEDs on failed drives
def CheckSmart():
    print "Checking Smart Health"
    try:
        cs = open(test_dir + "/CheckSMART.txt", 'a')
        for device in DEV_list:
            status_cmd = ("smartctl --health /dev/" + device +
                          " | grep 'SMART overall' | sed 's/.*: //g'")
            status = Popen(status_cmd)                                          # Smart status reported by smartctl
            print "     found status:", status
            if status == "PASSED":
                print " Drive " + device + " is healthy"
            else:                                                               # Add the drive to the failed list
                print " Drive " + device + " has failed!!!"
            cs.write(device + ": " + status)
        cs.close()
    except:
        sys.exit("smart health check error")

#Powers on the specified set of drives
def DriveSync(jbod_list, slot):
    print "Powering on selected slots"
    times_checked = 0
    while True:
        off_list = []
        for jbod in jbod_list:
            if (slot != "all"):                                                 #Only look at given slot
                awk = "==" + str(slot+1)                                        #Return only the line for the given slot
            else:
                awk = "<" + str(tray_size+1)                                    #Return a line for each slot within the tray size
            check_cmd = ("ocpjbod hdd /dev/" + jbod + " | awk 'NR" + awk +
                         "' | grep -v /dev/s | awk '{print$3}'")
            for line in iter(PopenIter(check_cmd), ''):
                off_tup = (jbod, line.rstrip())                                 #Tuple for sg device and slot number
                off_list.append(off_tup)                                        #Add tuple to off list
        print "     number of off slots: ", len(off_list)
        print "     off slots: ", off_list
        if len(off_list) == 0:
            print "All slots synced"
            return                                                              #Expected number of slots are on, continue with operations

        drives_checked = 0
        for off_tup in off_list:
            PrintProgress(drives_checked, len(off_list))                        #Print to screen to show activity
            PowerCycle(off_tup[0], off_tup[1])                                  #Power cycle the slot
            drives_checked+=1                                                   #Number of items in the off list that have been 'checked'
        PrintProgress(drives_checked, len(off_list))                            #Print to screen to show activity
        times_checked+=1                                                        #Number of times that the off list has been 'checked'
        time.sleep(sleep_timer)                                                 #Wait

#Powers all slots of all jbods off
def PowerOffAll():
    print "Powering off all slots"
    for jbod in JBOD_list:
        for slot in range(tray_size):
            Call("ocpjbod hdd --hdd-off " + str(slot) + " /dev/" + jbod)        #Power off all slots

# Powers off all slots that are on
def PowerOffActive():
    print "Powering off all active slots"
    for jbod in JBOD_list:
        check_cmd = ("ocpjbod hdd /dev/" + jbod +
                     " | grep 'Power On' | awk '{print$3}'")
        slots = []
        for line in iter(PopenIter(check_cmd), ''):
            slots.append(line.rstrip())
        for slot in slots:
            Call("ocpjbod hdd --hdd-off " + slot + " /dev/" + jbod)

# Power cycles the given slot
def PowerCycle(jbod, slot):
    Call("ocpjbod hdd --hdd-off " + str(slot) + " /dev/" + jbod)
    time.sleep(5)
    Call("ocpjbod hdd --hdd-on " + str(slot) + " /dev/" + jbod)
    time.sleep(5)

#Print drive sync progress bar
def PrintProgress(done, total):
    sys.stdout.write("\r" + str(done) + "/" + str(total) + " checked")          # Print to stdout how many have been seen
    sys.stdout.flush()
    if done == total:
        sys.stdout.write("\n")                                                  # If it is the last one, add a newline
        sys.stdout.flush()

def LogDump(filepath):
    Call("hugo l -m " + MODEL  + " -p " + filepath)
    return


# Prepare a fio job based then run it
def PrepFIO(loop, slot):
    output = (test_dir + "/Workload" + str(loop) 
            + "_" + str(slot) + ".txt")
    fio_cmd = ("fio --name=global --bs=512k --minimal --output=" + output +
               " --rw=randrw --runtime=2000 --continue_on_error=0 " +
               "--size=100% --direct=1 --time_based ")
    job_str = ""
    for dev in ACTIVE_dev_list:
        job_str += "--name=" + dev + " --filename=/dev/" + dev + " "            # Active devices to run fio on

    return (fio_cmd + job_str.rstrip(), output)                                 # Command to run fio with this job file

# Calls fio and prints the output continuously
def RunFIO(cmd):
    print "Starting fio"
    try:
        #print cmd
        print subprocess.check_call(cmd, shell=True)                            # Run the given fio command
    except KeyboardInterrupt:
        print "\n\nCtrl-C called, please wait"
        pid_cmd = ("ps aux | grep fio | grep -v grep\ fio " +
                   "| awk '{print$2}'")
        for pid in iter(PopenIter(pid_cmd), ''):                                # Find fio's pids
            Call("kill -9 " + str(pid))                                         # Kill fio
        time.sleep(60)
        sys.exit("exiting")
    except:
        print "error in fio"

# Check fio output for any errors, mark those devices as failed
def CheckFIO(output):
    print "Checking fio output"
    for device in ACTIVE_dev_list:
        errors_cmd = ("cut -d\; -f3-4 " + output + " | grep " +
                      device + " | sed 's/.*;//'")
        errors = int(Popen(errors_cmd))                                         # Number of errors on this device
        print "     " + device + " error count:", errors
        if errors != 0:
            sys.exit("error in fio")
    return

# get serial number based on the model string
def get_serial_number():
    #global SERIAL_LIST
    SERIAL_LIST = []
    cmd = ("hugo show | grep " + MODEL + " | awk '{print$4}'")
    for serial in iter(PopenIter(cmd), ''):
        SERIAL_LIST.append(serial.rstrip())
    return SERIAL_LIST


# Create template for test log.
def __create_csv_title(name =''):
    header = (['Cycle','Slot', 'Serial', 'Timelength', 'From', 'To'])   # create header for columns
    with open(name, 'ab') as outcsv:                                    # wb <binary mode> overwrite
        writer = csv.writer(outcsv, dialect='excel',
                            lineterminator='\r\n')
        writer.writerow('\n')
        writer.writerow(header)
    outcsv.close()
    return


# Create Test log
# The module select the important data to save up into .csv file
# return nothing. The log_file is saved up in the current directory
def __create_test_log(name = '', cycle = int, slot=int, serial = '', time_length=float, fw =()):
    data = ([cycle, slot, serial, time_length, fw[0], fw[1]])

    try:
        with open(name, 'ab') as outcsv:                                # append in binary mode
            writer = csv.writer(outcsv)
            writer.writerow(data)
    finally:
        outcsv.close()
    return



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

tray_size = 15                                                          # [0 - 15] tray
sleep_timer = 20                                                        # every 5minues ?? continue for an hour
check_model = "HUH721010AL"
slot_list = range(tray_size)
testname = "FW-Download"
test_dir = "/root/Desktop/" + testname
num_loops = range(4)

FW_list = []
for item in sys.argv[1:]:
    FW_list.append(item)

global FW_to_down
FW_to_down = [(FW_list[0], FW_list[1]),
              (FW_list[1], FW_list[0]),
              (FW_list[0], FW_list[2]),
              (FW_list[2], FW_list[1]),
              (FW_list[1], FW_list[2]),
              (FW_list[2], FW_list[0])]

main()
