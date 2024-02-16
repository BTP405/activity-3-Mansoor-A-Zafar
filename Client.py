import socket;
import Q1;

MAX_RECV = 1024;

def run_client(file):
    client_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server_address = ('localhost', 12345);
    client_socket.connect(server_address);

    try:
        #change this to file_path later
        message = Q1.serializeFiles("test.txt");
        client_socket.sendall(message);
        #Doesn't need to recieve anything from the serverr
    except:
        print(f'Err, something went wrong :(');
    finally:
        client_socket.close();

def main():
    file = __file__.replace(f'Client.py', "me.txt");
    run_client(file);

if __name__ == "__main__":
    main();