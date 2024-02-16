import pickle;
import socket;
import Q1;

MAX_RECV = 1024;

def run_server():
    # Socket will use -> IPv4 & TCP
    server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server_address = ('localhost', 12345);
    server_socket.bind(server_address);
    server_socket.listen(1);

    print(f'Listening for incoming connections...');

    while True:
        #Accept the connection
        client_socket, client_address = server_socket.accept();
        try:
            data = Q1.deserializeFiles(client_socket.recv(MAX_RECV)); #is a unpickled file object
            Q1.saveToDisk("res.txt", data); 
        except:
            print(f'Erorr, something went wrong');
        finally:
            client_socket.close();

if __name__ == "__main__":
    run_server();