import socket
HOST = "" # удаленный компьютер (localhost)
PORT = 33333 # порт на удаленном компьютере
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send("kso".encode())
result = sock.recv(1024)
sock.close()
print("Получено:", result)