import random

def random_prime_number():
    sike = [5,7,11,13,17,19,23,29,31,37,41,43,47]
    return sike[random.randint(0,len(sike)-1)]

def mutually_prime_number(a, b):
    if a == b:
        return a == 1
    else:
        if a > b:
            return mutually_prime_number(a - b, b)
        else:
            return mutually_prime_number(b - a, a)

def multiplicatively_obratnoe(e, f):
    d = 2
    while not (d*e)%f == 1:
        d += 1
    return d

def rsa():
    p = random_prime_number()
    q = random_prime_number()
    n = p * q
    f = (p-1)*(q-1)
    e = 2 # public
    while not mutually_prime_number(e,f):
        e += 1
    d = multiplicatively_obratnoe(e, f) #private
    print(n, e, d)
    

    x = 25
    x = (x ** e) % n
    y = x
    y = (y ** d) % n
    print(x, y)
rsa()
input()