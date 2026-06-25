#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:22:11 2026

@author: estanislaomolinas
"""

# Algoritmo 2.0 para determinar el valor a pagar en una factura con 20% de descuento.

# Ingresar el importe bruto con validación
while True:
    try:
        print("Ingrese el monto bruto de la factura:")
        factura = float(input("monto bruto: "))
        if factura < 0:
            print("El monto no puede ser negativo. Intentá de nuevo.\n")
            continue
        break
    except ValueError:
        print("Error: Ingresá un número válido.\n")

# Calculamos el 20% de descuento sobre el valor de la factura
desc = round(factura * 0.20, 2)
total = round(factura - desc, 2)

# Mostrar los resultados
print(f"Monto bruto: ${factura:.2f}")
print(f"Descuento aplicado: ${desc:.2f}")
print(f"Total a pagar: ${total:.2f}")