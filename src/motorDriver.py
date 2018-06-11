import serial


serial_port = ''
i = 0
speedSetting = '255' # 0 -> 255
def init():
    try:
        global serial_port,arduino
        #arduino = serial.Serial(serial_port, 9600)
        #connected = 1
        #print(connected)
        
        ports = list(serial.tools.list_ports.comports())
        ports.reverse()
        for p in ports:
            #print(p)
            if "XDS110" not in str(p): 
                serial_port = str(p).split()[0]
                print("Arduino:"+ serial_port + str(p))
                break
        arduino = serial.Serial(serial_port, 115200)
        
        arduino.flushInput()
        arduino.flushOutput()
        '''
        if logger_enabled:
            comment = input("Test Comment?:- ")
            open_log(comment)
        '''
        msg = b'0:0;'
        arduino.write(msg)
    except serial.SerialException:
        print("No arduino at" + serial_port)
        exit

def commandMotor(command):
    global i
    if command is 1: #UP
        direction = '1'
        
    elif command is 0: #DOWN
        direction = '0'
    
    arduino.flushOutput()
    send_data(direction)
    
def send_data(dir):
    global arduino, speedSetting
    msg=dir.encode()+b':'+speedSetting.encode()+b';'
    #print(msg)
    arduino.write(msg)
    
init()
'''
while True:
    string=input("Enter: ")
    print(string)
    commandMotor(int(string))
'''
    