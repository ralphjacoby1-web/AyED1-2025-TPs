def llenar_conj():
    conj = set()
    for i in range(10):
        conj.add(i)
    return conj

def solicitar(conj):
    while True:
        valor = int(input("Ingrese un valor: "))
        if valor == -1:
            break
        else:
            try:
                conj.remove(valor)
            except KeyError:
                print("Ese valor no esta en el conjunto")
    print(conj)

def main():
    conj = llenar_conj()
    solicitar(conj)

main()