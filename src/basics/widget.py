class Widget:

    def __init__(self, name, x=50, y=50):
        self.name = name
        self.x = x
        self.y = y

    def size(self):
        return self.x, self.y
