#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.

import Q1;
"""
* This function will broadcast to the current Client the response from the Server
* coming from any client
* 
* @client_socket: the current Client connected to the Server
"""
def handle_server(client_socket):
    try:
        while True:
            data = Q1.pickle.loads(client_socket.recv(Q1.MAX_RECV));
            if not data:
                break;
            print(f'> {data}');
    except:
        print('Err closing connection')

"""
* This function will recieve a pickled object
* -> unpickle it
* -> print it to all the connected workers
"""
def handle_client(connection, workers, lock):
    try:
        while True:
            data = Q1.pickle.loads(connection.recv(Q1.MAX_RECV))
            if not data:
                break
 
            # Acquire the lock before accessing and modifying the workers list
            with lock:
                for worker_conn in workers:
                    worker_conn.sendall(Q1.pickle.dumps(data))
    except:
        print('Error processing task')
    finally:
        connection.close()

#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.