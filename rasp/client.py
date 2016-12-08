# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:59:03 2016

@author: jc
"""
import paho.mqtt.client as mosquitto

mqttc = mosquitto.Client("python_pub")


mqttc.connect("192.168.43.235", 1883)
mqttc.publish("hello/world", "Hello, World!")
mqttc.loop(2) 

