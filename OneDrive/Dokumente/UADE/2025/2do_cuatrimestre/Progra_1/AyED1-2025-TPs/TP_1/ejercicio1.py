from typing import List

def tomar_numeros() ->list:
    """
    Esta funcion permite ingresar 3 numeros y los guarda en una lista
    Pre : No recibe ningun parametro
    Post : Devuelve una lista con los numeros recibidos
    """
    lista_numeros = []
    for i in range(3):
        numero = input("Ingrese un numero positivo y entero (enter para omitir): ")
        if numero != "":
            numero = int(numero)
            if numero > 0:
                lista_numeros.append(numero)
    return lista_numeros

def ordenar_lista(lista_numeros:list)->list:
    """
    Esta funcion ordena los valores dentro de una lista de menor a mayor
    Pre : Recibe una lista con 3 numeros
    Post : Devuelve la lista recibida ordenada
    """
    lista_numeros_ordenada = sorted(lista_numeros)
    return lista_numeros_ordenada

def validar(lista_numeros_ordenada:list) ->int:
    """
    Esta funcion se ocupa de avisar si la lista recibida esta vacia o el numero mayor esta repetido
    Pre : Recibe de parametro una lista ordenada
    Post : Devuelve un entero
    """
    if len(lista_numeros_ordenada) == 0:
        return -1
    elif lista_numeros_ordenada[1] == lista_numeros_ordenada[2]:
        return -2
    else:
        return lista_numeros_ordenada[2]

def main():
    """
    Esta funcion recibe 3 numeros y dice cual es el mayor de los 3
    Pre : No recibe ningun parametro
    Post : Devuelve cual es el numero mayor
    """
    numeros = tomar_numeros()    
    lista_numeros_ordenada = ordenar_lista(numeros)
    mayor = validar(lista_numeros_ordenada)               
    if mayor == -1:
        print(f"No se ingresó ningún número.")
    elif mayor == -2:
        print("Se repite el numero mayor")
    else:
        print(f"El número mayor es: {mayor}")

main()
