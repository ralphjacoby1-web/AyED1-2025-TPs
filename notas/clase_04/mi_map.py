from typing import List

#Funciones de orden superior.
#map,filter,reduce()
#map: Agarro un iterable, por cada elemnento lo "proceso" mediante una funcion, si entran 100 salen 100.
#Filter: Filtra con True o False. "Pasan" los True. ej: es_citrico y le paso frutas.
#Reduce: Toma todos los datos y retorna uno solo.

def doble(x:int)->int:
    return x*2

doble_lambda = lambda x: x * 2 

def map_(doble_lambda, lista:list[int])->List[int]:
    lista_interna = list()
    for elem in lista:
        lista_interna.append(doble_lambda(elem))
    #return [doble(elem) for elem in lista]
        return lista_interna 

lista_original = [x for x in range(1,11)]

lista_modificada = map_(doble, lista_original)

print(lista_modificada)

