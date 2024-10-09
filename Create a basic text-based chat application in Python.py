import socket
server = socket.socket()
server.bind(("",5000))
server.listen()
connection,adress =server.accept()
print(f"new connection from : {adress}")

while True:
    recieved = connection.recv(1024).decode()
    print(f"client : {recieved}")
    message = input(">>")
    connection.send(message.encode())
    