import random as rn
from functools import reduce


def crear_matriz()->tuple:
    """
    Esta funcion crea una matriz
    Pre : No recibe nada
    Post : Devuelve una lista de listas y un entero
    """
    cantidad_fabricas = int(input("Ingrese la candtidad de farbicas: "))
    matriz = [[rn.randint(0,150) for x in range(7)] for x in range(cantidad_fabricas)]
    return matriz, cantidad_fabricas

def cantidad_por_fabrica(matriz:list)->None:
    """
    Esta funcion calcula la cantidad de productos producidos por fabrica
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    lista_produ = []
    for elem in matriz:
        suma = lambda x,y: x+y
        lista_produ.append(reduce(suma, elem))
    for i, elemento in enumerate(lista_produ):
        print(f"La fabrica {i+1} produjo {elemento} bicicletas")

def mas_produccion(matriz:list)->None:
    """
    Esta funcion muestra el dia con mas produccion
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    mayor = (0,0,0)
    for j, fila in enumerate(matriz):
        for i,columna in enumerate(fila):
            if columna > mayor[0]:
                mayor = columna, i, j
    
    print(f"El dia con mayor produccion fue el {indices_dias(mayor[1])} en la fabrica {mayor[2] + 1} y produjo {mayor[0]}")

def indices_dias(dia:int)->str:
    """
    Esta funcion pasa un numero a un dia en formato string
    Pre : Recibe un entero
    Post : Devuelve un string
    """
    dia += 1
    if dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miercoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sabado"
    else:
        return "Domingo"

def cantidad_por_dia(matriz:list)->None:
    """
    Esta funcion muestra el dia con mas produccion
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    lista_menor = []
    mayor = 0
    indice_mayor = -1
    matriz_traspuesta = list(zip(*matriz))
    for elem in matriz_traspuesta:
        lista_menor.append(reduce(lambda x,y: x+y, elem))
    for i,elemento in enumerate(lista_menor):
        if elemento > mayor:
            mayor = elemento
            indice_mayor = i
    print(f"El dia con mas produccion es el {indices_dias(indice_mayor)} y se produjeron {mayor} bicicletas")


def menor_fabricas(matriz:list)->None:
    """
    Esta funcion muestra la fabrica con menor produccion
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    lista = [(min(x)) for x in matriz]
    print(f"La lista con las menores produccion por farbica es: {lista}")

def main()-> None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    matriz, cantidad_fabricas = crear_matriz()
    print(matriz)
    cantidad_por_fabrica(matriz)
    mas_produccion(matriz)
    cantidad_por_dia(matriz)
    menor_fabricas(matriz)


main()