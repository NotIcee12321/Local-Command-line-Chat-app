import socket

def recv_data(client_socket):
    data = client_socket.recv(1024).decode("utf-8")
    print(f"Client: {data}")
    return data

def procces_data(data):
    data_split = data.split()
    command = data_split[0]
    commands = {
        "register_commands": ["register", "r"],
        "login_commands": ["login", "l"]
    }

    try:
        if command in commands["register_commands"]:
            username = data_split[1]
            password1 = data_split[2]
            password2 = data_split[3]
            if password1 == password2:
                with open("db.txt", "a") as database:
                    database.write(f"{username} {password1}\n")
                response = "Registered successfully."
                print(f"{username}: Registered successfully.")
            else:
                response = "Password didn't match!"
        elif command in commands["login_commands"]:
            username = data_split[1]
            password = data_split[2]
            login_data = f"{username} {password}"
            with open("db.txt", "r") as database:
                lines = database.readlines()
                for line in lines:
                    if login_data.strip() == line.strip():
                        print(f"{client_address}: Login successfully.")
                        response = "Login successfully."
                        break
                else:
                    response = "Wrong username or password!"
                    print(f"{client_address}: Wrong username or password!")
        else:
            response = "Wrong command!"
            print(f"Client: Wrong command!")

        return response
    except Exception as e:
        print(f"Error: {e}")
        return "Error!"

def send_data(client_socket, response):
    client_socket.send(response.encode("utf-8"))

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST} {PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} connected!")

    data = recv_data(client_socket)
    response = procces_data(data)
    send_data(client_socket, response)

    client_socket.close()

