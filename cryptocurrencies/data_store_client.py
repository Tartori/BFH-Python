import hashlib
from data_store_server import Server
s = Server()
hashes = []

def create(file):
    h = hashlib.sha256(file)
    s.create(file)
    hashes.append(h)

def delete(h):
    s.delete(h)
    hashes.remove(h)

def read(h):
    f=s.read(h)
    if hashlib.sha256(f)==h:
        return f

def update(f, h):
    h2 = hashlib.sha256(f)
    s.update(f, h)
    hashes.append(h2)
