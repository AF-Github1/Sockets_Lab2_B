class Subtrair:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Subtrai 2 números
        :param x: valor a que se subtrai
        :param y: valor a subtrair
        :return: devolve o resultado da subtração
        """
        self.res = self.x - self.y
        return self.res