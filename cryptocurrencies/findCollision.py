import binascii
def findcollision(t):
    a = binascii.crc32(t.to_bytes())
    b=0
    i=0
    while a!=b:
        b=binascii.crc32(i.to_bytes(64, 'big'))
        i+=1
