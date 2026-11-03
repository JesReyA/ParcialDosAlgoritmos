#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:59:08 2026

@author: Alexander
"""

class Nodo:
    def __init__(self,datos,hijos=None):
        self.datos=datos
        self.hijos=hijos
        self.padre=None
    def set_hijos(self,hijos):
        self.hijos=hijos
        if(self.hijos!=None):
            for hij in self.hijos:
                hij.padre=self
    def get_hijos(self):
        return self.hijos
    def get_padre(self):
        return self.padre
    def set_padre(self,padre):
        self.padre=padre
    def set_datos(self,datos):
        self.datos=datos
    def get_datos(self):
        return self.datos
    def igual(self,nodo):
        if(self.get_datos()==nodo.get_datos()):
            return True
        else:
            return False
    def en_lista(self,lista_nodos):
        esta_en_lista=False
        for n in lista_nodos:
            if self.igual(n):
                esta_en_lista=True
        return esta_en_lista
    def __str__(self):
        return str(self.get_datos())

cambios=[
    ("cambio_cero_uno",     0,1),
    ("cambio_uno_dos",      1,2),
    ("cambio_dos_tres",     2,3),
    ("cambio_tres_cuatro",  3,4),
    ("cambio_cuatro_cinco", 4,5),
]
def busqueda_amplitud(estado_inicial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_pendientes=[]
    nodoInicial=Nodo(estado_inicial)
    nodos_pendientes.append(nodoInicial)
    while((not solucionado) and (len(nodos_pendientes)!=0)):
        nodo=nodos_pendientes.pop(0)
        #estraer el nodo y se agrega a visitando
        nodos_visitados.append(nodo)
        if(nodo.get_datos()==solucion):
            solucionado=True
            return nodo
        else:
            dato_nodo=nodo.get_datos()
            hijos=[]
            for nombre,a,b in cambios:
                hijo=dato_nodo[:]
                hijo[a], hijo[b]= hijo[b],hijo[a]
                nuevo=Nodo(hijo)
                if((not nuevo.en_lista(nodos_pendientes)) and
                   (not nuevo.en_lista(nodos_visitados))):
                    nodos_pendientes.append(nuevo)
                hijos.append(nuevo)
            nodo.set_hijos(hijos)
            
if __name__=="__main__":
    estado_inicial=[3,6,1,4,2,5]
    solucion=[1,2,3,4,5,6]
    nodo_solucion=busqueda_amplitud(estado_inicial,solucion)
    #resultados
    resultado=[]
    nodo=nodo_solucion
    while(nodo.get_padre()!=None):
        resultado.append(nodo.get_datos())
        nodo=nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)