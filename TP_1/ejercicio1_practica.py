def tomar_numeros():
    lista_numeros = []
    for i in range(3):
        numeros = input("ingrese numeros del 1 al 3 (enter para salir)")
        if numeros != "":
            if numeros == "1":
                lista_numeros.append(numeros)
            if numeros == "2":
                lista_numeros.append(numeros)
            if numeros == "3":
                lista_numeros.append(numeros)
    return lista_numeros

def conoces_mayor(lista_numeros):
    if len(lista_numeros) == 0:
        return -1
    mayor = lista_numeros[0]
    for i in range(1, len(lista_numeros)):
        if i > mayor:
            mayor = i
    return mayor

def main():
    numeros = tomar_numeros()
    numero_mayor = conoces_mayor(numeros)
    if numero_mayor == -1:
        print("No se ingreso ningun numero")
    else:
        print(f"El numero mayor es {numero_mayor}")

main()