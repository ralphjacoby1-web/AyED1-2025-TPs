def es_capicua():
    string = input("Ingrese un string: ")
    if "".join(reversed(string)) == string:
        print("Es capicua.")
    else: 
        print("No es capicua")

es_capicua()