import socket
s = socket.socket()
print ("Socket creer avec succes")
port = 12345
s.bind(('',port))
print ("Socket binded to %s"%(port))
s.listen(5)
print ("Socket is listening")
while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    data = c.recv(1024)
    a = ""
    for i in range (0,len(data)):
        if (data[i]=='a' or data[i]=='e' or data[i]=='i' or data[i]=='o' or data[i]=='u' or data[i]=='y' or data[i]=='A' or data[i]=='E' or data[i]=='O' or data[i]=='I' or data[i]=='U' or data[i]=='Y'): 
            a=a+'#'
        else :
            a=a+data[i]
    if not data:
        break
c.sendall(a)
c.close()