

def millerRabin(n):
    m=n-1
    r=getR(m, 0)
    if r==0:
        raise Exception()
    u=m/2**r
    return (r,u)

def getR(n, i):
    if n%2==1:
        return i
    return getR(n/2, i+1)

def isprime(n):
    import random
    if n==2:
        return True
    (r,u) = millerRabin(n)
    for _ in range(40):
        a=random.randint(2,n-1)
        if iscomposite(a,n,r,u):
            return False
    return True

def squareAndMultiplyIterative(x,y,n):
    ret = 1
    while y > 0:
        if y%2==0:
            x=x**2%n
            y=y/2
        else:
            ret=ret*x%n
            y=y-1
    return ret


def squareAndMultiply(x,y,n):
    if y==0:
        return 1
    if y%2==0:
        return squareAndMultiply(x**2%n, y/2, n)
    return x*squareAndMultiply(x, y-1, n)%n

def iscomposite(a,n,r,u):
    x=squareAndMultiply(a,u,n)
    if x==1:
        return False
    for _ in range(0,r):
        if x==n-1:
            return False
        x=x**2%n
    return True

def generateFirstPrimes(k):
    if k<1:
         return []
    primes = [2]
    i=3
    while len(primes)<k:
        while not isprime(i):
            i+=2
        primes.append(i)
        i+=2
        print(primes)
    return primes

if __name__ == '__main__':
    print(generateFirstPrimes(150))
    print(squareAndMultiply(48, 33,127))
    print(squareAndMultiplyIterative(48, 33,127))
