from math import exp

def attackerSuccessProbability(q, z):
    p=1-q
    lam = z*(q/p)
    s=1
    for k in range(z+1):
        poisson = exp(-lam)
        for i in range(1,k+1):
            poisson *= lam/i
        s-= poisson*(1-pow(q/p,z-k))
    return s
    

if __name__ == '__main__':
    s = 1
    i=1
    while(s>1/2**256):
        s=attackerSuccessProbability(0.1, i)
        i+=1
    print(s)
    print(i)
    print(attackerSuccessProbability(0.1, 340))
