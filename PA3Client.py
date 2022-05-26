# Names: 
# Date: May XX, 2022
# Title: PA3Client.py
# Description: This is a TCP client program that ...

# socket module used for network communications
from socket import *

serverName = '127.0.0.1'    # The ip address of server
serverPort = 12000          # The server port to be used

# create TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Establish TCP connection with server
clientSocket.connect((serverName, serverPort))

# Message from server
serverMessage = clientSocket.recv(1024)
print('From Server: ', serverMessage.decode())

clientMessage = input('Enter message to send to server: ')
# send client message
clientSocket.send(clientMessage.encode())

serverMessage = clientSocket.recv(1024)
# Display message from server
print('From Server: ', serverMessage.decode())

# closes the socket.  end of process.
clientSocket.close()