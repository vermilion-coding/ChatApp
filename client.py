import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER_PORT = 8180
SERVER_IP = socket.gethostbyname(socket.gethostname())

def send_message(msg, client_socket):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    msg_length = str(msg_length).encode(FORMAT)
    msg_length += b' ' * (HEADER - len(msg_length))

    client_socket(msg_length)
    client_socket(message)

def start_client():
    SERVER_ADDR = (SERVER_IP, SERVER_PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDR)
    msg = input("Enter the messsage to be sent to server (Type quit to exit)")
    while msg != 'quit':
        send_message((msg, client_socket))
        msg = input("Enter the message to be sent to server (Type quit to exit)")
    send_message(DISCONNECT_MESSAGE, client_socket)
    client_socket.close()
    print("[EXIT] Sending Disconnect request to server")

start_client()
