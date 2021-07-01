import math as micos

salario = float(input("ingrese el salario : "))

alimentos = salario*0.2
pasajes = salario*0.15
cine = salario*0.1
libros = salario*0.15

alquiler = salario - (alimentos + pasajes + cine + libros)


print(alquiler)
