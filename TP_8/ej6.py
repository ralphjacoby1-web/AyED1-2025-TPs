import re

def ingresar_frase():
    frase = input("Ingrese una frase: ")
    return frase

def palabras_repetidas(frase):
    conjunto = set()
    frase_nueva = re.sub(r"[^a-zA-Z0-9]"," ",frase)
    x_palabras = frase_nueva.split()
    for elem in x_palabras:
        conjunto.add(elem)
    return conjunto

def ordenar(conj):
    conj = sorted(conj, key=len)
    print(conj)

def main():
    frase = ingresar_frase()
    conj = palabras_repetidas(frase)
    ordenar(conj)

main()