## 服务器
import socket  # 导入 socket 模块

class user:
    #定义一个用户对象，如果有用户登陆则实例化一个
    def __init__(self,name=0,pwd=0):
        self.name=name
        self.pwd=pwd
    def intro(self):
        print(self.name,self.pwd)


# 配置服务器
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 10000)) # bind(ip,port)
print("服务器已开启，正在监听{}".format(server.getsockname()))

while True:
    #接受客户端的数据
    data, address = server.recvfrom(1024)
    print(data.decode('UTF-8'), address)
    if data:
        sent = server.sendto('已接收到你发来的消息'.encode('UTF-8'), address)

server.close()