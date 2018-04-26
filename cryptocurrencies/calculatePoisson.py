from math import exp
import itertools

def attack_success_probability(q,z):
    """
    Returns  the  success  probability  of  a  double-spending  attack  of  anattacker
     with  hashpower  share  q  against  a  transaction  with  z  confirmations
    """
    p=1.0-q
    lamb=z*(q/p)
    sum=1.0
    for k in range(0, z+1):
        poisson=exp(-lamb)
        for i in range(1,  k+1):
            poisson *= lamb / i
        sum-=poisson*(1-(q/p)**(z-k))
    return sum    

if __name__ == '__main__':
    s = 1
    i=1
    z=1
    while attack_success_probability(.1,  z)>=1/2**256:
        z+=1

    print(z)
