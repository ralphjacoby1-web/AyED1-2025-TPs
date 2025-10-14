def centrar()->None:
    """
    Esta funcion centra texto
    Pre : No recibe nada
    Post : No devuelve nada
    """
    cadena = input("Ingrese una oracion: ")
    funcion = lambda x: (80-x)//2
    cantidad_car = len(cadena)
    espacio = funcion(cantidad_car)
    print(f"{espacio * " "}{cadena}{espacio * " "}")

centrar()