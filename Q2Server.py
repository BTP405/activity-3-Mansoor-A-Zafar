import socket
import threading
import pickle

class TaskServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.workers = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Task server started on {self.host}:{self.port}")

    def handle_worker(self, worker_socket, worker_address):
        try:
            while True:
                task_data = worker_socket.recv(4096)
                if not task_data:
                    break  # If no data received, break the loop
                task_data = pickle.loads(task_data)
                task, *args = task_data
                result = task(*args)  # Execute the task with arguments
                worker_socket.send(pickle.dumps(result))
        except Exception as e:
            print(f"Error processing task: {e}")
        finally:
            print(f"Worker {worker_address} disconnected.")
            self.remove_worker(worker_socket)

    def add_worker(self, worker_socket):
        self.workers.append(worker_socket)
        print(f"Worker {worker_socket.getpeername()} connected.")

    def remove_worker(self, worker_socket):
        if worker_socket in self.workers:
            self.workers.remove(worker_socket)
            worker_socket.close()

    def start(self):
        try:
            while True:
                worker_socket, worker_address = self.server_socket.accept()
                self.add_worker(worker_socket)
                worker_thread = threading.Thread(target=self.handle_worker, args=(worker_socket, worker_address))
                worker_thread.start()
        except KeyboardInterrupt:
            print("Shutting down the task server.")
            self.server_socket.close()

if __name__ == "__main__":
    # Server configuration
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5555

    # Start the task server
    server = TaskServer(SERVER_HOST, SERVER_PORT)
    server.start()
