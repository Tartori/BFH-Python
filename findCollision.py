import binascii
a = binascii.crc32(b"Satoshi Nakamoto")
b=0
i=0
while a!=b:
    str(i)
    b=binascii.crc32(i.to_bytes(64, 'big'))
    i+=1
