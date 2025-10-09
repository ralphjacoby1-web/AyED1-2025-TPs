def son_ortogonales(tupla1=(2,3), tupla2=(-3,2))->bool:
    """
    Esta funcion se fija si dos puntos son ortogonales
    Pre : Recibe dos tuplas
    Post : Devuelve un booleano
    """
    return tupla1[0] * tupla2[0] + tupla1[1] * tupla2[1] == 0

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    if son_ortogonales():
        print("Las coord son ortogonales")
    else:
        print("Las coord no son ortogonales")

assert son_ortogonales((2,3),(-3,2)) == True
assert son_ortogonales((1,1),(2,3)) == False

main()