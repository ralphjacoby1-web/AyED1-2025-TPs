def ingresar_n():
    while True:
        n = int(input("Ingrese un valor: "))
        if 0 < n < 13:
            break
        else:
            print("Valor incorrecto.")
    diccionario = {i: n * i for i in range(1,13)}
    print(diccionario)

ingresar_n()