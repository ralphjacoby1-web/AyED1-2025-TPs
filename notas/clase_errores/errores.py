class ErrorPorNumeroNegativo(Exception):
    pass

def main():    
    legajo = int(input("Ingrese su legajo: "))
    if legajo < 0:
        raise ErrorPorNumeroNegativo("Legajo tiene que ser positivo.")
    print("Gracias.")

lista1 = [1,3,2,4]
lista = [x for x in lista1[::-1]]
print(lista)

lista2 = [x for x in lista1]
print(lista2)
