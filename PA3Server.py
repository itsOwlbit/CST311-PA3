# Names: 
# Date: May XX, 2022
# Title: PA3Server.py
# Description: This is a TCP server program that ...

# Question: Explain why you need multithreading to solve this problem.
# Answer: 

# socket module used for network communications
from email import message
from socket import *

# for threading 2 clients
import threading

serverPort = 12000                              # set listening port
serverSocket = socket(AF_INET, SOCK_STREAM)     # create TCP socket with IPv4
# serverSocket.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)

messages = []

def thread_function(connectionSocket, client):
    sMessage = 'Client {} connected'.format(str(client))
    connectionSocket.send(sMessage.encode())

    rMessage = connectionSocket.recv(1024).decode()
    messages.append(client + ': ' + rMessage)
    print('Client {} sent message {}: {}'.format(str(client), len(messages), rMessage))

    while True:
        if(len(messages) == 2):
            break

    sMessage = messages[0] + ' recieved before ' + messages[1]
    connectionSocket.send(sMessage.encode())

    # close connection socket
    # server socket is still open
    connectionSocket.close()

def Main():
    threadCount = 0
    threads = []        # list of threads
    clientValue = ''

    serverSocket.bind(('', serverPort))
    serverSocket.listen(2)      # maximum number of queued connections is 2
    print('The server is waiting to receive 2 connections....\n')

    # Create thread processes using accepted connections for max connections (2)
    for threadCount in range(2):
        connectionSocket, addr = serverSocket.accept()

        if threadCount == 0:
            clientValue = 'X'
            print('Accepted first connection, calling it client {}'.format(clientValue))
        else:
            clientValue = 'Y'
            print('Accepted second connection, calling it client {}\n'.format(clientValue))

        process = threading.Thread(target=thread_function, args=(connectionSocket, clientValue))
        threads.append(process)
        threadCount += 1

    # Start thread processes after max number of threads is reached (2)
    print('Waiting to receive messages from client X and client Y....\n')
    threads[0].start()
    threads[1].start()

    for t in threads:
        t.join()

    print('\nWaiting a bit for clients to close their connections')

    print('Done.')
    serverSocket.close()

if __name__ == '__main__':
    Main()
