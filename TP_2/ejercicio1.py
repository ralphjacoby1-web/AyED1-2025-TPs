import random as rn
from functools import reduce

def generar_lista()->list:
    """
    Esta funcion genera una lista random
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    return [rn.randint(1000, 9999) for x in range(rn.randint(10,99))]

def multiplicar(lista:list)->int:
    """
    Esta funcion multiplica todos los valores dentro de la lista
    Pre : Recibe una lista
    Post : Devuelve un entero
    """
    multiplicar = reduce(lambda x,y: x*y, lista)
    return multiplicar

def eliminar_valor(lista:list)->list:
    """
    Esta funcion elimina un valor de la lista elegido por el usuario
    Pre : Recibe una lista 
    Post : Devuelve una lista
    """
    valor_eliminar = int(input("Ingrese un valor a eliminar: "))
    cantidad = lista.count(valor_eliminar)
    for i in range(cantidad):
        lista.remove(valor_eliminar)
    return lista

def capicua(lista: list) -> bool:
    """
    Esta se fija si la lista es capicua
    Pre : Recibe una lista
    Post : Devuelve un booleano
    """
    return lista == lista[::-1]

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
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