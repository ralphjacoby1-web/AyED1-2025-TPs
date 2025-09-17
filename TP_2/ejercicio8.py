def generar_lista()->list:
    return [x for x in range(100,201) if x % 2 != 0]

def main():
    lista = generar_lista()
    print(lista)

main()