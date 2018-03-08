import hashlib

def solve(p):
    d=p.split(':')[1]
    difficulty = 2**(256-int(d))
    nonce = 1
    p=p.encode('utf-8')
    while True:
        nonce+=1
        if(int(hashlib.sha256(p+bytes(nonce)).hexdigest(),16) < difficulty):
            return nonce


def verify(p, nonce):
    d=p.split(':')[1]
    difficulty = 2**(256-int(d))
    p=p.encode('utf-8')
    return int(hashlib.sha256(p+bytes(nonce)).hexdigest(),16) < difficulty

if __name__ == '__main__':
    s='1:15:asdnlkanga'
    nonce=solve(s)
    print(nonce)
    print(verify(s, nonce))