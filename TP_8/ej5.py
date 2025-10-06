def son_ortogonales(tupla1=(2,3), tupla2=(-3,2)):
    return tupla1[0] * tupla2[0] + tupla1[1] * tupla2[1] == 0

def main():
    if son_ortogonales():
        print("Las coord son ortogonales")
    else:
        print("Las coord no son ortogonales")

assert son_ortogonales((2,3),(-3,2)) == True
assert son_ortogonales((1,1),(2,3)) == False

main()