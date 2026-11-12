#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 01:30:46 2026

"""
import matplotlib.pyplot as plt

class PuntoCoordenadas:
    def __init__(self, etiqueta,coordenadax, coordenaday):
        self.etiqueta = etiqueta
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday
    
    def __repr__(self):
        return f"{self.etiqueta} = ({self.coordenadax}, {self.coordenaday})"
    
    def graficar(lista):
        for i in lista:
            plt.scatter(i.coordenadax, i.coordenaday)
            plt.text(i.coordenadax + 0.1, i.coordenaday + 0.1, i.etiqueta)
        plt.title("Coordenadas")
        plt.xlabel("Eje x")
        plt.ylabel("Eje y")
        plt.grid(True)
        plt.show()