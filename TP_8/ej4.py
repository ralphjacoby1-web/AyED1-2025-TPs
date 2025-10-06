def pedir_fichas():
    lista = []
    for i in range(2):
        lista_interna = []
        for i in range(2):
            while True:
                valores = int(input("Ingrese los valores de la ficha: "))
                if not 0 < valores <= 6:
                    valores = int(input("Ingrese el valor correctamente: "))
                else:
                    lista_interna.append(valores)
                    break
        lista.append(tuple(lista_interna))
    return lista

def domino(lista):
    conjunto = set()
    for elem in lista:
        for elemento in elem:
            conjunto.add(elemento)
    return len(conjunto) < 4

def main():
    tuplas = pedir_fichas()
    if domino(tuplas):
        print("Si, son compatibles.")
    else:
        print("No, no son compatibles.")

assert domino([(1,2),(2,3)]) == True
assert domino([(1,2),(4,3)]) == False

main()