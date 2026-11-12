#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:11:26 2026

@author: j
"""
import random as rn

def ordenar_puntos(lista):

    if(len(lista) <= 1):
        return lista
    else:
        indice_pivote = rn.randint(0, len(lista)-1)
        pivote = lista[indice_pivote]
        sobrante = lista[:indice_pivote] + lista[indice_pivote+1:]
        menores_pivote = [i for i in sobrante if (i.coordenadax, -i.coordenaday) <= (pivote.coordenadax, -pivote.coordenaday)]
        mayores_pivote = [i for i in sobrante if (i.coordenadax, -i.coordenaday) > (pivote.coordenadax, -pivote.coordenaday)]
        return ordenar_puntos(menores_pivote) + [pivote] + ordenar_puntos(mayores_pivote)
    