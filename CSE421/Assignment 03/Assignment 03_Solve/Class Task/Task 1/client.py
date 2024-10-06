import socket

HEADER = 16
PORT = 5050

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "End"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)

    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(f"Client's IP address is {SERVER} and Client's Device name is {socket.gethostname()}")
send(DISCONNECT_MESSAGE)
