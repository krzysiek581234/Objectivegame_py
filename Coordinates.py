class Coordinates:
    x = None
    y = None
    def __init__(self,x,y):
        self.y = y
        self.x = x
    def update(self,x,y):
        self.x = x
        self.y =y
    def save(self):
        pass
    def load(self):
        pass