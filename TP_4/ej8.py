def subcadena_ultimos()->None:
    """
    Esta funcion muestra los ultimos caracteres de una cadena elegidos por un usuario
    Pre : No recibe nada
    Post : No devuelve nada
    """
    frase = input("Ingrese una frase: ")
    while True:
        try:
            menos = int(input("Ingrese un valor: "))
        except ValueError:
            print("Ingrese un entero")
        else:
            if not len(frase) > menos:
                print("No puede ser mayor el numero que la frase")
            else:
                break
    print(f"Los ultimos {menos} caracteres de la cadena: #{frase}# son {frase[-menos:]}")

subcadena_ultimos()
    
            