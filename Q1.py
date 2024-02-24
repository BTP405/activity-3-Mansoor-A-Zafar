#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.
import pickle;
"""
* The Max value that can be received from a Client or Server
"""
MAX_RECV = 1024;

"""
* This function will returned a pickled object
* -> if the data is a file:
*   -> read the file and put the info into a "content" variable
* -> otherwise assign the 'content' to the @data param
* -> return a pickled object of the content
*
* @data   : the information that will be pickled 
* @is_file: defaulting to True, used to determine how to pickle the object
            (for files, we read the all the content and pickle that, thats why
             files have a special process)
"""
def serializeFiles(data, is_file=True):
    if is_file:
        content = None;
        with open(data, "rb") as f:
            content = f.read(); #get the content
        #we use dumps over dump since we want binary format
    else:
        content = data;
    try:
        return pickle.dumps(content);
    except Exception as e:
        print(f'could not pickle.dumps(content) {e}')

#gets a 'pickled file obj'
#returns an UNpickled file obj
"""
* This function will return an un-pickled object
*
* @data: The information that will be unpickled
"""
def deserializeFiles(data):
    try:
        return pickle.loads(data);
    except Exception as e:
        print(f'could not pickle.loads(data) {e}');


#Takes in a new_file name and a UNpickled file object
"""
* This function will save an un-pickled object to a file
* -> open the file with binary writing
* -> dump the data into the new file 
*
* Note: We use 'wb' since it's a binary pickled file, meaning we need to write with binary too
*
* @new_file: the file that the information from the data will be saved to
* @data    : the information to be put into a file
"""
def saveToDisk(new_file, data):
    with open(new_file, "wb") as f:
        try:
            pickle.dump(data, f);
        except Exception as e:
            print(f'could not pickle.dump(data, f) into new file {e}')

"""
* This function determines the process on the Client's end for the File Transfer
* -> Take input as to which file to read from
* -> pickle the file
* -> send the file to the Server
*
* @client_socket: The current session of the Client 
"""
def question1_client(client_socket):
    print(f'!!! Question 1 !!!');
    file = input("Enter the file name\n> ");
    pickled_file = serializeFiles(file);
    client_socket.send(pickled_file);
    print(f'{client_socket.recv(MAX_RECV).decode()}');

"""
* This function determines the process on the Server's side for the File Transfer
* -> Take input as to which file to save the result to
* -> Receive the pickled object from the client
* -> Save the file to the disk
*
* @client_socket: The current session of the Client
"""
def question1_server(client_socket):
    print("!!! Question 1 !!!");
    server_file = input("Enter the Receiving File\n> ");
    pickled_file = client_socket.recv(1024);
    saveToDisk(server_file, deserializeFiles(pickled_file));
    client_socket.sendall("Successful Trasnfer of files".encode())
    print("!!! Success    !!!");
#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.
