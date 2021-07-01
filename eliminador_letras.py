# Indicar al usuario que ingrese una palabra

userWord = input("ingrese la palabra")
# y asignarlo a la variable userWord.
userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
        continue
    else:
        print(letra)

