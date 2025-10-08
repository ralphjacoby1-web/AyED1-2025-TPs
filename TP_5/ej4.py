def generar_numeros():
    try:
        generador()
    except KeyboardInterrupt:
        while True:
            op = input("Desea terminar el proceso? 1 para confirmar: ")
            if op == "1":
                print("Gracias.")
                break
            else:
                print("Opcion incorrecta.")

def generador():
    for i in range(1,100001):
            print(i)

generar_numeros()