import hashlib


class Server:
    def __init__(self):
        self.files = []

    def create(self,file):
        self.files.append(file)

    def delete(self,h):
        for file in self.files:
            if hashlib.sha256(file)==h:
                self.files.remove(file)
                return
    
    def update(self, file, h):
        self.delete(h)
        self.create(file)

    def read(self,h):
        for file in self.files:
            if hashlib.sha256(file)==h:
                return file