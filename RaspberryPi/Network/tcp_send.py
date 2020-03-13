import socket              # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.0.16'
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
#s.send("Hello server!")
f = open('test_send.txt','rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.sendall(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
s.shutdown(socket.SHUT_WR) # Close the socket when done
print(s.recv(1024))
s.close()