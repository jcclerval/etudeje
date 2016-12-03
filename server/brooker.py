# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:14:30 2016

@author: jc
"""
#import paho.mqtt.client as mqtt
# Brooker


#
#print "Début de la boucle"
#
## Si on a quelque chose On met à jour la base de données
#
#import pynotify
#import mosquitto
#
## The callback for when the client receives a CONNACK response from the server.
#def on_connect(rc):
#    print("Connected with result code "+str(rc))
#
#    # Subscribing in on_connect() means that if we lose the connection and
#    # reconnect then subscriptions will be renewed.
#
#    print "test"
#
## The callback for when a PUBLISH message is received from the server.
##def on_message(client, userdata, msg):
##    print(msg.topic+" "+str(msg.payload))
##    print "test"
#def on_message(msg):
#    print msg
#    n = pynotify.Notification(msg.topic, msg.payload)
#    n.show ()
#
##create a broker
#mqttc = mosquitto.Mosquitto("python_sub")
#
##define the callbacks
#mqttc.on_message = on_message
#mqttc.on_connect = on_connect
#
##connect
#mqttc.connect("localhost", 1883, 60, True)
#
##subscribe to topic test
#mqttc.subscribe("hello/world", 2)
#
#print "Suscribed"
##keep connected to broker
#while mqttc.loop() == 0:
#    pass
#print "test"




import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print "Connected with result code " + str(rc)
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
    client.subscribe("hello/world")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Topic: ", msg.topic+"\nMessage: "+str(msg.payload)

client = mqtt.Client("python_sub")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.43.235", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
print "Entrée dans la boucle"
client.loop_forever()