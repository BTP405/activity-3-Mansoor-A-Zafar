import socket
import Shared;
HOST = "localhost"
PORT = 12345

def question_one(client_socket):
    print(f'!!! Question 1 !!!');
    file = input("Enter the file name\n> ");
    pickled_file = Shared.serializeFiles(file, True);
    client_socket.send(pickled_file);
    print(f'{client_socket.recv(Shared.MAX_RECV).decode()}');

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    question_one(client_socket);
    
