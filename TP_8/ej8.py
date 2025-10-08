def generar_diccionario():
    return {i: i**2 for i in range(1,21)}

def mostrar():
    diccionario = generar_diccionario()
    for k,v in diccionario.items():
        print(f"{k}:{v}")

mostrar()
    