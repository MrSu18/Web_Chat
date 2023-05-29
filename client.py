import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 给服务器发送请求登陆的信号
msg = '请求登陆'.encode('UTF-8')
sent = client.sendto(msg, ('localhost', 10000))
data, server = client.recvfrom(4096)
# 输入用户名发送给服务器查询
if data.decode('UTF-8')=='请输入用户名:':
    print(data.decode('UTF-8'))
    user_name=input().encode('UTF-8')
    client.sendto(user_name, ('localhost', 10000))
    data, server = client.recvfrom(4096)
# 输入密码给服务器
if data.decode('UTF-8')=='请输入密码:':
    print(data.decode())
    password=input().encode('UTF-8')
    client.sendto(password, ('localhost', 10000))
    data, server = client.recvfrom(4096)
print(data.decode())

# 关闭客户端
client.close()