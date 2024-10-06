import socket

HEADER = 16
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "End"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_hours(hours):
    message = str(hours).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    salary = client.recv(2048).decode(FORMAT)
    print(f"Salary: Tk {salary}")





connected=True
while connected:
    hours_worked = int(input("Enter the number of hours worked: "))
    if hours_worked !="I'm done":
        send_hours(hours_worked)
    else:
        connected=False
        client.send(DISCONNECT_MESSAGE.encode(FORMAT))
