# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:35:20 2016

@author: jc
"""

from subprocess import Popen, PIPE
from multiprocessing import Process
import os
import paho.mqtt.client as mosquitto

#os.chdir("/home/jc/Documents/EtudeJE/dev/skyetek-c-api-for-linux/Examples/linux/")



def read():
    proc = Popen(["./example"],stdout=PIPE)
    i = 1
    temp = []
    print "Yolo :",proc.stdout.readline()
    print "Yolo :",proc.stdout.readline()
    print "Yolo :",proc.stdout.readline()

    while i < 100:
        try:
            recep = proc.stdout.readline()
            if recep != "NTR\n":
                temp.append(recep.split('\n')[0])
                print i, recep
        except:
            pass
        print i
        i = i + 1
    temp = list(set(temp))
    print temp
    ## Connexion au broker mqtt
    mqttc = mosquitto.Client()
    
    for element in temp:
        
    proc.wait()
    print "Proc mort"
    return 0
    
if __name__ == '__main__':
    os.chdir("../../")
    proces = Process(target=read)
    proces.start()
    

    print "terminé"