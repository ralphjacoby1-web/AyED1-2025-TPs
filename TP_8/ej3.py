import re

def pedir_correo()->str:
    """
    Esta funcion pide un correo
    Pre : No recibe nada
    Post : Devuelve un string
    """
    correo = input("Ingrese un correo: ")
    return correo

def validez(correo:str)->bool:
    """
    Esta funcion verifica si el correo es valido
    Pre : Recibe un string
    Post : Devuelve un booleano
    """
    patron = r"^[a-bA-B@.]+$"
    if "@" not in correo:
        return False
    elif re.fullmatch(patron, correo):
        return False
    else:
        if correo.count("@") > 1:
            return False
        elif correo[0] == "@" == correo[-1]:
            return False
        elif "." not in correo:
            return False
        else:
            return True

def separar(correo:str)->None:
    """
    Esta funcion muestra las partes del correo
    Pre : Recibe un strnig
    Post : No devuelve nada
    """
    partes = tuple(re.split(r"[@.]", correo))
    print(partes)

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    correo = pedir_correo()
    if validez(correo):
        separar(correo)
    else:
        print(())

main()
