def tomar_valores()->list:
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

def generar_listas(pacientes:list):
    urgencia = [codigo for codigo, tipo in pacientes if tipo == 0]
    turno = [codigo for codigo, tipo in pacientes if tipo == 1]
    print("Pacientes por urgencia:", urgencia)
    print("Pacientes por turno:", turno)

def buscar_afiliado(pacientes:list):
    afliliado = 0
    while afliliado != -1:
        contador = 0
        afliliado = int(input("Ingrese el numero de afiliado: "))
        if afliliado == -1:
            print("Gracias!")
            break
        while afliliado > 9999 or afliliado < 1000:
            afliliado = int(input("Ingrese un codigo de afiliado valido (1000-9999): "))
        turno = sum(1 for paciente in pacientes if paciente[1] == 1 and paciente[0] == afliliado)
        urgencia = sum(1 for paciente in pacientes if paciente[1] == 0 and paciente[0] == afliliado)
        print(f"El paciente fue atendido {turno} veces con turno")
        print(f"El paciente fue atendido {urgencia} veces por urgencias")

def main():
    pacientes = tomar_valores()
    generar_listas(pacientes)
    buscar_afiliado(pacientes)


main()
