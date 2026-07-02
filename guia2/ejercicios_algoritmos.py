#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EJERCICIOS DE PRÁCTICA - ALGORITMOS UTN
Desde programación estructurada hasta TDA y análisis de algoritmos.
Completá cada ejercicio donde dice # TU CÓDIGO ACÁ
"""

# ============================================================
# BLOQUE 1 - IF / ELIF / ELSE
# ============================================================

# Ejercicio 1
# Escribí una función que reciba una nota (0-10) y retorne:
# "Desaprobado" si es menor a 6
# "Aprobado" si está entre 6 y 8
# "Distinguido" si está entre 8 y 9
# "Sobresaliente" si es 10
def calificar(nota):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 2
# Escribí una función que reciba tres números y retorne el mayor de los tres
def mayor_de_tres(a, b, c):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 3
# Escribí una función que reciba un año y retorne True si es bisiesto, False si no
# Un año es bisiesto si es divisible por 4, excepto los divisibles por 100,
# a menos que también sean divisibles por 400
def es_bisiesto(anio):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 2 - WHILE Y BREAK
# ============================================================

# Ejercicio 4
# Escribí una función que pida números al usuario hasta que ingrese 0
# y retorne la suma de todos los números ingresados
def sumar_hasta_cero():
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 5
# Escribí una función que reciba un número n y use while para retornar
# la suma de todos los números del 1 al n
def sumar_hasta_n(n):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 6
# Escribí una función que reciba una lista de números y use while para
# retornar el primero que sea negativo. Si no hay ninguno, retornar None.
# Usá break cuando lo encuentres.
def primer_negativo(lista):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 3 - FOR Y RETURN
# ============================================================

# Ejercicio 7
# Escribí una función que reciba una lista de strings y retorne
# una nueva lista con todos los strings en mayúscula
def mayusculas(lista):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 8
# Escribí una función que reciba una lista de números y retorne
# cuántos son pares
def contar_pares(lista):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 9
# Escribí una función que reciba una lista y un elemento,
# y retorne True si el elemento está en la lista, False si no
# SIN usar el operador "in" — recorrela con for
def esta_en_lista(lista, elemento):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 4 - MANEJO DE ARCHIVOS
# ============================================================

# Ejercicio 10
# Dado este archivo de texto con el formato "nombre;edad"
# Escribí una función que lo lea y retorne una lista de tuplas (nombre, edad)
# Ejemplo de línea: "Juan Pérez;25"
def leer_personas(ruta_archivo):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 11
# Modificá la función anterior para que ignore líneas vacías
# y convierta la edad a entero
def leer_personas_v2(ruta_archivo):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 5 - CLASES Y OBJETOS
# ============================================================

# Ejercicio 12
# Definí una clase "Producto" con atributos _nombre y _precio
# Constructor, getters getNombre y getPrecio
# __str__ que retorne "nombre: $precio"
class Producto:
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 13
# Definí una clase "Carrito" que tenga una lista de productos (_productos)
# Métodos:
# - agregarProducto(producto)
# - calcularTotal() — retorna la suma de todos los precios
# - __str__ — retorna cada producto en una línea
class Carrito:
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 6 - HERENCIA
# ============================================================

# Ejercicio 14
# Definí una clase "Animal" con atributos _nombre y _sonido
# Método hacerSonido() que imprime "nombre dice sonido"
# Definí una clase hija "Perro" que herede de Animal
# y sobreescriba hacerSonido() para que diga "nombre dice Guau! Guau!"
class Animal:
    # TU CÓDIGO ACÁ
    pass

class Perro(Animal):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 15
# Definí una clase "Vehiculo" con atributos _marca y _modelo
# Definí una clase hija "Auto" que agregue _patente
# Usá super().__init__() en Auto
# __str__ de Auto retorna "marca modelo - patente"
class Vehiculo:
    # TU CÓDIGO ACÁ
    pass

class Auto(Vehiculo):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 7 - ALGORITMOS DE ORDENAMIENTO
# ============================================================

# Ejercicio 16 - Bubble Sort
# Ordená esta lista usando bubble sort
# Comparás pares adyacentes y los intercambiás si están en orden incorrecto
def bubble_sort(lista):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 17 - Selection Sort
# Buscás el mínimo de la lista y lo ponés al principio, repetís con el resto
def selection_sort(lista):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 18 - Insertion Sort
# Tomás cada elemento y lo insertás en la posición correcta de la parte ordenada
def insertion_sort(lista):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 19 - Quick Sort
# Implementá quicksort recursivo
def quick_sort(lista):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 8 - ALGORITMOS DE BÚSQUEDA
# ============================================================

# Ejercicio 20 - Búsqueda lineal
# Recorrés la lista elemento por elemento
# Retornás el índice si lo encontrás, -1 si no
def busqueda_lineal(lista, elemento):
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 21 - Búsqueda binaria
# La lista tiene que estar ordenada
# Retornás el índice si lo encontrás, -1 si no
def busqueda_binaria(lista, elemento):
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# BLOQUE 9 - ANÁLISIS ASINTÓTICO (V o F y preguntas)
# ============================================================

"""
Respondé estas preguntas como comentarios:

