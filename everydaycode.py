#server side code

import socket

server = socket.socket()
print("socket created")

server.bind(("localhost",9999))

server.listen(3) #listen upto 3 hosts

print("waiting for connections")

while True:
    client,address = server.accept() #accept the ip address and client socket

    name =  client.recv((1024)).decode()
    print("connected with", address , name)
    client.send(bytes("welcome to rajNetworks","utf-8"))
    client.close()

#

#client side code

import socket

client = socket.socket()

client.connect(("localhost", 9999))

name = input("enter your name: ")

client.send(bytes(name, "utf-8"))

print(client.recv(1024).decode())
