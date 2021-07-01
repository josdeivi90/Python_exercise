def readint(prompt, min, max):
    try:
        if(min<prompt<max):
            return prompt
        else:
            raise TypeError
    except TypeError:
        return print("numero fuera del rango ", prompt )

'''Ingresa un número entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1'''

readint(100,-10,10)