import serial
import RPi.GPIO as GPIO      
import os, time
import csv

def reset():
    global input_user
    if input_user==0:
        # Enable Serial Communication
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
         
        # Transmitting AT Commands to the Modem
        # '\r\n' indicates the Enter key
        for j in range(length):
            for i in range(1):
                if i == 0:
                    port.write('AT'+'\r\n')
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    port.write('ATE0'+'\r\n')      # Disable the Echo
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    # Sending a message to a particular Number
                    set_reset = data[j]
                    set_r1 = '"' + set_reset + '"'
                    port.write('AT+CMGS='+ set_r1 +'\r\n')
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    port.write('Fire alaram has been Reset. Contact security personel for more info.'+'\r\n')  # Message
                    rcv = port.read(10)
                    print rcv
             
                    port.write("\x1A") # Enable to send SMS
                    for i in range(10):
                        rcv = port.read(10)
                    print rcv
        while True:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(16, GPIO.IN)
            input_user = GPIO.input(16)
            if input_user == 1:
                z = run_mode()

            
def run_mode():
    print "bandhe"
    global input_user
    if input_user == 1:
        # Enable Serial Communication
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        print "1" 
        # Transmitting AT Commands to the Modem
        # '\r\n' indicates the Enter key
        for k in range(length):
            print "2"
            for i in range(1):
                print i
                if i == 0:
                    port.write('AT'+'\r\n')
                    rcv = port.read(100)
                    print rcv
##                    time.sleep(1)
             
                    port.write('ATE0'+'\r\n')      # Disable the Echo
                    rcv = port.read(100)
                    print rcv
##                    time.sleep(1)
             
                    port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
                    rcv = port.read(100)
                    print rcv
##                    time.sleep(1)
             
                    port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
                    rcv = port.read(100)
                    print rcv
##                    time.sleep(1)
             
                    # Sending a message to a particular Number
                    s = data[k]
                    s1 = '"' + s + '"'
                    port.write('AT+CMGS='+ s1 +'\r\n')
                    rcv = port.read(100)
                    print rcv
##                    time.sleep(1)
             
                    port.write('Welcome to CASSINS HAWK SAFETY Equip. Nature of project: Fire alarm automed systems. This is a test message. Please dont reply'+'\r\n')  # Message
                    rcv = port.read(10)
                    print rcv
                    time.sleep(2)
             
                    port.write("\x1A") # Enable to send SMS
                    for i in range(10):
                        rcv = port.read(10)
                    print rcv
        while True:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(16, GPIO.IN)
            input_user = GPIO.input(16)
            if input_user == 0:
                port.close()
                y = reset()

data=[]
print "hi"
f = open("//home//pi//project//file.csv", "r")
for line in f:
    cells = line.split(",")
    data.append((cells[2]))
f.close()
data = data[1:]
data = map(lambda s: s.strip(), data)
length = len(data)
print length
global input_user
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
input_user = GPIO.input(16)
input_user==1
print"here"
run = run_mode()
  
