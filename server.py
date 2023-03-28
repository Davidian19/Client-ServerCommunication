import socket
import threading

counter = 3
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.18.13', 8000))
server.listen(1)
print('Aguardando conexões...')

def worker(i):
    print(f'Aguardando cliente {i}')
    connection, clientAdress = server.accept()
    print(f'Conexão estabelecida com {clientAdress}')
    connection.settimeout(30)
    
    while True:
        try:
            data = connection.recv(1024)
        except socket.timeout:
            print(f'Tempo limite excedido. Conexão com {clientAdress} encerrada.')
            msg = 'TIMEOUT'
            connection.send(msg.encode())
            connection.close()
            break
        except Exception as e:
            print(f'Erro ao receber dados: {e}')
            connection.close()
            break

        if not data:
            connection.close()
            print(f'Conexão com {clientAdress} encerrada.')
            break
        else:
            print(f'Dados recebidos: {data.decode()}')

        if data.decode().upper() == 'TCHAU':
            connection.close()
            print(f'Conexão com {clientAdress} encerrada.')
            break

        msg = input("insira a mensagem: ")
        connection.send(msg.encode())

threads = []
for i in range(counter):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('Thread finalizada')