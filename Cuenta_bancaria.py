#Cuenta bancaria
class cuenta:
    #creamos una cuenta con un saldo actual
    def __init__(self,longitud, dinero_act):
        self.longitud = longitud
        self.dinero_act = dinero_act
        
    #mostramos los datos de la cuenta principal
    def display(self):
        print("Datos de la cuenta1:\n","Número de cuenta: ",self.longitud,"\nsaldo Actual: ",self.dinero_act)
            
    #para el ingreso unicamente necesitamos sumar lo que tenemos a lo que introducimos por teclado
    def ingresar(self):
        ingreso = input("introduce la cantidad a ingresar: ")
        self.dinero_act = int(self.dinero_act)+ int(ingreso)
        print("Saldo actual tras ingresar: ", self.dinero_act)
        
    #para retirar restamos el dinero existente, lo que controlamos que el dinero a retirar sea menor al existente
    def retirar(self):
        retirar = input("introduce el dinero a retirar: ")
        if(int(retirar) >= self.dinero_act):
            print("Error intenta retirar una cantidad que no tiene")
        else:
            self.dinero_act = int(self.dinero_act) - int(retirar)
            print("su saldo actual es ", self.dinero_act)
            
    #realizamos una transferencia entre dos cuentas, para ello creamos obj cuenta 2 y le enviamos un dinero.
    def transferencia(self):
        #creamos cuenta2 con saldo 0
        num_cuenta2=input("¿Cúal es el número de la cuenta2, recuerde ingresar 24 digitos: ")
        saldo_cuenta2= input("¿Cúal es el saldo de la cuenta2")
        cuenta2 = cuenta(num_cuenta2,saldo_cuenta2)
        if(len(cuenta2.longitud)==24):
            dinero_trans = input("¿Cuanto desea transferir? ")
            if(int(self.dinero_act) >= int(dinero_trans)):
                self.dinero_act= int(self.dinero_act) - int(dinero_trans)
                cuenta2.dinero_act = dinero_trans
                
                #mostramos los datos de la cuenta 2 tras la transferencia.
                print("Datos de la cuenta2:\n","Número de cuenta: ",cuenta2.longitud,"\nsaldo Actual: ",cuenta2.dinero_act)
            else:
                print("el dinero a transferir de la cuenta 1 a la cuenta 2 debe ser superior al existente")
        cuenta1.display()
    
longitud = "ES6511122233344455566677"

#realizamos un control de longitud de 24 digitos e inicializamos 2 cuentas, la primera sera la principal, y la segunda para la transferencia.
if(len(longitud) == 24):
    saldo = 1000
    cuenta1 = cuenta(longitud,saldo)
    cuenta2 = cuenta(0,0)
    cuenta1.transferencia()
else:
    print("la longitud de la cuenta no es igual a 24 dígitos")
