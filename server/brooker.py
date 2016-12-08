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
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if (msg.payload == "Hello world!"):
    print("Yes!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("192.168.1.35",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()


