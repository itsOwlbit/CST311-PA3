# Names: 
# Date: May XX, 2022
# Title: PA3Server.py
# Description: This is a TCP server program that uses threads with two client programs
# that connect to it.  Both client programs must be connected before the server
# sends a message to both clients that they have been connected to the server.
# The server then waits for both clients to send a message to the server before
# sending the same output to both clients indicating the order in which the client's
# messages was received by the server and the message they both sent.
# After both client threads close, the server does some final messages and terminates.

# Question: Explain why you need multithreading to solve this problem.
# Answer: 

# socket module used for network communications
from socket import *
# for threading 2 clients
import threading
# for sleep while waiting for the threads to close
import time

serverPort = 12000                              # set listening port
serverSocket = socket(AF_INET, SOCK_STREAM)     # create TCP socket with IPv4

"""
This function is used by threads processes of two connected clients so that
they can function in parallel.
"""
def thread_function(connectionSocket, client, mList):
    # Send acknowledgement to clients that they are connected
    sMessage = 'Client {} connected'.format(str(client))
    connectionSocket.send(sMessage.encode())

    # Receive and store messages into list
    rMessage = connectionSocket.recv(1024).decode()
    mList.append(client + ': ' + rMessage)
    print('Client {} sent message {}: {}'.format(str(client), len(mList), rMessage))

    # Loop until client X and Y messages are received and stored in mList (messages list)
    while True:
        if(len(mList) == 2):
            break

    # Send final message result to clients showing message receiving order
    sMessage = mList[0] + ' recieved before ' + mList[1]
    connectionSocket.send(sMessage.encode())

    connectionSocket.close()

"""
This is the main function.
"""
def Main():
    threadCount = 0     # counter used to know which client connected first.  0 = X, 1 = Y
    threads = []        # list of threads [0] = X, [1] = Y
    clientValue = ''    # used to pass client char to its thread
    messages = []       # list of messages from client in order received

    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)
    print('The server is waiting to receive 2 connections....\n')

    # Create thread processes using accepted connections for max connections (2)
    for threadCount in range(2):
        connectionSocket, addr = serverSocket.accept()

        # Output which client connected first and set their client value to be passed to its thread
        if threadCount == 0:
            clientValue = 'X'
            print('Accepted first connection, calling it client {}'.format(clientValue))
        else:
            clientValue = 'Y'
            print('Accepted second connection, calling it client {}\n'.format(clientValue))

        # create thread and add to threads list
        process = threading.Thread(target=thread_function, args=(connectionSocket, clientValue, messages))
        threads.append(process)
        threadCount += 1

    # Start thread processes after max number of threads are received (2)
    print('Waiting to receive messages from client X and client Y....\n')
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('\nWaiting a bit for clients to close their connections')
    time.sleep(2)

    print('Done.')
    serverSocket.close()

"""
Start the program by running Main()
"""
if __name__ == '__main__':
    Main()
