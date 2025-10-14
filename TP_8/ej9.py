def ingresar_n()->None:
    """
    Esta funcion crea la tabla del 1 al 12
    Pre : No recibe nada
    Post : No devuelve nada
    """
    while True:
        n = int(input("Ingrese un valor: "))
        if 0 < n < 13:
            break
        else:
            print("Valor incorrecto.")
    diccionario = {i: n * i for i in range(1,13)}
    print(diccionario)

ingresar_n()