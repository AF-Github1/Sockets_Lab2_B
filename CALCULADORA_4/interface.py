from Operacoes import dividir, somar, subtrair


class Interface:
	def __init__(self):
		pass
	def execute(self):
		print("Qual é o cálculo que quer efetuar? x + - /")
		res:str = input()
		print("Preciso que introduza dois valores:")
		x:float = float(input("x="))
		y:float = float(input("y="))
		if res =="+":
			s:object = somar.Somar(x,y)
			res = s.executar()
			print("O valor da operação somar é:", res)
		elif res =="-":
			s:object = subtrair.Subtrair(x,y)
			res = s.executar()
			print("O valor da operação subtrair é:", res)

		elif res =="/":
			s:object = dividir.Dividir(x,y)
			res = s.executar()
			if type(res)==str:
				print (res)
			else:
				print("O valor da operação divisão é:",res)
