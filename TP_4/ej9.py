import re

def ordenar(cadena:str="hola   me lll aaa mo .. ffa")->None:
    frase = re.split(r"[:.;, ]", cadena)
    frase.sort(key=len)
    frase = [x for x in list(frase) if x != ""]
    print(frase)

ordenar()
