#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:59:25 2026

@author: j
"""

class Nodo:
    def __init__(self, coordenaday_punto, punto_referenciado):
        self.hijo_izquierdo = None                   #Puntero al hijo del nodo
        self.hijo_derecho = None                      #Puntero al hijo del nodo
        
        self.coordenaday_punto = coordenaday_punto           #Coordenada guardada de cada punto que se compara
        self.punto_referenciado = punto_referenciado          #Referencia al punto completo del cual pertenece la coordenada, servirá para mencionar exactamente a cuales se domina
        self.altura = 1                                       #Se usará al momento del balanceo del arbol, además de en la parte de sweep line
        