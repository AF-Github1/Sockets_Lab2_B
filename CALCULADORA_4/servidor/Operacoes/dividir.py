from typing import Union

class Dividir:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.res = 0


    def executar(self)->Union[float,str]:
        """
        Divide dois números
        :param x: valor dividido
        :param y: valor a dividir
        :return: retorna o resultado da divisão ou mensagem de erro caso tenha ocorrido divisão por 0
        """
        try:
            self.res = self.x / self.y
        except ZeroDivisionError:
            return "error:dividing by zero"
        return self.res