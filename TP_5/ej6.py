def generar_lista():
    lista = []
    while True:
        try:
            valor = int(input("Ingrese un valor: "))
            if valor == -1:
                break
        except ValueError:
            print("Ingrese un valor valido")
        else:
            lista.append(valor)
    return lista

def buscar_indice(lista):
    contador = 0
    while contador < 4:
        try:
            buscar = int(input("Ingrese un valor para buscar: "))
            indice = lista.index(buscar)
        except ValueError:
            print("No existe ese valor en la lista.")
            contador += 1
        else:
            print(f"El valor en la posicion {indice} es {buscar}.")
    raise ValueError("Se intento 3 veces.")


def main():
    lista = generar_lista()
    buscar_indice(lista)

main()