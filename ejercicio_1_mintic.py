# Un empleado quiere saber cuanto se le descontara de su salario basado en las siguientes reglas:

# Salario básico bruto <= 2000000 Descuento = 20% Salario neto = 80%
# Salario básico bruto <= 3000000 Descuento = 25% Salario neto = 75%
# Salario básico bruto <= 4000000 Descuento = 30% Salario neto = 70%
# Salario básico bruto > 4000000 Descuento = 35% Salario neto = 65%

# Escriba un programa que le permita al empleado ingresar sus salario bruto y devuelva su salario neto.
import time
while True:
    salario = (input("Ingrese su salario: "))
    k = type(salario)
    print(k)
    if( k == str):
        print("ingreso una letra y no una cantidad numerica")
    else:
        salario = int(salario)


        if(0<salario <= 2000000):
            descuento = salario*0.2
            neto = salario*0.8
            flag = 1
        elif(2000001< salario <= 3000000):
            descuento = salario*0.25
            neto = salario*0.75
            flag = 1
        elif(3000001< salario <= 4000000):
            descuento = salario*0.3
            neto = salario*0.70
            flag = 1
        elif(salario > 4000001):
            descuento = salario*0.35
            neto = salario*0.65
            flag = 1
        elif(salario <= 0):
            print("el valor ingresado no es valido")
            flag = 0
            

        if (flag == 1):
            print("Su salario = "+ str(salario)+"\n" + "descuento = "+ str(descuento) + "\n" + "Salario neto = "+str(neto))
   
    time.sleep(2)