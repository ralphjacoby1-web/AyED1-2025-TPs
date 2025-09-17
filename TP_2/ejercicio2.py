import random as rn

def cantidad_numeros()->list:
    aleatorios = int(input("Ingrese un la cantidad de numeros que desea: "))
    return [rn.randint(1,100) for x in range(aleatorios)]

def repetido(lista:list)->bool:
    for elem in lista:
        repetido = lista.count(elem)
        if repetido >= 2:
            return True
    else:
        return False

def unicos(lista:list)->list:
    nueva_lista = []
    for elem in lista:
        if lista.count(elem) ==  1:
            nueva_lista.append(elem)
    return nueva_lista

def main():
    lista = cantidad_numeros()
    print(lista)
    if repetido(lista):
        print("Tiene por lo menos un valor repetido")
    else:
        print("No tiene ningun vlaor repetido")
    unico = unicos(lista)
    print(unico)

main()