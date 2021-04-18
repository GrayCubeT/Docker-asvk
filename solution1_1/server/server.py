#!/usr/bin/python3

import socket
from mylib import solution


HOST = ''
PORT = 9090
LISTEN_AMOUNT = 1

def main():
    global HOST, PORT, LISTEN_AMOUNT
    # create a socket and bind it
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(LISTEN_AMOUNT)
    while True:
        # serve one connection
        conn, addr = sock.accept()
        print('connected:', addr, flush=True)

        while True:
            # serve one problem
            data = ''
            while True:
                # recieve problem
                data += str(conn.recv(1024), 'utf-8')
                if ('\n' in data): break

            # stopping sequence
            if (data == 'stop\n'):
                conn.close()
                sock.close()
                return

            print("Recieved problem: ", data)
            ans = solution.calculate(data)
            # answer parsing
            if (not isinstance(ans, str)):
                ans = str(ans)
                print("Server answer: " + ans)

                # send result back with a request for next problem
                conn.sendall(bytes("Server answer: " + 
                    ans + "\nnext problem\n", 'utf-8'))
            else:
                print("Calculation failed:\n" + ans)
                conn.sendall(bytes("Calculation failed:\n{}\nnext problem\n".format(ans), 'utf-8'))
        
        conn.close()
    sock.close()



if __name__ == "__main__":
    main()