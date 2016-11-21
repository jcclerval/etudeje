# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:59:03 2016

@author: jc
"""

import sys
import socket

sys.path.append('../')
from bibli import *
hote = "bord3l"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

print "Création de l'objet"
cat = 'tournevis'
id='35435435'

item = Item(cat,id)

socket.send(item)



print "Close"
socket.close()