def generar_lista()->tuple:
    lista = [x for x in range(1, 101)]
    return list(filter(lambda x: x % 2 == 0 + 1,lista)), lista

def main():
    lista, lista1 = generar_lista()
    print(lista)
    print(lista1)

main()