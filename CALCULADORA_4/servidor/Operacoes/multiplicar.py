class Multiplicar:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->float:
        """
        Multiplica dois números
        :param x: valor multiplicado
        :param y: valor a multiplicar
        :return: retorna o resultado da multiplicação
        """
        self.res = self.x * self.y
        return self.res