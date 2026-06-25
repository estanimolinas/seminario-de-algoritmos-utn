# Algoritmo de Descuento en Factura - Versión Básica

## Descripción
Programa simple en Python que calcula el valor final de una factura aplicando un descuento del 20%.

## Cómo funciona
1. El usuario ingresa el monto bruto de la factura.
2. El programa calcula el 20% de descuento.
3. Muestra el monto final a pagar.

## Código
```python
print("Ingrese el monto bruto de la factura:")
factura = int(input("monto bruto: "))

# Calculamos el 20% de descuento
descuento = factura * 0.20
total_a_pagar = factura - descuento

print(f"Monto bruto: ${factura}")
print(f"Descuento (20%): ${descuento}")
print(f"Total a pagar: ${total_a_pagar}")
```

## Limitaciones
- No valida si el usuario ingresa un número válido.
- No redondea decimales (si usas decimales en el monto).
- Si ingresás un número negativo, calcula igual sin validar.

## Mejoras futuras
Ver la versión mejorada (algoritmo2.py) con validación y manejo de errores.