registro = "Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
nombre = "Daniel"
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "julio", "Agosto", "Septiembre", "octubre"\
        ,"Noviembre", "Diciembre" ] # para leer los distintos meses
lis_name = registro.replace(";",",;,").split(",") #Divido mi lista en ","
lis_name.append(";") #agrego este item para poder sumar un ultimo valor

lon = len(lis_name) 
lista_key = []
# convierto a entero los numeros y saco las claves
for i in range(lon):
    if(lis_name[i] not in meses and lis_name[i]!=";"):
        lis_name[i] = int(lis_name[i])
    elif(lis_name[i] in meses):
        lista_key.append(lis_name[i])
    
f={}       
cont = 0
lista1 = []
#ya hago la suma
for j in lis_name:
    if (j == ";"): # ; lo tengo como valor de parada
        suma = sum(lista1)
        f[lista_key[cont]]=suma
        cont += 1
        lista1 = []
        #pregunto si es entero para poder agregarlo a la lista y sumar despues
    elif(type(j) == int ):
        lista1.append(j)
        
salida_final = (nombre, f)    

print(salida_final)

