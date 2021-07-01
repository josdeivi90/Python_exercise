'''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika'''

#n = int(input("cuantos = "))
student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
#for i in range(n):
#    name, *line = input("nombres = ").split() #aqui ingreso los nombres y valores y split los separa OJO
#    scores = list(map(float, line)) #map me vuelve una flotante y de paso hago una lista
#    student_marks[name] = scores #forma de crear un diccionario
query_name = 'Malika'#input("quien = ") #nombre al cual debo calcular el promedioS

print(student_marks)

#saco los valores de Malika
nombre = []
for i in student_marks.keys():
    if (query_name == i):
        nombre = (student_marks[i])
print(nombre)

#promedio
promedio = sum(nombre)/len(nombre)

print("{0:.2f}".format(promedio)) #lo paso para dos cifras significativas