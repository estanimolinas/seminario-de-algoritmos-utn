#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:27:54 2026

@author: estanislaomolinas
"""

# POO para resolver listado de calificaciones de una materia
class Estudiante:
    """ representa a un estudiante que tomo los 3 examenes de la materia """
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    def obtener_condicion(self):
        if self.nota1 >= 6 and self.nota2 >= 6 and self.nota3 >= 6:
            return "aprobacion_directa"
        elif self.nota1 >= 4 and self.nota2 >= 4 and self.nota3 >= 4 and (self.nota1 + self.nota2 + self.nota3) * 1/3 >= 6:
            return "aprobacion_indirecta"
        else:
            return "no_aprobado"

# diccionario de estudiantes
estudiantes = {
    "aprobacion_directa": [],
    "aprobacion_indirecta": [],
    "no_aprobado": []
}

def main():
    while True:
        nombre = input("Ingresa el nombre del estudiante: ")
        if nombre == "fin":
            break
        
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        
        estudiante = Estudiante(nombre, nota1, nota2, nota3)
        condicion = estudiante.obtener_condicion()
        estudiantes[condicion].append(estudiante)
    
    # Mostrar resultados
    for condicion in estudiantes:
        print(f"\n--- {condicion} ---")
        for estudiante in estudiantes[condicion]:
            print(estudiante.nombre)

if __name__ == "__main__":
    main()
    
# Reflexion

"""Dominio del problema:
Un estudiante en este contexto es una entidad que encapsula tres datos: nombre y tres notas numéricas.
A partir de esos datos, el estudiante puede clasificarse en una de tres categorías según reglas de aprobación.

Decisiones de diseño:

1. Clase Estudiante:
   Atributos: nombre, nota1, nota2, nota3
   Método obtener_condicion(): Evalúa las tres notas contra las reglas de aprobación y devuelve un string.
   Esta separación permite que el profesor sepa la condicion de cada estudiante..

2. Diccionario de clasificación:
   En lugar de hacer tres listas separadas, usé un diccionario con claves que coinciden con los resultados de obtener_condicion().
   Esto permite agregar directamente cada estudiante a su categoríi sin necesidad de recorrer tres veces.

3. Loop de entrada:
   Usé while True con break cuando nombre == "fin".
   Esto es natural para un problema donde no se sabe a priori cuántos estudiantes habrá.

4. Mostrar resultados:
   Dos loops for anidados: uno recorre las condiciones, otro recorre los estudiantes en cada categoría.
   Esto es más limpio que hardcodear tres prints separados.

Aprendizajes principales:
- La POO permite modelar entidades del mundo real (un estudiante) de forma natural.
- Los métodos encapsulan lógica que pertenece a la entidad.
- Las estructuras de datos (diccionarios) se eligen según cómo se vayan a usar después.
"""
    
    
    