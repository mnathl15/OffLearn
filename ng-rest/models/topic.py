
from json import dumps

class Topic:

    def __init__(self):

        self.name = ""
        self.pages = []

    def setName(self, name):
        self.name = name

    def addPage(self, page):
        self.pages.append(page)

    def __str__(self):
        return self.name

    def serialize(self):
        return {'name': self.name, 'pages': self.pages}
        