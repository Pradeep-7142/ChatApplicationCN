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

# Now we will write a function that will handle new clients
def new_client_controller(clnt_sckt, adr):
    print(f"We have a new connection from {adr}")

    #it will run until whole message from client is not decoded
    while True:
        try:
            msg=clnt_sckt.recv(1024).decode()

            if not msg:
                break

            # now we check the prefix of message
            # if it was a new joinee
            if msg.startswith("JOINING"):
                name_of_user=msg.split(" ",1)[1]
                dict_for_client_username_map[clnt_sckt]=name_of_user

                print(f"{name_of_user} is now in the chat as a new joinee")

                func_to_broadcast(f"{name_of_user} has joined the chat")
            # if it is a message from already joinned member
            elif msg.startswith("MESSAGE"):
                main_mess=msg.split(" ",1)[1]
                name_of_user=dict_for_client_username_map.get(clnt_sckt,"Unknown")

                combined_mess=f"{name_of_user}: {main_mess}"

                print(combined_mess)

                func_to_broadcast(combined_mess, clnt_sckt)
            
            # if client want to quit
            elif msg.startswith("QUITING"):
                name_of_user=dict_for_client_username_map.get(clnt_sckt,"Unknown")
                print(f"{name_of_user} has left the chat ")

                func_to_broadcast(f"{name_of_user} has left the chat")

                break
        except:
            break

    # now if user has left the chat then we can remove its data from
    # our storage of map and array both

    if clnt_sckt in list_of_clients:
        list_of_clients.remove(clnt_sckt)
    
    if clnt_sckt in dict_for_client_username_map:
         del dict_for_client_username_map[clnt_sckt]

    clnt_sckt.close()

# Now we need to start the server by creating another socket
def begin_server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(("127.0.0.1",5000))
    server.listen()

    print("The server has started on port 5000")
    print("The server is waiting for connections to join for chat....\n")

    while True:
        clnt_sock, address=server.accept()

        list_of_clients.append(clnt_sock)

        new_thread= threading.Thread(
            target=new_client_controller,
            args=(clnt_sock,address)
        )
        new_thread.start()


begin_server()