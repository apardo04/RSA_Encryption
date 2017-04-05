import math

def isPrime(n):
    prime = True
    if n == 2:
        prime = True
    elif n % 2 == 0:
        prime = False
    else:
        k = 3
        while k <= int(math.sqrt(float(n))):
            if n % k == 0:
                prime = False
                break;
            k = k + 2
    return "isPrime(" + str(n) + ") = " + str(prime) + "\n"

n = 1
while n <= 1:
    n = int(raw_input("Enter n > 1: "))

print isPrime(n)

