class Topic:

    def __init__(self):

        self.name = ""
        self.pages = []

    def setName(self, name):
        self.name = name

    def addPage(self, page):
        self.pages.append(page)
        