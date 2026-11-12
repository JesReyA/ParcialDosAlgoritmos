#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:00:37 2026

@author: erikazr
"""
import logica_puntos
from punto_coordenadas import PuntoCoordenadas
from arbol_avl import ArbolAVL

punto_A = PuntoCoordenadas("A", 2, 3)
punto_B = PuntoCoordenadas("B", 5, 4)
punto_C = PuntoCoordenadas("C", 1, 8)
punto_D = PuntoCoordenadas("D", 7, 2)
punto_E = PuntoCoordenadas("E", 8, 8)
punto_F = PuntoCoordenadas("F", 3, 6)
punto_G = PuntoCoordenadas("G", 6, 7)
punto_H = PuntoCoordenadas("H", 4, 1)
punto_I = PuntoCoordenadas("I", 9, 5)
punto_J = PuntoCoordenadas("J", 10,9)
punto_K = PuntoCoordenadas("K", 2, 7)
punto_L = PuntoCoordenadas("L", 5, 2)
punto_M = PuntoCoordenadas("M", 7, 6)
punto_N = PuntoCoordenadas("N", 4, 5)
punto_O = PuntoCoordenadas("O", 8, 3)

lista_puntos=[]
lista_puntos.append(punto_A)
lista_puntos.append(punto_B)
lista_puntos.append(punto_C)
lista_puntos.append(punto_D)
lista_puntos.append(punto_E)
lista_puntos.append(punto_F)
lista_puntos.append(punto_G)
lista_puntos.append(punto_H)
lista_puntos.append(punto_I)
lista_puntos.append(punto_J)
lista_puntos.append(punto_K)
lista_puntos.append(punto_L)
lista_puntos.append(punto_M)
lista_puntos.append(punto_N)
lista_puntos.append(punto_O)

print(lista_puntos)

lista_ordenada = logica_puntos.ordenar_puntos(lista_puntos)

print(lista_ordenada)

print("---------------------------------------")


arbol = ArbolAVL()
arbol.imprimir_rangos_punto(lista_ordenada)
PuntoCoordenadas.graficar(lista_ordenada)



