#!/usr/bin/env python3

import socket
import sys
import pickle

SERV_ADDR = '127.0.0.1'  
SERV_PORT = 5001        

n = len(sys.argv)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((SERV_ADDR, SERV_PORT))
    if(sys.argv[1:]):
        send_data = [sys.argv[1]]
        for i in range(2, n):
            send_data.append(sys.argv[i])
        final = pickle.dumps(send_data)
        soc.send(final)
        print("Sent: ", " ".join(send_data))
    else:
        f = pickle.dumps("Haven't recieved any data!")
        soc.send(f)
        print("Sent: None")
    data = soc.recv(1024)
    data = pickle.loads(data)

print('Received: ', "".join(data))