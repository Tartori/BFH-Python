def breakDiffieHellman(p,g,A,B):
    ex = findExponent(p=p, g=g, X=A)
    key=(B**ex)%p
    return key

def findExponent(*,p,g,X,i=1):
    if i==p:
        return -1
    if (g**i)%p==X:
        return i
    return findExponent(p=p, g=g, X=X, i=i+1)

if __name__ == '__main__':
    print(breakDiffieHellman(11,6,7,5))