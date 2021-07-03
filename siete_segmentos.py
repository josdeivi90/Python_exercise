uno1 = ["1","#","#","#","#","#"]
dos2 = ['2','###','  #','###','#  ','###']
tres3 = ['3','###','  #','###','  #','###']
cuatro4 = ['4','# #','# #','###','  #','  #']
cinco5 = ['5','###','#  ','###','  #','###']
seis6 = ['6','###','#  ','###','# #','###']
siete7 = ['7','###','  #','  #','  #','  #']
ocho8 = ['8','###','# #','###','# #','###']
nueve9 = ['9','###','# #','###','  #','###']
cero0 = ['0','###','# #','# #','# #','###']



numero =[cero0,uno1,dos2,tres3,cuatro4,cinco5,seis6,siete7,ocho8,nueve9]
entra = input('aqui = ')
l=[]
#funcion para separa los datos
def number_split(datos):
    for i in datos:
        l.append(i)
    return l


x =[]
x = number_split(entra)
k =[[],[],[],[],[]]
for i in range(len(x)):
    for j in range(len(numero)):
        if(x[i]==numero[j][0]):
            k[0].append(numero[j][1])
            k[1].append(numero[j][2])
            k[2].append(numero[j][3])
            k[3].append(numero[j][4])
            k[4].append(numero[j][5])

print("el numero ingresado es = ",entra)
#debo hacer una funcion para imprimir linea a linea
for v in range(len(k)):
    print(k[v])