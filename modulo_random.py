from random import random, seed,randrange, randint,choice, sample

#seed(3)

#for i in range(5):
 #   seed(i)
 #   print(random())

'''randrange(fin)x
randrange(inico, fin)
randrange(inicio, fin, incremento)
randint(izquierda, derecha)'''



print(randrange(5), end=' ')
print(randrange(0, 10), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 50))



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst)) #elije un valor de entre mi lista
print(sample(lst, 5)) # elije 5 valores aleatorios
print(sample(lst, 10)) # elije 10 valores NOTA: no puede superar len(lst)