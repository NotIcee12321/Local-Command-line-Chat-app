import socket

def send_data(client_socket):
    data = input("> ")
    client_socket.send(data.encode("utf-8"))

def recv_data(client_socket):
    data = client_socket.recv(1024).decode("utf-8")
    print(data)

PORT = 5050
HOST = input("Enter host ip: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print("Connected successfully.")
except ConnectionRefusedError:
    print("You can't connect to this host!")
except Exception as e:
    print(f"error: {e}")

while True:
    send_data(client_socket)
    recv_data(client_socket)