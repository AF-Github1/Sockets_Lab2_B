import socket
import json
COMMAND_SIZE = 9
INT_SIZE = 8
ADD_OP = "add      "
OBJ_OP = "add_obj  "
SYM_OP = "sym      "
SUB_OP = "sub      "
BYE_OP = "bye      "
END_OP = "stop     "
PORT = 35000
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
    connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

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

def execute(connection):
    """
    Recebe objecto dicionário, realiza operação de soma
    """
    dados = receive_object(connection)
    operacao = dados.get("sinal")
    v1 = dados.get("op1")
    v2 = dados.get("op2")
    
    if operacao == "+":
        resultado = v1 + v2
        print("Operação por dicionário pedida com " + str(v1) + " e " + str(v2))
    else:
        resultado = 0
        print("Operação não foi de adição")

    send_int(connection, resultado, INT_SIZE)

def execute_list(connection):
    """
    Recebe objecto lista, realizada operação de soma
    """
    dados = receive_object(connection)
    operacao = dados[0]
    v1 = dados[1]
    v2 = dados[2]

    if operacao == "+":
        resultado = v1 + v2
        print("Operação por lista pedida com " + str(v1) + " e " + str(v2))
    else:
        resultado = 0
        print("Operação não foi de adição")

    send_int(connection, resultado, INT_SIZE)



def main():
    """
    Runs the server server until the client sends a "terminate" action
    """
    s = socket.socket()
    s.bind(('', PORT))
    s.listen(1)
    print("Waiting for clients to connect on port " + str(PORT))
    keep_running = True
    while keep_running:
        print("On accept...")
        connection, address = s.accept()
        print("Client " + str(address) + " just connected")
        last_request = False
        #Recebe messagens...
        while not last_request:
            request_type = receive_str(connection,COMMAND_SIZE)
            if request_type == ADD_OP:

                a = receive_int(connection,INT_SIZE)
                b = receive_int(connection,INT_SIZE)
                print("Pediram para somar:",a,"+",b)
                result = a + b
                send_int(connection,result, INT_SIZE)
            elif request_type == SUB_OP:
                a = receive_int(connection,INT_SIZE)
                b = receive_int(connection,INT_SIZE)
                print("Pediram para subtrair:",a,"-",b)
                result = a-b
                send_int(connection,result, INT_SIZE)
            elif request_type == OBJ_OP: # Operação de soma com dicionário
                #execute(connection)
                execute_list(connection)
            elif request_type == BYE_OP:
                print("Last request...")
                last_request = True
                #keep_running = False
            elif request_type == END_OP:
                last_request = True
                keep_running = False
    print("Stopping...")
    s.close()
    print("Server stopped")

if __name__=="__main__":
    main()
