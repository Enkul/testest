import socket
import rc4
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1337  # The port used by the server
key = "SUP3RS3CR3T"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plaintext = input('Enter your plaintext: ')
    ciphertext = rc4.encrypt(plaintext,key)
    # print(ciphertext)
    s.sendall(ciphertext.encode())
    data = s.recv(1024)

print(f"Received {data!r}")

