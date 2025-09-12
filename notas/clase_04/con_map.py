lista_original = [x for x in range(1, 101)]

lista_modificada = list(map(lambda x: x*2, lista_original))

print(lista_modificada)

lista_filter = list(filter(lambda x: not x % 3, lista_modificada))

print(lista_filter)