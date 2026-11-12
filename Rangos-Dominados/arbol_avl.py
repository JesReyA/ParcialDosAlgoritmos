#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:21:30 2026

@author: j
"""
from nodo_arbol import Nodo
from punto_coordenadas import PuntoCoordenadas

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        
    def obtener_altura(self, nodo):
        return 0 if(nodo) == None else nodo.altura
    
    def factor_balance(self, nodo):
        return 0  if (nodo) == None else self.obtener_altura(nodo.hijo_izquierdo) - self.obtener_altura(nodo.hijo_derecho)
    
    
    def rotacion_izquierda(self, nodo):
        nuevo_nodo_raiz = nodo.hijo_derecho             #Variable para guardar el nodo que subirá
        
        nodo_intercambiable_guardado = nuevo_nodo_raiz.hijo_izquierdo  #Variable necesaria para guardar el nodo de forma temporal
    
        nuevo_nodo_raiz.hijo_izquierdo = nodo           #El hijo izquierdo del nodo raíz ahora es todo todo lo que esta a la izquierda del raiz anterior, incluido este
        
        nodo.hijo_derecho = nodo_intercambiable_guardado        #El hijo derecho del subarbol izquierdo es el nodo que se guardó para no perderse
        
        #Se calculan las alturas de los subarboles modificados y se suma uno por el nodo actual que se toma en cuenta
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijo_izquierdo),self.obtener_altura(nodo.hijo_derecho))
        nuevo_nodo_raiz.altura = 1 + max(self.obtener_altura(nuevo_nodo_raiz.hijo_izquierdo),self.obtener_altura(nuevo_nodo_raiz.hijo_derecho))
        
        #Se retorna el nodo que se ha modificado o subido para ser el nuevo
        return nuevo_nodo_raiz
    
    
    
    def rotacion_derecha(self, nodo):
        nuevo_nodo_raiz = nodo.hijo_izquierdo            #Variable para guardar el nodo que subirá
        
        nodo_intercambiable_guardado = nuevo_nodo_raiz.hijo_derecho  #Variable necesaria para guardar el nodo de forma temporal
    
        nuevo_nodo_raiz.hijo_derecho = nodo           #El hijo derecho del nodo raíz ahora es todo todo lo que esta a la derecha del raiz anterior, incluido este
        
        nodo.hijo_izquierdo = nodo_intercambiable_guardado        #El hijo izquierdo del subarbol derecho es el nodo que se guardó para no perderse
        
        #Se calculan las alturas de los subarboles modificados y se suma uno por el nodo actual que se toma en cuenta
        nodo.altura = 1 + max(self.obtener_altura(nodo.hijo_izquierdo),self.obtener_altura(nodo.hijo_derecho))
        nuevo_nodo_raiz.altura = 1 + max(self.obtener_altura(nuevo_nodo_raiz.hijo_izquierdo),self.obtener_altura(nuevo_nodo_raiz.hijo_derecho))
        
        #Se retorna el nodo que se ha modificado o subido para ser el nuevo
        return nuevo_nodo_raiz
    
    
        
    #Método para realizar las inserciones en el árbol
    def insertar(self, punto):
        self.raiz  = self._insertar_nodos(self.raiz, punto)
            
    #Metodo recursivo de insercion
    def _insertar_nodos(self, nodo_actual, punto):
        #Caso base
        if (nodo_actual == None):
            return Nodo(punto.coordenaday, punto)
        else:
            #Si es menor se inserta en los nodos izquierdos, se llama de forma recursiva a la funcion para localizar su lugar
            if (punto.coordenaday <= nodo_actual.coordenaday_punto):
                nodo_actual.hijo_izquierdo = self._insertar_nodos(nodo_actual.hijo_izquierdo, punto)
            #Caso contrario se inserta del lado derecho
            else:
                nodo_actual.hijo_derecho = self._insertar_nodos(nodo_actual.hijo_derecho, punto)
            
            #Se obtiene la altura del nodo actual luego de las inserciones
            nodo_actual.altura = 1 + max(self.obtener_altura(nodo_actual.hijo_izquierdo),self.obtener_altura(nodo_actual.hijo_derecho))
            
            #se obtiene el factor de balance del nodo actual luego de cada insercion
            factor_balance_actual = self.factor_balance(nodo_actual)
            
            #Rotacion izquierda
            if(factor_balance_actual < -1 and self.factor_balance(nodo_actual.hijo_derecho) <= 0 ):
                return self.rotacion_izquierda(nodo_actual)
            
            #Rotacion derecha
            if(factor_balance_actual > 1 and self.factor_balance(nodo_actual.hijo_izquierdo) >= 0 ):
                return self.rotacion_derecha(nodo_actual)
            
            #Rotacion derecha-izquierda
            if(factor_balance_actual < -1 and self.factor_balance(nodo_actual.hijo_derecho) >= 0 ):
                nodo_actual.hijo_derecho = self.rotacion_derecha(nodo_actual.hijo_derecho)
                return self.rotacion_izquierda(nodo_actual)
            
            #Rotación izquierda-derecha
            if(factor_balance_actual > 1 and self.factor_balance(nodo_actual.hijo_izquierdo) <= 0 ):
                nodo_actual.hijo_izquierdo = self.rotacion_izquierda(nodo_actual.hijo_izquierdo)
                return self.rotacion_derecha(nodo_actual)
            
            return nodo_actual
        
        
        
    #Imprimir 
    def imprimir_in_order(self):
        self._recorrido_in_order_recursivo(self.raiz)
        
    #Método para recorrer todo el arbol AVL para imprimir desde menores hasta los mayores.
    def _recorrido_in_order_recursivo (self, nodo_actual):
        if nodo_actual != None:
            #Va al hijo izquierdo (Menor)
            self._recorrido_in_order_recursivo(nodo_actual.hijo_izquierdo)
            #Imprime el dato del nodo central
            print(f"Y:{nodo_actual.coordenaday_punto}  | {nodo_actual.punto_referenciado.etiqueta}")
            #Va al hijo derecho(Mayor)
            self._recorrido_in_order_recursivo(nodo_actual.hijo_derecho)
            
    #Método para obtener los dominados (cantidad y cuales)
    def obtener_rangos(self, coordenaday):
        lista_dominados = []
        self._obtener_rangos_recursivo(self.raiz, coordenaday, lista_dominados)
        return f"Cantidad Dominados = {len(lista_dominados)} \n Dominados = {lista_dominados}"
        
    def _obtener_rangos_recursivo(self, nodo_actual, coordenaday, lista):
        if nodo_actual == None:
            return 
        else:
            if coordenaday > nodo_actual.coordenaday_punto:
                self._obtener_rangos_recursivo(nodo_actual.hijo_izquierdo, coordenaday, lista)
                lista.append(nodo_actual.punto_referenciado.etiqueta) 
                self._obtener_rangos_recursivo(nodo_actual.hijo_derecho,coordenaday, lista)
                
            else:
                self._obtener_rangos_recursivo(nodo_actual.hijo_izquierdo, coordenaday, lista)
                
    def imprimir_rangos_punto(self, lista):
        for i in lista:
            print(i)
            print(self.obtener_rangos(i.coordenaday))
            self.insertar(i)
                
                