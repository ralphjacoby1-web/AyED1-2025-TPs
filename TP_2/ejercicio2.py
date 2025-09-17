import random as rn

def cantidad_numeros()->list:
    """
    Esta pide una cantidad de numeros que el usuario desea generar aleatoriamente
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    aleatorios = int(input("Ingrese un la cantidad de numeros que desea: "))
    return [rn.randint(1,100) for x in range(aleatorios)]

def repetido(lista:list)->bool:
    """
    Esta funcion se fija si hay un elemento repetido
    Pre : Recibe una lista 
    Post : Devuelve un booleano
    """
    for elem in lista:
        repetido = lista.count(elem)
        if repetido >= 2:
            return True
    else:
        return False

def unicos(lista:list)->list:
    """
    Esta funcion guarda en una lista los numeros que sean unicos de la lista ingresada
    Pre : Recibe una lista de parametro
    Post : Devuelve una lista
    """
    nueva_lista = []
    for elem in lista:
        if lista.count(elem) ==  1:
            nueva_lista.append(elem)
    return nueva_lista

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista = cantidad_numeros()
    print(lista)
    if repetido(lista):
        print("Tiene por lo menos un valor repetido")
    else:
        print("No tiene ningun vlaor repetido")
    unico = unicos(lista)
    print(unico)

main()