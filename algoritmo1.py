# Algoritmo para determinar el valor a pagar en una factura con 20% de descuento.
  
# Ingresar el importe bruto
print("Ingrese el monto bruto de la factura:")
factura = int(input("monto bruto: ")) 

# Calculamos el 20% de descuento sobre el valor de la factura
desc = factura * 0.20

# Total a pagar
total = factura - desc 

# Mostrar los resultados 
print(f"Monto bruto: ${factura}") 
print(f"Descuento aplicado: ${desc}") 
print(f"Total a pagar: ${total}")