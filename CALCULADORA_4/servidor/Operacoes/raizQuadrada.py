import math
from typing import Union

class RaizQuadrada:
    def __init__(self, x:float):
        self.x = x

    def executar(self,x:float)->Union[float,str]:
        """
        Realiza a raiz quadrada de um número
        :param x: valor para o qual é calculada a raiz quadrada
        :return: retorna da raiz quadrada, em float, ou o valor com números imaginários
        """
        try:
            return math.sqrt(self.x)
        except:
            i = math.sqrt(abs(self.x))
            return "Raiz de número negativo (número imaginário) = " + str(i) + "i"