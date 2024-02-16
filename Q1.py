#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.
import pickle;

#This function will 
# -> Pickle a file
# -> returned pickle obj
def serializeFiles(file_path):
    content = None;
    with open(file_path, "rb") as f:
        content = f.read(); #get the content
    
    #we use dumps over dump since we want binary format
    try:
        return pickle.dumps(content);
    except:
        print('could not pickle.dumps(content)')

#gets a 'pickled file obj'
#returns an UNpickled file obj
def deserializeFiles(data):
    try:
        return pickle.loads(data);
    except:
        print('could not pickle.loads(data)');


#Takes in a new_file name and a UNpickled file object
def saveToDisk(new_file, data):
    with open(new_file, "wb") as f:
        try:
            pickle.dump(data, f);
        except:
            print('could not pickle.dump(data, f) into new file')
        


saveToDisk("res.txt", deserialize(serialize("test.txt")));
#Passed Tests

#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.
