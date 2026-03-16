class Subtrair:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self,x:float, y:float)->float:
        self.x = x
        self.y = y
        self.res = x - self.y
        return self.res