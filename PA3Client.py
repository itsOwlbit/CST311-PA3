# Names: 
# Date: May XX, 2022
# Title: PA3Client.py
# Description: This is a TCP client program that connects to a server.  The server takes
# two client connections.  When two clients are connected, this client will receive a
# message that it is connected.  Both client programs are threaded on the server and
# only after both clients send a message to the server will there be a response
# indicating which of the clients sent their message first and what it was.
# The program terminates after the 2nd message from the server is received.
# NOTE:  Takes two command line arguments.  Use command (or use default values):
#   python3 <filename.py> serverName serverPort

# socket module used for network communications
from socket import *
# for commandline arguments
import sys

serverName = '10.0.0.2'     # The ip address of server (h2 on mininet set as server)
serverPort = 12000          # The server port to be used

# create TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Check for command line arguments
# If there are 3 (0: filename, 1: serverName, 2: serverPort)
if len(sys.argv) == 3:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

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