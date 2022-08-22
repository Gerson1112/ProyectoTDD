def menu():
    print("-----Bienvenido a la maquina de Cafe-----")
    VasosTamano()
    Cucharitas()
    Sirviendo()
    input("Presione enter para terminar su proceso")

def VasosTamano():
    Op = str(input("Por favor seleccione cual vaso desea: 1-Pequeño 2-Mediano 3-Grande: "))
    if Op == "1":
        VasoPequeño()
    elif Op == "2":
        VasoMediano()
    elif Op == "3":
        VasoGrande()
    else:
        print("Numero fuera de rango, Las opciones van de 1 al 3")
        VasosTamano()

def Cucharitas():
    azucar = int(input("Cuantas cucharaditas de azucar quiere?: "))
    print(f"echando {azucar} cucharitas de azucar")

def VasoPequeño():
    print("entregando vaso pequeño")

def VasoMediano():
    print("entregando vaso mediano")

def VasoGrande():
    print("entregando vaso grande")

def Sirviendo():
    print("Aqui esta su cafe espero que lo disfrute.")

menu()
