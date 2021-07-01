final = True
numero = 4
while final:
    x = int(input("ingrese el numero entre 1-9 = "))
    if (x == numero):
        final = False
        print("Has acertado con el numero1")
    else:
        print("Sigue intentando")
        final = True
