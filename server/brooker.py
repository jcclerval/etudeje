# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:14:30 2016

@author: jc
"""
#!/usr/bin/env python

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("etudeje")

def on_message(client, userdata, msg):
    print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
    
    # Mise à jour de la base de donnees
    con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf')
    data = []
    cur.execute("INSERT INTO outils VALUES({data0}, {data1},{data2},{data3},{data5});".format(data0 = data[0], data1 = data[1], data2 = data[2], data3 = data[3], data4 = data[4]))
    con.close()
    
client = mqtt.Client()
client.connect("192.168.1.35",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()


