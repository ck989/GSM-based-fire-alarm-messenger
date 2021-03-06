##AUTHOR 1. KEERTHAN REDDY G K
##       2. CHAYA KUMAR GOWDA (KUMAR A C)
##DATE   22/06/2018




import serial
import RPi.GPIO as GPIO      
import os, time
import csv
import numpy as np

def reset():
    if input_user_reset==1:
        # Enable Serial Communication
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
         
        # Transmitting AT Commands to the Modem
        # '\r\n' indicates the Enter key
        for j in range(length):
            for i in range(1):
                print i
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
                    z = run_mode()
def run_mode():
    if input_user == 1:
        # Enable Serial Communication
        port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
         
        # Transmitting AT Commands to the Modem
        # '\r\n' indicates the Enter key
        for k in range(length):
            for i in range(1):
                print i
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
                    print data[k]
                    s = data[k]
                    s1 = '"' + s + '"'
                   
                    port.write('AT+CMGS='+ s1 +'\r\n')
                    rcv = port.read(10)
                    print rcv
##                    time.sleep(1)
             
                    port.write('ALERT! Fire alaram is activated. Evacuate to saftey.'+'\r\n')  # Message
                    rcv = port.read(1)
                    print rcv
             
                    port.write("\x1A") # Enable to send SMS
                    for i in range(10):
                        rcv = port.read(10)
                    print rcv
                    
        else:
            print "alaram not activated"
        port.close()
        y = reset()

data=[]
new_data=[]
f = open("//home//pi//project//file.csv", "r")
for line in f:
    cells = line.split(",")
    data.append((cells[2]))
f.close()
data = data[1:]
data = map(lambda s: s.strip(), data)
print data
length = len(data)
for l in range(len(data)):
    new_data.append(int(data[l]))
print new_data
length = len(new_data)

##new_data_usable= map(int,new_data)


        
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)
input_user = GPIO.input(16)
GPIO.setup(18, GPIO.IN)
input_user_reset = GPIO.input(18)
print input_user
if input_user==1:
    run = run_mode()
elif input_user_reset == 1:
    run = reset()    
