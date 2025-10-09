import re

def ingresar_frase()->str:
    """
    Esta funcion le pide una frase al usuario
    Pre : No recibe nada
    Post : Devuelve un string
    """
    frase = input("Ingrese una frase: ")
    return frase

def palabras_repetidas(frase:str)->set:
    """
    Esta funcion separa las palabras y se fija que no esten repetidas
    Pre : Recibe un string
    Post : Devuelve un conjunto
    """
    conjunto = set()
    frase_nueva = re.sub(r"[^a-zA-Z0-9]"," ",frase)
    x_palabras = frase_nueva.split()
    for elem in x_palabras:
        conjunto.add(elem)
    return conjunto

def ordenar(conj:set)->None:
    """
    Esta funcion ordena el conjunto por largo
    Pre : Recibe un conjunto
    Post : No devuelve nada
    """
    conj = sorted(conj, key=len)
    print(conj)

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    frase = ingresar_frase()
    conj = palabras_repetidas(frase)
    ordenar(conj)

main()