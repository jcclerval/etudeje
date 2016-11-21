# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:03:26 2016

@author: jc
"""

# Bibliothèque de fonctions pour l'étude JE


class Item:
    def __init__(self, cat, id):
        self.cat = cat
        self.id = id
    def display(self):
        print "Objet de catégorie : {categorie}, d'identifiant : {id}".format(categorie=self.cat,id = self.id)
        return 0
    def send(self):
        return str(self.cat)+"//"+str(self.id)

def read(message):
    try:
        temp = message.split('//')
        return Item(temp[0],temp[1])
    except:
        return 0
        
        
if __name__ == '__main__':
    cat = 'tournevis'
    id='35435435'
    
    item = Item(cat,id)
    item.display()
    
    print "fin"