def tomar_valores():
    turno_urgencia = -2
    pacientes = []
    while turno_urgencia != -1:
        codigo = int(input("Ingrese su codigo de afiliado: "))
        while codigo > 9999 or codigo < 1000:
            codigo = int(input("Ingrese un codigo de afiliado valido (1000-9999): "))
        turno_urgencia = int(input("Ingrese si el paciente ingresó con turno (1) o por urgencia (0) (-1 para salir): "))
        while turno_urgencia not in (-1, 0, 1):
            turno_urgencia = int(input("Ingrese una opcion valida (0=urgencia, 1=turno, -1=salir): "))
        if turno_urgencia != -1: 
            pacientes.append((codigo, turno_urgencia))
    return pacientes

def generar_listas(pacientes):
    urgencia = [codigo for codigo, tipo in pacientes if tipo == 0]
    turno = [codigo for codigo, tipo in pacientes if tipo == 1]
    print("Pacientes por urgencia:", urgencia)
    print("Pacientes por turno:", turno)

def buscar_afiliado(pacientes):
    pass


def main():
    pacientes = tomar_valores()
    generar_listas(pacientes)


main()
