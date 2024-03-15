import re

SALDO = 650
PIN = "225125"

def validar_pin(pin):

    return bool(re.match(r'^\d{6}$', pin))

while True:
    U = input("Ingrese su usuario: ")
    if U == "BCC-2215":
        while True:
            C = input("Ingrese su PIN: ")
            if validar_pin(C):
                if C == PIN:
                    print("MENÚ")
                    print("1: Consultar saldo")
                    print("2: Depositar")
                    print("3: Retirar")
                    print("4: Cambiar PIN")
                    while True:
                        o = int(input("Seleccione una opción: "))
                        if o == 1:
                            print("Su saldo es de: " + str(SALDO))
                            break
                        elif o == 2:
                            print("MENÚ")
                            print("1: Q50.00")
                            print("2: Q100.00")
                            print("3: Q150.00")
                            print("4: Q200.00")
                            print("5: Q250.00")
                            print("6: Q300.00")
                            D = int(input("Seleccione una cantidad: "))
                            if D in range(1, 7):
                                SALDO += D * 50
                            else:
                                print("Opción incorrecta")
                        elif o == 3:
                            print("MENÚ")
                            print("1: Q50.00")
                            print("2: Q100.00")
                            print("3: Q150.00")
                            print("4: Q200.00")
                            print("5: Q250.00")
                            print("6: Q300.00")
                            R = int(input("Seleccione una cantidad: "))
                            if R in range(1, 7):
                                SALDO -= R * 50
                            else:
                                print("Selección incorrecta")
                        elif o == 8:
                            p = input("Escriba el PIN nuevo: ")
                            if validar_pin(p):
                                PIN = p
                                break
                            else:
                                print("El PIN debe tener 6 dígitos.")
                        elif o == 7:
                            break
                else:
                    print("Contraseña Incorrecta")
                    break
            else:
                print("El PIN debe tener 6 dígitos.")
    else:
        print("Usuario Incorrecto")