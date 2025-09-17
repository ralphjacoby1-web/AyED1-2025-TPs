def generar_lista()->list:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    return [x for x in range(a,b) if x % 7 == 0 and x % 5 != 0]

def main():
    lista = generar_lista()
    print(lista)

main()