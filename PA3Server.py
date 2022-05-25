# Names: 
# Date: May XX, 2022
# Title: PA3Server.py
# Description: This is a TCP server program that ...

# socket module used for network communications
from socket import *

serverPort = 12000      # set listening port

# create TCP socket with IPv4
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind() binds (assigns) the port number 12000 to the server's socket.
# welcoming socket created
serverSocket.bind(('', serverPort))

# server ready to listen for TCP connection request from the client
# 1: indicates maximum number of queued connections (at least 1)
serverSocket.listen(1)

print('The server is ready to receive')

# TCPServer enters loop and waits for a connection to be established
while True:
    # client knocks on door
    # creates a new 'connection' socket in the server
    # handshaking time
    connectionSocket, addr = serverSocket.accept()

    # received sentence
    sentence = connectionSocket.recv(1024).decode()

    print("Server received: ", sentence)

    # modified sentence to uppercase
    capitalizedSentence = sentence.upper()

    print("Server sending: ", capitalizedSentence)

    # sends modified sentence to client through connection socket
    connectionSocket.send(capitalizedSentence.encode())

    # close connection socket
    # server socket is still open
    connectionSocket.close()