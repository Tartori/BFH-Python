def breakDiffieHellman(p,g,A,B):
    ex,isA = findExponentBetter(p, g, A, B, g, 1)
    key=(B**ex)%p if isA else (A**ex)%p
    return key

def findExponentBetter(p,g,A,B,m,i):
    if(m==A):
        return (i,True)
    if(m==B):
        return (i,False)
    return findExponentBetter(p,g,A,B,m*g%p, i+1)

def findExponent(*,p,g,X,i=1):
    if i==p:
        return -1
    if (g**i)%p==X:
        return i
    return findExponent(p=p, g=g, X=X, i=i+1)

if __name__ == '__main__':
    print(breakDiffieHellman(11,6,7,5))