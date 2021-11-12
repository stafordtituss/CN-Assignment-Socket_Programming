#!/usr/bin/env python3

import socket
import pickle
from re import search

SERV_ADDR = '127.0.0.1'  
SERV_PORT = 5001     


def hasDigit(inp):
    # print('inp', inp)
    sd = []
    if any("SECRET" in w for w in inp):
        for w in inp:
                for c in w:
                    if c.isdigit():
                        sd.append(c)
                        # print(sd)
        return sd


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((SERV_ADDR, SERV_PORT))
    soc.listen()
    con, con_addr = soc.accept()
    with con:
        print('Connection to ', con_addr, ' has been established!')
        while True:
            recv_data = con.recv(1024)
            if not recv_data:
                break
            recv_data = pickle.loads(recv_data)
            print("Recieved: ", recv_data)
            test = hasDigit(recv_data)
            if test:
                count = len(test)
                send_out = "Digits: " + "".join(test) + " Count: " + str(count)
                final = pickle.dumps(send_out)
                con.send(final)
            else:
                final = pickle.dumps("Secret Code not found")
                con.send(final)