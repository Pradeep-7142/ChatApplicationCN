import socket
import threading


# we need a list to store clients socket dynamically
list_of_clients=[]

# we need client socket to username mapping so that
# we can tell which sender sent this message
dict_for_client_username_map={}


# we need a function to send the message from one sender 
# to all other chat participants (broadcasting)
def func_to_broadcast(mess, clnt_sock=None):
    for clnt in list_of_clients:
        # Here we are making sure that the message 
        # should not sent  back to the sender
        if clnt!=clnt_sock:
            try:
                clnt.send(mess.encode())
            except:
                clnt.close()
                list_of_clients.remove(clnt)

