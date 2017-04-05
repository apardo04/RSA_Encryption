arr = []
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        arr.append({"a":a,"b":b,"q":a/b,"r":a%b})
        return gcd(b, a % b)

a = raw_input("Enter a: ")
b = raw_input("Enter b: ")
d = gcd(int(a),int(b))

print "\nGCD(" + a + ", " + b + ") = " + str(d) + "\n"


for i in arr:
    print str(i["a"]) + " = " + str(i["b"]) + " * " + str(i["q"]) + " + " + str(i["r"])


