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
    print msg.topic.split('/')
    
    # Mise à jour de la base de donnees
def fetchData(camion, etiId):
    con = False
    try:
        con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf');
        cur = con.cursor()
        cur.execute("SELECT * FROM outils WHERE ref='{ref}';".format(ref=etiId))
        temp = cur.fetchone()
        updateData(camion, temp)
        return 0
    except mdb.Error, e:
      
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
        
    finally:    
            
        if con:    
            con.close()

    return 0
    
def updateData(camion, data):
    con = False
    try:
        con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf');
    
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO effectifs VALUES({data0}, '{data1}', '{data2}', '{data3}');".format(data0 = NULL, data1 = camion, data2 = data[0], data3 = 1))
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