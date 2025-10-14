def crear_dicc()->dict:
    """
    Esta funcion crea un diccionario con datos cargados por el usuario
    Pre : No recibe nada
    Post : Devuelve un diccionario
    """
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

def descuento_cuadernos(diccionario:dict)->None:
    """
    Esta funcion le aplica descuanto a la categoria de cuadernos
    Pre : Recibe un diccionario
    Post : No devuelve nada
    """
    for k,v in diccionario.items():
        k = k.lower().strip()
        if k == "cuaderno" or k == "cuadernos":
            diccionario[k] = round(v * 1.15)
    print(diccionario)


def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    dicc = crear_dicc()
    descuento_cuadernos(dicc)

main()
