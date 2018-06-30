import threading
import time

class MyWork(threading.Thread):
    def __init__(self,threadID,threadName,Counter,sleep):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.threadName = threadName
        self.counter = Counter
        self.s = sleep
    def run(self):
        print("Starting Thread {} which has id {}".format(self.threadName,self.threadID))
        self.hello()
        print("Ending Thread {} which has id {}".format(self.threadName,self.threadID))
    def hello(self):
        for var in range(self.counter):
            print("\nHey I am Thread\n",self.threadName)
            time.sleep(self.s)

a = MyWork(1,'THREAD1',10,2)
b = MyWork(2,'THREAD2',6,3)

a.start()
b.start()

a.join()
b.join()
