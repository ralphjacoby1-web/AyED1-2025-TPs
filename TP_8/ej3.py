import re

def pedir_correo():
    correo = input("Ingrese un correo: ")
    return correo

def validez(correo):
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

def separar(correo):
    partes = tuple(re.split(r"[@.]", correo))
    print(partes)

def main():
    correo = pedir_correo()
    if validez(correo):
        separar(correo)
    else:
        print(())

main()
