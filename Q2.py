#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

import Q1;

"""
* This function will take in a function, send it to the Server, print the response from the Server
*
* @client_socket: The current socket for this session
* @func         : The function being sent over to the Server
* @args         : The arguments for the @func
"""
def question2_client(client_socket, func, args):
    task = Q1.serializeFiles((func, args), False);
    client_socket.sendall(task);
    res = Q1.deserializeFiles(client_socket.recv(Q1.MAX_RECV));

    print(f'result: {res}');

"""
* This function will receive the pickled object
* -> break it down into the function and arguments
* -> send to the Client the result of the function with its arguments
*
* @client_socket: The socket of the current session
"""
def question2_server(client_socket):
    task = client_socket.recv(Q1.MAX_RECV);
    print(f'got task: {task}')
    task_function, args = Q1.deserializeFiles(task);
    result = task_function(*args);
    client_socket.sendall(Q1.serializeFiles(result, False));

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.