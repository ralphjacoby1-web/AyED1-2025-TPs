def es_capicua()->None:
    """
    Esta funcion se fija si una cadena es capicua
    Pre : No recibe nada
    Post : No devuelve nada
    """
    string = input("Ingrese un string: ")
    if "".join(reversed(string)) == string:
        print("Es capicua.")
    else: 
        print("No es capicua")

es_capicua()