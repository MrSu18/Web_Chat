## 服务器
import socket  # 导入 socket 模块

class user:
    #定义一个用户对象，如果有用户登陆则实例化一个
    def __init__(self,name=0,pwd=0,address=(0,0)):
        self.name=name
        self.pwd=pwd
        self.address=address
    def intro(self):
        print(self.name,self.pwd,self.address)

def User_Login(address):
    # 文本读写获取用户密码进行核对
    server.sendto('请输入用户名:'.encode('UTF-8'), address)
    data, address = server.recvfrom(1024)
    user_name=data.decode('UTF-8')
    file=open('UserAccount.txt','r')
    for line in file: #把文件的每一行都给line
        line=line.strip().split(',') #分割出[用户名，密码]的列表
        if line[0]==user_name:
            server.sendto('请输入密码:'.encode('UTF-8'), address)
            data, address = server.recvfrom(1024)
            key=data.decode('UTF-8')
            if key==line[1]:
                server.sendto('登陆成功'.encode('UTF-8'), address)
                return 1
    return 0

# 配置服务器
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 10000)) # bind(ip,port)
print("服务器已开启，正在监听{}".format(server.getsockname()))

while True:
    #接受客户端的数据
    data, address = server.recvfrom(1024)
    if data.decode('UTF-8')=='请求登陆':
        User_Login(address)

server.close()