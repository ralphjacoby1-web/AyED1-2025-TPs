import random as rn

def generar_lista():
    lista1 = []
    lista2 = []
    for i in range(5):
        lista1.append(rn.randint(1,20))
        lista2.append(rn.randint(1,20))
    return lista1, lista2

def intercalar(lista1, lista2): 
    for i, elem in enumerate(lista2):
        lista1[i:i] = [elem]
        return lista1
    #usar enumerate

def main():
    lista1, lista2 = generar_lista()
    print(lista1)
    print(lista2)
    lista = intercalar(lista1, lista2)
    print(lista)

main()