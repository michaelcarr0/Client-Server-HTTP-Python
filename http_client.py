# Michael Carr
# MIS 443
# Professor Hayes
# 04/07/2024

import socket
webhost = '127.0.0.1'
# localhost IP address of the server
webport = 8085
# Port number of the server
print("Contacting %s on port %d ..." % (webhost, webport))
# The script attempts to establish a connection to 127.0.0.1 on the specified webport: 8085
webclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Creates a socket object
webclient.connect((webhost, webport))
# Connects to the server
webclient.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode('utf-8')))
# Sending an HTTP GET request to the server
reply = webclient.recv(4096)
print("Response from %s:" % webhost)
print(reply.decode())
# Receives the response from the server