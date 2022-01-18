import socket
from getpass import getpass

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 23))

user_name = input(soc.recv(1024).decode("utf-8"))
soc.send(bytes(str(user_name),'utf-8'))
pwd = getpass(soc.recv(1024).decode("utf-8"))
soc.send(bytes(str(pwd),'utf-8'))
print(soc.recv(1024).decode("utf-8"))

while True:
    command = input(soc.recv(1024).decode("utf-8")+'>')
    soc.send(bytes(str(command),'utf-8'))
    print(soc.recv(1024).decode("utf-8"))

# import paramiko
# import sys

# results = []
# def connect():
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.connect('192.168.1.9',username='HarshSeta',password='qwerty',port=23)
#     ssh_stdin,ssh_stdout,ssh_stderr = client.exec_command('ls')

#     for line in ssh_stdout:
#         results.append(line.strip('\n'))

# connect()
# for i in results:
#     print(i.strip())

# sys.exit()