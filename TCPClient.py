from socket import *
serverPort = 12000
serverHost = ''

#AF_INET betyder den bruger IPv4 hvilke der bruger 32-bit addresses
#SOCK_STREAM betyder den bruger TCP
#AF_INET: address format is host and port number
#SOCK_STRAM : Betyder TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM) #opretter en klientsocket
#Her Initialeres en TCP forbindelse mellem Client og server. 
clientSocket.connect((serverHost,serverPort))
#Input hvro clienten skriver 
sentence = input('Input lowercase sentence:')
#Clienten sender beskeden
clientSocket.send(sentence.encode())
#recv() bruges til at modtage data fra en socket med en given beskrivelse og gemme data midlertidigt."
modifiedSentence = clientSocket.recv(2048)
#decode() bruges til at konvertere en bytes af data til en tekststrnge. 
print ('From Server:', modifiedSentence.decode())
clientSocket.close()