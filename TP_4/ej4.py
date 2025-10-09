def nums_romanos():
    diccionario_romano = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }
    return diccionario_romano

def transformador(diccionario):
    numero_romano = ""
    lista = []
    while True:
        try:
            numero = int(input("Ingrese un numero del 0 al 3999: "))
            if 0 <= numero <= 3999:
                break
        except ValueError:
            print("Ingrese un numero.")
    numero_original = numero
    for k, v in sorted(diccionario.items(), reverse=True):
        while numero >= k:
            lista.append(v)
            numero = int(numero) - int(k)

    numero_romano = "".join(lista)
    print(f"{numero_original} en números romanos es: {numero_romano}")

def main():
    dicc = nums_romanos()
    transformador(dicc)

main()

