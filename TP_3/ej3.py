import random as rn

def crear_matriz():
    matriz = []
    tamanio = int(input("Ingrese el tamanio de la matriz: "))
    for i in range(tamanio):
        matriz.append([])
    return matriz, tamanio

def llenar_matriz(matriz, tamanio):
    indice = 0
    numero = rn.sample(range(tamanio**2),tamanio**2)
    for i in range(tamanio):
        for x in range(tamanio):
            matriz[i].append(numero[indice])
            indice += 1
    return matriz

def main():
    matriz, tamanio = crear_matriz()
    llenar_matriz(matriz,tamanio)
    print(matriz)

main()