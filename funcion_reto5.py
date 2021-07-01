def calculadoraMes(registro,nombre):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "julio", "Agosto", "Septiembre", "octubre","Noviembre", "Diciembre" ]
    lis_name = registro.replace(";",",;,").split(",")
    lis_name.append(";")
    lon = len(lis_name) 
    lista_key = []
    for i in range(lon):
        if(lis_name[i] not in meses and lis_name[i]!=";"):
            lis_name[i] = int(lis_name[i])
        elif(lis_name[i] in meses):
            lista_key.append(lis_name[i])
    
    f={}       
    cont = 0
    lista1 = []

    for j in lis_name:
        if (j == ";"):
            suma = sum(lista1)
            f[lista_key[cont]]=suma
            cont += 1
            lista1 = []
        elif(type(j) == int ):
            lista1.append(j)    
    salida_final = (nombre, f) 
    return salida_final

print(calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4","Daniel"))
print(calculadoraMes("Enero,1,3,1;Febrero,2,3;Marzo,5,4,3,4;Abril,4,4,4","Jose"))
print(calculadoraMes("Enero,1,1,1;Febrero,2,3,5;Marzo,50,1,3,4;Abril,4,3,4","David"))