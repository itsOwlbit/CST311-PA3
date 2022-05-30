# Names: 
# Date: May XX, 2022
# Title: PA3ChatClient.py
# Description: This is a TCP client program that ...

# socket module used for network communications
from socket import *
# for threading send and receive
import threading
# for command line arguments
import sys
import time

'''
This is a thread function for receiving messages from the server.
'''
def receive(cSocket, threads):
    with cSocket:
        while True:
            try:
                message = cSocket.recv(1024).decode()
                print(message)
                # 'bye' is the exit chat keyword
                if 'bye' in message.lower():
                    break
            except:
                break
            
'''
This is a thread function for sending messages from the client to the other
client with the server as the helper.
'''
def send(cSocket, threads):
    with cSocket:
        while True:
            try:
                message = input('')
                if message:
                    cSocket.send(message.encode())
                # 'bye' is the exit chat keyword
                if 'bye' in message.lower():
                    break
            except:
                break
    
"""
This is the main function.
"""
def main():
    serverName = '127.0.0.1'    # The ip address of server
    serverPort = 12000          # The server port to be used

    threads = []    # List of the thread processes

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

    # Create send and receive message threads
    sendThread = threading.Thread(target=send, args=(clientSocket, threads))
    threads.append(sendThread)
    receiveThread = threading.Thread(target=receive, args=(clientSocket, threads))
    threads.append(receiveThread)

    # Setting send thread as the daemon thread
    sendThread.setDaemon(True)

    # Start threads
    sendThread.start()
    receiveThread.start()

    # Wait for non-daemon thread to finish
    receiveThread.join()

    time.sleep(2)

    clientSocket.close()

"""
Start the program by running Main()
"""
if __name__ == '__main__':
    main()

