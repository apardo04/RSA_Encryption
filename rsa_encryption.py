import random
import math

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
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def keyGenerator(p, q):
    n = p * q

    #Eulers Totient
    phi = (p - 1) * (q - 1)

    #find e, such that e and phi are coprimes
    #e = 7
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicativeInverse(e, phi)

    return [(e, n), (d, n)]

def encrypt():
    m = raw_input("Enter a message you want to encrypt: ")
    p = int(raw_input("Enter a prime number > 127: "))
    q = int(raw_input("Enter another distinct prime number > 127  "))
    if not (isPrime(p) and isPrime(q) and p > 127 and q > 127):
        print "Both entries must be distinct prime integers > 127\nPlease try again"
        return encrypt()
    c = ""
    publicKey, privateKey = keyGenerator(p, q)
    for x in m:
        c = c + str(ord(x) ** publicKey[0] % publicKey[1]) + " "
        #print (ord(x) ** publicKey[0] % publicKey[1])
    print "Your encrypted message is: " + c[:-1]
    print "Your private key is: " + str(privateKey) + " You will need this to decrypt later."
    print "Your public key is: " + str(publicKey)
    #print "publicKey[0] = " + str(publicKey[0])

def decrypt():
    c = raw_input("Enter a message you want to decrypt: ").split()
    d = int(raw_input("Enter your private key d: "))
    n = int(raw_input("Enter n: "))
    m = ''
    for x in c:
        m = m + chr(int(x) ** d % n)
    print m

userInp = raw_input("Would You like to Encrypt or Decrypt?\nEnter 1 to encrypt\nEnter 2 to decrypt\n")
if (userInp == '1'):
    encrypt()
elif (userInp == '2'):
    decrypt()