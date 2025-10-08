def crear_dicc():
    diccionario = {}
    while True:
        clave = input("Ingrese el producto (-1 para salir): ")
        if clave == "-1":
            break
        while True:
            precio = int(input("Ingrese el precio: "))
            if precio < 0:
                print("Precio invalido.")
            else:
                break
        diccionario[clave] = precio
    return diccionario

def descuento_cuadernos(diccionario):
    for k,v in diccionario.items():
        k = k.lower().strip()
        if k == "cuaderno" or k == "cuadernos":
            diccionario[k] = round(v * 1.15)
    print(diccionario)


def main():
    dicc = crear_dicc()
    descuento_cuadernos(dicc)

main()
