#!/usr/bin/python3

import socket
import sys
from os import listdir, getcwd
from os.path import isfile, join
from time import sleep

HOST, PORT = "localhost", 9090
BUFFER_SIZE = 1024

def main():
    global HOST, PORT, BUFFER_SIZE
    # create a socket
    sock = socket.socket()

    # 5 tries to connect
    tries = 0
    while tries < 5:
        try:
            sock.connect((HOST, PORT))
        except Exception as exc:
            tries += 1
            if (tries >= 5):
                print("Connection failed, aborting")
                print(exc)
                return
            print("Can't get a response from server, try number: ", tries)
            sleep(3)
        else: 
            break
    
    # get all files from current directory
    inputfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
    data = ''
    # iterate over those files
    for i in inputfiles:
        # if a file contains '.txt' -> it is an input file
        if '.txt' in i:
            # read contents
            file = open(i, 'r')
            data = file.read().replace('\n', '')
            file.close()
            
            # 'stop\n' is a stopping sequence -> putting _ after every stop
            data.replace("stop", "stop_")

            # send data -> \n is used to determine the end of transmission
            sock.sendall(bytes(str(data) + '\n', 'utf-8'))
            
            # recieve answer
            data = ''
            while True:
                data += str(sock.recv(1024), 'utf-8')
                if ('next problem\n' in data): break
            print(data.replace('next problem\n', ''))

    # send a stopping sequence for the server 
    sock.sendall(bytes("stop\n", 'utf-8'))
    sock.close()

if __name__ == "__main__":
    main()