<h1>Comunicação cliente-servidor com sockets em Python</h1>
<p>Este código em Python ilustra a comunicação entre um cliente e um servidor usando sockets.</p>

<p>A comunicação é feita através do protocolo TCP (Transmission Control Protocol) e o código é dividido em duas partes: cliente e servidor.</p>
<h3>Cliente</h3>
<p>O cliente estabelece uma conexão com o servidor e envia mensagens para ele. O usuário pode digitar mensagens que serão enviadas ao servidor através do socket. O cliente fica esperando a resposta do servidor e exibe no terminal.</p>

<h3>Servidor</h3>
<p>O servidor é responsável por receber as mensagens do cliente e respondê-las. Ele é capaz de lidar com múltiplos clientes simultaneamente através de threads.</p>

<p>O servidor fica escutando na porta 8000 e aguarda conexões de clientes. Quando um cliente se conecta, o servidor cria uma nova thread para lidar com ele.</p>

<p>Cada thread fica esperando por mensagens do cliente, e quando uma mensagem é recebida, o servidor envia uma resposta de volta para o cliente. Se o cliente enviar a mensagem "TCHAU", a conexão é encerrada.</p>

<p>O servidor também define um tempo limite para a conexão. Se um cliente não enviar nenhuma mensagem dentro de 30 segundos, o servidor envia uma mensagem de "TIMEOUT" de volta para o cliente e encerra a conexão.</p>

<h3>Como executar</h3>
Para executar o código, primeiro execute o servidor e depois execute o cliente. Certifique-se de que o servidor esteja em execução antes de executar o cliente.

<p>O servidor e o cliente devem ser executados em terminais separados.</p>

<h4>Executar o servidor</h4>
```
python server.py
```
<h4>Executar o Cliente</h4>
```
python client.py
```
<p>O cliente irá pedir que o usuário digite a mensagem para enviar ao servidor. O servidor irá responder com a mensagem recebida ou com "TIMEOUT" caso o tempo limite seja excedido. O usuário pode digitar "TCHAU" a qualquer momento para encerrar a conexão</p>

<h1>Client-Server Communication with Sockets in Python</h1>
<p>This Python code illustrates communication between a client and a server using sockets.</p>
<p>Communication is done through the Transmission Control Protocol (TCP) protocol, and the code is divided into two parts: client and server.</p>
<h3>Client</h3>
<p>The client establishes a connection with the server and sends messages to it. The user can type messages that will be sent to the server via the socket. The client waits for a response from the server and displays it in the terminal.</p>
<h3>Server</h3>
<p>The server is responsible for receiving messages from the client and responding to them. It is capable of handling multiple clients simultaneously through threads.</p>
<p>The server listens on port 8000 and waits for client connections. When a client connects, the server creates a new thread to handle it.</p>
<p>Each thread waits for messages from the client, and when a message is received, the server sends a response back to the client. If the client sends the message "TCHAU", the connection is terminated.</p>
<p>The server also defines a timeout for the connection. If a client does not send any messages within 30 seconds, the server sends a "TIMEOUT" message back to the client and terminates the connection.</p>
<h3>How to Run</h3>
To run the code, first run the server and then run the client. Make sure the server is running before running the client.
<p>The server and the client should be run in separate terminals.</p>
<h4>Run the Server</h4>
```
python server.py
```
<h4>Run the Client</h4>
```
python client.py
```
<p>The client will prompt the user to type the message to send to the server. The server will respond with the received message or "TIMEOUT" if the timeout is exceeded. The user can type "TCHAU" at any time to terminate the connection.</p>
