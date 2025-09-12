def generar_lista():
    return [x for x in range(100,201) if x % 2 != 0]

def main():
    lista = generar_lista()
    print(lista)

main()