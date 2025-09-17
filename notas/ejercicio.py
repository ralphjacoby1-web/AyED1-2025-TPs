lista = [x fox x in range(1,32)]

print(lista)

def organizar_mes(lista):
    return [x for x in lista if lista[i:i+7]]

organizar_mes(lista)

print(lista)
