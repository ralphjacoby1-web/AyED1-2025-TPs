def ingresar_datos()->list:
    """
    Esta funcion pide el codigo de socio y lo guarda una lista si es correcto
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    lista_socios = []
    codigo = -1
    while codigo != 0:
        codigo = int(input("Ingrese su codigo de socio: "))
        if codigo == 0:
               break
        while codigo > 99999 or codigo < 9999:
                    codigo = int(input("Ingrese su codigo de socio correctamente: "))
        lista_socios.append(codigo)
    return lista_socios

def cuantas_veces(lista_socios:list)->list:
    """
    Esta funcion muestra la cantidad de veces que un socio ingreso
    Pre : Recibe una lista
    Post : Devuelve una lista
    """
    base = []
    for elem in set(lista_socios):
            tupla = elem, lista_socios.count(elem)
            base.append(tupla)
            print(f"el usuario con el codigo {elem}, fue una cantidad de {lista_socios.count(elem)} veces")
    return base

def eliminar(base:list):
    """
    Esta funcion elimina un socio por codigo de socio
    Pre : Recibe una lista de tuplas
    Post : Devuelve una lista de tuplas
    """
    print(f"Esta es la lista de ingresados {base}")
    a_eliminar = int(input("Ingrese el socio que se bajo: "))
    while a_eliminar > 99999 or a_eliminar < 9999:
            a_eliminar = int(input("Ingrese su codigo de socio correctamente: "))
    base_modificada = [x for x in base if x[0] != a_eliminar]
    if a_eliminar not in base:
          print("Se ingreso un codigo no existente, por lo tanto no se elimino ningun usuario.")
    print(f"Asi esta la lista de usuarios ahora {base_modificada}, se elimino a {[x for x in base if x[0] == a_eliminar]}")

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    datos = ingresar_datos()
    base = cuantas_veces(datos)
    eliminar(base)
main()

