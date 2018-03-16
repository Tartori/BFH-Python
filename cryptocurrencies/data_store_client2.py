import hashlib
from data_store_server2 import Server
s = Server()
hashes = {}

def create(name, content):
    hashes[name]=hashlib.sha256(content)
    s.create(name, content)

def update(name, content):
    hashes[name]=hashlib.sha256(content)
    s.update(name, content)

def delete(name):
    del hashes[name]
    s.delete(name)

def read(name):
    c=s.read(name)
    if(hashlib.sha256(c)!=hashes[name]):
        raise EnvironmentError()
    return c
    


