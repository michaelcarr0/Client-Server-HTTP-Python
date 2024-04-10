# Michael Carr
# MIS 443
# Professor Hayes
# 04/07/2024

import socket
# Imports a socket. Sockets are an endpoint that receives data.
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creates a new TCP socket object using the IPv4 and TCP socket type.
# This socket is used to establish connections, send and receive data over the network using TCP.
mySocket.bind(('localhost', 8085))
# Binds a socket to a specific address and port of 8085. This allows server to receive incoming connections on that address and port.
mySocket.listen(5)
# Adds a queue for incoming traffic, in this case 5
while True:
    print('HTTP Server started. Waiting and listening for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    # sets up a basic HTTP server that listens for connections and prints any received HTTP requests
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>MIS 443. Student Name is: Michael Carr</h1></body></html> \r\n", 'utf-8'))
    recvSocket.close()
