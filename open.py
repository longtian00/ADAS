#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import os
import schedule
import psutil



    
def openclose():
    os.startfile("new 2.bat")
    time.sleep(10)
    for process in psutil.process_iter():
        if process.name() == "notepad.exe":
            os.system("taskkill /im " + str(process.pid))
            counter = 0;

def repeat():
    for i in range(3):
        print ("open")
        openclose()

schedule.clear()
schedule.every().day.at("11:35").do(repeat)




while True:
    schedule.run_pending()
    



