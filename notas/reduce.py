from functools import reduce

producto = reduce((lambda x, y: x*y), [1, 2, 3, 4])

print(producto)

#multiplica todos los numeros de la lista dada
#reduce junta todos los elementos de una lista(suma, resta, producto, etc.)

enteros = [True, False]
suma = reduce(lambda a, b: a + b, enteros)

print(suma)

#suma de los booleanos = or
#multiplicacion de los booleanos = and  