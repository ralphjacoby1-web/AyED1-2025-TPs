import random as rn

def crear_matriz()->tuple:
    """
    Esta funcion crea una matriz
    Pre : No recibe nada
    Post : Devuelve una lista de listas y un entero
    """
    matriz = []
    tamanio = int(input("Ingrese el tamanio de la matriz: "))
    for i in range(tamanio):
        matriz.append([])
    return matriz, tamanio

def llenar_matriz(matriz:list, tamanio:int)->list:
    """
    Esta funcion llena una matriz
    Pre : Recibe una lista de listas y un entero
    Post : Devuelve una lista de listas
    """
    indice = 0
    numero = rn.sample(range(tamanio**2),tamanio**2)
    for i in range(tamanio):
        for x in range(tamanio):
            matriz[i].append(numero[indice])
            indice += 1
    return matriz

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    matriz, tamanio = crear_matriz()
    llenar_matriz(matriz,tamanio)
    print(matriz)

main()