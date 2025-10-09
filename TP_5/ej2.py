def sumar(cadena1:int="43251", cadena2:int="53435")->None:
    """
    Esta funcion toma dos strings y los suma si se pueden castear, sino devuelve -1
    Pre : Recibe dos cadenas
    Post : Devuelve -1 o None
    """
    try:
        numero1 = int(cadena1)
        numero2 = int(cadena2)
        numero1 += numero2
    except ValueError:
        print(-1)
    else:
        print(f"La suma de las dos cadenas es {numero1}")

sumar()