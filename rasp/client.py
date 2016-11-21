# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:59:03 2016

@author: jc
"""


import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(u"Hey my name is Olivier!")

print "Close"
socket.close()