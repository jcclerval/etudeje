# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:39:01 2016

@author: jc
"""

import Tkinter as tk
impot sys


class Interface(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.pack()
        
        # Création de la frame de boutons
        self.mainFrame = tk.Frame(self)
        self.mainFrame.pack(side="left")
        self.frame1 = tk.Frame(self.mainFrame)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.mainFrame)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.mainFrame)
        self.frame3.pack()
        self.frame4 = tk.Frame(self.mainFrame)
        self.frame4.pack()
        self.frame5 = tk.Frame(self.mainFrame)
        self.frame5.pack()
        
        # Cration des boutons
        
        # Nom de l'outil
        self.toolName = tk.StringVar()
        self.toolName.Set('')
        tk.Label(self.frame1, text="Entrez le nom de l'outil").pack(side="left")
        tk.Entry(self.frame1, textvariable=self.toolName).pack()
        
        # 
if __name__ == '__main__':
    root = tk.tk()
    inter = Interface(root)
    
    root.mainloop()
    sys.exit(0)
        