1. ¿Cuál es la complejidad de búsqueda lineal en el peor caso? ¿Por qué?
# TU RESPUESTA:

2. ¿Cuál es la complejidad de búsqueda binaria? ¿Por qué es mejor que la lineal?
# TU RESPUESTA:

3. ¿Cuál es la complejidad promedio de quicksort?
# TU RESPUESTA:

4. Verdadero o Falso: O(n log n) es mejor que O(n²) para listas grandes
# TU RESPUESTA:

5. Verdadero o Falso: La búsqueda binaria funciona sobre listas desordenadas
# TU RESPUESTA:

6. ¿Qué significa que un algoritmo sea O(1)?
# TU RESPUESTA:
"""

# ============================================================
# BLOQUE 10 - DEBUGGING
# ============================================================

# Ejercicio 22
# Este código tiene errores. Encontralos y corregílos SIN correrlo primero.
"""
class persona:
    def __init__(self, dni, nom)
        self._dni = dni
        self.nom = nom
    
    def getNombre(self):
        return self._nom
    
    def __str__(self):
        return f"{self._dni} | {self._nom}"

p = persona(12345678, "Juan")
print(p.getNombre)
print(p._apellido)
"""

# Ejercicio 23
# ¿Este código tiene error de sintaxis o de semántica? ¿Por qué?
"""
def sumar(a, b):
    return a - b

resultado = sumar(3, 4)
print(resultado)  # imprime -1 en vez de 7
"""

# Ejercicio 24
# ¿Este código tiene error de sintaxis o de semántica? ¿Por qué?
"""
def saludar(nombre)
    print(f"Hola {nombre}")

saludar("Estani")
"""

# ============================================================
# BLOQUE 11 - TDA (TIPO DE DATO ABSTRACTO)
# ============================================================

# Ejercicio 25
# Implementá un TDA Pila (Stack) con los métodos:
# - push(elemento) — agrega al tope
# - pop() — saca del tope y retorna el elemento
# - peek() — mira el tope sin sacarlo
# - esta_vacia() — retorna True si está vacía
# - __str__ — muestra el contenido
class Pila:
    # TU CÓDIGO ACÁ
    pass

# Ejercicio 26
# Implementá un TDA Cola (Queue) con los métodos:
# - encolar(elemento) — agrega al final
# - desencolar() — saca del frente y retorna el elemento
# - esta_vacia() — retorna True si está vacía
# - __str__ — muestra el contenido
class Cola:
    # TU CÓDIGO ACÁ
    pass

# ============================================================
# MAIN - probá tus implementaciones acá
# ============================================================

def main():
    # Bloque 1
    print("=== CALIFICACIONES ===")
    # TU CÓDIGO ACÁ

    # Bloque 5
    print("=== CARRITO ===")
    # TU CÓDIGO ACÁ

    # Bloque 7
    print("=== ORDENAMIENTO ===")
    lista = [64, 34, 25, 12, 22, 11, 90]
    # TU CÓDIGO ACÁ

    # Bloque 8
    print("=== BÚSQUEDA ===")
    # TU CÓDIGO ACÁ

main()
