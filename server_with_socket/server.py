#!/usr/bin/python3

import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 7773  # initiate port no above 1024

    server_socket = socket.socket() 

    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(10)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    while True:

        data = conn.recv(1024).decode()
        #if not data:
        #    # if data is not received break
        #    break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()