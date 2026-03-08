Welcome to my chat Application: 

#########################################
I've created a Python chat program that makes use of socket programming. I decided to employ the client-server architecture. This allows several clients to connect to a single server and communicate with one another. Multiple connections can be accepted simultaneously by the server, which will then forward those messages to each client that is connected. 

Every time a client connects to the server, it will forward the message to every other client that is connected to the server. 

I decided to use TCP sockets for this chat program in order to ensure dependable communication.

#######################################

To demand the following: 
Python  must be installed. 
To run the application, no external libraries are required. 

#########################################
To operate the server: 

Before any client can connect, the server needs to be operational. Go to the server's directory, launch the terminal, and type the following command to start the server: 
 python server.py in terminal and run it.


The server will wait for clients to connect to it after it has started. 

#######################################
To manage the client: 

To launch a client, open the terminal, navigate to the client's directory, and execute the following command: 

Python client.py
You will then be prompted to enter your name by the client program.


#########################################
To simulate multiple users taking part in the chat, you can then run multiple instances of the client from multiple terminals. 


I have used  Three prefixes to tell server what to do with the message recieved from client:

1. JOINING:  This will tell that send a joining message to all for this client 
2. MESSAGE: This will tell that this is actual message sent by already joined client
3. QUITING: This will tell server to send a quit message to all that this user is quiting the chat

#########################################

These Features of This Chat:

A maximum of 255 clients can be served concurrently by the server.

When a client sends a message, the server replies by sending the same message to every client that is presently connected to the server.

When a client connects or disconnects from the server, the server notifies all connected clients.

When a client disconnects from the chat, the server will be aware of it.

######################################

Thankyou.