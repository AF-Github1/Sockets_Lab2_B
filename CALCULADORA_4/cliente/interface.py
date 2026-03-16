from servidor.gestor import maquina

class Interface:
	def __init__(self):
		pass
	def execute(self):
		print("Qual é o cálculo que quer efetuar? x + - /")
		res:str = input()
		print("Preciso que introduza dois valores:")
		x:float = float(input("x="))
		y:float = float(input("y="))
		# chamar maquina.py
		_maquina = maquina.Maquina(res,x,y)
		valor_calculado = _maquina.execute(res,x,y)

		if res == "+":
			print("O valor da operação somar é:", valor_calculado)
		elif res== "-":
			print("O valor da operação subtrair é:", valor_calculado)
		elif res== "x":
			print("O valor da operação multiplicar é:", valor_calculado)
		elif res == "/":
			print ("O valor da operação divisão é:", valor_calculado)
		else:
			print("O valor da raiz quadrada é", valor_calculado)
