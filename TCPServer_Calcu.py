from socket import *
#TCP port 12000 uses the Transmission Control Protocol
#CP enables two hosts to establish a connection and exchange streams of data.
serverPort = 12000
serverHost = '172.20.10.4'
servertSocket=socket(AF_INET, SOCK_STREAM) #create a TCP/IP client socket object
servertSocket.bind((serverHost, serverPort))
servertSocket.listen(1)
print("The server is ready to receive")
print("Wating for client request")

connectionSocket, addr = servertSocket.accept()
print(f'Connected {addr}')

while True:
    sentence = connectionSocket.recv(1024).decode()
    if sentence.islower() == 'Over':#.islower():
        print("Connection is over")
        break
    print("Equation is received")
    print("Calculating...")
    result = 0
    # Index 0 : receive  str and convert str to int 
    # Index 1 : handel the opertor choice 
    # Index 2 : receive str and convert str to int
    if sentence[1] == '+':
        result = int(sentence[0]) + int(sentence[2])
    elif sentence[1] == '-':
        result = int(sentence[0]) - int(sentence[2])
    elif sentence[1] == '*':
        result = int(sentence[0]) * int(sentence[2])
    elif sentence[1] == '/':
        result = int(sentence[0]) / int(sentence[2])
    else:
        print("Wrong input")
        print('Result:',result,'\n')
    connectionSocket.send(str(result).encode())
    print("Result is sent")
connectionSocket.close()