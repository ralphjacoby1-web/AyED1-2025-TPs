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
    if 0 <= fila <= num:
        return True
    

# def trasponer():
#     matriz_traspuesta = []
#     for elem in matriz:
#         matriz_traspuesta.appen([])
#         for i in range(len(elem)):
#             matriz.traspuesta[i].append(elem[i])

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



matriz, n  = generar_matriz()
ordenar_matriz(matriz)
print(matriz)
cambiar_lugar(matriz, n)
print(matriz)
promedio(matriz,n)