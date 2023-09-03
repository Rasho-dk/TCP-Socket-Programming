from socket import *
serverPort = 12000
serverHost ='192.168.0.37'
#serverSocket er ligsom en dør som venter at modtage data.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost,serverPort))
#Dvs. at der er en plads til ventende forbindelse i køen. 
serverSocket.listen(1)
print ('The server is ready to receive')
#while True:
# -accept() : en metod der venter på en forbindelse fra client side
# -Når forbindelse bliver oprettes, bliver der oprettet en ny Socket i Serve som hedder ('connectionSocket')
# -addr : Clientes adresse oplysninger (IP-adresse og portnummer) er gemt i 'addr'
# -ConnectionSocket: bruges til at kommunikere med den specifikke klient, som har oprettet forbinedelsen til server.
#(bruges til at sende/modtager data)
#Når alt går godt så oprettes en *TCP* connection mellem klient "clientSocekt" og Server(ConnectionSocket)
#Data sende ved "bytes" i rækkefølge 
connectionSocket, addr = serverSocket.accept() 
#modtager data fra clienten
print(f'Connected by {addr}')
sentence = connectionSocket.recv(1024).decode()
#laver beskeden om til store bogstaver
capitalizedSentence = sentence.upper()
#sender beskeden tilbage til clienten
#encode() metoden bruges til at konvertere tekststregnen til en sekvens af bytes ved hjælp af (den tilfælde UTF-8)
connectionSocket.send(capitalizedSentence.encode())
#lukker forbindelsen
connectionSocket.close()