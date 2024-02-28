import socket
import threading
import Shared;

class ChatClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def receive_messages(self):
        try:
            while True:
                message = Shared.deserializeFiles(self.client_socket.recv(Shared.MAX_RECV))
                print(message)
        except KeyboardInterrupt:
            pass

    def send_message(self, message):
        try:
            self.client_socket.send(Shared.serializeFiles(f"{self.name}: {message}"))
        except:
            print("Error: Failed to send message.")

    def disconnect(self):
        self.client_socket.close()

if __name__ == "__main__":
    # Client configuration
    SERVER_HOST = "localhost"
    SERVER_PORT = 12345

    # Start a chat client
    print(f'enter "quit" to leave or CTRL + C')
    client_name = input("Enter your name: ")
    client = ChatClient(SERVER_HOST, SERVER_PORT, client_name)
    # Chat loop
    try:
        while True:
            message = input()
            if message.lower() == "quit":
                client.disconnect()
                break
            client.send_message(message)
    except KeyboardInterrupt:
        client.disconnect()
