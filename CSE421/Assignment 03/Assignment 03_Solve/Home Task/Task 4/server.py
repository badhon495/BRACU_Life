import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def calculate_salary(hours_worked):
    if hours_worked <= 40:
        salary = hours_worked * 200
    else:
        salary = 8000 + (hours_worked - 40) * 300
    return salary

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg:
                hours_worked = int(msg)
                salary = calculate_salary(hours_worked)
                conn.send(str(salary).encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print("[LISTENING] Server is Listening")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

print("[STARTING] Server is starting...")
start()
