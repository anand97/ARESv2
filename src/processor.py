import numpy as np
import datetime as dt
import motorDriver as motor
import os

calib_done = False
starttime = dt.datetime.now()
current = dt.datetime.now()
i=0

class Muscle:
    correction=1
    def __init__(self, name):
        self.name=name
        self.dataset=[]
        
    def calib(self):
        avg=np.mean(self.dataset)
        std=np.std(self.dataset)
        self.thresh=avg+4*std  
        self.dataset=[]
  
    def eval(self):
        
        if len(self.dataset) > 20: #To obtain mean value of frames, each with 20 data points
            
            if np.mean(self.dataset)>self.thresh:
                #print(self.name+ " Active!")
                self.status=True
            else:
                #print(self.name + " Inactive!")
                self.status=False
            self.dataset=[]
        
            return (self.status,True)
        else:
            return (False,False)
    
    def threshold(self):
        return self.thresh
    
    def acquire(self, data):
        self.dataset.append(data)
        
muscle1=Muscle("Biceps")
muscle2=Muscle("Triceps")

def collect(val):
    #val.reverse()
    global calib_done
    
    if not calib_done:
        print("Calibration running.....")
        calibrate(val)
    
    else:
        muscle1.acquire(val[0])
        muscle2.acquire(val[1])
        (status1,flag) = muscle1.eval()
        (status2,flag) = muscle2.eval()
        if flag:
            command(status1,status2)
        
def calibrate(val):
    
    global calib_done,current,starttime
    current=dt.datetime.now()
    elapsed = (current-starttime).seconds
    
    if elapsed > 2: #after first 2 seconds
        muscle1.acquire(val[0])
        muscle2.acquire(val[1])
        
    print(elapsed)
    
    if elapsed>12: #10 seconds calibration time
        muscle1.calib()
        muscle2.calib()
        calib_done = True
        
        print("Calibration Complete. Thresholds Set as 1:"+ str(muscle1.thresh)+", 2:" + str(muscle2.thresh))
        '''
        print(type(muscle1.threshold()))
        print(muscle1.threshold())
        print(type(muscle2.threshold()))
        if int(muscle1.threshold()) not in range(200,650) or int(muscle2.threshold()) not in range(200,650):
            calib_status = input("Retry(r), Continue(c): ")
             
            if calib_status is 'r':
                starttime = dt.datetime.now()
                calib_done = False
        '''
        input()
        
def setstart():
    global starttime
    starttime = dt.datetime.now()
    #print(starttime

def command(status1,status2):
    global i
    if status1^status2: #Any one is Active
        if status1:     #Biceps is Active
            print("Up!")
            motor.commandMotor(1)
        else:           #Triceps is Active
            print("Down!")
            motor.commandMotor(0)
    else:               # Both or None are active
        print("Stay")
    
    i=i+1;
    if i is 100:
    #    os.system('clear')
        i=0
        
        
        
