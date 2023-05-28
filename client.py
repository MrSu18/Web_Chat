import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    msg = "发送消息到服务器".encode('utf-8')
    sent = client.sendto(msg, ('localhost', 10000)) #socket.sento(msg,(ip,port))
    data, server = client.recvfrom(4096)
    print(data.decode())
finally:
    client.close()