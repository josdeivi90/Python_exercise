'''def hola(nombre):    # definiendo una función
    print("Hola,", nombre)    # cuerpo de la función


nombre = input("Ingresa tu nombre: ")

hola(nombre)    # invocación de la función

def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Skywalker" ,"Luke" )
presentar("Quick", "Jesse")
presentar("Kent", "Clark")

Escribe una función que tome por parámetro la fecha de nacimiento de una persona y devuelva su edad actual
datetime
'''

def par_impar(a):
    if(a%2==0):
        return True
    else:
        return False

n = int(input("ingrese = "))
if par_impar(n):
    print("es par")
else:
    print("es impar")


'''
def aburrimiento(a,b="ON"):
    
    print(a,"aburrimiento",b)
    return None

aburrimiento("hola")
valor = aburrimiento
if valor == None:
    print("Lo siento, no tienes ningún valor") 



def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum

print(sumaDeLista([5, 4, 3])) 

# numeros en reversa
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))'''