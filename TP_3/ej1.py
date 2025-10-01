import random as rn

def generar_matriz():
    matriz = []
    n = int(input("Ingrese el tamanio de la matriz: "))
    for i in range(n):
        matriz.append([])
        for x in range(n):
            # valor = int(input("Ingrese valores: "))
            matriz[i].append(rn.randint(1,20))
    return matriz, n 

def ordenar_matriz(matriz):
    for elem in matriz:
        elem.sort()
    return matriz

def cambiar_lugar(matriz, n):
    while True:
        fila_1 = int(input("Ingrese la lista que desea cambiar: "))
        if validar_fila(fila_1, n):
            break
    while True:
        fila_2 = int(input("Ingrese la otra lista que desea cambiar: "))
        if validar_fila(fila_2, n):
            break
    matriz[fila_1], matriz[fila_2] = matriz[fila_2], matriz[fila_1]
    return matriz

def validar_fila(fila, num):
    if 0 <= fila < num:
        return True

def trasponer(matriz, n):
    matriz_traspuesta = []
    for i in range(n):
        matriz_traspuesta.append([])
    for fila in matriz:
        for i, columna in enumerate(fila):
            matriz_traspuesta[i].append(columna)
    return matriz_traspuesta

def promedio(matriz, n):
    acumulador = 0
    contador = 0
    while True:
        fila = int(input("Ingrese una fila: "))
        if validar_fila(fila, n):
            break
    for elem in matriz[fila]:
        acumulador += elem
        contador += 1
    promedio = acumulador / contador
    print(f"El promeido de los numeros de la fila {fila} es de {promedio}.")

def impar_porcentaje(matriz_columnas, n):
    while True:
        columna = int(input("Ingrese una columna: "))
        if validar_fila(columna, n):
            break
    lista_impares = [x for x in matriz_columnas[columna] if x % 2 != 0]
    largo_impares = len(lista_impares)
    largo_normal = len(matriz_columnas[columna])
    porcentaje = (largo_impares * 100)//largo_normal
    print(f"El porcentaje de numeros impares es de {porcentaje}%")

def matriz_simetrica(matriz1, matriz2):
    return matriz1 == matriz2

def invertir_matriz_x_fila(matriz, n):
    matriz_invertida = []
    for elem in matriz:
        matriz_invertida.append(elem[::-1])
    return matriz_invertida

def palindromos(matriz):
    capicuas = []
    for elem in matriz:
        if elem == elem[::-1]:
            capicuas.append(elem)
    return capicuas

def divisor():
    print(50 * "=")

def main():
    matriz, n  = generar_matriz()
    print(matriz)
    divisor()
    ordenar_matriz(matriz)
    print(matriz)
    divisor()
    cambiar_lugar(matriz, n)
    print(matriz)
    divisor()
    promedio(matriz,n)
    divisor()
    matriz_nueva = trasponer(matriz, n)
    print(matriz_nueva)
    divisor()
    impar_porcentaje(matriz_nueva, n)
    divisor()
    if matriz_simetrica(matriz, matriz_nueva):
        print("Es simetrica con respecto a su diagonal principal.")
    else: 
        print("No es simetria con respecto a su diagonal principal")
    divisor()
    matriz_inv = invertir_matriz_x_fila(matriz, n)
    matriz_invsec = invertir_matriz_x_fila(matriz_nueva, n)
    if matriz_simetrica(matriz_inv, matriz_invsec):
        print("Es simetrica con respecto a su diagonal secundaria.")
    else: 
        print("No es simetria con respecto a su diagonal secundaria")
    divisor()
    capicuas = palindromos(matriz_nueva)
    print(f"Las columnas capicuas son las siguientes: {capicuas}")
    divisor()

main()