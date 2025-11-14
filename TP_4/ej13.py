def diccionario_numeros():
    diccionario_numeros_sueltos = {
        1 : "uno",
        2 : "dos",
        3 : "tres",
        4 : "cuatro",
        5 : "cinco",
        6 : "seis",
        7 : "siete",
        8 : "ocho",
        9 : "nueve",
        10 : "diez",
        11 : "once",
        12 : "doce",
        13 : "trece",
        14 : "catorce",
        15 : "quince"
    }
    diccionario_cantidad_numeros = {
        2 : "diez",
        3 : "cien",
        4 : "mil",
        7 : "millon",
        13 : "billon"
    }
    return diccionario_cantidad_numeros, diccionario_numeros_sueltos

def transformador(diccionario_cantidad_numeros, diccionario_numeros_sueltos):
    numero_string = ""
    lista = []
    while True:
        try:
            numero = int(input("Ingrese un numero del 0 al 3999: "))
            if 0 <= numero <= 1_000_000_000_000:
                break
        except ValueError:
            print("Ingrese un numero.")
    numero_original = numero
    numero_str = str(numero)
    uno = acortar_uno(numero_str)
    numero_string += uno
    for k,v in diccionario_cantidad_numeros.items():
        if k == len(str(numero)):
            numero_string += v
    for key,value in diccionario_numeros_sueltos.items():
        if key == int(numero_str[-1]):
            numero_string += value
    print(numero_string)

def acortar_uno(num):
    if num[0] == "1":
        return "un "
    else:
        return ""

a,b = diccionario_numeros()
transformador(a,b)