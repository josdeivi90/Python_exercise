def factorial(a):
    fac = 1
    L = []
    for i in range(1, a+1):
        fac = fac * i
        print(fac, end=' * ')


n = int(input("ingrese el numero a calcular el factorial = "))
factorial(n)