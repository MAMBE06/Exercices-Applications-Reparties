import socket

hote = "127.0.0.1"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hote, port))

input_str = input("Entrer les donnees a renvoyer : ")
s.sendall(input_str)

print (s.recv(1024))
s.close()