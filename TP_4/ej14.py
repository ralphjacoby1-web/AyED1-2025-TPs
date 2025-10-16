import re

def validez(correo:str)->bool:
    """
    Esta funcion verifica si el correo es valido
    Pre : Recibe un string
    Post : Devuelve un booleano
    """
    patron = r"^[a-bA-B@.]+$"
    dos_partes = correo.split("@")
    if "@" not in correo:
        return False
    elif re.fullmatch(patron, correo):
        return False
    else:
        if correo.count("@") > 1:
            return False
        elif correo[0] == "@"  or "@"== correo[-1]:
            return False
        elif ".com.ar" not in dos_partes[1] and ".com" not in dos_partes[1]:
            return False
        else:
            return True

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    while True:
        correo = input("Ingrese su correo: ")
        if correo == "":
            print("Gracias!")
            break
        else:
            if validez(correo):
                print("Es valido")
            else:
                print("No es valido.")

main()