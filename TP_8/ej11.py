def contar_vocales(palabra = "Murcieeelgo"):
    diccionario = {}
    vocales = ("a","e","i","o","u")
    palabra_chica = palabra.lower()
    for elem in vocales:
        diccionario[elem] = palabra_chica.count(elem)
    return diccionario

def contar_en_frase(frase="Hola me llamo ralph"):
    lista_palabras = frase.split()
    for elem in lista_palabras:
        dicc = contar_vocales(elem)
        print(f"La palabra {elem} tiene {dicc}")

contar_en_frase()