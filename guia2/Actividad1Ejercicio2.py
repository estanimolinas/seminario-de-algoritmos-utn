#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 18:15:06 2026

@author: estanislaomolinas
"""

class persona:
    
    def __init__(self, dni, nom):
        self._dni = int(dni)   
        self._nom = nom

    def getDNI(self):
        return self._dni

    def getNombre(self):
        return self._nom

    def __str__(self):
        return f"{self._dni:8d} | {self._nom}"

class promotor(persona):
    def __init__(self, dni, nom):
        super().__init__(dni, nom) 
        self._clientes = [] 
    def addCliente(self, cli):
        self._clientes.append(cli)
    def getCntClientes(self):
        return len(self._clientes)
    def getClientes(self):
        return self._clientes
    def __str__(self):
        return self._nom
    def ordenarClientes(self): 
        self._clientes = self._ordenar_quickSort(self._clientes)
    def _ordenar_quickSort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [c for c in lista[1:] if c.getDNI() <= pivote.getDNI()]
        mayores = [c for c in lista[1:] if c.getDNI() > pivote.getDNI()]
        return self._ordenar_quickSort(menores) + [pivote] + self._ordenar_quickSort(mayores)
    def buscarCliente(self, dni):
        izq = 0
        der = len(self._clientes) - 1
        while izq <= der:
            mid = (izq + der) // 2
            if self._clientes[mid].getDNI() == dni:
                return self._clientes[mid]
            elif self._clientes[mid].getDNI() < dni:
                izq = mid + 1
            else:
                der = mid - 1
        return None

class cliente(persona):

    def __init__(self, dni, nom, prom, tipo_seguro):
        super().__init__(dni, nom)       
        self._promotor = prom            
        self._seguros = [tipo_seguro]    


    def getPromotor(self):
        return self._promotor

    def addTipoSeguro(self, seguro):
        self._seguros.append(seguro)

  
    def getSeguros(self):
        return self._seguros


def main():
    prom = promotor(24317128, "Diego de la Vega") 
    with open("/Users/estanislaomolinas/algoritmos/clientespoo.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue
            partes = linea.split(";")
            dni = partes[0].strip()
            nom = partes[1].strip()
            seguros = partes[2].strip().split("|")
            cli = cliente(int(dni), nom, prom, seguros[0].strip())
            for s in seguros[1:]:
                cli.addTipoSeguro(s.strip())
            prom.addCliente(cli)

    prom.ordenarClientes()
    

    print(f"{prom}")
    print("Listado de clientes:")
    for cli in prom.getClientes():
        print(f"{cli}")
    
    
    dni_buscar = int(input("Ingresá un DNI (0 o negativo para salir): "))
    while dni_buscar > 0:
        resultado = prom.buscarCliente(dni_buscar)
        if resultado is not None:
            print(f"{resultado}")
            print("Productos contratados:")
            for s in resultado.getSeguros():
                print(f"\t {s}")
        else:
            print("No se encontró un cliente con ese DNI.")
        dni_buscar = int(input("Ingresá un DNI (0 o negativo para salir): "))

main()