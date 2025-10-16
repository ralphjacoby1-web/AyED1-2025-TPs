def encontrar_cadena(cadena:str = "hola me llamo ralplaj")->None:
    """
    Esta funcion muestra cuenta la cantidad de veces que aparece una subcadena en una cadena
    Pre : Recibe un string
    Post : No devuelve nada
    """
    lista_ = []
    cadena_buscar = input("Ingrese una palabra que desee buscar: ")
    for elem in cadena:
        for elemento in cadena_buscar:
            if elemento == elem:
                lista_.append(elem)
    cadena_final = "".join(lista_)
    cantidad = cadena_final.count(cadena_buscar)
    print(f"En la cadena '{cadena}' la subcadena '{cadena_buscar}' aparece una cantidad de {cantidad} veces")

encontrar_cadena()
            