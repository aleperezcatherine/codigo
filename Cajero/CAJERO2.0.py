SALDO=5600
PIN=1234
while True:
    U=input("Ingrese su usuario: ")
    if U==("ADMIN"):
        while True:
         C=int(input("Ingrese su PIN: "))
         if C==PIN:
            print("MENÚ")
            print("1: Consultar saldo")
            print("2: Depositar")
            print("3: Retirar")
            print("4: Cambiar PIN")
            while True:
               o=int (input("Seleccione una opción: "))
               if o==1:
                  print("Su saldo es de: " + str(SALDO))
                  break; 
               elif o==2:
                   print("MENÚ")
                   print("1: Q50.00")
                   print("2: Q100.00")
                   print("3: Q200.00")
                   print("4: Q300.00")
                   print("5: Q400.00")
                   print("6: Q500.00")
                   D=int(input("Seleccione una candtidad: "))
                   if D==1:
                      SALDO=SALDO+50
                   elif D==2:
                      SALDO=SALDO+100
                   elif D==3:
                      SALDO=SALDO+200
                   elif D==4:
                      SALDO=SALDO+300 
                   elif D==5:
                      SALDO=SALDO+400
                   elif D==6:
                      SALDO=SALDO+500
                   else:
                      print("Opcion incorrecta")
               elif o==3:
                   print("MENÚ")
                   print("1: Q50.00")
                   print("2: Q100.00")
                   print("3: Q200.00")
                   print("4: Q300.00")
                   print("5: Q400.00")
                   print("6: Q500.00")
                   R=int(input("Seleccione una candtidad: "))
                   if R==1:
                      SALDO=SALDO-50
                   elif R==2:
                      SALDO=SALDO-100
                   elif R==3:
                      SALDO=SALDO-200
                   elif R==4:
                      SALDO=SALDO-300 
                   elif R==5:
                      SALDO=SALDO-400
                   elif R==6:
                      SALDO=SALDO-500
                   else:
                      print("Selección incorrecta")
                      break
               elif o==4:
                  p=int(input("Escriba el pin nuevo: "))
                  PIN=p
                  break
               elif o==7:
                  break
        else:
         print("Contraseña Incorrecta")
    else:
       print("Usuario Incorrecto")