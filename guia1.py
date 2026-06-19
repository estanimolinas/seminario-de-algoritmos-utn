def es_cliente_potencial(edad):
    return edad >= 35 and edad <= 45

def cantidad_sobre_promedio(edades, promedio):
    cantidad = 0
    for edad in edades:
        if edad > promedio:
            cantidad += 1
    return cantidad

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

    total = 0
    potenciales = 0
    edades = []

    fp = open('datos.txt', 'r', encoding='utf8')
    for linea in fp:
        lineaLimpia = linea.strip()
        datosCliente = lineaLimpia.split(";")
        if len(datosCliente) == 2:
            dni = int(datosCliente[0].strip())
            edad = int(datosCliente[1].strip())
            edades.append(edad)
            total += 1
            if es_cliente_potencial(edad):
                potenciales += 1
                print(f"Cliente potencial: {dicNombres[dni]}")
    fp.close()

    if total > 0:
        porcentaje = (potenciales / total) * 100
        promedio = sum(edades) / len(edades)
        sobre_promedio = cantidad_sobre_promedio(edades, promedio)
        print(f"Total clientes: {total}")
        print(f"Clientes potenciales: {potenciales}")
        print(f"Porcentaje: {porcentaje:.2f}%")
        print(f"Promedio de edades: {promedio:.2f}")
        print(f"Edades sobre el promedio: {sobre_promedio}")
    else:
        print("No se ingresaron datos.")

if (__name__ == "__main__"):
    main()