import random as rn
from functools import reduce

def generar_lista()->list:
    return [rn.randint(1000, 9999) for x in range(rn.randint(10,99))]

def multiplicar(lista:list)->int:
    multiplicar = reduce(lambda x,y: x*y, lista)
    return multiplicar

def eliminar_valor(lista:list):
    valor_eliminar = int(input("Ingrese un valor a eliminar: "))
    cantidad = lista.count(valor_eliminar)
    for i in range(cantidad):
        lista.remove(valor_eliminar)
    return lista

def capicua(lista):
    copia = lista.copy()
    al_reves = copia.reverse()
    if lista == al_reves:
        return True
    else:
        return False

def main():
    lista = generar_lista()
    producto = multiplicar(lista)
    print(producto)
    print(lista)
    nueva_lista = eliminar_valor(lista)
    print(nueva_lista)
    if capicua(lista):
        print("Es capicua")
    else:
        print("No es capicua")

main()