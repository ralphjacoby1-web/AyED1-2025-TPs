import random as rn 

def generar_listas()->list:
    return [rn.randint(1,20) for x in range(9)]

def esta_ordenada(lista:list)->bool:
     lista_ordenada = lista.copy()
     lista_ordenada.sort()
     return lista == lista_ordenada
     
def main():
    lista = generar_listas()
    print(lista)
    ordenada = esta_ordenada(lista)
    print(lista)
    if ordenada:
        print("Esta ordenada.")
    else:
        print("No esta ordenada.")

main()

assert esta_ordenada([1,3,4]) == True
assert esta_ordenada([2,1,2]) == False