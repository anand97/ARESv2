import serial
import datetime
import serial.tools.list_ports
import sys

#import pygame
#import graphics
import processor as proc

connected = 0
serial_port = ''
#ser = serial.Serial(serial_port, 115200)
prev = datetime.datetime.now()
current = datetime.datetime.now()
logger_enabled = False
temp = []
freq = []
valArray=[]

def read_volt():
    #with serial.Serial('/dev/ttyACM0', 9600) as ser:
    line = ser.readline().strip()
    valArray = line.split()
    
    while len(valArray)!=2:
        line = ser.readline().strip()
        valArray = line.split()
        
    try:
        #print(valArray)
        adc = [int(valArray[0]),int(valArray[1])]
        #adc = int(line)
        #ret = adc*5.0/1023
        #print(adc)#line #ret
        return adc
    except ValueError:
        print("Invalid number " + str(line))
        print(e)
        return [-1,-1]

def write_log(val):
    global log
    log.write(str(val[0])+"\t"+str(val[1])+"\n")

def open_log(comment):
    global log
    date = datetime.datetime.now()
    datestr = date.strftime('%Y%m%d_%H%M%S')
    log = open("../Logs/RawEMG_" + comment + "_" + datestr + ".txt","a")
    #log.write("Log created on " + str(date) + "\n")

def average(a):
    avg = sum(a)/len(a)
    return avg

def close():
    global ser, logger_enabled
    ser.close()
    if logger_enabled:
        log.close()
    

def main():
    global current,prev, connected, logger_enabled
    try:
        print("Hello")
        
        proc.setstart()
        print("Start Time Set!....")
        while connected:
            #print("running")
            value=read_volt()
            #print("read")
            proc.collect(value)
            if logger_enabled:
                write_log(value)
            #graphics.linedraw()
            
            current = datetime.datetime.now()
            
            #print(volt[-1])
            '''
            freq.append(1000000/(current-prev).microseconds)
            if len(freq)==10000:
                f = average(freq)
                print("Avg Frequency: %0.1fHz" % (f))
                del freq[:]
            prev=current
            '''


    except KeyboardInterrupt:
        close()
        print("\n" + "Bye")
        exit

def init():
    
    global connected, ser, serial_port
    
    ports = list(serial.tools.list_ports.comports())
    ports.reverse()
    for p in ports:
        #print(p)
        if "XDS110" in str(p): 
            if serial_port is '':
                serial_port = str(p).split()[0]
                print("MSP: "+ serial_port)
                break
    input()
    try:
        ser = serial.Serial(serial_port, 115200)
        connected = 1
        #print(connected)
        ser.flushInput()
        ser.flushOutput()
        if logger_enabled:
            comment = input("Test Comment?:- ")
            open_log(comment)
        main()
    except serial.SerialException:
        print("No device at" + serial_port)
        exit

init()