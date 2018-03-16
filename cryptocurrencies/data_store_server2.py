
class Server:
    def __init__(self):
        self.files = {}

    def create(self, name, content):
        self.files[name]=content

    def update(self, name, content):
        self.files[name]=content

    def delete(self, name):
        del self.files[name]

    def read(self, name):
        return self.files[name]