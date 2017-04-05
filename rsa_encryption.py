import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
    return prime

def multiplicativeInverse(e, phi):
    #todo

def keyGenerator(p, q):
    if not (isPrime(p) and isPrime(q)):
        return "Both entries must be distinct prime integers"

    n = p * q

    #Eulers Totient
    phi = (p - 1) * (q - 1)

    #find e, such that e and phi are coprimes
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #multiplicativeInverse(e, phi) would go here

    return [(e, n), (d, n)]

p = int(raw_input("Enter a prime number: "))
q = int(raw_input("Enter another distinct prime number  "))

#publicKey, privateKey = generate_keypair(p, q)
