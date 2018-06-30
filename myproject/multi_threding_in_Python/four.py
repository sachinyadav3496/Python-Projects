import threading
from random import randint
import time

class MyWork(threading.Thread):
    def __init__(self,threadName,num):
        threading.Thread.__init__(self)
        self.num = num
        self.threadName = threadName
    def run(self):
        print("\n\n",threading.activeCount())
        print(threading.currentThread())
        print(threading.enumerate())
        print("Starting Thread {} ".format(self.threadName))
        self.squre()
        print("Ending Thread {} ".format(self.threadName))
    def squre(self):
        for var in range(self.num,0,-1):
            print("\nHey I am Thread\n",self.threadName,"Squre of {} is {}".format(var,var**2))
            time.sleep(randint(1,5))

a = MyWork('THREAD1',5)
b = MyWork('THREAD2',4)
c = MyWork('THREAD1',6)
d = MyWork('THREAD1',3)
b.start()
a.start()
c.start()
d.start()
a.join()
b.join()
c.join()
d.join()
