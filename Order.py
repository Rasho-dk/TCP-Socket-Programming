from socket import *
import threading

def handle_client(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode().strip()
        print(sentence)
        response = "Didn't understand, please send a proper message"
        if sentence == "stop":
            keep_communicating = False
            response = "closing the connection"
        elif sentence[-8:] == ",,,upper":
            sentence = sentence[:-8]
            response = sentence.upper()
        elif sentence[-8:] == ",,,lower":
            sentence = sentence[:-8]
            response = sentence.lower()
        elif sentence[-10:] == ",,,reverse":
            sentence = sentence[:-10]
            response = sentence[::-1] + "\n"
        elif sentence[-8:] == ",,,count":
            sentence = sentence[:-8]
            response = str(sentence.__len__())
        elif sentence[-11:] == ",,,swapcase":
            sentence = sentence[:-11]
            response = sentence.swapcase()
        connectionSocket.send(response.encode())
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()