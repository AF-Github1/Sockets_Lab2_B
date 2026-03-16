class Somar:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Soma 2 números
        :param x: valor a que se adiciona
        :param y: valor a adicionar
        :return: devolve o resultado da soma
        """
        self.res = self.x + self.y
        return self.res