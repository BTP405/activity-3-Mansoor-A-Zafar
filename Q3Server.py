import socket
import threading
import Shared;

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Chat server started on {self.host}:{self.port}")

    def broadcast_messages(self, message, sender):
        for client in self.clients:
            if client != sender:
                try:
                    client.send(Shared.serializeFiles(message))
                except:
                    self.remove_client(client)

    def handle_client(self, client_socket, client_address):
        try:
            while True:
                message = Shared.deserializeFiles(client_socket.recv(Shared.MAX_RECV))
                self.broadcast_messages(message, client_socket)
        except:
            pass

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)

    def start(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                self.clients.append(client_socket)
                print(f"Client {client_address} connected.")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Shutting down the server.")
            self.server_socket.close()

if __name__ == "__main__":
    # Server configuration
    SERVER_HOST = "localhost"
    SERVER_PORT = 12345

    # Start the chat server
    server = ChatServer(SERVER_HOST, SERVER_PORT)
    server.start()
