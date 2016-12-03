# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:35:20 2016

@author: jc
"""

from subprocess import Popen, PIPE
from multiprocessing import Process
import os

os.chdir("/home/jc/Documents/EtudeJE/dev/skyetek-c-api-for-linux/Examples/linux/")



def read():
    proc = Popen(["./example"],stdout=PIPE)
    i = 0
    while i < 10:
        try:
            print proc.communicate()[0]
            i += 1
        except:
            pass
    return 0
    
if __name__ == '__main__':
    os.chdir("/home/jc/Documents/EtudeJE/dev/skyetek-c-api-for-linux/Examples/linux/")
    proces = Process(target=read)
    proces.start()
    
    proces.join(10)
    print "terminé"