import pygame,sys,math
from pygame.locals import *
from time import sleep
#import test

WHITE=(255,255,255)
BLUE=(0,0,255)
l2=500 #Lower arm
l1=300 #Upper Arm
shoulder=(950,300)
angle1=45 #shoulder
angle2=0 #elbow
'''
class graphics (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        init()
            
    def run(self, angle):
        print ("Starting " + self.name)
        linedraw(angle) 
            
        print ("Exiting " + self.name)
'''     
def rotate(ang1,ang2):
    
    x1=shoulder[0]-(l1*math.cos(math.radians(-ang1)))
    y1=shoulder[1]-(l1*math.sin(math.radians(-ang1)))
    
    x2=x1-(l2*math.cos(math.radians(ang2-ang1)))
    y2=y1-(l2*math.sin(math.radians(ang2-ang1)))
    
    
    return (x1,y1,x2,y2)

def init():
    pygame.init()

    global DISPLAY, l1, x1, y1
    DISPLAY=pygame.display.set_mode((1000,1000),0)
    
    
#    angle=0
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

    #print("Hello")
    

def linedraw(angle2):
    #init()
    #pygame.draw.line(DISPLAY,blue,(0,0),(100,50), 5)
    #i=1
    global DISPLAY, angle, l1, x1, y1
    
    DISPLAY.fill(WHITE)
    
    (x1,y1,x2,y2)=rotate(angle1,angle2)
    #print(x1,y1,x2,y2)
    #pygame.draw.circle(DISPLAY,BLUE,(x1,y1),l1, 5)
    pygame.draw.line(DISPLAY,BLUE,shoulder,(x1,y1), 5)
    pygame.draw.line(DISPLAY,BLUE,(x1,y1),(x2,y2), 5)
    pygame.display.update()
    
        #sleep(.0001)

#if __name__ == '__linedraw__':
#linedraw()
