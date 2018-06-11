import log,graphics
import threading,time


class main (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        print ("Starting " + self.name)
        while True: 
            print(self.name)
        print ("Exiting " + self.name)

if __name__ == '__main__':
    
    graphics.init()
    
    thread1 = main(1, "Thread-1")
    thread2 = graphics(2, "Thread-2")
    thread1.start()
    thread2.start()

