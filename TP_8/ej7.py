def llenar_conj()->set:
    """
    Esta funcion llena un conjunto
    Pre : No recibe nada
    Post : Devuelve un conjunto
    """
    conj = set()
    for i in range(10):
        conj.add(i)
    return conj

def solicitar(conj:set)->None:
    """
    Esta funcion elimina un valor de un conjunto
    Pre : Recibe un conjunto
    Post : No devuelve nada
    """
    while True:
        valor = int(input("Ingrese un valor: "))
        if valor == -1:
            break
        else:
            try:
                conj.remove(valor)
            except KeyError:
                print("Ese valor no esta en el conjunto")
    print(conj)

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    conj = llenar_conj()
    solicitar(conj)

main()