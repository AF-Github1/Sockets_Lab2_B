from CALCULADORA_4.servidor.Operacoes import dividir, somar, subtrair ,multiplicar,raizQuadrada
import socket
import json
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
SERVER_ADDRESS = "localhost"
# ---------------------- interaction with sockets ------------------------------
def receive_int(connection, n_bytes: int) -> int:
    """
    :param n_bytes: The number of bytes to read from the current connection
    :return: The next integer read from the current connection
    """
    data = connection.recv(n_bytes)
    return int.from_bytes(data, byteorder='big', signed=True)

def send_int(connection, value: int, n_bytes: int) -> None:
    """
    :param value: The integer value to be sent to the current connection
    :param n_bytes: The number of bytes to send
    """
    connection.send(int(value).to_bytes(n_bytes, byteorder="big", signed=True))

def receive_str(connection, n_bytes: int) -> str:
    """
    :param n_bytes: The number of bytes to read from the current connection
    :return: The next string read from the current connection
    """
    data = connection.recv(n_bytes)
    return data.decode()

def send_str(connection, value: str) -> None:
    """
    :param value: The string value to send to the current connection
    """
    connection.send(value.encode())

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
    size = receive_int(connection, INT_SIZE) #   Recebe o tamanho
    data = connection.recv(size)  # Recebe o objeto
    return json.loads(data.decode('utf-8'))


class Maquina: # #Maquina como servidor
    def __init__(self):
        pass

    def server_call(self, connection, op_sinal, dicionario_op):
        """
        Função que lida com o envio de dicionários por sockets
        """
        send_str(connection, op_sinal)
        send_object(connection, dicionario_op)
        return receive_int(connection, INT_SIZE)

    def execute(self):
        """
        Esta função aceita o dicionário vindo de um cliente e realiza uma operação dependendo do sinal que estiver na primeira chave, usando para esse efeito os operandos
        da segunda e terceira chave. Caso a operação seja invalida, devolve 0,
        """
        s = socket.socket()
        s.bind(('', PORT))
        s.listen(1)
        
        keep_running = True
        while keep_running:
            connection, address = s.accept()
            last_request = False
            while not last_request:
                request_type = receive_str(connection, COMMAND_SIZE)
                
                if request_type == OBJ_OP:
                    dados = receive_object(connection)
                    sinal = dados.get("sinal")
                    v1 = dados.get("op1")
                    v2 = dados.get("op2")

                    if sinal == "+":
                        op_obj = somar.Somar(v1, v2)
                    elif sinal == "-":
                        op_obj = subtrair.Subtrair(v1, v2)
                    elif sinal == "x":
                        op_obj = multiplicar.Multiplicar(v1, v2)
                    elif sinal == "/":
                        op_obj = dividir.Dividir(v1, v2)
                    elif sinal == "sqrt":
                        op_obj = raizQuadrada.RaizQuadrada(v1)
                    else:
                        op_obj = None
                    if op_obj:
                        res = op_obj.executar()
                    else:
                        res = 0
                    
                    send_int(connection, res, INT_SIZE)
                
                elif request_type == END_OP:
                    last_request = True
                    keep_running = False
            connection.close()
        s.close()

if __name__ == "__main__":
    _server = Maquina()
    _server.execute()
