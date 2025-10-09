def pedir_fichas()->list[tuple]:
    """
    Esta funcion crea dos fichas de domino
    Pre : No recibe nada
    Post : Devuelve una lista de tuplas
    """
    lista = []
    for i in range(2):
        lista_interna = []
        for i in range(2):
            while True:
                valores = int(input("Ingrese los valores de la ficha: "))
                if 0 < valores <= 6:
                    lista_interna.append(valores)
                    break
                else:
                    print("Valor invalido.")
        lista.append(tuple(lista_interna))
    return lista

def domino(lista:list[tuple])->bool:
    """
    Esta funcion se fija si se pueden juntar las fichas de domino
    Pre : Recibe una lista de tuplas
    Post : Devuelve un booleano
    """
    conjunto = set()
    for elem in lista:
        for elemento in elem:
            conjunto.add(elemento)
    return len(conjunto) < 4

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    tuplas = pedir_fichas()
    if domino(tuplas):
        print("Si, son compatibles.")
    else:
        print("No, no son compatibles.")

assert domino([(1,2),(2,3)]) == True
assert domino([(1,2),(4,3)]) == False

main()