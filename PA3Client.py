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

# client initiates contact with server
# establishing a TCP connection between client and server
# a three-way handshake happens in the background
clientSocket.connect((serverName, serverPort))

# prompts user for sentence
sentence = input('Input lowercase sentence: ')

# send sentence into socket
clientSocket.send(sentence.encode())

# read reply from socket
modifiedSentence = clientSocket.recv(1024)

# displays the message converted from bytes to string
print('From Server: ', modifiedSentence.decode())

# closes the socket.  end of process.
clientSocket.close()