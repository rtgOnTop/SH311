import socket
import subprocess
from sys import argv


print("""
SH311
 $$$$$$\  $$\   $$\  $$$$$$\    $$\     $$\   
$$  __$$\ $$ |  $$ |$$ ___$$\ $$$$ |  $$$$ |  
$$ /  \__|$$ |  $$ |\_/   $$ |\_$$ |  \_$$ |  
\$$$$$$\  $$$$$$$$ |  $$$$$ /   $$ |    $$ |  
 \____$$\ $$  __$$ |  \___$$\   $$ |    $$ |  
$$\   $$ |$$ |  $$ |$$\   $$ |  $$ |    $$ |  
\$$$$$$  |$$ |  $$ |\$$$$$$  |$$$$$$\ $$$$$$\ 
 \______/ \__|  \__| \______/ \______|\______|
 made by rtgOnTop
-----------------------------
# type in "continue" if you #
# want to use this tool     #
-----------------------------                              
 """)
first_user_input = input("[*]")
if first_user_input.lower() == "continue":
 port = 8080
 host = '127.0.0.1'
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(20)
        print(f"Listen on port {port}")

        conn, addr = s.accept()  # Wait for a connection
        with conn:
            print('Connected by', addr)
            while True:
                cmd = input(f"{argv}$")
                if cmd:
                    try:
                        conn.sendall(cmd.encode())  # Send the command to the client
                        data = conn.recv(1024).decode()  # Receive the output from the client
                        print(data)
                        continue
                    except subprocess.CalledProcessError as e:
                        conn.sendall(f"Command failed with return code {e.returncode}".encode())
                        continue
                    except Exception as e:
                        conn.sendall(f"An error occurred: {str(e)}".encode())
                        continue
    

