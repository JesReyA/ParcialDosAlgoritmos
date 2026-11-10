#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:59:08 2026

@author: Alexander
"""

from busqueda import busqueda_amplitud, reconstruir_camino


def main():
    estado_inicial = [3, 6, 1, 4, 2, 5]
    solucion = [1, 2, 3, 4, 5, 6]

    nodo_solucion = busqueda_amplitud(estado_inicial, solucion)

    if nodo_solucion is None:
        print("No se encontró solución.")
        return

    print(reconstruir_camino(nodo_solucion, estado_inicial))


if __name__ == "__main__":
    main()