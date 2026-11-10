# -*- coding: utf-8 -*-
"""Algoritmo de búsqueda en amplitud y reconstrucción del camino."""

from nodo import Nodo
from operaciones import cambios


def busqueda_amplitud(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_pendientes = []
    nodoInicial = Nodo(estado_inicial)
    nodos_pendientes.append(nodoInicial)

    while (not solucionado) and (len(nodos_pendientes) != 0):
        nodo = nodos_pendientes.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            hijos = []
            for nombre, a, b in cambios:
                hijo = dato_nodo[:]
                hijo[a], hijo[b] = hijo[b], hijo[a]
                nuevo = Nodo(hijo)
                if (not nuevo.en_lista(nodos_pendientes)) and \
                   (not nuevo.en_lista(nodos_visitados)):
                    nodos_pendientes.append(nuevo)
                    hijos.append(nuevo)
            nodo.set_hijos(hijos)
    return None


def reconstruir_camino(nodo_solucion, estado_inicial):
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    return resultado