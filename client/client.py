import socket  #It will be used to make network connections using  ipv4(AF_INET) and tcp(SOCK_STREAM)
import threading #we need it to do more than one task at the same time.

def accept_messages(clientSocket): # a common function to capture the message from server and display it.
    while True:
        try:
            mess_recieved=clientSocket.recv(1024).decode() #we will read 1024 bytes at a time and decode them from bytes to readble format
            
            if not mess_recieved:
                print("User has Disconnected  himself from server")
                break
            print(mess_recieved)

        except:
            print("The connection for this user is closed")
            break
    


def begin_client():
    clt=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # we will create a socket  using tcp and ipv4 protocols.
    clt.connect(("127.0.0.1",5000)) # connect to server that is running on localhost at port 5000

    print("Connected to server")

    u_name=input("Please Enter your userName: ") # To recognise different users we ask an username before sending any message

    clt.send(f"JOINNING {u_name}".encode()) # we will notify all other clients that this user with username joined the chat

    recv_thread=threading.Thread( # we will make another thread so that the same client can accept other's messages as well as send his message to all others
        target=accept_messages,
        args=(clt,)
    )

    recv_thread.start()

    while True:
        mess=input("Type a message or type /quit for quitting") # will continue until this client want to quit 

        if mess=="/quit":
            clt.send("QUITTING".encode())
            break
        clt.send(f"MESSAGE {mess}".encode())

    clt.close() # after quiting we can close the client
    print("You have left the chatting")


begin_client()