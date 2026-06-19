#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:54:21 2026

@author: estanislaomolinas
"""

def main():
    fp = open('datos.txt', 'r', encoding='utf8')
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if(len(datosCliente) == 2):
            dni = int(datosCliente[0].strip())
            edad = int(datosCliente[1].strip())
            print(f"DNI: {dni} Edad: {edad}")
    fp.close()

if __name__ == '__main__':
    main()