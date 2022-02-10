import sys
import threading
from dialog import errorMain
from updateData import updateData

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run	
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:   
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

    def func():
        while True:
            print('thread running')

    def readData(self,message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice):
        try:
            hello = updateData(message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice)
            hello.getData()
        except:
            empty = ""

    def dataUpdate(self,message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice):
        try:
            niftyTable = updateData(message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice)
            niftyTable.dataUpdate(message)
        except:
            empty = ""

    def dataUpdate2(self,message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice):
        try:
            bankniftyTable = updateData(message,niftyTable,bankniftyTable,niftyPrice,bankniftyPrice)
            bankniftyTable.dataUpdate2(message)
        except:
            empty = ""