def euler(n):
    num=0
    primes=prime_factors(n)
    print(primes)
    for i in range(1, n):
        for prime in primes:
            if i%prime==0:
                break
        else:
            num+=1
    return num

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