import math;

#aufgabe 1
print ("------------Aufgabe 1---------------")

def pqFormel(p,q):
    x1 = (-p + math.sqrt(p**2 + q))
    x2 = (-p - math.sqrt(p**2 + q))
    return x1, x2

def pqFormel2(p,q):
    x1 = -p-math.sqrt(p*p+q)
    x2 = -q/x1
    return x1, x2

def testNull(p,q,x):
    return x**2 + 2*p*x - q

def printAufgabe(p,q):
    print("Variante 1:",pqFormel(p,q), testNull(p,q,pqFormel(p,q)[0]), testNull(p,q,pqFormel(p,q)[1]))
    print("Variante 2:",pqFormel2(p,q), testNull(p,q,pqFormel2(p,q)[0]), testNull(p,q,pqFormel2(p,q)[1]))
    print("----------------------------------")

printAufgabe(10**2,1)
printAufgabe(10**4,1)
printAufgabe(10**6,1)
printAufgabe(10**7,1)
printAufgabe(10**8,1)
# Variante 2 ist genauer

# aufgabe 2
print ("------------Aufgabe 2---------------")

def exponenialFormel(n,x):
    sum = 0
    for i in range(0,n):
        sum += x**i/math.factorial(i)
    return sum

def exponentialFormel2(n,x):
    sum = 0
    for i in range(0,n):
        sum += x**(n-i)/math.factorial(n-i)
    return sum

def testExponential(n,x):
    return math.exp(x)-exponenialFormel(n,x)

def testExponential2(n,x):
    return math.exp(x)-exponentialFormel2(n,x)

def printAufgabe2(n,x):
    print("Variante 1:",exponenialFormel(n,x), "Test:", testExponential(n,x) , "n:", n, "x:", x)
    print("Variante 2:",exponentialFormel2(n,x), "Test:", testExponential2(n,x), "n:", n, "x:", x)
    print("----------------------------------")

printAufgabe2(10,2)
printAufgabe2(100,2)
printAufgabe2(1000,2)
printAufgabe2(10,100)
printAufgabe2(100,100)
printAufgabe2(1000,100)

# 