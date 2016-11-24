# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:59:03 2016

@author: jc
"""

import sys
import socket

sys.path.append('../')
from bibli import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("bord3l", 1111))

print("Envoyer des données")
file_name = input(">> ") # utilisez raw_input() pour les anciennes versions python
s.send(file_name.encode())
print s.recv(9999999)

s.close()