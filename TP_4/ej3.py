def clave_maestra(clave= "1234235"):
    clave_lista=list(clave.strip())
    clave1 = []
    clave2 = []
    for i,elem in enumerate(clave_lista):
        if i % 2 == 0:
            clave1.append(elem)
        else:
            clave2.append(elem)
    clave1_texto = "".join(clave1)
    clave2_texto = "".join(clave2)
    print(f"Las dos claves de {clave} son {clave1_texto} y {clave2_texto}")

clave_maestra()