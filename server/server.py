#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:58:23 2016

@author: jc
"""
import MySQLdb as mdb
import sys

import socket
import threading

sys.path.append('../')
from bibli import *

def connect(message):
    con = False
    try:
        con = mdb.connect(host='localhost', user='root', passwd='jcclerval', db='u925639974_grdf');
    
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
    
        ver = cur.fetchone()
        
        print "Database version : %s " % ver
        
        cur.execute("SELECT * FROM centres")
        print cur.fetchone()
        
        print "Message :",message
        data = message.split("//")
        
        try:
            cur.execute("INSERT INTO outils VALUES({data0}, {data1},{data2},{data3},{data5});".format(data0 = data[0], data1 = data[1], data2 = data[2], data3 = data[3], data4 = data[4]))
        except:
            pass
    except mdb.Error, e:
      
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
        
    finally:    
            
        if con:    
            con.close()
    return 0
    


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048)
        self.clientsocket.send("Yolo : "+r)
        connect(r)
        print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
stock.close()

