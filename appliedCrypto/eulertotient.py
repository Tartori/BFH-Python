def euler(n):
    num=0
    for i in range(1, n):
        if gcd(n,i)==1:
            num+=1
    return num

def euler2(n):
    primes = prime_factors(n)
    num=1
    for p in primes:
        num*=(1-1/p)
    return num*n

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            while not n%i:
                n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def gcd(i,j):
    if i%j==0:
        return j
    return gcd(j, i%j)
