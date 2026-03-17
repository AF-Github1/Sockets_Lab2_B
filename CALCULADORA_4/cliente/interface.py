from CALCULADORA_4.servidor.gestor import maquina
import socket
import json
# PORT e SERVER ADDRESS

COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "add_obj  "
SYM_OP = "sym      "
SUB_OP = "sub      "
MLT_OP = "mult     "
DIV_OP = "div      "
SQR_OP = "sqr      "
BYE_OP = "bye      "
END_OP = "stop     "
PORT = 36000
SERVER_ADDRESS = "192.168.233.1"

# ----- enviar e receber strings ----- #
def receive_str(connect, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connect.recv(n_bytes)
        return data.decode()

def send_str(connect, value: str) -> None:
    connect.send(value.encode())

def send_int(connect:socket.socket, value: int, n_bytes: int) -> None:
    connect.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

def receive_int(connect: socket.socket, n_bytes: int) -> int:
    data = connect.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)


#TODO
# Implement a method that sends and object and returns an object.
def send_object(connection, obj):
    """1º: envia tamanho, 2º: envia dados.""" 
    data = json.dumps(obj).encode('utf-8')
    size = len(data)
    send_int(connection, size, INT_SIZE) # Envio do tamanho
    connection.send(data)# Envio do objeto
def receive_object(connection):
    """1º: lê tamanho, 2º: lê dados.""" 
    size = receive_int(connection, INT_SIZE) # Recebe o tamanho
    data = connection.recv(size)  # Recebe o objeto
    return json.loads(data.decode('utf-8'))


class Interface: ## Interface como cliente
	def __init__(self):
		self._maquina = maquina.Maquina()
	def execute(self):
		connection = socket.socket()
		connection.connect((SERVER_ADDRESS,PORT))
		print("Qual é o cálculo que quer efetuar? + - x / sqrt")
		sinal_op = str(input())
		print("Preciso que introduza dois valores:")
		a:float = float(input("x="))
		b:float = float(input("y="))
            
		dicionario_op = {"sinal" : sinal_op, "op1" : a, "op2" : b}
		valor_calculado = self._maquina.server_call(connection, OBJ_OP, dicionario_op)
		
		print("O resultado da operação de (dicionário) é: ", valor_calculado)
            
		send_str(connection, END_OP) # Terminar ligação
		connection.close()

		