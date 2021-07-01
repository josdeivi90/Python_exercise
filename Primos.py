def isPrime(num):
    for n in range(2, num):
        if num % n == 0:
            #print("No es primo", n, "es divisor")
            return False
    #print("Es primo")
    return True
    
for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
    