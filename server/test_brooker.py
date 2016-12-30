# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:14:30 2016

@author: jc
"""
#!/usr/bin/env python

import MySQLdb as mdb
import paho.mqtt.client as mqtt
import sys

## Définition des variables ---------------------------------------------------
serverName = "bord3l"
serverPort = 1883

## ----------------------------------------------------------------------------

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("etudeje/+")

def on_message(client, userdata, msg):
    print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
    fetchData(msg.topic.split('/')[-1], str(msg.payload))
    
    # Mise à jour de la base de donnees
def fetchData(camion, etiId):
    con = False
    print "INSERT INTO effectifs VALUES({data0}, {data1}, '{data2}', {data3});".format(data0 = str(NULL), data1 = int(camion), data2 = str("YoloSwag"), data3 = int(1))
    try:
        print "Etiquette :", etiId
        con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf');
        cur = con.cursor()
        cur.execute("SELECT id FROM outils WHERE ref='{ref}';".format(ref=str(etiId)))
        temp = cur.fetchone()
        print temp[0]
        return 0
    except mdb.Error, e:
      
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
        
    finally:    
            
        if con:    
            con.close()
    try:
        updateData(camion, temp[0])
    except:
        pass
    return 0
    
def updateData(camion, data):
    print data
    con = False
    try:
        con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf');
    
        cur = con.cursor()
        print "INSERT INTO effectifs VALUES({data0}, {data1}, '{data2}', {data3});".format(data0 = str(NULL), data1 = int(camion), data2 = str(data[0]), data3 = int(1))
        try:
            cur.execute("INSERT INTO effectifs VALUES({data0}, {data1}, '{data2}', {data3});".format(data0 = str(NULL), data1 = int(camion), data2 = str(data[0]), data3 = int(1)))
        except:
            pass
    except mdb.Error, e:
      
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
        
    finally:    
            
        if con:    
            con.close()
    return 0
    
def main():
    client = mqtt.Client()
    client.connect(serverName,serverPort,60)
    
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.loop_forever()
    
    sys.exit(0)

if __name__ == '__main__':
    
    main()
    print 'Terminé'