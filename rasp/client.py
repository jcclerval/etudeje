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

id = 5
nom = 'cle à pipe'
ref = 'YoloSwag'
nbrMin = 20
photo = 'cle.jpg'

data = [id, nom, ref, nbrMin, photo]


s.send("//".join(data))
print "Donénes envoyées"

s.close()