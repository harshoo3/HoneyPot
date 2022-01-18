import socket
from getpass import getpass

def get_connection():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Enter your IPv4 address
    soc.connect(('172.22.0.1', 23))
    
    user_name = input(soc.recv(1024).decode("utf-8"))
    soc.send(bytes(str(user_name),'utf-8'))
    pwd = getpass(soc.recv(1024).decode("utf-8"))
    soc.send(bytes(str(pwd),'utf-8'))
    print(soc.recv(1024).decode("utf-8"))

    while True:
        command = input(soc.recv(1024).decode("utf-8")+'>')
        soc.send(bytes(str(command),'utf-8'))
        print(soc.recv(1024).decode("utf-8"))

get_connection()