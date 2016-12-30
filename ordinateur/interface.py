# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:39:01 2016

@author: jc
"""

import Tkinter as tk
import sys

## Définition des variables ---------------------------------------------------
serverName = "bord3l"
serverPort = 1883

## ----------------------------------------------------------------------------
def publish(temp):
    # Connexion au broker mqtt
    mqttc = mosquitto.Client()
    mqttc.connect(serverName, serverPort)
    
    if len(temp) == 3:
        mqttc.publish("etudeje/NouvelOutil/"+temp0+"/genre", temp1)
        mqttc.publish("etudeje/NouvelOutil/"+temp0+"/photo", temp2)
        
        mqttc.loop(2)
    return 0
    

class Interface(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.pack()
        
        # Création de la frame de boutons
        self.mainFrame = tk.LabelFrame(self)
        self.mainFrame.pack(side="left")
        self.frame1 = tk.Frame(self.mainFrame)
        self.frame1.pack(expand='true', fill='x')
        self.frame2 = tk.Frame(self.mainFrame)
        self.frame2.pack(expand='true', fill='x')
        self.frame3 = tk.Frame(self.mainFrame)
        self.frame3.pack(expand='true', fill='x')
        self.frame4 = tk.Frame(self.mainFrame)
        self.frame4.pack(expand='true', fill='x')
        self.frame5 = tk.Frame(self.mainFrame)
        self.frame5.pack(expand='true', fill='x')
        
        # Cration des boutons
        
        # Nom de l'outil
        self.toolName = tk.StringVar()
        self.toolName.set('')
        tk.Label(self.frame1, text="Entrez le nom de l'outil").pack(side="left")
        tk.Entry(self.frame1, textvariable=self.toolName).pack(anchor='w')
        # Boite de dialogue pour la photo
        # Plutot upload de la photo
        
        # Bouton Scanner
        tk.Button(self.frame4, text='Lancer un scan', command=self.scan).pack(anchor='w')
        # Bouton enregistrer
        tk.Button(self, text="Enregistrer l'outil", command=self.save).pack(anchor='w')
        # Bouton Quitter
        tk.Button(self.frame5, text='Quitter', command=self.quit).pack(anchor='w')
        
    def scan(self):
        # Checker les conditions avant de lancer un scan
        # Subprocess tout ca
        #if trop d'étiquettes ou pas d'étiquettes --> soucis
        return 0
        
    def save(self):
        # Upload de la photo
        toolName = self.toolName.get()
        etiquetteId = self.etiquetteId.get()
        photo = self.photo.get()
        publish([etiquetteId, toolName, photo])
        return 0
if __name__ == '__main__':
    root = tk.Tk()
    inter = Interface(root)
    
    root.mainloop()
    sys.exit(0)
        