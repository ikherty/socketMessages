import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('ksoo'.encode())

data = sock.recv(1024)
sock.close()

print (data)

#https://xn--90aeniddllys.xn--p1ai/ochen-prostoj-chatklient-server-na-python/
#https://www.ibm.com/developerworks/ru/library/l-python_part_10/
