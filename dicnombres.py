#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:18:29 2026

@author: estanislaomolinas
"""
def main():
    dicNombres = {}
    fp = open('nombres.txt', 'r', encoding='utf8')
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if len(datosCliente) == 2:
            dni = int(datosCliente[0].strip())
            nombre = datosCliente[1].strip()
            dicNombres.update({dni: nombre})
    fp.close()

    for vDni in dicNombres.keys():
        nom = dicNombres[vDni]
        print(f"DNI: {vDni} - Nombre: {nom}")

if __name__ == '__main__':
    main()