#Cajero Automatico hecho en Python
#cambio en rama develop
import sys 
from datetime import datetime
HistorialMov = list() 
acceso=False
intentos =3
saldo =1000

def sinSaldo():
    print("No se tienen fondos suficientes!!")
    print("(1) Continuar al Menu")
    print("(2) Salir")
    opcion = input("Seleccione la opcion: ")
    if(opcion=="1"):
        print()
    else:
        sys.exit()

def validaNumero(numero):
    if(numero.isnumeric()):
        return True
    else:
        try:
            float(numero)
            return True
        except ValueError:
            return False

def Retiro():
    global saldo
    valido=False
    while(valido==False):
        if(saldo<=0):
            print("")
        else:
            cadena = input("Ingrese la cantidad a Retirar: ")
            if(validaNumero(cadena)):
                retiro=float(cadena)
                if((saldo-retiro)<0):
                    print("El retiro sobrepasa tu saldo")
                else:
                    now = datetime.now()
                    saldoAnterior=saldo
                    saldo=saldo - retiro
                    print(f"Retiro correcto por ${retiro}")

                    historial=f"{now} - R:${retiro} - SA:${saldoAnterior} - SN:${saldo}"
                    HistorialMov.append(historial)
                    valido=True
            else:
                print("Monto Ingresado Incorrecto. Intenta Denuevo")  

def Historial():
    if(len(HistorialMov)<1):
        print("No se tienen Movimientos Registrados") 
    else:
        for x in range(0,len(HistorialMov)):
            print (f"[{x+1}] {HistorialMov[x]}")

            

while intentos > 0:
    pin = input('Ingresa el Pin: ')
    if(pin=="1235"):
        acceso = True
        break
    else:
        intentos-=1
        print("PIN Incorrecto. Intente Denuevo")

if(acceso):
    answer = "s"
    while(answer=="s" or answer=="S"):
        print("Bienvenido al CajeroAutomatico")
        print("** MENU DE OPCIONES **")
        print("(1) CONSULTAR SALDO")
        print("(2) RETIRAR SALDO")
        print("(3) HISTORIAL DE MOVIMIENTOS")
        print("(4) SALIR")
        opcion = input("Seleccione la Opción: ")
        if(opcion =="1"):
            if(saldo<=0):
                sinSaldo()
            else:
                print("** CONSULTA DE SALDO **")
                print(f"Su saldo actual es de ${saldo}")
        elif(opcion =="2"):
            print("** RETIRO DE SALDO **")
            Retiro()
        elif(opcion =="3"):
            print("** HISTORIAL DE MOVIMIENTOS **")  
            Historial()
        answer = input("¿Desea Realizar otra operacion? S/N ")
else:
    print("Acceso Denegado!!")




 