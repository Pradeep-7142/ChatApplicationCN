# Chat Application (Socket Programming)

# Overview
This project is about the implementing a  simple multi-client chat application. I have used python scokets to implement it. This system includes a client-server architecture where a server is at the center and this mananges the communication between all connected clients simultaneously.

This application will work in terminal where we can make multiple clients by launching a new tab in terminal.

User can enter the chat , send the messages and they will also recieve messages from other users that are currently active in the chat.

# Features

More than one client or user can join and chat simultaneously
Messages will be sent to all the participants
Notification when any new user join as well as leave the chat
Time stamp is added with every message to track the record
Empty message are handled 
Long messages are also not allowed to send once.You can send in small sentences
It will also notify when any user unexpectedly leaves the chat or closes the terminal


# Project Structure
ChatAppCn/
|
|__ server.py
|__ client.py
|__ Readme.md
|__Report.pdf

server.py: This file handles all client connectins and broadcasts messages
client.py: This file allows users to connect and communicate with all participants

# Requirements
python must be installed.
No external libraries are required.

# How to run the porject
1. Firslty Start the server
Open a terminal and then run this command : python server.py
hit enter

server output example:
The server has started on port 5000
Ther server is waiting for connections to join for chat...

2. Start Clients
Open multiple terminals and run same command in all : python client.py

enter a username when you see a message saying to do the same.
example: pradeep

3. Type and send messages
4. Leave the chat by typing /quit and hint enter.

# Example Chat
[10:10:01] User 1 joined the chat
[10:20:05] User 2: hello everyone
[12:02:01] User 1 left the chat


# Handelling The Edge cases
Empty messages are not allowed. Messages only containing whitspaces will not be sent

Messages that are out of the length will not be sent and told that send in small parts

If a client closes the terminal or any other unexpected thing happen then a message will be sent to all and user will be removed from the chat.

# Author
Pradeep Kumar

Thankyou !