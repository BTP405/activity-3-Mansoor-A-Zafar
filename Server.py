import multiprocessing;
import socket;
import Q1;
import Q2;
import Q3;

HOST = 'localhost';
PORT = 12345;

def main(server_socket, workers, lock):
    while True:
        conn, address = server_socket.accept()
        Q1.question1_server(conn)
        Q2.question2_server(conn)
        with lock:
            workers.append(conn)
        process = multiprocessing.Process(target=Q3.handle_client, args=(conn, workers, lock))
        process.start()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    manager = multiprocessing.Manager()
    workers = manager.list()
    lock = manager.Lock()  # Add a lock for synchronization

    try:
        main(server_socket, workers, lock)
    except:
        print("Closing Server...")
    finally:
        with lock:  # Acquire lock before closing connections
            for worker_conn in workers:
                worker_conn.close()
        server_socket.close()
