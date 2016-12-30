# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:35:20 2016

@author: jc
"""

from subprocess import Popen, PIPE
from multiprocessing import Process, active_children
import os
import paho.mqtt.client as mosquitto
import sys

#os.chdir("/home/jc/Documents/EtudeJE/dev/skyetek-c-api-for-linux/Examples/linux/")



def read():
    try:
        proc = Popen(["./example"],stdout=PIPE)
        proc.wait()
        recep = proc.stdout.readline()
        if recep != "NTR\n":
            print recep.split('\n')[0]
            return recep.split('\n')[0]
    except:
        return ''
def scan(l):
    print "Nombre d'itération",l
    temp = []
    for i in range(0,l):
        print "Tour ",i
        red = read()
        if red != None:
            temp.append(red)
    temp = list(set(temp))
    print temp
    return temp
    
def publish(temp):
    # Connexion au broker mqtt
    mqttc = mosquitto.Client()
    mqttc.connect("bord3l", 1883)
    
    for element in temp:
        mqttc.publish("etudeje", element)
        mqttc.loop(2)
    return 0
    
def main(l):
    os.chdir("../../")
    proces = Process(target=lambda : scan(l))
    proces.start()
    proces.join()
    
if __name__ == '__main__':
    try:
#        l = 60
#        main(l)
        print "Envoi en cours"
        publish(['yolo','test'])
        print "Elements envoyés"
        sys.exit(0)
    except KeyboardInterrupt:
        print '\nInterrupted'
        try:
            for child in active_children():
                print child
                child.terminate()
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    print "terminé"