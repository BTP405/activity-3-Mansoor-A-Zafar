import socket
import pickle
import Shared

class TaskClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_task(self, task):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((self.host, self.port))
                serialized_task = pickle.dumps(task)
                server_socket.send(serialized_task)
                result = pickle.loads(server_socket.recv(4096))
                print("Result:", result)
        except Exception as e:
            print(f"Error processing task: {e}")

if __name__ == "__main__":
    # Client configuration
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5555

    # Start a task client
    task_client = TaskClient(SERVER_HOST, SERVER_PORT)

    # Example tasks
    queue = [(Shared.add, 5, 10), (Shared.multiply, 5, 10)]
    
    for job in queue:
        task_client.send_task(job)
