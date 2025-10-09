def generar_lista()->list:
    """
    Esta funcion llena una lista con enteros ingresados por el usuario
    Pre : No recibe nada
    Post : Devuelve una lista
    """
    lista = []
    while True:
        try:
            valor = int(input("Ingrese un valor: "))
            if valor == -1:
                break
        except ValueError:
            print("Ingrese un valor valido")
        else:
            lista.append(valor)
    return lista

def buscar_indice(lista:list)->None:
    """
    Esta funcion devuelve el indice de un valor en una lista
    Pre : Recibe una lista
    Post : No devuelve nada
    """
    contador = 0
    while contador < 4:
        try:
            buscar = int(input("Ingrese un valor para buscar: "))
            indice = lista.index(buscar)
        except ValueError:
            print("No existe ese valor en la lista.")
            contador += 1
        else:
            print(f"El valor en la posicion {indice} es {buscar}.")
    raise ValueError("Se intento 3 veces.")


def main()->None:
    """
    Esta funcion junta las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    lista = generar_lista()
    buscar_indice(lista)

main()