import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.18.13', 8000))

while True:
    msg = input('Escreva a mensagem: ')
    client.send(msg.encode())
    if msg.upper() == 'TCHAU':
        break

    resposta = client.recv(1024)
    if resposta.decode().upper() == 'TCHAU':
        break
    elif resposta.decode().upper() == 'TIMEOUT':
        print("Tempo limite excedido. Conexão encerrada.")
        break
    else:
        print(f'Resposta do servidor: {resposta.decode()}')


client.close()