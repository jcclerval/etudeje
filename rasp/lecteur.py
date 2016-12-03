# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:12:54 2016

@author: jc
"""
#
#import subprocess
#
## Script permettant de lancer un scan et envoyer les données au brooker
#
#tuyau_in, tuyau_out = subprocess.Pipe()
## Lancer le subprocess avec le code en C

"""
import pynotify
import mosquitto

#define what happens after connection
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#create a broker
mqttc = mosquitto.Mosquitto("python_pub")

mqttc.on_message = on_message
mqttc.on_connect = on_connect


#define the callbacks

mqttc.connect("192.168.43.235", 1883)
mqttc.publish("hello/world", "Hello, World!")
"""

import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")

mqttc.connect("192.168.43.235", 1883)
mqttc.publish("hello/world", "Hello, World!")
mqttc.loop(2)