def multiplicativeSubgroupOf(n):
    elements = []
    for i in range(1,n):
        if gcd(n,i)==1:
            elements.append(i)
    return elements

def orderOf(n, e):
    elements = multiplicativeSubgroupOf(n)
    if not e in elements:
        return 0
    for i in range(1,n):
        if e**i%n ==1:
            return i
    else:
        return 0


def gcd(i,j):
    if i%j==0:
        return j
    return gcd(j, i%j)

def isGenerator(g, p):
    """ Checks for a save prime p=2q+1 if g is Generator of Gq """
    q=(p-1)/2
    return g**q%p==1

def savePrimeSubgroups(p):
    elements = multiplicativeSubgroupOf(p)
    groups = [[1]]
    groups.append([1,p-1])
    group=[]
    for e in elements:
        if isGenerator(e,p):
            group.append(e)
    groups.append(group)
    groups.append(elements)
    return groups

def subgroups(n):
    elements=multiplicativeSubgroupOf(n)
    groups = []
    for e in elements:
        group=[e]
        for i in range(2, n):
            val=(e**i)%n
            if(val == e):
                break
            group.append(val)
        groups.append(group)
    return groups

