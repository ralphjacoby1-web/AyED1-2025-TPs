def ordenar(cadena:str="hola, me llamo ralph")->None:
    """
    Esta funcion ordena una cadena sin tener en cuenta el largo de los signo de puntuacion
    Pre : Recibe un string
    Post : No devuelve nada
    """
    caracteres = [",",".",";",":"]
    frase = cadena.split()
    frase_lista = []
    for elem in frase:
        nuevo = [x for x in elem if x not in caracteres]
        nuevo = "".join(nuevo)
        frase_lista.append(nuevo)
    combinadas = list(zip(frase_lista, frase))
    ordenadas = sorted(combinadas, key=lambda x: len(x[0]))
    palabras_ordenadas, frase_ordenada = zip(*ordenadas)
    frase_ordenada = " ".join(frase_ordenada)
    print(f"La frase del principio era '{cadena}' y ordenada queda '{frase_ordenada}'")

ordenar()
