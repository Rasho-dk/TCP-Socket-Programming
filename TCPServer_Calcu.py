from socket import *
import threading
    #TCP port 12000 uses the Transmission Control Protocol
    #CP enables two hosts to establish a connection and exchange streams of data.
def handle_client(connectionSocket, addr): 
    print(f'Connected {addr}')
    try:
        connectionSocket.send("Hello : \n".encode()) 
        while keep_cummunicating:
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
    except ConnectionResetError:
        print("Server is close")
    except ConnectionAbortedError:
        print("Connection is dead")

serverPort = 12000
serverHost = '10.200.160.105'
servertSocket=socket(AF_INET, SOCK_STREAM) #create a TCP/IP client socket object IPV4 socket of TVP stream type
servertSocket.bind((serverHost, serverPort))
servertSocket.listen(1)
print("The server is ready to receive")
print("Wating for client request")

keep_cummunicating = True
while True: 
    connectionSocket, addr = servertSocket.accept()
    # Server is able to handle more then one clinte at the same time.
    #Threading is running code simultaneously with other code. In this case, 
    #we need to be able to have several handleClient calls running at the same time.
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()



