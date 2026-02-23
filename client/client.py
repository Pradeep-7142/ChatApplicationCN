import socket
import threading

def accept_messages(clientSocket):
    while True:
        try:
            mess_recieved=clientSocket.recv(1024).decode()
            
            if not mess_recieved:
                print("User has Disconnected  himself from server")
                break
            print(mess_recieved)

        except:
            print("The connection for this user is closed")
            break
    clientSocket.close()


def begin_client():
    clt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clt.connect(("127.0.0.1",5000))

    print("Connected to server")

    u_name=input("Please Enter your userName: ")

    clt.send(f"JOINNING {u_name}".encode())

    recv_thread=threading.Thread(
        target=accept_messages,
        args=(clt,)
    )

    recv_thread.start()

    while True:
        mess=input("Type a message or type /quit for quitting")

        if mess=="/quit":
            clt.send("QUITTING".encode())
            break
        clt.send(f"MESSAGE {mess}".encode())

    clt.close()
    print("You have left the chatting")


begin_client()