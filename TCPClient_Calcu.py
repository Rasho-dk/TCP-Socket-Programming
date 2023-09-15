from socket import *
serverPort = 12000
serverHost = '172.20.10.4'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost,serverPort))

while True:
    print("Example : 4 + 5")
    inp = input("Enter the operation: ")
    if inp.islower() == 'over':
        break
    clientSocket.send(inp.encode())
    #answer
    modifiedSentence = clientSocket.recv(2048)
    print("Answer is " + modifiedSentence.decode())
    print("Type Over to terminat")
