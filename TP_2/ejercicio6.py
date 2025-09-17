import random as rn
from functools import reduce

def generar_listas()->list:
    return [rn.randint(1,10) for x in range(9)]

def normalizar(lista:list)->list:
    normalizado = []
    suma = 0
    for elem in lista:
        suma += elem
    for elem in lista:
        normalizado.append(elem/suma)
    return normalizado

def main():
    lista = generar_listas()
    print(lista)
    lista_normal = normalizar(lista)
    print(lista_normal)

main()