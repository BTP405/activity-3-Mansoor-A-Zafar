import socket
import pickle
import multiprocessing
import Q1  # Import from the correct module or path
import Q2  # Import from the correct module or path
import Q3  # Import from the correct module or path
import tasks  # Import from the correct module or path

HOST = 'localhost'
PORT = 12345

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    process = None

    try:
        Q1.question1_client(client_socket)  # Send file transfer request first
        queue = [(tasks.my_task, (1,2))];
        for func, args in queue:
            Q2.question2_client(client_socket, func, args);    
        # Q2.question2_client(client_socket, tasks.my_task, (1, 2))
        process = multiprocessing.Process(target=Q3.handle_server, args=(client_socket,))
        process.start()

        while True:
            message = input()
            pickled_message = pickle.dumps(message)
            client_socket.sendall(pickled_message)

    except KeyboardInterrupt:
        print("Closing client")
        if process is not None:
            process.terminate()  # Terminate Q3 process as well
        client_socket.close()
