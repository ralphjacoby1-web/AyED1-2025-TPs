def sumar(cadena1="43251", cadena2="53435"):
    try:
        numero1 = int(cadena1)
        numero2 = int(cadena2)
        numero1 += numero2
    except ValueError:
        print(-1)
    else:
        print(f"La suma de las dos cadenas es {numero1}")

sumar()