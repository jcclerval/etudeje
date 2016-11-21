#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:58:23 2016

@author: jc
"""
import sys
import socket

sys.path.append('../')
from bibli import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print "{} connected".format( address )

        response = client.recv(255)
        if response != "":
                print response
                try:
                    read(response).display()
                except:
                    pass
print "Close"
client.close()
stock.close()