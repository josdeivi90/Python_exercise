try:
    print("1")
    x = 1/0 #aqui el codigo salta a otra linea 
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")

'''try:
    :
except exc1:
    :
except exc2:
    :
except:
    :
  si el try lanza la excepción exc1, esta será manejada por el bloque except exc1:

De la misma manera, si el try lanza la excepción exc2, esta será manejada por el bloque except exc2:.

Si el try lanza cualquier otra excepción, será manejado por el bloque sin nombre except.  
    

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError: #si la division entre 1/x == 1/0
    print("No puedes dividir entre cero, lo siento.")
except ValueError: si ingreso una letra
    print("Debes ingresar un valor entero.")
except: #cualquier otro error
    print("Oh cielos, algo salio mal...")

print("THE END.")   
    
    '''